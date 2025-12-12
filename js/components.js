/**
 * Component Loader for Somerset American Legion Post 228
 * Loads shared components (top-bar, header, nav, footer) into pages
 */
(function() {
    const components = ['top-bar', 'header', 'nav', 'footer'];
    
    async function loadComponent(name) {
        const el = document.querySelector(`[data-component="${name}"]`);
        if (!el) return;
        
        try {
            const res = await fetch(`components/${name}.html`);
            if (res.ok) {
                el.outerHTML = await res.text();
            }
        } catch (e) {
            console.error(`Failed to load ${name}:`, e);
        }
    }
    
    async function init() {
        // Load all components
        await Promise.all(components.map(loadComponent));
        
        // Set active nav link based on current page
        const page = location.pathname.split('/').pop().replace('.html', '') || 'index';
        document.querySelectorAll(`[data-page="${page}"]`).forEach(link => {
            link.classList.add('active');
        });
        
        // Update copyright year
        const yearEl = document.getElementById('copyright-year');
        if (yearEl) yearEl.textContent = new Date().getFullYear();
        
        // Re-init mobile menu if main.js already loaded
        if (typeof initMobileMenu === 'function') initMobileMenu();
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
