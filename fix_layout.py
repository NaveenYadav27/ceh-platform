import re

def fix_layout(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove the floating w-stat elements and welcome-hint
    bad_html = """          <div class="w-stat"><div class="w-stat-val">70+</div><div class="w-stat-lbl">TOPICS</div></div>
          <div class="w-stat"><div class="w-stat-val">700+</div><div class="w-stat-lbl">QUIZ QS</div></div>
          <div class="w-stat"><div class="w-stat-val">70+</div><div class="w-stat-lbl">CTF FLAGS</div></div>
        </div>
        <div class="welcome-hint">⌨️ &nbsp;Select a topic from the sidebar to start → </div>"""
    
    # We will use regex to remove anything from `<div class="w-stat">` to the `</div>` after welcome-hint
    html = re.sub(r'\s*<div class="w-stat">.*?</style>', '</style>', html, flags=re.DOTALL) # wait, no, they are right before <div id="topic-view" style="display:none;"></div>
    
    # Let's cleanly replace the exact floating artifacts:
    pattern = r'<div class="w-stat">.*?<div class="welcome-hint">.*?</div>'
    html = re.sub(pattern, '', html, flags=re.DOTALL)
    
    # If the exact character for the keyboard icon is weird, we just match:
    pattern2 = r'\s*<div class="w-stat">[\s\S]*?</div>\s*</div>\s*<div class="welcome-hint">[\s\S]*?</div>'
    html = re.sub(pattern2, '', html)

    # Clean up any remaining w-stats just in case
    html = re.sub(r'\s*<div class="w-stat">[\s\S]*?</div>', '', html)
    html = re.sub(r'\s*<div class="welcome-hint">[\s\S]*?</div>', '', html)
    # The stray closing </div> from welcome-stats
    html = html.replace('</div>\n      <div id="topic-view" style="display:none;"></div>', '<div id="topic-view" style="display:none;"></div>')

    # 2. Update the Hero text for GFS
    old_hero = """<h1>SHADOWXLAB CEHv13 AI</h1>
            <p>Welcome to your centralized learning management system. Track your progress, execute hands-on labs, and master both traditional and AI-powered offensive security tools.</p>"""
            
    new_hero = """<h1>GLOBAL FINANCIAL SERVICES</h1>
            <p>Welcome to your first day at Global Financial Services. Track your active incidents, execute defensive operations, and master your role as a Cybersecurity Analyst.</p>"""
            
    html = html.replace(old_hero, new_hero)
    
    # 3. Update the left top logo in case it was missed
    html = html.replace('CEH v13 AI', 'GFS SOC')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Layout and Hero text fixed.")

fix_layout('frontend/index.html')
