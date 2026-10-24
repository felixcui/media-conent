"""逐帧渲染科普短视频：PIL 绘制画面 -> ffmpeg 编码，并混入逐句配音。

用法: python render.py <工作目录> [--preview 秒数,...]
"""
import json, math, subprocess, sys, os
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont, ImageOps

WD = sys.argv[1]
B = os.path.join(WD, 'build')
OUT = os.path.join(WD, 'output')
W, H, FPS = 1080, 1920, 30
SS = 3  # 形状超采样倍数（抗锯齿）

# ---- 5 色调色板（暖米白系） ----
BG = (245, 239, 228)      # 暖米白 背景
INK = (46, 42, 38)        # 深棕黑 主文字
ACC = (214, 110, 58)      # 陶土橙 强调
MUT = (152, 136, 118)     # 灰褐 次要
CARD = (233, 222, 204)    # 沙色 卡片

FONT = '/System/Library/AssetsV2/com_apple_MobileAsset_Font7/3419f2a427639ad8c8e139149a287865a90fa17e.asset/AssetData/PingFang.ttc'
WEIGHT = {'bold': 11, 'med': 7, 'reg': 3}


@lru_cache(None)
def font(size, w='bold'):
    return ImageFont.truetype(FONT, size, index=WEIGHT[w])


@lru_cache(None)
def text_sprite(s, size, color, w='bold', stroke=0):
    f = font(size, w)
    l, t, r, b = f.getbbox(s, stroke_width=stroke)
    im = Image.new('RGBA', (r - l + 4, b - t + 4), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((2 - l, 2 - t), s, font=f, fill=color,
                            stroke_width=stroke, stroke_fill=color)
    return im


def aa(w, h, fn):
    """在 SS 倍画布上绘制再缩小，得到抗锯齿 sprite。fn(draw, s) 中 s 为缩放系数。"""
    big = Image.new('RGBA', (w * SS, h * SS), (0, 0, 0, 0))
    fn(ImageDraw.Draw(big), SS)
    return big.resize((w, h), Image.LANCZOS)


@lru_cache(None)
def rrect(w, h, r, fill, outline=None, width=0):
    return aa(w, h, lambda d, s: d.rounded_rectangle(
        (0, 0, w * s - 1, h * s - 1), r * s, fill=fill, outline=outline, width=width * s))


@lru_cache(None)
def circle(d, fill, outline=None, width=0):
    return aa(d, d, lambda dr, s: dr.ellipse((0, 0, d * s - 1, d * s - 1), fill=fill,
                                             outline=outline, width=width * s))


@lru_cache(None)
def gear(radius, teeth, fill, hole=BG):
    size = int(radius * 2 + 40)
    c = size / 2

    def fn(d, s):
        pts = []
        tooth_h = radius * 0.16
        rin, rout = radius - tooth_h, radius + tooth_h * 0.6
        n = teeth * 4
        for i in range(n):
            a = 2 * math.pi * i / n
            rr = rout if i % 4 in (1, 2) else rin
            pts.append(((c + rr * math.cos(a)) * s, (c + rr * math.sin(a)) * s))
        d.polygon(pts, fill=fill)
        hr = radius * 0.55
        d.ellipse(((c - hr) * s, (c - hr) * s, (c + hr) * s, (c + hr) * s), fill=hole)
        # 辐条
        for k in range(teeth >= 12 and 4 or 3):
            a = 2 * math.pi * k / (teeth >= 12 and 4 or 3)
            x2, y2 = c + hr * math.cos(a), c + hr * math.sin(a)
            d.line((c * s, c * s, x2 * s, y2 * s), fill=fill, width=int(radius * 0.13 * s))
        ar = radius * 0.16
        d.ellipse(((c - ar) * s, (c - ar) * s, (c + ar) * s, (c + ar) * s), fill=fill)
    return aa(size, size, fn)


def ease(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def back(x):
    x = max(0.0, min(1.0, x))
    c1 = 1.5
    return 1 + (c1 + 1) * (x - 1) ** 3 + c1 * (x - 1) ** 2


def put(frame, sp, cx, cy, alpha=1.0, scale=1.0, rot=0):
    if alpha <= 0.01:
        return
    if rot:
        sp = sp.rotate(rot, resample=Image.BICUBIC)
    if abs(scale - 1) > 0.005:
        sp = sp.resize((max(1, int(sp.width * scale)), max(1, int(sp.height * scale))), Image.BICUBIC)
    if alpha < 0.99:
        sp = sp.copy()
        sp.putalpha(sp.getchannel('A').point(lambda v: int(v * alpha)))
    frame.alpha_composite(sp, (int(cx - sp.width / 2), int(cy - sp.height / 2)))


def appear(frame, sp, cx, cy, t, t0, dur=0.45, dy=40, pop=False):
    """在 t0 时刻淡入上浮（或弹出）"""
    p = (t - t0) / dur
    if p <= 0:
        return
    if pop:
        put(frame, sp, cx, cy, ease(p), 0.6 + 0.4 * back(p))
    else:
        put(frame, sp, cx, cy + dy * (1 - ease(p)), ease(p))


def chip(text, fg, bg, size=48, padx=36, pady=18):
    ts = text_sprite(text, size, fg)
    w, h = ts.width + padx * 2, ts.height + pady * 2
    base = rrect(w, h, h // 2, bg).copy()
    base.alpha_composite(ts, (padx, pady))
    return base


@lru_cache(None)
def chip_c(text, fg, bg, size=48):
    return chip(text, fg, bg, size)


@lru_cache(None)
def card_with_text(lines, w, h, size, color, bg=CARD, r=36):
    base = rrect(w, h, r, bg).copy()
    tot = sum(text_sprite(l, size, color).height for l in lines) + 20 * (len(lines) - 1)
    y = (h - tot) // 2
    for l in lines:
        ts = text_sprite(l, size, color)
        base.alpha_composite(ts, ((w - ts.width) // 2, y))
        y += ts.height + 20
    return base


# ---------------- 时间线 ----------------
items = json.load(open(os.path.join(B, 'script.json')))
GAP, LEAD, TAIL = 0.22, 0.5, 1.4
t = LEAD
for it in items:
    it['start'] = t
    it['end'] = t + it['dur']
    t = it['end'] + GAP
TOTAL = items[-1]['end'] + TAIL

scenes = []
for i, it in enumerate(items):
    if not scenes or scenes[-1]['name'] != it['scene']:
        scenes.append({'name': it['scene'], 'start': it['start'] - (GAP / 2 if i else LEAD), 'sent': []})
    scenes[-1]['sent'].append(it)
for a, b2 in zip(scenes, scenes[1:]):
    a['end'] = b2['start']
scenes[-1]['end'] = TOTAL


def rel(sc, k):
    """场景内第 k 句开始的相对时间"""
    return sc['sent'][k]['start'] - sc['start']


# ---------------- 各场景 ----------------
GEAR_A = gear(170, 18, INK)
GEAR_B = gear(110, 12, ACC)
GEAR_C = gear(80, 9, MUT)
GEAR_A_M = gear(170, 18, MUT)
GEAR_B_M = gear(110, 12, MUT)
GEAR_C_M = gear(80, 9, CARD)


def gear_train(f, t, cx, cy, speed=40, explode=0.0, muted=False, hi=None, scale=1.0):
    a, b, c = (GEAR_A_M, GEAR_B_M, GEAR_C_M) if muted else (GEAR_A, GEAR_B, GEAR_C)
    ang = t * speed
    # 啮合中心距 ≈ 两半径之和
    ra, rb, rc = 170 * scale, 110 * scale, 80 * scale
    pa = (cx - 60 * scale, cy + 40 * scale)
    db = (ra + rb + 6 * scale)
    pb = (pa[0] + db * math.cos(math.radians(-35)), pa[1] + db * math.sin(math.radians(-35)))
    dc = (rb + rc + 6 * scale)
    pc = (pb[0] + dc * math.cos(math.radians(70)), pb[1] + dc * math.sin(math.radians(70)))
    ex = explode * 90 * scale
    pa = (pa[0] - ex, pa[1] + ex * 0.5)
    pb = (pb[0] + ex * 0.6, pb[1] - ex)
    pc = (pc[0] + ex, pc[1] + ex * 0.7)
    gl = [(a, pa, ang, 'a'), (b, pb, -ang * 18 / 12 + 7, 'b'), (c, pc, ang * 18 / 9 + 3, 'c')]
    for sp, p, r, key in gl:
        if hi == key:
            pulse = 0.5 + 0.5 * math.sin(t * 6)
            put(f, circle(int(sp.width * 1.0), CARD), p[0], p[1], 0.6 + 0.4 * pulse, scale)
        put(f, sp, p[0], p[1], 1, scale, r)
    return {'a': pa, 'b': pb, 'c': pc}


def s_hook(f, t, sc):
    appear(f, text_sprite('一句话', 170, ACC, stroke=2), W / 2, 430, t, 0.0, pop=True)
    appear(f, text_sprite('让AI现做一个', 92, INK), W / 2, 610, t, 0.35)
    appear(f, text_sprite('科普动画', 92, INK), W / 2, 730, t, 0.55)
    # 对话输入框 + 打字
    t1 = 0.9
    if t > t1:
        box = rrect(860, 130, 65, CARD)
        put(f, box, W / 2, 920, ease((t - t1) / 0.4))
        msg = '机械表是怎么走的？'
        n = int(max(0, (t - t1 - 0.3)) / 0.11)
        shown = msg[:min(n, len(msg))]
        if shown:
            ts = text_sprite(shown, 52, INK, 'med')
            f.alpha_composite(ts, (W // 2 - 380, 920 - ts.height // 2))
        else:
            ts = None
        if int(t * 2.5) % 2 == 0:
            x = W // 2 - 380 + (ts.width if ts else 0) + 6
            put(f, rrect(5, 56, 2, ACC), x, 920)
        put(f, circle(84, ACC), W / 2 + 360, 920, ease((t - t1) / 0.4))
        put(f, text_sprite('↑', 50, BG), W / 2 + 360, 918, ease((t - t1) / 0.4))
    t2 = rel(sc, 1) + 0.6
    if t > t2:
        p = ease((t - t2) / 0.5)
        put(f, text_sprite('↓', 70, MUT), W / 2, 1040, p)
        put(f, rrect(600, 250, 40, CARD), W / 2, 1220, p)
        g = gear(70, 12, INK)
        put(f, g, W / 2 - 190, 1225, p, 1, t * 60)
        g2 = gear(52, 9, ACC)
        put(f, g2, W / 2 - 190 + 112, 1225 - 30, p, 1, -t * 60 * 12 / 9 + 10)
        put(f, text_sprite('动起来！', 60, INK), W / 2 + 170, 1220, p)


def s_intro(f, t, sc):
    appear(f, chip_c('开源 Skill', BG, ACC, 60), W / 2, 480, t, 0.0, pop=True)
    appear(f, text_sprite('Anatomy', 190, INK, stroke=2), W / 2, 720, t, 0.6, pop=True)
    if t > 1.1:
        p = ease((t - 1.1) / 0.6)
        put(f, rrect(max(2, int(560 * p)), 14, 7, ACC), W / 2, 850)
    appear(f, text_sprite('意思是：深度剖析', 64, MUT, 'med'), W / 2, 960, t, 1.4)
    if t > 1.0:
        put(f, gear(90, 12, CARD), W / 2 - 360, 1200, ease((t - 1.0) / 0.5), 1, t * 30)
        put(f, gear(60, 9, CARD), W / 2 + 380, 1180, ease((t - 1.0) / 0.5), 1, -t * 45)


@lru_cache(None)
def ai_badge():
    base = circle(260, INK).copy()
    ts = text_sprite('AI', 110, BG, stroke=2)
    base.alpha_composite(ts, ((260 - ts.width) // 2, (260 - ts.height) // 2 - 6))
    return base


@lru_cache(None)
def skill_box():
    """技能包：带提手的盒子"""
    w, h = 300, 280
    base = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    base.alpha_composite(rrect(120, 70, 28, None, ACC, 14), (90, 0))
    base.alpha_composite(rrect(300, 220, 36, ACC), (0, 50))
    base.alpha_composite(rrect(300, 16, 0, BG), (0, 120))
    ts = text_sprite('Skill', 64, BG)
    base.alpha_composite(ts, ((w - ts.width) // 2, 170))
    return base


def s_skill(f, t, sc):
    appear(f, text_sprite('Skill = 给AI装的技能包', 66, INK), W / 2, 380, t, 0.0)
    d = sc['sent'][0]['dur']
    # 技能包从右侧滑入，与 AI 合体
    put(f, ai_badge(), W / 2 - 200, 760, ease(t / 0.4))
    put(f, text_sprite('+', 100, ACC), W / 2, 760, ease((t - 0.5) / 0.3))
    p = ease((t - 0.7) / 0.6)
    if p > 0:
        put(f, skill_box(), W / 2 + 200 + 200 * (1 - p), 760, p)
    t3 = d * 0.55  # “装上它”之后
    appear(f, text_sprite('↓', 80, MUT), W / 2, 980, t, t3)
    if t > t3 + 0.3:
        q = (t - t3 - 0.3) / 0.45
        put(f, chip_c('学会把原理做成动画', BG, INK, 60), W / 2, 1130, ease(q), 0.6 + 0.4 * back(q))
        g = gear(46, 9, ACC)
        put(f, g, W / 2 + 390, 1060, ease(q), 1, t * 80)


def s_idea(f, t, sc):
    appear(f, text_sprite('Anatomy 的理念', 60, MUT, 'med'), W / 2, 420, t, 0.0)
    appear(f, card_with_text(('物体本身，', '就是解释。'), 840, 420, 104, INK), W / 2, 800, t, 0.2, dy=60)
    appear(f, text_sprite('“', 220, ACC), W / 2 - 360, 610, t, 0.4, pop=True)
    appear(f, text_sprite('The object is the explanation.', 40, MUT, 'med'), W / 2, 1090, t, 1.4)
    appear(f, text_sprite('不靠文字讲，直接让你看到', 56, INK, 'med'), W / 2, 1220, t, 2.0)


def s_demo(f, t, sc):
    appear(f, text_sprite('问：机械表怎么计时？', 64, INK), W / 2, 360, t, 0.0)
    ex = 0.0
    if 2.6 < t < 4.6:
        ex = math.sin(math.pi * (t - 2.6) / 2.0)
    p = ease(t / 0.6)
    if p > 0:
        gear_train(f, t, W / 2, 800, speed=45, explode=ex)
    chips = [('能转', 1.2), ('能拆', 2.6), ('能亲手拨', 4.4)]
    xs = [W / 2 - 300, W / 2 - 40, W / 2 + 270]
    for (txt, t0), x in zip(chips, xs):
        appear(f, chip_c(txt, BG, ACC, 54), x, 1250, t, t0, pop=True)


@lru_cache(None)
def case_image():
    im = Image.open(os.path.join(WD, 'assets', 'src', 'img2.png')).convert('L')
    im = ImageOps.autocontrast(im, cutoff=1)
    im = ImageOps.colorize(im, black=INK, white=(250, 246, 238), mid=MUT).convert('RGBA')
    tw = 900
    im = im.resize((tw, int(im.height * tw / im.width)), Image.LANCZOS)
    mask = rrect(im.width, im.height, 28, (255, 255, 255)).getchannel('A')
    im.putalpha(mask)
    frame = rrect(im.width + 24, im.height + 24, 38, CARD).copy()
    frame.alpha_composite(im, (12, 12))
    return frame


def s_cases(f, t, sc):
    appear(f, text_sprite('原作者的案例合集', 56, MUT, 'med'), W / 2, 380, t, 0.0)
    p = ease(t / 0.6)
    put(f, case_image(), W / 2, 780 + 40 * (1 - p), p, 0.94 + 0.06 * p)
    tags = ['发动机', '显卡', '刹车', '机械表']
    pos = [(W / 2 - 330, 1180), (W / 2 - 75, 1180), (W / 2 + 150, 1180), (W / 2 + 370, 1180)]
    for i, (tg, (x, y)) in enumerate(zip(tags, pos)):
        appear(f, chip_c(tg, INK, CARD, 50), x, y, t, 0.8 + i * 0.35, pop=True)
    appear(f, text_sprite('各种原理  都能做', 70, INK), W / 2, 1310, t, 2.6)


def s_problem(f, t, sc):
    gear_train(f, t, W / 2, 780, speed=20, muted=True, scale=0.95)
    for i, (x, y, s) in enumerate([(W / 2 - 330, 470, 140), (W / 2 + 330, 520, 170), (W / 2 + 260, 1060, 110)]):
        bob = 18 * math.sin(t * 3 + i)
        appear(f, text_sprite('?', s, ACC, stroke=2), x, y + bob, t, 0.3 + i * 0.25, pop=True)
    appear(f, text_sprite('外行看了：懵', 84, INK), W / 2, 1250, t, 0.9)
    t2 = rel(sc, 0) + sc['sent'][0]['dur'] * 0.6  # “这个零件是啥”大约在句子 60% 处
    if t > t2:
        appear(f, chip_c('这是啥？', INK, BG, 54), W / 2 - 230, 360, t, t2, pop=True)
        appear(f, chip_c('在干嘛？', INK, BG, 54), W / 2 + 200, 1110, t, t2 + 0.8, pop=True)


@lru_cache(None)
def icon_card(label, kind):
    w, h = 270, 270
    base = rrect(w, h, 40, CARD).copy()
    d = ImageDraw.Draw(base)
    cx, cy = w // 2, 105
    if kind == 'anim':
        g = gear(52, 10, INK)
        base.alpha_composite(g, (cx - g.width // 2, cy - g.height // 2))
    elif kind == 'talk':
        b = rrect(130, 90, 26, INK)
        base.alpha_composite(b, (cx - 65, cy - 50))
        for i, ww in enumerate((80, 60)):
            base.alpha_composite(rrect(ww, 12, 6, CARD), (cx - 45, cy - 30 + i * 28))
        d.polygon([(cx - 40, cy + 38), (cx - 10, cy + 38), (cx - 42, cy + 62)], fill=INK)
    elif kind == 'voice':
        for i, hh in enumerate((40, 80, 110, 70, 100, 50, 30)):
            base.alpha_composite(rrect(16, hh, 8, INK), (cx - 98 + i * 28, cy - hh // 2))
    ts = text_sprite(label, 56, INK)
    base.alpha_composite(ts, ((w - ts.width) // 2, 205 - ts.height // 2))
    return base


def s_solve(f, t, sc):
    t2 = rel(sc, 1)
    if t < t2 - 0.1:
        a = 1.0
    else:
        a = max(0.0, 1 - (t - t2 + 0.1) / 0.35)
    if a > 0:
        xs = [W / 2 - 320, W / 2, W / 2 + 320]
        cards = [('动画', 'anim', 0.2), ('讲解', 'talk', 1.6), ('配音', 'voice', 3.0)]
        for (lab, kind, t0), x in zip(cards, xs):
            p = ease((t - t0) / 0.45)
            put(f, icon_card(lab, kind), x, 620 + 40 * (1 - p), p * a, 0.7 + 0.3 * back((t - t0) / 0.45) if p < 1 else 1)
        for x, t0 in ((W / 2 - 160, 1.3), (W / 2 + 160, 2.7)):
            put(f, text_sprite('+', 80, ACC), x, 620, ease((t - t0) / 0.3) * a)
        put(f, text_sprite('=', 90, ACC), W / 2, 850, ease((t - 4.2) / 0.3) * a)
        p = (t - 4.4) / 0.5
        if p > 0:
            put(f, chip_c('一段科普视频', BG, ACC, 76), W / 2, 1060, ease(p) * a, 0.6 + 0.4 * back(p))
        appear(f, text_sprite('门外汉也能看懂', 0 or 60, MUT, 'med'), W / 2, 1230, t, 5.2) if a >= 1 else None
    if t > t2 - 0.1:
        tt = t - t2
        p = ease((tt + 0.1) / 0.45)
        # 模拟视频画面
        put(f, rrect(900, 760, 44, CARD), W / 2, 800, p)
        pts = gear_train(f, t, W / 2 + 20, 830, speed=30, scale=0.8, hi='b' if tt > 0.8 else None) if p > 0.5 else None
        if pts and tt > 0.8:
            q = ease((tt - 0.8) / 0.4)
            bx, by = pts['b']
            lab = chip_c('讲到它  就高亮它', BG, INK, 44)
            put(f, lab, W / 2, 470, q)
        appear(f, text_sprite('讲到哪  亮到哪', 80, INK), W / 2, 1270, t, t2 + 1.0)


@lru_cache(None)
def adv_card(num, title, desc):
    w, h = 880, 210
    base = rrect(w, h, 40, CARD).copy()
    c = circle(110, ACC)
    base.alpha_composite(c, (50, (h - 110) // 2))
    ts = text_sprite(num, 64, BG)
    base.alpha_composite(ts, (105 - ts.width // 2, h // 2 - ts.height // 2 - 4))
    ts = text_sprite(title, 72, INK)
    base.alpha_composite(ts, (200, 38))
    ts = text_sprite(desc, 44, MUT, 'med')
    base.alpha_composite(ts, (204, 128))
    return base


def s_adv(f, t, sc):
    appear(f, text_sprite('这个工具好在哪？', 80, INK), W / 2, 400, t, 0.0, pop=True)
    rows = [('1', '简单', '一句话就能用 · 开源免费'),
            ('2', '真实', '照真实结构做 · 宁慢不瞎编'),
            ('3', '按需定制', '讲浅讲细 · 说一声就行')]
    for k, (n, ti, de) in enumerate(rows):
        t0 = rel(sc, k + 1)
        y = 640 + k * 250
        p = (t - t0) / 0.45
        if p > 0:
            put(f, adv_card(n, ti, de), W / 2 + 120 * (1 - ease(p)), y, ease(p))


def s_warn(f, t, sc):
    p = ease(t / 0.5)
    put(f, rrect(860, 760, 50, CARD), W / 2, 820, p)
    appear(f, circle(200, ACC), W / 2, 620, t, 0.2, pop=True)
    appear(f, text_sprite('!', 140, BG, stroke=3), W / 2, 616, t, 0.3, pop=True)
    appear(f, text_sprite('AI 也会出错', 96, INK), W / 2, 880, t, 0.6)
    appear(f, text_sprite('关键内容  记得核对', 58, MUT, 'med'), W / 2, 1020, t, 1.6)


def s_end(f, t, sc):
    t2 = rel(sc, 1)
    # 以前
    appear(f, chip_c('以前', BG, MUT, 50), W / 2 - 360, 400, t, 0.0, pop=True)
    appear(f, text_sprite('在现成资料里挑', 66, MUT), W / 2 + 70, 400, t, 0.3)
    if t > 0.5:
        for i in range(5):
            q = ease((t - 0.5 - i * 0.12) / 0.4)
            hgt = [150, 120, 165, 135, 110][i]
            put(f, rrect(70, hgt, 10, CARD), W / 2 - 220 + i * 110, 600 - hgt / 2 + 75, q)
    # 现在
    appear(f, chip_c('现在', BG, ACC, 50), W / 2 - 360, 820, t, t2, pop=True)
    appear(f, text_sprite('想了解啥 AI现做一份', 60, INK), W / 2 + 90, 820, t, t2 + 0.3)
    if t > t2 + 0.5:
        q = ease((t - t2 - 0.5) / 0.45)
        put(f, rrect(300, 170, 26, ACC), W / 2, 1010, q, 0.7 + 0.3 * q)
        put(f, aa(70, 80, lambda d, s: d.polygon([(0, 0), (70 * s, 40 * s), (0, 80 * s)], fill=BG)), W / 2 + 6, 1010, q)
    t3 = t2 + 3.1
    appear(f, text_sprite('好奇心，不用再被放弃', 74, INK, stroke=1), W / 2, 1250, t, t3, pop=True)


SCENE_FN = {'hook': s_hook, 'intro': s_intro, 'skill': s_skill, 'idea': s_idea, 'demo': s_demo,
            'cases': s_cases, 'problem': s_problem, 'solve': s_solve, 'adv': s_adv, 'warn': s_warn,
            'end': s_end}


# ---------------- 字幕 ----------------
def wlen(s):
    """按视觉宽度计长：中文 1，英文/数字/空格约 0.55"""
    return sum(1 if ord(c) > 127 else 0.55 for c in s)


def hard_cut(l, maxc):
    """超长行按宽度切开，不把英文单词切断"""
    i, acc = 0, 0
    while i < len(l) and acc + wlen(l[i]) <= maxc:
        acc += wlen(l[i])
        i += 1
    while 0 < i < len(l) and l[i].isascii() and l[i].isalnum() and l[i - 1].isascii() and l[i - 1].isalnum():
        i -= 1
    return l[:i], l[i:]


def sub_lines(text, maxc=14):
    text = text.rstrip('。')
    parts, cur = [], ''
    for ch in text:
        cur += ch
        if ch in '，：；？。！':
            parts.append(cur)
            cur = ''
    if cur:
        parts.append(cur)
    lines, line, brk = [], '', False
    for p in parts:
        end = p[-1] == '。'  # 句号处强制换行
        p = p.rstrip('，；。') if p[-1] in '，；。' else p
        if line and (brk or wlen(line) + wlen(p) + 1 > maxc):
            lines.append(line)
            line = p
        else:
            line = (line + ' ' + p) if line else p
        brk = end
    if line:
        lines.append(line)
    out = []
    for l in lines:  # 仍然过长的再硬切
        while wlen(l) > maxc + 2:
            a, l = hard_cut(l, maxc)
            out.append(a)
        out.append(l)
    out = [l.rstrip('：') for l in out]
    # 每屏最多两行
    return [out[i:i + 2] for i in range(0, len(out), 2)]


for it in items:
    pages = sub_lines(it['text'])
    tot = sum(sum(len(x) for x in pg) for pg in pages)
    acc, it['pages'] = it['start'], []
    for pg in pages:
        d = it['dur'] * sum(len(x) for x in pg) / tot
        it['pages'].append((acc, acc + d, pg))
        acc += d


def draw_sub(f, t):
    for it in items:
        if it['start'] - 0.05 <= t < it['end'] + GAP * 0.9:
            for a, b, pg in it['pages']:
                if a - 0.05 <= t < (b if b < it['end'] - 0.01 else it['end'] + GAP * 0.9):
                    y = 1540 - (len(pg) - 1) * 48
                    for l in pg:
                        put(f, text_sprite(l, 64, INK, 'bold'), W / 2, y)
                        y += 96
                    return


# ---------------- 固定元素 ----------------
HEADER = chip('AI 学习新玩法', ACC, BG, 40, 30, 12)
HEADER_LINE = rrect(140, 6, 3, ACC)


def render(t):
    f = Image.new('RGBA', (W, H), BG + (255,))
    put(f, HEADER, W / 2, 170)
    cur = [s for s in scenes if s['start'] <= t < s['end']] or [scenes[-1]]
    sc = cur[0]
    lt = t - sc['start']
    XF = 0.3
    idx = scenes.index(sc)
    if lt < XF and idx > 0:
        prev = scenes[idx - 1]
        a = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        SCENE_FN[prev['name']](a, t - prev['start'], prev)
        put(f, a, W / 2, H / 2, 1 - lt / XF)
        b2 = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        SCENE_FN[sc['name']](b2, lt, sc)
        put(f, b2, W / 2, H / 2, lt / XF)
    else:
        SCENE_FN[sc['name']](f, lt, sc)
    put(f, HEADER_LINE, W / 2, 1420)
    draw_sub(f, t)
    return f.convert('RGB')


def build_audio():
    wav = os.path.join(B, 'voice.wav')
    inputs, filt = [], []
    for i, it in enumerate(items):
        inputs += ['-i', os.path.join(B, f'a{i:02d}.mp3')]
        ms = int(it['start'] * 1000)
        filt.append(f'[{i}:a]aresample=48000,adelay={ms}|{ms}[s{i}]')
    filt.append(''.join(f'[s{i}]' for i in range(len(items))) +
                f'amix=inputs={len(items)}:normalize=0,apad,atrim=0:{TOTAL:.3f},loudnorm=I=-16:TP=-1.5[out]')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', *inputs, '-filter_complex', ';'.join(filt),
                    '-map', '[out]', '-ar', '48000', '-ac', '2', wav], check=True)
    return wav


def main():
    if '--preview' in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index('--preview') + 1].split(',')]
        for x in ts:
            render(x).save(os.path.join(B, f'preview_{x:05.1f}.jpg'), quality=85)
        print('scenes', [(s['name'], round(s['start'], 2), round(s['end'], 2)) for s in scenes])
        return
    wav = build_audio()
    out = os.path.join(OUT, '视频_一句话让AI做科普视频.mp4')
    p = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                          '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p',
                          '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest', out],
                         stdin=subprocess.PIPE)
    n = int(TOTAL * FPS)
    for i in range(n):
        p.stdin.write(render(i / FPS).tobytes())
        if i % 300 == 0:
            print(f'{i}/{n}', flush=True)
    p.stdin.close()
    p.wait()
    print('done', out, round(TOTAL, 2))


if __name__ == '__main__':
    main()
