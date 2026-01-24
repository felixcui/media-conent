#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 转微信公众号 HTML 工具

功能：
1. 将 Markdown 文件转换为带公众号样式的 HTML
2. 支持代码高亮
3. 支持图片处理
4. 可复制到剪贴板或保存为 HTML 文件
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Optional

# 导入 API 客户端（可选）
try:
    from wechat_api_client import WeChatAPIClient, WeChatAPIError
    HAS_API_CLIENT = True
except ImportError:
    HAS_API_CLIENT = False

try:
    import markdown
    from markdown.extensions import codehilite, fenced_code, tables, toc
    from pygments.formatters import HtmlFormatter
except ImportError:
    print("缺少必要的依赖包，请先安装：")
    print("pip install markdown pygments")
    sys.exit(1)

try:
    import pyperclip
    HAS_CLIPBOARD = True
except ImportError:
    HAS_CLIPBOARD = False


# 公众号样式 CSS
WECHAT_CSS = """
<style>
/* 公众号样式 */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 16px;
    line-height: 1.8;
    color: #333;
    max-width: 100%;
    margin: 0 auto;
    padding: 20px;
}

/* 标题样式 */
h1 {
    font-size: 24px;
    font-weight: bold;
    color: #000;
    margin: 30px 0 15px;
    padding-bottom: 10px;
    border-bottom: 2px solid #3f51b5;
}

h2 {
    font-size: 22px;
    font-weight: bold;
    color: #000;
    margin: 25px 0 12px;
    padding-left: 10px;
    border-left: 4px solid #3f51b5;
}

h3 {
    font-size: 20px;
    font-weight: bold;
    color: #333;
    margin: 20px 0 10px;
}

h4 {
    font-size: 18px;
    font-weight: bold;
    color: #555;
    margin: 18px 0 8px;
}

/* 段落样式 */
p {
    margin: 10px 0;
    text-align: justify;
    word-wrap: break-word;
}

/* 链接样式 */
a {
    color: #3f51b5;
    text-decoration: none;
    border-bottom: 1px solid #3f51b5;
}

a:hover {
    color: #303f9f;
    border-bottom-color: #303f9f;
}

/* 列表样式 */
ul, ol {
    margin: 10px 0;
    padding-left: 30px;
}

li {
    margin: 5px 0;
    line-height: 1.8;
}

/* 引用样式 */
blockquote {
    margin: 15px 0;
    padding: 15px 20px;
    border-left: 4px solid #42a5f5;
    background-color: #e3f2fd;
    color: #555;
    border-radius: 4px;
}

blockquote p {
    margin: 0;
}

/* 代码样式 */
code {
    font-family: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
    font-size: 14px;
    padding: 2px 6px;
    margin: 0 2px;
    background-color: #f5f5f5;
    border: 1px solid #e0e0e0;
    border-radius: 3px;
    color: #e91e63;
}

/* 代码块样式 */
pre {
    margin: 15px 0;
    padding: 15px;
    background-color: #282c34;
    border-radius: 6px;
    overflow-x: auto;
    line-height: 1.6;
}

pre code {
    display: block;
    padding: 0;
    margin: 0;
    background-color: transparent;
    border: none;
    color: #abb2bf;
    font-size: 14px;
}

/* Pygments 代码高亮样式 (Monokai 风格) */
.codehilite { background: #272822; color: #f8f8f2; }
.codehilite .hll { background-color: #49483e }
.codehilite .c { color: #75715e } /* Comment */
.codehilite .k { color: #66d9ef } /* Keyword */
.codehilite .l { color: #ae81ff } /* Literal */
.codehilite .n { color: #f8f8f2 } /* Name */
.codehilite .o { color: #f92672 } /* Operator */
.codehilite .p { color: #f8f8f2 } /* Punctuation */
.codehilite .cm { color: #75715e } /* Comment.Multiline */
.codehilite .cp { color: #75715e } /* Comment.Preproc */
.codehilite .c1 { color: #75715e } /* Comment.Single */
.codehilite .cs { color: #75715e } /* Comment.Special */
.codehilite .kc { color: #66d9ef } /* Keyword.Constant */
.codehilite .kd { color: #66d9ef } /* Keyword.Declaration */
.codehilite .kn { color: #f92672 } /* Keyword.Namespace */
.codehilite .kp { color: #66d9ef } /* Keyword.Pseudo */
.codehilite .kr { color: #66d9ef } /* Keyword.Reserved */
.codehilite .kt { color: #66d9ef } /* Keyword.Type */
.codehilite .ld { color: #e6db74 } /* Literal.Date */
.codehilite .m { color: #ae81ff } /* Literal.Number */
.codehilite .s { color: #e6db74 } /* Literal.String */
.codehilite .na { color: #a6e22e } /* Name.Attribute */
.codehilite .nb { color: #f8f8f2 } /* Name.Builtin */
.codehilite .nc { color: #a6e22e } /* Name.Class */
.codehilite .no { color: #66d9ef } /* Name.Constant */
.codehilite .nd { color: #a6e22e } /* Name.Decorator */
.codehilite .ni { color: #f8f8f2 } /* Name.Entity */
.codehilite .ne { color: #a6e22e } /* Name.Exception */
.codehilite .nf { color: #a6e22e } /* Name.Function */
.codehilite .nl { color: #f8f8f2 } /* Name.Label */
.codehilite .nn { color: #f8f8f2 } /* Name.Namespace */
.codehilite .nx { color: #a6e22e } /* Name.Other */
.codehilite .py { color: #f8f8f2 } /* Name.Property */
.codehilite .nt { color: #f92672 } /* Name.Tag */
.codehilite .nv { color: #f8f8f2 } /* Name.Variable */
.codehilite .ow { color: #f92672 } /* Operator.Word */
.codehilite .w { color: #f8f8f2 } /* Text.Whitespace */
.codehilite .mf { color: #ae81ff } /* Literal.Number.Float */
.codehilite .mh { color: #ae81ff } /* Literal.Number.Hex */
.codehilite .mi { color: #ae81ff } /* Literal.Number.Integer */
.codehilite .mo { color: #ae81ff } /* Literal.Number.Oct */
.codehilite .sb { color: #e6db74 } /* Literal.String.Backtick */
.codehilite .sc { color: #e6db74 } /* Literal.String.Char */
.codehilite .sd { color: #e6db74 } /* Literal.String.Doc */
.codehilite .s2 { color: #e6db74 } /* Literal.String.Double */
.codehilite .se { color: #ae81ff } /* Literal.String.Escape */
.codehilite .sh { color: #e6db74 } /* Literal.String.Heredoc */
.codehilite .si { color: #e6db74 } /* Literal.String.Interpol */
.codehilite .sx { color: #e6db74 } /* Literal.String.Other */
.codehilite .sr { color: #e6db74 } /* Literal.String.Regex */
.codehilite .s1 { color: #e6db74 } /* Literal.String.Single */
.codehilite .ss { color: #e6db74 } /* Literal.String.Symbol */
.codehilite .bp { color: #f8f8f2 } /* Name.Builtin.Pseudo */
.codehilite .vc { color: #f8f8f2 } /* Name.Variable.Class */
.codehilite .vg { color: #f8f8f2 } /* Name.Variable.Global */
.codehilite .vi { color: #f8f8f2 } /* Name.Variable.Instance */
.codehilite .il { color: #ae81ff } /* Literal.Number.Integer.Long */

/* 图片样式 */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 15px auto;
    border-radius: 4px;
}

/* 表格样式 */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 14px;
}

table th {
    background-color: #7986CB;
    color: white;
    padding: 12px 8px;
    text-align: left;
    font-weight: bold;
    border: 1px solid #ddd;
}

table td {
    padding: 10px;
    border: 1px solid #ddd;
}

table tr:nth-child(even) {
    background-color: #f9f9f9;
}

table tr:hover {
    background-color: #f5f5f5;
}

/* 水平分割线 */
hr {
    margin: 25px 0;
    border: none;
    border-top: 2px solid #e0e0e0;
}

/* 强调样式 */
strong, b {
    font-weight: bold;
    color: #000;
}

em, i {
    font-style: italic;
    color: #555;
}
</style>
"""


class MarkdownToWechat:
    """Markdown 转微信公众号 HTML 转换器"""
    
    def __init__(self):
        self.md = markdown.Markdown(
            extensions=[
                'fenced_code',
                'codehilite',
                'tables',
                'toc',
                'nl2br',
                'sane_lists',
            ],
            extension_configs={
                'codehilite': {
                    'css_class': 'codehilite',
                    'linenums': False,
                    'guess_lang': False,
                }
            }
        )
    
    def convert_file(self, markdown_file: str) -> str:
        """转换 Markdown 文件为 HTML
        
        Args:
            markdown_file: Markdown 文件路径
            
        Returns:
            转换后的 HTML 字符串
        """
        if not os.path.exists(markdown_file):
            raise FileNotFoundError(f"文件不存在: {markdown_file}")
        
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        return self.convert_text(markdown_content)
    
    def convert_text(self, markdown_text: str) -> str:
        """转换 Markdown 文本为 HTML
        
        Args:
            markdown_text: Markdown 文本
            
        Returns:
            转换后的 HTML 字符串
        """
        # 转换 Markdown 为 HTML
        html_content = self.md.convert(markdown_text)
        
        # 重置转换器状态（为下次转换做准备）
        self.md.reset()
        
        # 组合完整 HTML
        full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微信公众号文章</title>
    {WECHAT_CSS}
</head>
<body>
{html_content}
</body>
</html>
"""
        return full_html
    
    def get_content_only(self, markdown_text: str, inline_style: bool = True) -> str:
        """仅转换 Markdown 内容，不包含完整 HTML 结构
        
        用于 API 发布，只返回 body 内容
        
        Args:
            markdown_text: Markdown 文本
            inline_style: 是否将样式内联化（用于微信 API）
            
        Returns:
            转换后的 HTML 内容（不含 html, head, body 标签）
        """
        html_content = self.md.convert(markdown_text)
        self.md.reset()
        
        # 如果需要内联样式
        if inline_style:
            try:
                import css_inline
                
                # 创建完整的 HTML 文档用于样式处理
                full_html = f"""<!DOCTYPE html>
<html>
<head>
{WECHAT_CSS}
</head>
<body>
{html_content}
</body>
</html>"""
                
                # 内联样式
                inliner = css_inline.CSSInliner(keep_style_tags=False)
                inlined_html = inliner.inline(full_html)
                
                # 提取 body 内容
                import re
                body_match = re.search(r'<body[^>]*>(.*)</body>', inlined_html, re.DOTALL)
                if body_match:
                    html_content = body_match.group(1).strip()
                
            except ImportError:
                print("⚠️  未安装 css-inline，使用无样式版本")
                print("提示: pip install css-inline")
            except Exception as e:
                print(f"⚠️  样式内联化失败: {e}")
                print("使用无样式版本")
        
        return html_content
    
    def process_images_with_api(self, markdown_text: str, api_client, base_path: Optional[str] = None) -> str:
        """处理 Markdown 中的本地图片，上传到微信素材库
        
        Args:
            markdown_text: Markdown 文本
            api_client: WeChatAPIClient 实例
            base_path: 基础路径，用于解析相对路径
            
        Returns:
            处理后的 Markdown 文本（图片链接已替换为微信 URL）
        """
        # 查找所有图片引用：![alt](path)
        image_pattern = r'!\[([^\]]*)\]\(([^\)]+)\)'
        matches = re.finditer(image_pattern, markdown_text)
        
        replacements = {}
        for match in matches:
            alt_text = match.group(1)
            image_path = match.group(2)
            
            # 跳过已经是 URL 的图片
            if image_path.startswith(('http://', 'https://')):
                continue
            
            # 处理相对路径
            if base_path and not os.path.isabs(image_path):
                image_path = os.path.join(base_path, image_path)
            
            # 上传图片
            try:
                wechat_url = api_client.upload_news_image(image_path)
                replacements[match.group(0)] = f'![{alt_text}]({wechat_url})'
            except Exception as e:
                print(f"⚠️  图片上传失败 {image_path}: {e}")
        
        # 替换所有图片链接
        for old, new in replacements.items():
            markdown_text = markdown_text.replace(old, new)
        
        return markdown_text
    
    def process_images(self, html: str, base_path: Optional[str] = None) -> str:
        """处理图片链接
        
        Args:
            html: HTML 内容
            base_path: 基础路径，用于解析相对路径
            
        Returns:
            处理后的 HTML
        """
        # TODO: 实现图片处理逻辑
        # 1. 检测本地图片
        # 2. 上传到图床
        # 3. 替换为公网 URL
        return html


def save_html(html: str, output_file: str):
    """保存 HTML 到文件
    
    Args:
        html: HTML 内容
        output_file: 输出文件路径
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ HTML 已保存到: {output_file}")


def copy_to_clipboard(html: str):
    """复制 HTML 到剪贴板
    
    Args:
        html: HTML 内容
    """
    if not HAS_CLIPBOARD:
        print("⚠️  未安装 pyperclip，无法复制到剪贴板")
        print("提示: pip install pyperclip")
        return
    
    try:
        pyperclip.copy(html)
        print("✅ HTML 已复制到剪贴板！")
        print("💡 现在可以直接粘贴到公众号编辑器")
    except Exception as e:
        print(f"❌ 复制失败: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='将 Markdown 文件转换为微信公众号 HTML',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 转换并复制到剪贴板
  python publish_to_wechat.py article.md
  
  # 转换并保存为 HTML 文件
  python publish_to_wechat.py article.md -o output.html
  
  # 预览模式（保存为临时 HTML 并打开浏览器）
  python publish_to_wechat.py article.md --preview
        """
    )
    
    parser.add_argument(
        'markdown_file',
        help='Markdown 文件路径'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='输出 HTML 文件路径（不指定则只复制到剪贴板）'
    )
    
    parser.add_argument(
        '--preview',
        action='store_true',
        help='预览模式：生成 HTML 并在浏览器中打开'
    )
    
    parser.add_argument(
        '--no-clipboard',
        action='store_true',
        help='不复制到剪贴板'
    )
    
    # API 发布相关参数
    parser.add_argument(
        '--api',
        action='store_true',
        help='使用微信公众号 API 发布（需要认证服务号）'
    )
    
    parser.add_argument(
        '--draft-only',
        action='store_true',
        help='仅创建草稿，不发布（配合 --api 使用）'
    )
    
    parser.add_argument(
        '--title',
        default='',
        help='文章标题（不指定则从 Markdown 中提取）'
    )
    
    parser.add_argument(
        '--author',
        default='',
        help='文章作者'
    )
    
    parser.add_argument(
        '--digest',
        default='',
        help='文章摘要（会显示在文章列表）'
    )
    
    parser.add_argument(
        '--cover-image',
        help='封面图片路径（建议 900x383 或 2:1 比例）'
    )
    
    parser.add_argument(
        '--thumb-media-id',
        help='封面图的 media_id（使用后台已有图片，与 --cover-image 二选一）'
    )
    
    parser.add_argument(
        '--source-url',
        default='',
        help='原文链接'
    )
    
    args = parser.parse_args()
    
    # 转换 Markdown
    converter = MarkdownToWechat()
    
    try:
        # API 发布模式
        if args.api:
            if not HAS_API_CLIENT:
                print("❌ 缺少 wechat_api_client 模块")
                print("请确保 wechat_api_client.py 在同一目录下")
                sys.exit(1)
            
            print(f"📄 正在处理: {args.markdown_file}")
            
            # 读取 Markdown 文件
            with open(args.markdown_file, 'r', encoding='utf-8') as f:
                markdown_text = f.read()
            
            # 提取标题（第一个 # 开头的行）
            title_match = re.search(r'^#\s+(.+)$', markdown_text, re.MULTILINE)
            # 优先使用命令行参数指定的标题
            if args.title:
                title = args.title
            elif title_match:
                title = title_match.group(1)
            else:
                title = os.path.basename(args.markdown_file)
            
            # 移除第一个 H1 标题（避免在正文中重复显示）
            if title_match:
                markdown_text = markdown_text.replace(title_match.group(0), '', 1)
                # 移除标题后可能留下的空行
                markdown_text = markdown_text.lstrip('\n')
            
            # 移除水平分割线（--- 或 *** 或 ___）
            markdown_text = re.sub(r'^\s*[-*_]{3,}\s*$', '', markdown_text, flags=re.MULTILINE)
            
            # 生成摘要（如果没有提供）
            digest = args.digest
            if not digest:
                # 提取第一段作为摘要
                paragraphs = [p.strip() for p in markdown_text.split('\n\n') if p.strip() and not p.strip().startswith('#')]
                if paragraphs:
                    digest = paragraphs[0][:120]  # 限制 120 字
            
            # 初始化 API 客户端
            try:
                client = WeChatAPIClient()
            except ValueError as e:
                print(f"❌ {e}")
                print("\n配置步骤：")
                print("1. 复制 .env.example 为 .env")
                print("2. 编辑 .env 填入你的 WECHAT_APPID 和 WECHAT_APPSECRET")
                print("3. 在公众号后台设置 IP 白名单")
                sys.exit(1)
            
            # 处理本地图片
            base_path = os.path.dirname(os.path.abspath(args.markdown_file))
            markdown_text = converter.process_images_with_api(markdown_text, client, base_path)
            
            # 转换为 HTML（仅内容部分）
            content_html = converter.get_content_only(markdown_text)
            
            # 创建草稿
            try:
                media_id = client.create_draft(
                    title=title,
                    content=content_html,
                    author=args.author,
                    digest=digest,
                    cover_image_path=args.cover_image,
                    thumb_media_id=args.thumb_media_id,
                    content_source_url=args.source_url
                )
                
                # 是否发布
                if not args.draft_only:
                    confirm = input("\n是否立即发布文章？(y/N): ")
                    if confirm.lower() == 'y':
                        client.publish_draft(media_id)
                    else:
                        print("💡 文章已保存到草稿箱，请登录公众号后台发布")
                
                print("\n✨ 完成！")
                
            except WeChatAPIError as e:
                print(f"❌ 微信 API 错误: {e}")
                if e.errcode == 88000:
                    print("\n可能的原因：")
                    print("1. 你的公众号不是认证服务号")
                    print("2. 未开通草稿箱和发布接口权限")
                    print("3. IP 未加入白名单")
                sys.exit(1)
        
        # 普通 HTML 转换模式
        else:
            print(f"📄 正在转换: {args.markdown_file}")
            
            # 读取文件
            with open(args.markdown_file, 'r', encoding='utf-8') as f:
                markdown_text = f.read()
            
            # 移除第一个 H1 标题（保持与 API 模式一致）
            title_match = re.search(r'^#\s+(.+)$', markdown_text, re.MULTILINE)
            if title_match:
                markdown_text = markdown_text.replace(title_match.group(0), '', 1)
                markdown_text = markdown_text.lstrip('\n')
            
            # 移除水平分割线（--- 或 *** 或 ___）
            markdown_text = re.sub(r'^\s*[-*_]{3,}\s*$', '', markdown_text, flags=re.MULTILINE)
            
            html = converter.convert_text(markdown_text)
            
            # 保存到文件
            if args.output:
                save_html(html, args.output)
            
            # 预览模式
            if args.preview:
                import tempfile
                import webbrowser
                
                temp_file = tempfile.NamedTemporaryFile(
                    mode='w',
                    suffix='.html',
                    delete=False,
                    encoding='utf-8'
                )
                temp_file.write(html)
                temp_file.close()
                
                print(f"🌐 预览文件: {temp_file.name}")
                webbrowser.open(f'file://{temp_file.name}')
            
            # 复制到剪贴板
            if not args.no_clipboard:
                copy_to_clipboard(html)
            
            print("\n✨ 转换完成！")
        
    except Exception as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
