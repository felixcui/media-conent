#!/usr/bin/env python3
"""
AICoding 资讯周报生成工具

自动计算日期范围并生成周报，保存到 weekly/ 目录
"""
import os
import sys
import argparse
import subprocess
from datetime import datetime, timedelta

# 项目根目录 (技能脚本位于 .claude/skills/weekly-news/scripts/)
# 需要回溯到项目根目录: .claude/skills/weekly-news/scripts/ -> ../../../../
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", ".."))
WEEKLY_DIR = os.path.join(PROJECT_ROOT, "weekly")


def get_week_range(target_date: datetime = None) -> tuple[str, str]:
    """
    获取周报的日期范围

    Args:
        target_date: 目标日期，默认为今天

    Returns:
        (start_date, end_date): 格式为 YYYY-MM-DD 的日期元组
        周报以当前自然周的周六为结束日期，上周六为开始日期（共7天）
    """
    if target_date is None:
        target_date = datetime.now()

    # 计算当前自然周的周六作为结束日期
    # weekday(): 周一=0, 周二=1, ..., 周六=5, 周日=6
    current_weekday = target_date.weekday()

    # 计算到本周六的天数差
    # 如果今天是周日(6)，则本周六是昨天，需要-1天
    # 如果今天是周一(0)，则本周六是+5天
    # 如果今天是周六(5)，则本周六是今天，+0天
    if current_weekday == 6:  # 周日
        days_to_saturday = -1
    else:
        days_to_saturday = 5 - current_weekday

    end_date = target_date + timedelta(days=days_to_saturday)
    # 开始日期为上周六（本周六往前推7天）
    start_date = end_date - timedelta(days=7)

    return (
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d")
    )


# 公众号封面图素材 ID（固定）
WECHAT_THUMB_MEDIA_ID = "qxQUqgd9fe1MaWRFFohGgvlKAcpIakKP0x4GUfNTl3JbVRj64hVIZi8V68JE1q53"


def publish_to_wechat(md_file: str, end_date: str = None, preview: bool = False, weixin: bool = False, draft_only: bool = False) -> bool:
    """
    调用 publish_to_wechat.py 处理 markdown 文件

    Args:
        md_file: markdown 文件路径
        end_date: 周报结束日期 (YYYY-MM-DD)，用于生成标题
        preview: 是否预览模式
        weixin: 是否直接发布到公众号
        draft_only: 是否仅创建草稿

    Returns:
        是否成功
    """
    publish_script = os.path.join(SCRIPT_DIR, "publish_to_wechat.py")
    cmd = [sys.executable, publish_script, md_file]

    if weixin:
        # 公众号 API 发布模式
        cmd.extend(["--api", "--draft-only"])
        cmd.extend(["--thumb-media-id", WECHAT_THUMB_MEDIA_ID])
        # 周报固定摘要
        cmd.extend(["--digest", "工具动态，编程实践，编程模型，业界观点"])
        # 周报固定作者
        cmd.extend(["--author", "AICoding基地"])
        # 格式化标题：AI Coding资讯周报-2026.01.24
        if end_date:
            formatted_date = end_date.replace('-', '.')
            title = f"AI Coding资讯周报-{formatted_date}"
            cmd.extend(["--title", title])
        if not draft_only:
            # 交互式确认发布（不使用 --draft-only）
            cmd.remove("--draft-only")
        print(f"\n📱 调用公众号 API 发布工具...")
    else:
        # HTML 转换模式
        cmd.append("--no-clipboard")
        if preview:
            cmd.append("--preview")
        print(f"\n📱 调用公众号发布工具{' (预览模式)' if preview else ''}...")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"⚠️ 发布工具调用失败: {result.stderr}")
        return False

    print(result.stdout)
    return True


def generate_weekly_report(start_date: str, end_date: str, output_file: str = None, publish: bool = False, preview: bool = False, weixin: bool = False) -> str:
    """
    生成周报

    Args:
        start_date: 开始日期 (YYYY-MM-DD)
        end_date: 结束日期 (YYYY-MM-DD)
        output_file: 输出文件路径，默认为 data/weekly/{end_date}.md
        publish: 是否调用公众号发布工具（HTML 转换）
        preview: 是否预览模式（生成公众号预览网页）
        weixin: 是否直接发布到公众号 API

    Returns:
        生成的文件路径
    """
    if output_file is None:
        output_file = os.path.join(WEEKLY_DIR, f"{end_date}.md")

    # 如果文件已存在，先删除
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"已删除旧文件: {output_file}")

    # 确保目录存在
    os.makedirs(WEEKLY_DIR, exist_ok=True)

    # 调用 feishu_news.py 生成周报
    feishu_script = os.path.join(SCRIPT_DIR, "feishu_news.py")
    cmd = [sys.executable, feishu_script, "--start", start_date, "--end", end_date]

    print(f"正在生成周报 ({start_date} 至 {end_date})...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"错误: {result.stderr}")
        return None

    # 保存到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result.stdout)

    print(f"✓ 周报已保存到: {output_file}")

    # 调用公众号发布工具
    if publish or preview or weixin:
        publish_to_wechat(output_file, end_date=end_date, preview=preview, weixin=weixin, draft_only=True)

    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='生成 AICoding 资讯周报',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 生成本周周报
  python generate_weekly.py

  # 生成指定日期的周报
  python generate_weekly.py --date 2026-01-15

  # 生成指定日期范围的周报
  python generate_weekly.py --start 2026-01-01 --end 2026-01-07

  # 生成周报并调用公众号发布工具（复制到剪贴板）
  python generate_weekly.py --publish

  # 生成周报并生成公众号预览网页
  python generate_weekly.py --preview

  # 生成周报并直接发布到公众号（创建草稿）
  python generate_weekly.py --weixin
        """
    )
    parser.add_argument('--date', type=str, help='目标日期 (YYYY-MM-DD)，默认为今天')
    parser.add_argument('--start', type=str, help='开始日期 (YYYY-MM-DD)')
    parser.add_argument('--end', type=str, help='结束日期 (YYYY-MM-DD)')
    parser.add_argument('--output', type=str, help='输出文件路径')
    parser.add_argument('--publish', action='store_true', help='生成后调用公众号发布工具（HTML 转换）')
    parser.add_argument('--preview', action='store_true', help='生成公众号预览网页')
    parser.add_argument('--weixin', action='store_true', help='生成后直接发布到公众号 API（创建草稿）')

    args = parser.parse_args()

    # 确定日期范围
    if args.start and args.end:
        start_date, end_date = args.start, args.end
    elif args.date:
        target_date = datetime.strptime(args.date, "%Y-%m-%d")
        start_date, end_date = get_week_range(target_date)
    else:
        start_date, end_date = get_week_range()

    print(f"📅 日期范围: {start_date} 至 {end_date}")

    # 生成周报
    output_file = args.output or os.path.join(WEEKLY_DIR, f"{end_date}.md")
    result = generate_weekly_report(
        start_date,
        end_date,
        output_file,
        publish=args.publish,
        preview=args.preview,
        weixin=args.weixin
    )

    if not result:
        sys.exit(1)

    print("\n✅ 周报生成完成!")


if __name__ == "__main__":
    main()
