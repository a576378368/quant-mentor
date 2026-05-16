# -*- coding: utf-8 -*-
"""
游资心法教材 Sphinx 配置文件
原始简洁版本
"""

import os
import sys

# 项目信息
project = '游资心法：从入门到大师的进阶之路'
copyright = '2026, Stock Assistant'
author = 'Stock Assistant'

# 版本
version = '1.0'
release = '1.0.0'

# 语言
language = 'zh_CN'

# Sphinx扩展
extensions = [
    'myst_parser',
    'sphinx_book_theme',
    'sphinx_copybutton',
]

# 源文件目录
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
}

# 主入口文件
master_doc = 'index'

# HTML主题
html_theme = 'sphinx_book_theme'
html_title = '游资心法：从入门到大师的进阶之路'

# 主题选项
html_theme_options = {
    'repository_url': 'https://github.com/a576378368/quant-mentor',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
    'home_page_in_toc': True,
    'show_toc_level': 3,
}

# HTML 输出配置
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# MyST配置
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'attrs_inline',
    'attrs_block',
    'dollarmath',
    'amsmath',
]

# 禁用某些警告
suppress_warnings = ['myst.xref_missing']
