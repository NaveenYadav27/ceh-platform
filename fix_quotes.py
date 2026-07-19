import re
import sys

def fix_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # We need to replace unescaped single quotes inside the CONTENT object definitions.
    # But since that is complex, we can simply look for common words with apostrophes
    # that are not escaped and replace them with escaped versions.
    
    replacements = [
        ("don't", r"don\'t"),
        ("doesn't", r"doesn\'t"),
        ("isn't", r"isn\'t"),
        ("aren't", r"aren\'t"),
        ("can't", r"can\'t"),
        ("couldn't", r"couldn\'t"),
        ("wouldn't", r"wouldn\'t"),
        ("shouldn't", r"shouldn\'t"),
        ("won't", r"won\'t"),
        ("wasn't", r"wasn\'t"),
        ("weren't", r"weren\'t"),
        ("didn't", r"didn\'t"),
        ("hasn't", r"hasn\'t"),
        ("haven't", r"haven\'t"),
        ("hadn't", r"hadn\'t"),
        ("attacker's", r"attacker\'s"),
        ("victim's", r"victim\'s"),
        ("company's", r"company\'s"),
        ("building's", r"building\'s"),
        ("it's", r"it\'s"),
        ("that's", r"that\'s"),
        ("he's", r"he\'s"),
        ("she's", r"she\'s"),
        ("they're", r"they\'re"),
        ("we're", r"we\'re"),
        ("you're", r"you\'re"),
        ("let's", r"let\'s"),
        ("world's", r"world\'s"),
        ("What's", r"What\'s"),
        ("organization's", r"organization\'s"),
        ("target's", r"target\'s")
    ]

    for unescaped, escaped in replacements:
        # First, ensure we don't double escape. 
        # Temporarily replace correctly escaped ones with a placeholder
        html = html.replace(escaped, "%%%ESCAPED%%%")
        # Now replace unescaped ones with escaped ones
        html = html.replace(unescaped, escaped)
        # Restore the originally escaped ones
        html = html.replace("%%%ESCAPED%%%", escaped)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed unescaped quotes.")

fix_quotes('frontend/index.html')

# Verify by extracting JS and checking
match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if match:
    with open('frontend/temp.js', 'w', encoding='utf-8') as out:
        out.write(match.group(1))
