"""9:16 封面图，复用 render.py 的配色与绘图工具。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R
from PIL import Image

W, H = R.W, R.H
f = Image.new('RGBA', (W, H), R.BG + (255,))
R.put(f, R.chip('开源 Skill · Anatomy', R.BG, R.ACC, 50, 40, 16), W / 2, 230)
R.put(f, R.text_sprite('一句话', 250, R.ACC, stroke=4), W / 2, 480)
R.put(f, R.text_sprite('让AI给你做', 140, R.INK, stroke=3), W / 2, 700)
R.put(f, R.text_sprite('科普视频', 140, R.INK, stroke=3), W / 2, 870)
R.put(f, R.rrect(180, 14, 7, R.ACC), W / 2, 990)
# 齿轮主视觉
R.put(f, R.gear(150, 18, R.INK), W / 2 - 150, 1250, 1, 1, 8)
R.put(f, R.gear(100, 12, R.ACC), W / 2 + 120, 1150, 1, 1, 3)
R.put(f, R.gear(72, 9, R.MUT), W / 2 + 205, 1355, 1, 1, 20)
# 关键信息
y = 1560
for t in ('机械表 · 发动机 · 显卡 · 刹车', '能转能拆的原理动画 + 讲解配音'):
    R.put(f, R.card_with_text((t,), 900, 120, 52, R.INK), W / 2, y)
    y += 150
f.convert('RGB').save(os.path.join(R.OUT, '封面_9x16.png'))
print('ok')
