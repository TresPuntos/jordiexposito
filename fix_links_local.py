import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll replace href="/path" with href="path.html"
# and href="/" with href="index.html"

# Specific paths to replace
paths = [
    'work', 'workflow', 'about', 'contacto', 'linkedin', 
    'retailgen', 'invoices', 'sync-engine', 'gym', 'privacidad'
]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change href="/" to href="index.html"
    content = re.sub(r'href="/"', r'href="index.html"', content)
    
    # Change href="/..." to href="....html"
    for path in paths:
        # Match href="/path" exactly or href="/path#"
        # e.g. href="/work" -> href="work.html"
        pattern = r'href="/' + path + r'(?=[#"])'
        replacement = f'href="{path}.html'
        content = re.sub(pattern, replacement, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Enlaces actualizados con .html exitosamente!")
