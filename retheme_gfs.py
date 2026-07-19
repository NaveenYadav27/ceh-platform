import re

def retheme(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Branding Replacements
    html = html.replace('>X</span> SHADOWXLAB', '>GFS</span> CYBER DEFENSE')
    html = html.replace('CEH v13<br/>', 'GLOBAL FINANCIAL<br/>')
    html = html.replace('<span class="neon-text-cyan">AI POWERED</span><br/>', '<span class="neon-text-cyan">SERVICES</span><br/>')
    html = html.replace('ETHICAL <span class="neon-text-red">HACKING</span>', 'CYBER <span class="neon-text-red">DEFENSE</span>')
    
    old_desc = "Train inside a real-world AI-powered cyber range with enterprise-grade labs, Red Team attack simulations, SOC integrations, cloud exploitation, Active Directory attacks, AI threat hunting, and browser-based hacking environments."
    new_desc = "Welcome to your first day at Global Financial Services. Step into the shoes of a cybersecurity analyst, navigate real-world financial sector threats, and defend the firm's critical infrastructure in this live corporate simulation."
    html = html.replace(old_desc, new_desc)

    html = html.replace('Launch Cyber Range', 'Start Shift')
    html = html.replace('Explore Labs', 'View Assignments')
    
    html = html.replace('12.5K+', '1,250+')
    html = html.replace('Operators Trained', 'Active Analysts')
    html = html.replace('246+', '24+')
    html = html.replace('Live Labs', 'Active Incidents')
    html = html.replace('99.9%', '100%')
    html = html.replace('Range Uptime', 'Threat Mitigation')
    
    html = html.replace('shadowx://ops/cyber-range/session-0xA31F', 'gfs://soc/terminal-session-0xA31F')
    html = html.replace('KALI@SHADOWX', 'ANALYST@GFS-SOC')
    html = html.replace('corp.shadowx.lab', 'corp.gfs.internal')

    # 2. Terminology Replacements in UI (LMS Dashboard)
    html = html.replace('lms-mod-num">MODULE ', 'lms-mod-num">PHASE ')
    html = html.replace(' Topics</span>', ' Tasks</span>')
    html = html.replace(' Topics</th>', ' Tasks</th>')
    html = html.replace('topics_completed', 'tasks_completed') # Make sure this matches backend or just UI? Wait, backend sends topics_completed. So let's only replace UI.
    html = html.replace('${u.topics_completed || 0}</td>', '${u.topics_completed || 0}</td>') # leave backend alone
    html = html.replace('<th>Topics</th>', '<th>Tasks</th>')
    
    html = html.replace('>MODULES<', '>CAREER PATH<')
    html = html.replace('>LABS<', '>INCIDENTS<')

    # 3. Module Name Replacements in the JS Array
    roles = [
        "Phase 01: Security Analyst Trainee",
        "Phase 02: Threat Intelligence Analyst",
        "Phase 03: Vulnerability Assessment Analyst",
        "Phase 04: Vulnerability Assessment Analyst",
        "Phase 05: Vulnerability Management Specialist",
        "Phase 06: Junior Penetration Tester",
        "Phase 07: Malware Analyst",
        "Phase 08: Network Security Analyst",
        "Phase 09: Security Awareness Officer",
        "Phase 10: Network Defense Analyst",
        "Phase 11: Application Security Analyst",
        "Phase 12: Advanced Penetration Tester",
        "Phase 13: Web Application Pentester",
        "Phase 14: Web Application Pentester",
        "Phase 15: Database Security Specialist",
        "Phase 16: Wireless Security Specialist",
        "Phase 17: Mobile Security Engineer",
        "Phase 18: OT/IoT Security Researcher",
        "Phase 19: Cloud Security Architect",
        "Phase 20: Cryptographic Specialist"
    ]
    
    orig_names = [
        "Introduction to Ethical Hacking",
        "Footprinting & Reconnaissance",
        "Scanning Networks",
        "Enumeration",
        "Vulnerability Analysis",
        "System Hacking",
        "Malware Threats",
        "Sniffing",
        "Social Engineering",
        "Denial of Service",
        "Session Hijacking",
        "Evading IDS/Firewalls",
        "Web Server Hacking",
        "Hacking Web Applications",
        "SQL Injection",
        "Wireless Hacking",
        "Hacking Mobile Platforms",
        "IoT & OT Hacking",
        "Cloud Computing Threats",
        "Cryptography"
    ]

    # Use regex to carefully replace module names in the JS MODULES array
    for i in range(20):
        # Find exactly: name: "Introduction to Ethical Hacking"
        target = f'name: "{orig_names[i]}"'
        replacement = f'name: "{roles[i]} ({orig_names[i]})"'
        html = html.replace(target, replacement)
        
        # Also fix the sidebar if it generates from this, it does! 
        # But wait, some places might have hardcoded names. 
        # Let's replace the raw string everywhere just in case, but carefully.
        html = html.replace(f'>{orig_names[i]}<', f'>{roles[i]}<')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Re-theming complete.")

retheme('frontend/index.html')
