import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

inter_tight_links = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Inter with Inter Tight where it is imported via @import
    content = re.sub(
        r"@import url\('https://fonts\.googleapis\.com/css2\?family=Inter:wght@300;400;600;800&family=JetBrains\+Mono:wght@400;700&display=swap'\);",
        "@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');",
        content
    )

    # Replace manual font-family overrides that might exist
    content = re.sub(r"font-family:\s*'Inter',\s*sans-serif;", "font-family: 'Inter Tight', sans-serif;", content)

    # 2. Add inline style or attribute to prevent nav layout shift
    # Add title attributes to nav links if they don't have them
    nav_links = [
        ('>Work / Lab<', ' title="Work / Lab"'),
        ('>Workflow<', ' title="Workflow"'),
        ('>About<', ' title="About"'),
        ('>Work /', ' title="Work /Lab"'),
        ('>¿Hablamos?<', ' title="¿Hablamos?"')
    ]
    # Let's just fix the shifting by adding a small inline style to the <nav> in head, or maybe just using CSS in dist.css
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

with open('dist.css', 'a', encoding='utf-8') as f:
    f.write('''

/* Fix nav shift when bold */
nav.hidden.md\\:flex a {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}
nav.hidden.md\\:flex a::after {
    content: attr(data-text);
    content: attr(title);
    font-weight: 700;
    height: 0;
    visibility: hidden;
    overflow: hidden;
    user-select: none;
    pointer-events: none;
}
''')

print("Fonts replaced and CSS updated")
