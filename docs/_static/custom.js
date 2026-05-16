// 游资心法 - 自定义 JavaScript
// 增强交互性和用户体验

(function() {
    'use strict';
    
    // 初始化所有功能
    document.addEventListener('DOMContentLoaded', function() {
        initThemeToggle();
        initScrollEffects();
        initAnchors();
        initCopyButtons();
        initSearch();
        detectDarkMode();
    });

    // 主题切换
    function initThemeToggle() {
        const themeToggle = document.querySelector('.theme-switch-button');
        if (themeToggle) {
            themeToggle.addEventListener('click', toggleTheme);
        }
    }

    function toggleTheme() {
        const isDark = document.body.classList.toggle('dark');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    }

    // 滚动效果
    function initScrollEffects() {
        const header = document.querySelector('header');
        
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // 锚点链接
    function initAnchors() {
        const anchors = document.querySelectorAll('h1 a, h2 a, h3 a, h4 a, h5 a, h6 a');
        
        anchors.forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    history.pushState(null, null, targetId);
                }
            });
        });
    }

    // 复制代码按钮增强
    function initCopyButtons() {
        const copyButtons = document.querySelectorAll('.copybutton');
        
        copyButtons.forEach(button => {
            button.addEventListener('click', function() {
                this.classList.add('copied');
                setTimeout(() => {
                    this.classList.remove('copied');
                }, 2000);
            });
        });
    }

    // 搜索增强
    function initSearch() {
        const searchInput = document.querySelector('.search-bar input');
        
        if (searchInput) {
            searchInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    this.form.submit();
                }
            });
        }
    }

    // 平滑滚动到顶部
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    // 检测系统主题偏好
    function detectDarkMode() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.body.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        } else {
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark') {
                document.body.classList.add('dark');
            }
        }
    }

    // 生成目录
    function generateToc() {
        const content = document.querySelector('.bd-main');
        if (!content) return null;
        
        const headings = content.querySelectorAll('h1, h2, h3');
        const toc = document.createElement('div');
        
        toc.className = 'table-of-contents';
        toc.innerHTML = '<h3>目录</h3><ul></ul>';
        
        const list = toc.querySelector('ul');
        headings.forEach(heading => {
            const item = document.createElement('li');
            const link = document.createElement('a');
            
            link.href = '#' + heading.id;
            link.textContent = heading.textContent;
            
            item.appendChild(link);
            list.appendChild(item);
        });
        
        return toc;
    }

    // 复制文本到剪贴板
    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(() => {
            console.log('复制成功');
        }).catch(err => {
            console.error('复制失败:', err);
        });
    }

    // 键盘导航
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft') {
            const prevLink = document.querySelector('.prev a');
            if (prevLink) prevLink.click();
        } else if (e.key === 'ArrowRight') {
            const nextLink = document.querySelector('.next a');
            if (nextLink) nextLink.click();
        }
    });

    // 邮件链接处理
    document.addEventListener('click', function(e) {
        if (e.target.matches('a[href^="mailto:"]')) {
            e.preventDefault();
            window.location.href = e.target.href;
        }
    });

    // 联系卡片点击效果
    document.addEventListener('click', function(e) {
        if (e.target.closest('.contact-card')) {
            const card = e.target.closest('.contact-card');
            card.style.transform = 'scale(1.02)';
            setTimeout(() => {
                card.style.transform = 'scale(1)';
            }, 200);
        }
    });

    // 页面加载动画
    function showLoading() {
        const loading = document.createElement('div');
        loading.id = 'page-loading';
        loading.innerHTML = `
            <div class="loading-spinner">
                <div class="spinner-circle"></div>
                <div class="spinner-circle"></div>
                <div class="spinner-circle"></div>
            </div>
        `;
        document.body.appendChild(loading);
        
        setTimeout(() => {
            document.body.removeChild(loading);
        }, 100);
    }

    // 章节卡片交互
    function initChapterCards() {
        const cards = document.querySelectorAll('.feature-item');
        cards.forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-4px)';
            });
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
        });
    }

    // 初始化章节卡片
    document.addEventListener('DOMContentLoaded', function() {
        initChapterCards();
    });

    // 导航菜单展开
    function initNavbarDropdown() {
        const dropdowns = document.querySelectorAll('.dropdown');
        dropdowns.forEach(dropdown => {
            dropdown.addEventListener('click', function(e) {
                e.stopPropagation();
                this.classList.toggle('show');
            });
        });
    }

    // 文章元数据
    function initArticleMeta() {
        const date = new Date();
        const meta = document.querySelector('.article-meta');
        if (meta) {
            meta.innerHTML = `
                <div class="date">📅 ${date.toLocaleDateString('zh-CN')}</div>
                <div class="tags">
                    <span class="tag">投资</span>
                    <span class="tag">游资</span>
                    <span class="tag">实战</span>
                </div>
            `;
        }
    }

    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // 监听主题变化
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
        if (e.matches) {
            document.body.classList.add('dark');
        } else {
            document.body.classList.remove('dark');
        }
    });

    // 错误处理
    window.addEventListener('error', function(e) {
        console.error('Error:', e.error);
    });

    // 资源加载监听
    window.addEventListener('load', function() {
        console.log('页面加载完成');
    });

})();
