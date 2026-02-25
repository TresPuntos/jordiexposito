import os
import re

files_active = {
    'work.html': 'Work / Lab',
    'workflow.html': 'Workflow',
    'about.html': 'About',
    'contacto.html': '¿Hablamos?'
}

for file, active_text in files_active.items():
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # We want to find the link in the nav that exactly matches active_text
        # and replace its classes.
        # Currently it looks like:
        # <a href="..." class="..." data-text="...">Text</a>
        
        def replace_active(match):
            href = match.group(1)
            cls = match.group(2)
            data_text = match.group(3)
            text = match.group(4)
            
            if text == active_text:
                if '¿Hablamos?' in text:
                    new_cls = 'link--io text-acid text-sm font-bold uppercase tracking-widest ml-4 transition-colors'
                else:
                    new_cls = 'text-acid text-sm font-bold transition-colors'
                return f'<a href="{href}" class="{new_cls}" data-text="{data_text}">{text}</a>'
            return match.group(0)

        new_content = re.sub(r'<a href="([^"]+)" class="([^"]+)" data-text="([^"]+)">([^<]+)</a>', replace_active, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Active states fixed.")
