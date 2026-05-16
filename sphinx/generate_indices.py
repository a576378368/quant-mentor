#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成游资心法教材各篇章的index.rst文件（使用 reStructuredText 格式）"""

import os
import sys

# 使用相对路径，适应 GitHub Actions 环境
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "chapters")
SPHINX_DIR = os.path.join(PROJECT_DIR, "sphinx")

def generate_index_rst(part_name, part_dir):
    """为单个篇章生成index.rst（使用 reStructuredText 格式）"""
    output_dir = os.path.join(SPHINX_DIR, part_name)
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "index.rst")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{part_name}\n")
        f.write("=" * len(part_name) + "\n\n")
        f.write(".. toctree::\n")
        f.write("   :maxdepth: 2\n\n")
        
        # 获取所有rst文件（去掉.rst扩展名）
        if os.path.exists(output_dir):
            rst_files = sorted([f[:-4] for f in os.listdir(output_dir) if f.endswith(".rst")])
            for rst_file in rst_files:
                f.write(f"   {rst_file}\n")
    
    print(f"Generated: {output_file}")

def main():
    # 遍历所有part目录
    for i in range(1, 15):
        pattern = f"part{i}-*"
        if os.path.exists(CHAPTERS_DIR):
            for item in os.listdir(CHAPTERS_DIR):
                if item.startswith(f"part{i}-"):
                    part_dir = os.path.join(CHAPTERS_DIR, item)
                    if os.path.isdir(part_dir):
                        part_name = item
                        generate_index_rst(part_name, part_dir)
    
    print("\nAll index.rst files generated!")

if __name__ == "__main__":
    main()
