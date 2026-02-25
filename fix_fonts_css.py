import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The ideal link tags for fonts
fonts_link = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">"""

# The inline css to fix nav jump, let's put it in each html file just before </head> to be absolutely sure without relying on dist.css caching
nav_fix_css = """
  <style>
    /* Fix nav shift when bold */
    nav.hidden.md\\:flex a {
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
    }
    nav.hidden.md\\:flex a::after {
      content: attr(data-text);
      font-weight: 700;
      height: 0;
      visibility: hidden;
      overflow: hidden;
      user-select: none;
      pointer-events: none;
    }
  </style>
</head>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up "Work / Lab" inside nav by removing newlines
    # Just replace any occurrence of the split text
    content = re.sub(r'>\s*Work /\s+Lab\s*<', '>Work / Lab<', content)
    
    # Also fix title attributes
    content = re.sub(r'title="Work /\s+Lab"', 'title="Work / Lab"', content)
    
    # Convert title layout fix to use data-text so it's more explicit
    # Remove existing titles on nav links to avoid tooltip popup, and replace with data-text
    content = re.sub(r'<a([^>]+)title="([^"]+)"([^>]*)>', r'<a\1data-text="\2"\3>', content)

    # 2. Replace any @import for Inter/Jetbrains
    content = re.sub(r"@import\s+url\([^)]*fonts\.googleapis\.com[^)]*\);\n?", "", content)
    
    # 3. Add Google Fonts link if not present
    if "fonts.googleapis.com/css2?family=Inter+Tight" not in content:
        # insert before <link rel="stylesheet" href="dist.css">
        content = re.sub(r'(<link\s+rel="stylesheet"\s+href="dist\.css">)', fonts_link + r'\n  \1', content)

    # 4. Insert the nav fix CSS just before </head>
    # Try to avoid duplicating it
    if "/* Fix nav shift when bold */" not in content:
        content = content.replace("</head>", nav_fix_css)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav labels, fonts, and anti-shift CSS updated in all HTML files.")
