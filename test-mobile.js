const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function testMobile(url, name) {
    const browser = await chromium.launch();
    const page = await browser.newPage({
        viewport: { width: 375, height: 812 },
        deviceScaleFactor: 2,
        isMobile: true,
        hasTouch: true,
    });

    await page.goto('file://' + url);
    await page.waitForTimeout(2000); // Wait for animations

    // Capture screenshot
    const screenshotPath = path.join('/tmp', `mobile-${name}.png`);
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`Screenshot saved to ${screenshotPath}`);

    // Check for horizontal scroll
    const overflow = await page.evaluate(() => {
        const docWidth = document.documentElement.offsetWidth;
        const windowWidth = window.innerWidth;
        const elements = Array.from(document.querySelectorAll('*'));
        const overflowingElements = elements.filter(el => {
            const rect = el.getBoundingClientRect();
            return rect.right > windowWidth || rect.left < 0;
        }).map(el => ({
            tag: el.tagName,
            id: el.id,
            class: el.className,
            right: el.getBoundingClientRect().right,
            width: el.getBoundingClientRect().width
        }));

        return {
            docWidth,
            windowWidth,
            hasScroll: document.documentElement.scrollWidth > windowWidth,
            overflowingElements: overflowingElements.slice(0, 10) // top 10
        };
    });

    console.log(`Results for ${name}:`, JSON.stringify(overflow, null, 2));

    await browser.close();
}

(async () => {
    const pages = [
        { url: '/Users/jordi/Library/CloudStorage/Dropbox/backupok/TRESPUNTOS-LAB/jordiexposito/master/index.html', name: 'index' },
        { url: '/Users/jordi/Library/CloudStorage/Dropbox/backupok/TRESPUNTOS-LAB/jordiexposito/master/design-engineer-madrid.html', name: 'madrid' }
    ];

    for (const p of pages) {
        await testMobile(p.url, p.name);
    }
})();
