#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""复制 Markdown 文件到 sphinx 目录并转换为 reStructuredText 格式"""

import os
import re

# 使用相对路径，适应 GitHub Actions 环境
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "chapters")
SPHINX_DIR = os.path.join(PROJECT_DIR, "sphinx")

def md_to_rst(content):
    """将 Markdown 内容转换为 reStructuredText 格式（简化版）"""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_table = False
    table_rows = []
    
    for line in lines:
        # 处理代码块
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                result.append('::')
                result.append('')
            else:
                in_code_block = False
                result.append('')
            continue
        
        # 处理代码块内的内容
        if in_code_block:
            result.append('    ' + line)
            continue
        
        # 处理表格
        if line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(line)
            continue
        
        # 表格结束
        if in_table and not line.strip().startswith('|'):
            # 转换表格为 RST（简单处理）
            if len(table_rows) > 1:
                result.append('')
                result.append('.. table::')
                result.append('   :widths: auto')
                result.append('')
                
                # 转换每一行
                for row in table_rows:
                    cells = [cell.strip() for cell in row.split('|')[1:-1]]
                    result.append('   ' + '   '.join(cells))
                
                result.append('')
            in_table = False
            table_rows = []
        
        # 处理一级标题 # Title -> Title + ====
        if line.startswith('# ') and not line.startswith('## '):
            title = line[2:].strip()
            result.append(title)
            result.append('=' * len(title))
            result.append('')
            continue
        
        # 处理二级标题 ## Title -> Title + ---
        if line.startswith('## ') and not line.startswith('### '):
            title = line[3:].strip()
            result.append(title)
            result.append('-' * len(title))
            result.append('')
            continue
        
        # 处理三级标题 ### Title -> Title + ---
        if line.startswith('### '):
            title = line[4:].strip()
            result.append(title)
            result.append('-' * len(title))
            result.append('')
            continue
        
        # 处理列表
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            result.append(line)
            continue
        
        # 处理有序列表
        if line.strip().startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
            result.append(line)
            continue
        
        # 处理引用
        if line.strip().startswith('> '):
            result.append('   ' + line[2:].strip())
            continue
        
        # 处理加粗文本 **text**，移除中文引号干扰
        # 将中文引号替换为英文引号
        line = line.replace('”', '"').replace('“', '"')
        
        # 处理代码 `text`
        line = re.sub(r'`(.*?)`', r'``\1``', line)
        
        result.append(line)
    
    return '\n'.join(result)

def copy_markdown_files():
    """复制 Markdown 文件到 sphinx 目录"""
    print("复制 Markdown 文件到 sphinx 目录...")
    
    for i in range(1, 15):
        if os.path.exists(CHAPTERS_DIR):
            for item in os.listdir(CHAPTERS_DIR):
                if item.startswith(f"part{i}-"):
                    part_dir = os.path.join(CHAPTERS_DIR, item)
                    sphinx_part_dir = os.path.join(SPHINX_DIR, item)
                    
                    if os.path.isdir(part_dir):
                        os.makedirs(sphinx_part_dir, exist_ok=True)
                        
                        # 复制 .md 文件并转换为 .rst
                        for md_file in os.listdir(part_dir):
                            if md_file.endswith(".md"):
                                src = os.path.join(part_dir, md_file)
                                dst = os.path.join(sphinx_part_dir, md_file[:-3] + ".rst")
                                
                                with open(src, "r", encoding="utf-8") as f:
                                    content = f.read()
                                
                                # 转换为 reStructuredText 格式
                                rst_content = md_to_rst(content)
                                
                                with open(dst, "w", encoding="utf-8") as f:
                                    f.write(rst_content)
                        
                        print(f"  Copied {item}")
    
    print("Done!")

if __name__ == "__main__":
    copy_markdown_files()
