import re

def inject_m11_m15(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # PHASE 11: Application Security Analyst (Session Hijacking)
    m11_content = """
    topics: [
      {
        id: "t11_01",
        title: "Session Hijacking Concepts",
        scenario: "GFS AppSec detected an anomaly where a user session on the employee portal remained active from two different geographic locations simultaneously. Investigate potential session hijacking.",
        commands: [
          { os: "Linux", cmd: "ettercap -T -q -M arp:remote /10.10.1.5// /10.10.1.1//" },
          { os: "Windows", cmd: "netstat -ano | findstr ESTABLISHED" }
        ],
        summary: [
          "Session hijacking involves taking over a valid TCP/Web session.",
          "Network level (TCP sequence prediction) vs App level (Stealing session cookies).",
          "Prevention includes using HTTPS, HSTS, and unpredictable session IDs."
        ],
        flashcards: [
          { q: "What flag secures a cookie from being accessed by JavaScript?", a: "HttpOnly flag." },
          { q: "What secures a cookie to only be transmitted over HTTPS?", a: "Secure flag." }
        ],
        ctf: {
          scenario: "Extract the stolen session cookie from the provided network capture.",
          flag: "PHPSESSID=9a8b7c6d5e4f3g2h1i0",
          points: 50,
          hint: "Filter for HTTP GET requests and look at the Cookie header."
        }
      }
    ]
"""

    # PHASE 12: Advanced Penetration Tester (Evading IDS/Firewalls)
    m12_content = """
    topics: [
      {
        id: "t12_01",
        title: "Firewall & IDS Evasion",
        scenario: "As an Advanced Penetration Tester, you are tasked with verifying if the new GFS Next-Gen Firewall (NGFW) correctly detects fragmented packets and decoy scans.",
        commands: [
          { os: "Linux", cmd: "nmap -f -D 10.10.1.10,10.10.1.20 10.10.50.5" },
          { os: "Linux", cmd: "nmap --mtu 24 10.10.50.5" }
        ],
        summary: [
          "Fragmentation (-f) splits the TCP header over several packets to bypass simple packet filters.",
          "Decoy scanning (-D) masks your IP by generating packets from spoofed IPs.",
          "Source routing can bypass restrictive routing tables."
        ],
        flashcards: [
          { q: "What Nmap flag is used for decoy scanning?", a: "-D" },
          { q: "How does fragmentation evade IDS?", a: "The IDS must reassemble the packet to match the signature, which consumes resources or fails." }
        ],
        ctf: {
          scenario: "Analyze the IDS logs. What Nmap evasion technique corresponds to the alert 'TCP Segment Overlap Detected'?",
          flag: "Fragmentation",
          points: 50,
          hint: "Think about how Nmap splits packets into smaller MTUs."
        }
      },
      {
        id: "t12_02",
        title: "Honeypots",
        scenario: "GFS has deployed a high-interaction honeypot on the DMZ. Analyze the logs to determine the TTPs of the attacker who recently compromised it.",
        commands: [
          { os: "Linux", cmd: "cat /var/log/auth.log | grep Failed" },
          { os: "Windows", cmd: "Get-Content C:\\\\Logs\\\\Honeypot.txt -Tail 20" }
        ],
        summary: [
          "Low-interaction honeypots emulate services (e.g., Honeyd).",
          "High-interaction honeypots provide real operating systems for attackers to interact with.",
          "Honeynets are networks of honeypots."
        ],
        flashcards: [
          { q: "What is a Honeynet?", a: "A network simulating a production environment to lure attackers." },
          { q: "What is the primary purpose of a Honeypot?", a: "Gather threat intelligence and divert attackers from real assets." }
        ],
        ctf: {
          scenario: "The attacker uploaded a script to the honeypot. Read the payload: what IP address is it trying to exfiltrate data to?",
          flag: "198.51.100.42",
          points: 50,
          hint: "Look for the IP address in the bash reverse shell payload."
        }
      }
    ]
"""

    # PHASE 13: Web Application Pentester (Web Server Hacking)
    m13_content = """
    topics: [
      {
        id: "t13_01",
        title: "Web Server Misconfigurations",
        scenario: "Audit the configuration of the legacy GFS internal wiki server (Apache). Search for default credentials, directory traversal vulnerabilities, and outdated software.",
        commands: [
          { os: "Linux", cmd: "nikto -h http://wiki.gfs.internal" },
          { os: "Linux", cmd: "curl -I http://wiki.gfs.internal" }
        ],
        summary: [
          "Web server attacks target the underlying infrastructure (Apache, IIS).",
          "Directory traversal (../) accesses files outside the web root.",
          "Banner grabbing reveals the server version."
        ],
        flashcards: [
          { q: "What vulnerability allows accessing /etc/passwd via a web server?", a: "Directory Traversal / Path Traversal." },
          { q: "What command line tool grabs HTTP banners?", a: "curl -I or nc." }
        ],
        ctf: {
          scenario: "Use curl to grab the banner of the target server. What is the exact Apache version running?",
          flag: "Apache/2.4.41",
          points: 50,
          hint: "Look at the 'Server:' header in the HTTP response."
        }
      }
    ]
"""

    # PHASE 14: Web Application Pentester (Hacking Web Applications)
    m14_content = """
    topics: [
      {
        id: "t14_01",
        title: "OWASP Top 10",
        scenario: "Perform a dynamic application security test (DAST) on the new GFS Customer Portal. Focus on identifying XSS, CSRF, and Broken Access Control.",
        commands: [
          { os: "Linux", cmd: "sqlmap -u 'http://portal.gfs.internal/view?id=1' --dbs" },
          { os: "Linux", cmd: "wpscan --url http://blog.gfs.internal" }
        ],
        summary: [
          "Cross-Site Scripting (XSS): Injecting malicious scripts into web pages viewed by others.",
          "Cross-Site Request Forgery (CSRF): Forcing an authenticated user to execute unwanted actions.",
          "Injection: Untrusted data sent to an interpreter as part of a command or query."
        ],
        flashcards: [
          { q: "What type of XSS is stored in the database and served to victims?", a: "Stored XSS." },
          { q: "What defends against CSRF?", a: "Anti-CSRF Tokens." }
        ],
        ctf: {
          scenario: "Find the XSS vulnerability in the search bar. What payload successfully alerts document.cookie?",
          flag: "<script>alert(document.cookie)</script>",
          points: 50,
          hint: "Standard basic XSS payload using script tags."
        }
      }
    ]
"""

    # PHASE 15: Database Security Specialist (SQL Injection)
    m15_content = """
    topics: [
      {
        id: "t15_01",
        title: "SQL Injection (SQLi)",
        scenario: "The GFS Database Security team requires you to test the resilience of the HR database against SQL Injection. Attempt to extract the database schema using union-based and error-based techniques.",
        commands: [
          { os: "Linux", cmd: "sqlmap -u 'http://hr.gfs.internal/emp.php?id=1' -p id --tables" },
          { os: "Linux", cmd: "sqlmap -u 'http://hr.gfs.internal/emp.php?id=1' --dump -T users" }
        ],
        summary: [
          "In-band SQLi: Data is extracted using the same channel (Error-based, Union-based).",
          "Blind SQLi: Data is extracted by asking true/false questions (Boolean-based, Time-based).",
          "Prevention: Parameterized queries (Prepared Statements)."
        ],
        flashcards: [
          { q: "What is the best defense against SQLi?", a: "Parameterized Queries (Prepared Statements)." },
          { q: "Which SQLi technique relies on the database pausing for a specified time?", a: "Time-based Blind SQLi." }
        ],
        ctf: {
          scenario: "Bypass the login prompt using a classic SQL injection payload in the username field.",
          flag: "' OR 1=1 --",
          points: 50,
          hint: "You need a single quote, an always-true condition, and a comment character."
        }
      }
    ]
"""

    html = re.sub(r'id:\s*"m11".*?topics:\s*\[.*?\]', lambda m: f'id: "m11",\n    name: "Phase 11: Application Security Analyst (Session Hijacking)",\n{m11_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m12".*?topics:\s*\[.*?\]', lambda m: f'id: "m12",\n    name: "Phase 12: Advanced Penetration Tester (Evading IDS/Firewalls)",\n{m12_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m13".*?topics:\s*\[.*?\]', lambda m: f'id: "m13",\n    name: "Phase 13: Web Application Pentester (Web Server Hacking)",\n{m13_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m14".*?topics:\s*\[.*?\]', lambda m: f'id: "m14",\n    name: "Phase 14: Web Application Pentester (Hacking Web Applications)",\n{m14_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m15".*?topics:\s*\[.*?\]', lambda m: f'id: "m15",\n    name: "Phase 15: Database Security Specialist (SQL Injection)",\n{m15_content}', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Content for Phases 11-15 injected successfully.")

inject_m11_m15('frontend/index.html')
