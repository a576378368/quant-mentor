# 游资心法教材 - HTML 构建工具

这是一套用于将 Markdown 格式的教材转换为 HTML 文档的自动化脚本工具，已部署到 GitHub Pages。

## 功能特性

- ✅ 自动检测和安装 Python 环境
- ✅ 自动管理虚拟环境
- ✅ 自动安装 Sphinx 依赖
- ✅ 支持增量构建
- ✅ 生成美观的 HTML 文档
- ✅ 包含搜索和索引功能
- ✅ GitHub Pages 自动部署

## 快速开始

### 1. 构建 HTML 文档

构建 HTML 文档：

```bash
./build-html.sh build
```

### 2. 查看文档

在浏览器中打开：

```bash
open docs/index.html
# 或
xdg-open docs/index.html
```

## 命令说明

### build-html.sh

主要构建脚本，支持以下命令：

| 命令 | 说明 |
|------|------|
| `build` | 构建HTML文档（默认） |
| `rebuild` | 清理后重新构建 |
| `clean` | 清理构建文件 |
| `help` | 显示帮助信息 |

## 目录结构

```
游资心法教材工程/
├── build-html.sh              # 主构建脚本
├── README.md                  # 本文档
├── requirements.txt           # Python 依赖
├── chapters/                  # Markdown 源文件
│   ├── part1-认知升级篇/
│   │   ├── index.rst
│   │   └── 01-市场本质.md
│   ├── part2-择时系统篇/
│   │   ├── index.rst
│   │   └── ...
│   └── ...
├── sphinx/                    # Sphinx 构建配置
│   ├── conf.py                # Sphinx 配置文件
│   ├── index.rst              # 主索引文件
│   ├── _static/               # 静态资源
│   └── ...
├── docs/                      # 构建输出（GitHub Pages）
│   ├── index.html
│   ├── part1-认知升级篇/
│   └── ...
└── venv/                      # Python 虚拟环境
```

## 配置说明

### Sphinx 配置 (sphinx/conf.py)

```python
project = u'游资心法'
copyright = u'2026, Stock Assistant'
author = u'Stock Assistant'
release = '1.0'

html_theme = 'sphinx-book-theme'  # 主题
```

## 常见问题

### 1. 警告信息

构建时可能出现一些警告（如标题下划线不匹配），这不会影响文档生成，可以忽略。

### 2. 主题缺失

如果构建失败，检查依赖是否安装完整：

```bash
pip install sphinx myst-parser sphinx-book-theme sphinx-copybutton sphinx-design
```

### 3. 清理构建

如果需要完全重新构建：

```bash
./build-html.sh rebuild
```

## 工作流程

1. **编写 Markdown** - 在 `chapters/` 目录下编写 Markdown 文件
2. **运行构建** - 执行 `./build-html.sh build`
3. **查看效果** - 在浏览器中预览 `docs/index.html`
4. **部署更新** - 推送到 GitHub，GitHub Pages 自动更新

## 相关工具

- **Sphinx** - Python 文档生成工具
- **MyST** - Markdown 扩展
- **sphinx-book-theme** - 现代化主题
- **Python venv** - 虚拟环境管理

## 技术支持

如有问题，请检查：
1. Python 版本 >= 3.7
2. 网络连接（用于安装依赖）
3. 文件权限

---

**版本**: 1.0
**更新时间**: 2026-05-16
**GitHub Pages**: https://a576378368.github.io/quant-mentor/
