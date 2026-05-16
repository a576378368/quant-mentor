#!/bin/bash

# 游资心法教材 Sphinx HTML 构建脚本
# 作者：Stock Assistant
# 时间：2026-05-16

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 项目配置
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPHINX_DIR="${PROJECT_DIR}/sphinx"
BUILD_DIR="${PROJECT_DIR}/docs"
VENV_DIR="${PROJECT_DIR}/venv"

print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# 函数：检查并安装依赖
check_dependencies() {
    print_info "检查 Python 环境..."
    
    if [ ! -d "${VENV_DIR}" ]; then
        print_warning "虚拟环境不存在，创建中..."
        python3 -m venv "${VENV_DIR}"
    fi
    
    source "${VENV_DIR}/bin/activate"
    
    # 安装所需包
    print_info "安装 Sphinx 扩展..."
    pip install --upgrade pip
    pip install sphinx==7.4.7
    pip install myst-parser==2.0.0
    pip install sphinx-book-theme==1.1.3
    pip install sphinx-copybutton==0.5.2
    pip install sphinx-design==0.6.0
    
    python3 -c "import sphinx; print('Sphinx version:', sphinx.__version__)"
}

# 函数：生成 index.rst（入口文件）
generate_index() {
    print_info "生成主索引文件..."
    
    cat > "${SPHINX_DIR}/index.rst" << 'EOF'
游资心法：从入门到大师的进阶之路
===================================

"功夫未到时，你即使看了全部实盘，也不能了解；功夫到了，只言片语便知。"
    —— 炒股养家

这本书不是教你如何一夜暴富，而是教你如何建立一套可持续的盈利系统。

游资不是赌博，而是一门职业，需要信念、纪律、和系统。

目录
----

.. toctree::
   :maxdepth: 2
   :caption: 目录

   part1-认知升级篇/index
   part2-择时系统篇/index
   part3-选股系统篇/index
   part4-买入系统篇/index
   part5-仓位管理系统/index
   part6-卖出系统篇/index
   part7-风控系统篇/index
   part8-实战技巧篇/index
   part9-游资代表篇/index
   part10-学习路径篇/index
   part11-常见误区篇/index
   part12-实战案例篇/index
   part13-成功要素篇/index
   part14-总结篇/index

使用建议
--------

1. **循序渐进**：按顺序学习，不要跳过基础知识
2. **理论结合实践**：每个概念都要通过实盘或模拟验证
3. **建立系统**：不要依赖单一技巧，要建立完整的交易系统
4. **持续复盘**：定期回顾自己的交易记录，总结经验教训

目录结构
--------

- **认知升级篇**：建立正确的市场认知和信念
- **择时系统篇**：学会判断大盘环境和情绪周期
- **选股系统篇**：掌握筛选龙头股的方法
- **买入系统篇**：找到最佳买点
- **仓位管理系统**：科学分配资金
- **卖出系统篇**：不贪不恋，及时止盈止损
- **风控系统篇**：保护本金，控制风险
- **实战技巧篇**：龙头打板、低吸回封、T+0操作
- **游资代表篇**：学习大师的经验和思路
- **学习路径篇**：从入门到大师的成长路线
- **常见误区篇**：避免大部分散户的错误
- **实战案例篇**：完整案例分析
- **成功要素篇**：信念、纪律、耐心、学习
- **总结篇**：核心思想和口诀

----

**记住**：游资是一门职业，需要系统学习、长期实践和不断总结。
EOF
    
    print_success "主索引已生成"
}

# 函数：生成各篇章的 index.rst
generate_chapter_indices() {
    print_info "生成各篇章索引文件..."
    python3 "${SPHINX_DIR}/generate_indices.py"
    print_success "篇章索引已生成"
}

# 函数：复制 Markdown 文件到 sphinx 目录（可选）
copy_markdown_files() {
    print_info "检查 Markdown 文件结构..."
    
    # 检查 chapters 目录是否存在
    if [ ! -d "${PROJECT_DIR}/chapters" ]; then
        print_error "未找到 chapters 目录"
        exit 1
    fi
    
    # 运行复制和转换脚本
    print_info "复制并转换 Markdown 文件..."
    python3 "${SPHINX_DIR}/copy_md_files.py"
    
    print_success "Markdown 文件结构检查完成"
}

# 函数：构建 HTML
build_html() {
    print_info "开始构建 HTML 文档..."
    
    cd "${SPHINX_DIR}"
    source "${VENV_DIR}/bin/activate"
    
    # 清理旧的构建文件
    rm -rf "${BUILD_DIR}"
    mkdir -p "${BUILD_DIR}"
    
    # 构建 HTML
    sphinx-build -b html . "${BUILD_DIR}"
    
    print_success "HTML 文档构建完成！"
    echo ""
    print_info "访问地址: ${BUILD_DIR}/index.html"
    print_info "GitHub Pages 地址: https://a576378368.github.io/quant-mentor/"
}

# 函数：清理构建文件
clean() {
    print_info "清理构建文件..."
    rm -rf "${BUILD_DIR}"
    print_success "清理完成"
}

# 函数：重建
rebuild() {
    check_dependencies
    clean
    generate_index
    generate_chapter_indices
    copy_markdown_files
    build_html
}

# 函数：显示帮助
show_help() {
    cat << EOF
游资心法教材 HTML 构建脚本

用法: $0 [命令]

命令:
    build      构建 HTML 文档（默认）
    rebuild    完整重建（生成索引+复制文件+构建）
    prepare    仅准备文件（生成索引）
    clean      清理构建文件
    help       显示此帮助信息

示例:
    $0              # 构建文档
    $0 rebuild      # 完整重建
    $0 prepare      # 仅准备文件
    $0 clean        # 清理

EOF
}

# 主函数
main() {
    case "${1:-build}" in
        build)
            check_dependencies
            generate_index
            generate_chapter_indices
            copy_markdown_files
            build_html
            ;;
        rebuild)
            check_dependencies
            clean
            generate_index
            generate_chapter_indices
            copy_markdown_files
            build_html
            ;;
        prepare)
            check_dependencies
            generate_index
            generate_chapter_indices
            ;;
        clean)
            clean
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            print_error "未知命令: $1"
            show_help
            exit 1
            ;;
    esac
}

main "$@"
