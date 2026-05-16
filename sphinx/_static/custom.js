// 游资心法 - 自定义 JavaScript
// 增强交互性和用户体验

document.addEventListener('DOMContentLoaded', function() {
    // 初始化
    initThemeToggle();
    initScrollEffects();
    initAnchors();
    initCopyButtons();
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
                
                // 更新 URL
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
            // 显示复制提示
            this.classList.add('copied');
            setTimeout(() => {
                this.classList.remove('copied');
            }, 2000);
        });
    });
}

// 键盘导航
document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
        const prevLink = document.querySelector('.prev a');
        if (prevLink) {
            prevLink.click();
        }
    } else if (e.key === 'ArrowRight') {
        const nextLink = document.querySelector('.next a');
        if (nextLink) {
            nextLink.click();
        }
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

// 一键复制功能
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        console.log('复制成功');
    }).catch(err => {
        console.error('复制失败:', err);
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

// 平滑滚动
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// 检测深色模式偏好
function detectDarkMode() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }
}

// 初始化所有功能
document.addEventListener('DOMContentLoaded', function() {
    initThemeToggle();
    initScrollEffects();
    initAnchors();
    initCopyButtons();
    initSearch();
    
    // 检测用户主题偏好
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark');
    }
    
    // 检测系统主题偏好
    detectDarkMode();
});

// 生成目录
function generateToc() {
    const content = document.querySelector('.bd-main');
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
