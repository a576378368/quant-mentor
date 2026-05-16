# -*- coding: utf-8 -*-

project = '游资心法：从入门到大师的进阶之路'
copyright = '2026, Stock Assistant'
author = 'Stock Assistant'
release = '1.0'
version = '1.0.0'
language = 'zh_CN'
master_doc = 'index'

# 扩展配置
extensions = [
    'myst_parser',          # Markdown 支持
    'sphinx_book_theme',
    'sphinx_copybutton',
]

# MyST Markdown 扩展配置
myst_enable_extensions = [
    'dollarmath',           # $...$ 行内公式
    'amsmath',              # $$...$$ 块级公式
    'deflist',              # 定义列表
    'colon_fence',          # ::: 栅栏
]

# 主题配置
html_theme = 'sphinx_book_theme'
html_title = '游资心法：从入门到大师的进阶之路'
html_logo = '_static/logo.svg'
html_favicon = '_static/favicon.ico'

# 静态文件路径
html_static_path = ['_static']

# 目录深度
numfig = True

# 双星号加粗配置 - 确保 CommonMark 兼容
myst_commonmark_only = False
myst_gfm_only = False
