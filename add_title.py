import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add title attribute to the specific nav links
    def add_title(match):
        attrs = match.group(1)
        text = match.group(2).strip()
        # If title already exists, skip
        if 'title="' in attrs:
            return match.group(0)
        
        # We clean up any nested spans/svgs just in case, though these are mostly simple text
        if '<' in text:
            # Not a simple text node, ignore
            return match.group(0)
        
        return f'<a {attrs} title="{text}">{match.group(2)}</a>'

    # Match <a>...</a> tags in the nav by looking for text-zinc-400 or link--io
    content = re.sub(r'<a ([^>]+(?:text-zinc-400|link--io)[^>]+)>([^<]+)</a>', add_title, content)

    # Let me ensure all menu links get it by also matching mobile-link
    content = re.sub(r'<a ([^>]+mobile-link[^>]+)>([^<]+)</a>', add_title, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Title attributes added.")
