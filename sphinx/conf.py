# -*- coding: utf-8 -*-
"""
游资心法教材 Sphinx 配置文件
专业金融风格，增强美观度和用户体验
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
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
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
html_logo = '_static/logo.svg'
html_favicon = '_static/favicon.ico'

# 主题选项 - 金融专业风格
html_theme_options = {
    # 顶部导航栏
    'navbar_start': ['navbar-logo'],
    'navbar_center': ['navbar-nav'],
    'navbar_end': ['theme-switcher', 'navbar-icon-links'],
    
    # 仓库链接
    'repository_url': 'https://github.com/a576378368/quant-mentor',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
    'use_download_button': True,
    'use_fullscreen_button': True,
    
    # 导航图标
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/a576378368/quant-mentor',
            'icon': 'fa-brands fa-github',
            'type': 'fontawesome',
        },
        {
            'name': 'Email',
            'url': 'mailto:576378368@qq.com',
            'icon': 'fa-solid fa-envelope',
            'type': 'fontawesome',
        },
    ],
    
    # 路径配置
    'path_to_docs': 'sphinx',
    'home_page_in_toc': True,
    
    # 目录显示
    'show_toc_level': 3,
    'header_links_before_dropdown': 5,
    
    # 侧边栏
    'sidebar_before_document': True,
    'sidebar_collapse': True,
    
    # 页脚
    'footer_start': ['copyright', 'sphinx-version'],
    'footer_end': [],
    
    # 搜索框位置
    'search_bar_text': '搜索内容...',
}

# HTML 输出配置
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_js_files = [
    'custom.js',
]

# 自定义 HTML 变量
html_context = {
    'email': '576378368@qq.com',
    'github_url': 'https://github.com/a576378368/quant-mentor',
    'display_github': True,
    'github_user': 'a576378368',
    'github_repo': 'quant-mentor',
    'github_version': 'main',
    'conf_py_path': '/sphinx/',
}

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
    'toctree',
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

# 数学公式支持
mathjax3_config = {
    'tex': {
        'inlineMath': [['\\(', '\\)']],
        'displayMath': [['\\[', '\\]']],
    }
}

# Napoleon配置（Google/NumPy风格文档字符串）
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
