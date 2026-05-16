# -*- coding: utf-8 -*-
"""
游资心法教材 Sphinx 配置文件
优化版本：增强美观度和用户体验
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
    'sphinx_design',  # 添加设计组件支持
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
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

# 主题选项 - 美观优化版本
html_theme_options = {
    # 顶部导航栏
    'navbar_start': ['navbar-logo'],
    'navbar_center': ['navbar-nav'],
    'navbar_end': ['theme-switcher', 'navbar-icon-links'],
    
    # 仓库链接
    'repository_url': 'https://github.com/a576378368/stock',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
    
    # 导航图标
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/a576378368/stock',
            'icon': 'fa-brands fa-github',
            'type': 'fontawesome',
        },
    ],
    
    # 路径配置
    'path_to_docs': 'sphinx',
    'home_page_in_toc': True,
    
    # 表情符号支持
    'use_download_button': True,
    'use_fullscreen_button': True,
    'use_multitab_button': True,
    
    # 目录显示
    'show_toc_level': 3,
    'header_links_before_dropdown': 5,
    
    # 侧边栏
    'sidebar_before_document': True,
    'sidebar_collapse': True,
    
    # 页脚
    'footer_start': ['copyright', 'sphinx-version'],
    'footer_end': [],
}

# HTML 输出配置
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_js_files = [
    'custom.js',
]

# 自定义页面标题
html_show_sourcelink = False
html_show_sphinx = True
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'

# 默认角色
default_role = 'any'

# MyST配置
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'attrs_inline',
    'attrs_block',
    'amsmath',
    'dollarmath',
    'substitution',
    'toctree',  # 支持 toctree 功能
]

# 禁用某些警告
suppress_warnings = ['myst.xref_missing']

# 代码块样式
pygments_style = 'friendly'
pygments_dark_style = 'monokai'

# 搜索配置
html_search_language = 'zh'
html_search_options = {
    'type': 'default',
    'separator': r'(\s|[\u4e00-\u9fff])+',
}
