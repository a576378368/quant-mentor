#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成游资心法教材各篇章的index.rst文件（使用 reStructuredText 格式）"""

import os

PROJECT_DIR = "/home/yang/workspace/stock/游资心法教材工程"
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "chapters")
SPHINX_DIR = os.path.join(PROJECT_DIR, "sphinx")

def generate_index_rst(part_dir):
    """为单个篇章生成index.rst（使用 reStructuredText 格式）"""
    part_name = os.path.basename(part_dir)
    output_dir = os.path.join(SPHINX_DIR, part_name)
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "index.rst")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{part_name}\n")
        f.write("=" * len(part_name) + "\n\n")
        f.write(".. toctree::\n")
        f.write("   :maxdepth: 2\n\n")
        
        # 获取所有markdown文件（去掉.md扩展名）
        md_files = sorted([f[:-3] for f in os.listdir(part_dir) if f.endswith(".md")])
        for md_file in md_files:
            f.write(f"   {md_file}\n")
    
    print(f"Generated: {output_file}")

def main():
    # 遍历所有part目录
    for i in range(1, 15):
        pattern = f"part{i}-*"
        for item in os.listdir(CHAPTERS_DIR):
            if item.startswith(f"part{i}-"):
                part_dir = os.path.join(CHAPTERS_DIR, item)
                if os.path.isdir(part_dir):
                    generate_index_rst(part_dir)
    
    print("\nAll index.rst files generated!")

if __name__ == "__main__":
    main()
