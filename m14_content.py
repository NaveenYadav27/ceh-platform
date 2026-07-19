import os
import sys

TARGET_HTML = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"

CONTENT = """
CONTENT['web-app-concepts'] = {
  eyebrow: 'Module 14 · Topic 1',
  title: 'Web Application Concepts',
  module: 'Phase 14: Web Application Pentester',
  sub: 'Understand the core components, architectures, and technologies powering modern web applications.',
  objectives: [
    'Identify components of web application architecture.',
    'Understand HTTP/HTTPS protocols and status codes.',
    'Describe the role of web servers, databases, and application servers.'
  ],
  learn: {
    simple: 'Web applications are software programs that run on web servers and are accessed through web browsers. They rely on a client-server architecture, where the client (browser) sends HTTP requests to the server, and the server responds with data or resources (HTML, CSS, JS). Modern web applications are dynamic and often connect to backend databases to store and retrieve data.',
    analogy: 'Think of a web application like a restaurant. The browser is the customer ordering from a menu. The web server is the waiter taking the order. The application server is the kitchen preparing the food, and the database is the pantry storing all the ingredients. The waiter brings the prepared meal (web page) back to the customer.',
    architecture: 'A typical web application follows a three-tier architecture: Presentation Tier, Application Tier, and Data Tier. The Presentation Tier is the user interface running in the browser (HTML, CSS, JavaScript frameworks like React or Angular). The Application Tier contains the business logic, often written in Python, Java, C#, or Node.js, and runs on an application server. The Data Tier handles data storage and retrieval, utilizing relational databases (MySQL, PostgreSQL) or NoSQL databases (MongoDB).\\n\\nCommunication between tiers usually occurs over HTTP/HTTPS. APIs (Application Programming Interfaces), such as REST or GraphQL, are commonly used to allow the front end to communicate with the back end. State management is crucial, as HTTP is stateless; this is achieved using cookies, sessions, or tokens (like JWTs).',
    why: 'Understanding the underlying architecture is critical for identifying potential attack vectors. Flaws can exist in the presentation logic, business logic, or data handling. A pentester must know how the components interact to exploit vulnerabilities like injection or cross-site scripting.'
  },
  enterprise: {
    gfs: 'Global Financial Services relies heavily on web applications for online banking, trading portals, and internal employee portals, handling millions of transactions daily.',
    windows: 'Windows environments often use IIS (Internet Information Services) as the web server and .NET for application logic, integrating tightly with Active Directory for authentication.',
    linux: 'Linux environments frequently deploy LAMP (Linux, Apache, MySQL, PHP/Python/Perl) or MEAN/MERN stacks, utilizing Nginx or Apache as web servers.'
  },
  workflow: [
    'Step 1: Identify the target web application and its purpose.',
    'Step 2: Map the application footprint (subdomains, directories, APIs).',
    'Step 3: Analyze the technologies used (Wappalyzer, BuiltWith).',
    'Step 4: Understand the authentication and session management mechanisms.',
    'Step 5: Identify user roles and access control mechanisms.',
    'Step 6: Map out the data flow and backend interactions.'
  ],
  diagram: {
    caption: 'Click to interact with the Three-Tier Web Architecture diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="50" width="150" height="300" fill="#2d3748" rx="10"/><text x="125" y="80" fill="white" font-family="sans-serif" font-size="16" text-anchor="middle">Presentation Tier</text><text x="125" y="110" fill="#a0aec0" font-family="sans-serif" font-size="12" text-anchor="middle">Browser / Mobile</text><rect x="75" y="140" width="100" height="40" fill="#4a5568" rx="5"/><text x="125" y="165" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">HTML/CSS/JS</text><path d="M 210 200 L 240 200" stroke="#718096" stroke-width="2" marker-end="url(#arrow)"/><rect x="250" y="50" width="150" height="300" fill="#2d3748" rx="10"/><text x="325" y="80" fill="white" font-family="sans-serif" font-size="16" text-anchor="middle">Application Tier</text><text x="325" y="110" fill="#a0aec0" font-family="sans-serif" font-size="12" text-anchor="middle">Web &amp; App Servers</text><rect x="275" y="140" width="100" height="40" fill="#4a5568" rx="5"/><text x="325" y="165" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">Business Logic</text><path d="M 410 200 L 440 200" stroke="#718096" stroke-width="2" marker-end="url(#arrow)"/><rect x="450" y="50" width="120" height="300" fill="#2d3748" rx="10"/><text x="510" y="80" fill="white" font-family="sans-serif" font-size="16" text-anchor="middle">Data Tier</text><text x="510" y="110" fill="#a0aec0" font-family="sans-serif" font-size="12" text-anchor="middle">Databases</text><rect x="460" y="140" width="100" height="40" fill="#4a5568" rx="5"/><text x="510" y="165" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">SQL / NoSQL</text><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#718096"/></marker></defs></svg>'
  },
  commands: {
    lin: [
      { cmd: 'curl -I https://target.com', purpose: 'Fetch HTTP headers', out: 'HTTP/1.1 200 OK\\nServer: nginx', note: 'Helps identify the web server technology.', mistake: 'Forgetting the -I flag, which fetches the entire page instead of just headers.' },
      { cmd: 'whatweb target.com', purpose: 'Web technology fingerprinting', out: 'Apache, PHP/7.4.3, WordPress', note: 'Provides a summary of technologies used.', mistake: 'Relying solely on one tool for fingerprinting.' }
    ],
    win: [
      { cmd: 'Invoke-WebRequest -Uri https://target.com -Method Head', purpose: 'Fetch HTTP headers', out: 'Headers object', note: 'PowerShell equivalent for fetching headers.', mistake: 'Not handling self-signed certificates properly in PowerShell.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Beginner',
    duration: '30',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Curl', 'WhatWeb', 'Wappalyzer'],
    dependencies: [],
    safety: ['Perform fingerprinting only on authorized targets.'],
    scenario: 'GFS has launched a new internal portal. Your task is to profile the application stack to prepare for a vulnerability assessment.',
    objectives: ['Identify the web server and application frameworks in use.'],
    steps: [
      'Step 1: Open a terminal in Kali Linux.',
      'Step 2: Use curl to inspect the HTTP headers: `curl -I http://192.168.1.100`',
      'Step 3: Analyze the "Server" and "X-Powered-By" headers.',
      'Step 4: Run whatweb against the target: `whatweb http://192.168.1.100`',
      'Step 5: Access the site via a browser and use the Wappalyzer extension to confirm findings.'
    ],
    evidence: ['Terminal output showing identified technologies.', 'Screenshot of Wappalyzer results.'],
    validation: ['You should see the server type (e.g., Apache/2.4) and frameworks (e.g., PHP).'],
    troubleshooting: ['If the site is unreachable, verify network connectivity and port configuration.'],
    mitre: [{ id: 'T1592', name: 'Gather Victim Host Information', tactic: 'Reconnaissance' }],
    cleanup: ['Close the browser and terminal.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which HTTP method is typically used to retrieve data from a server without modifying it?',
      opts: ['POST', 'GET', 'PUT', 'DELETE'],
      correct: 1,
      fb: 'The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'In a 3-tier web architecture, which tier is responsible for business logic?',
      opts: ['Presentation Tier', 'Data Tier', 'Application Tier', 'Network Tier'],
      correct: 2,
      fb: 'The Application Tier (or Logic Tier) processes commands, makes logical decisions, and performs calculations.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does a 403 Forbidden HTTP status code indicate?',
      opts: ['The resource was not found', 'The server timed out', 'The client is not authenticated', 'The server understood the request but refuses to authorize it'],
      correct: 3,
      fb: 'A 403 Forbidden means the client authenticated successfully, but does not have the necessary permissions for the resource.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'HTTP is a stateful protocol by design.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'HTTP is stateless. State management is implemented using mechanisms like cookies or tokens.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is commonly used for client-side execution in a web browser?',
      opts: ['PHP', 'Node.js', 'JavaScript', 'SQL'],
      correct: 2,
      fb: 'JavaScript is executed by the browser on the client-side to create dynamic and interactive web pages.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary purpose of an API in web applications?',
      opts: ['To style web pages', 'To allow communication between different software systems', 'To store user passwords securely', 'To route DNS requests'],
      correct: 1,
      fb: 'APIs (Application Programming Interfaces) define how different software components communicate with each other.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'HTTPS uses SSL/TLS to encrypt HTTP requests and responses.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'HTTPS (HTTP Secure) uses SSL/TLS encryption to protect data transmitted between the client and server.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which component acts as an intermediary for requests from clients seeking resources from servers?',
      opts: ['Firewall', 'Proxy Server', 'Database Server', 'Switch'],
      correct: 1,
      fb: 'A proxy server acts as an intermediary, forwarding requests and sometimes caching responses.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which technology is typically associated with the Data Tier?',
      opts: ['React', 'Nginx', 'PostgreSQL', 'CSS'],
      correct: 2,
      fb: 'PostgreSQL is a relational database management system used in the Data Tier.'
    },
    {
      type: 'true-false',
      difficulty: 'Advanced',
      q: 'JSON Web Tokens (JWT) are used exclusively for encrypting data in transit.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. JWTs are used primarily for stateless authentication and information exchange, and are typically base64 encoded, not encrypted (unless specifically using JWE).'
    }
  ],
  flashcards: [
    { f: 'HTTP', b: 'Hypertext Transfer Protocol, the foundation of data communication for the World Wide Web.' },
    { f: 'Session Management', b: 'The process of securely handling multiple requests to a web-based application or service from a single user or entity.' },
    { f: 'REST', b: 'Representational State Transfer, an architectural style for designing networked applications.' },
    { f: 'API', b: 'Application Programming Interface, a set of rules allowing software to communicate.' },
    { f: 'Stateful vs Stateless', b: 'Stateful retains information between requests; Stateless treats each request as independent (like HTTP).' }
  ],
  summary: [
    'Web applications utilize a client-server model over HTTP/HTTPS.',
    'A typical architecture consists of Presentation, Application, and Data tiers.',
    'HTTP is stateless; applications use cookies or tokens for state management.',
    'APIs facilitate communication between front-end and back-end services.',
    'Understanding the technology stack is the first step in web app pentesting.'
  ],
  outcomes: [
    'Explain the components of a web application architecture.',
    'Identify common web technologies and frameworks.',
    'Understand the role of HTTP methods and status codes.'
  ],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Beginner",
    prerequisites: ["Networking Basics", "Basic Linux/Windows Command Line"],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['web-app-threats'] = {
  eyebrow: 'Module 14 · Topic 2',
  title: 'Web Application Threats (OWASP Top 10)',
  module: 'Phase 14: Web Application Pentester',
  sub: 'Master the most critical security risks to web applications as defined by the OWASP Top 10.',
  objectives: [
    'Understand the OWASP Top 10 web application security risks.',
    'Identify vulnerabilities such as Injection, Broken Authentication, and XSS.',
    'Describe mitigation strategies for common web threats.'
  ],
  learn: {
    simple: 'Web applications are exposed to the public internet, making them prime targets for attackers. The Open Web Application Security Project (OWASP) Top 10 is a standard awareness document that represents a broad consensus about the most critical security risks to web applications. These include vulnerabilities that allow attackers to steal data, hijack accounts, or take over servers.',
    analogy: 'Imagine a bank building. "Injection" is like tricking the teller with a fake ID. "Broken Access Control" is like finding an unlocked door to the vault. "Cross-Site Scripting (XSS)" is like putting up a fake sign inside the bank that redirects customers to a scammer.',
    architecture: 'The OWASP Top 10 covers a range of flaws. Injection (like SQLi or Command Injection) occurs when untrusted data is sent to an interpreter as part of a command or query. Broken Access Control allows users to act outside of their intended permissions. Cryptographic Failures lead to sensitive data exposure when data is not properly encrypted at rest or in transit.\\n\\nCross-Site Scripting (XSS) occurs when an application includes untrusted data in a web page without proper validation or escaping, allowing execution of malicious scripts in the victim\\'s browser. Security Misconfiguration is the most common issue, resulting from insecure default settings, open cloud storage, or verbose error messages.',
    why: 'The OWASP Top 10 provides a prioritized baseline for web security. Pentesters must be intimately familiar with these vulnerabilities to effectively assess web applications and help organizations prioritize remediation efforts.'
  },
  enterprise: {
    gfs: 'A SQL injection vulnerability in the GFS customer portal could allow an attacker to dump the entire customer database, leading to massive financial and reputational damage.',
    windows: 'Windows web apps using older ADO.NET without parameterized queries are highly susceptible to SQL injection.',
    linux: 'Linux web apps using outdated PHP versions with insecure functions might be vulnerable to remote code execution or command injection.'
  },
  workflow: [
    'Step 1: Test for Injection flaws by sending unexpected characters (e.g., `\\'`, `"`, `;`).',
    'Step 2: Assess Broken Access Control by attempting horizontal and vertical privilege escalation.',
    'Step 3: Test for XSS by injecting harmless script tags (e.g., `<script>alert(1)</script>`) into input fields.',
    'Step 4: Check for Cryptographic Failures by examining SSL/TLS configurations and data transmission.',
    'Step 5: Identify Security Misconfigurations like default credentials, exposed admin panels, and directory listing.',
    'Step 6: Evaluate Vulnerable and Outdated Components using vulnerability scanners.'
  ],
  diagram: {
    caption: 'Click to interact with the SQL Injection concept diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="100" width="120" height="80" fill="#2d3748" rx="5"/><text x="110" y="145" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">Attacker</text><path d="M 170 140 L 250 140" stroke="#e53e3e" stroke-width="3" marker-end="url(#arrow_red)"/><text x="210" y="130" fill="#e53e3e" font-family="sans-serif" font-size="12" text-anchor="middle">\\' OR 1=1 --</text><rect x="250" y="80" width="140" height="120" fill="#2d3748" rx="5"/><text x="320" y="115" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">Web Server</text><text x="320" y="145" fill="#a0aec0" font-family="sans-serif" font-size="10" text-anchor="middle">SELECT * FROM users</text><text x="320" y="165" fill="#a0aec0" font-family="sans-serif" font-size="10" text-anchor="middle">WHERE name = \\'\\'</text><text x="320" y="185" fill="#e53e3e" font-family="sans-serif" font-size="10" text-anchor="middle">OR 1=1 --\\'</text><path d="M 390 140 L 470 140" stroke="#e53e3e" stroke-width="3" marker-end="url(#arrow_red)"/><rect x="470" y="100" width="100" height="80" fill="#2d3748" rx="5"/><text x="520" y="145" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">Database</text><path d="M 470 160 L 390 160" stroke="#48bb78" stroke-width="3" marker-end="url(#arrow_green)" stroke-dasharray="5,5"/><text x="430" y="180" fill="#48bb78" font-family="sans-serif" font-size="12" text-anchor="middle">All Records</text><path d="M 250 160 L 170 160" stroke="#48bb78" stroke-width="3" marker-end="url(#arrow_green)" stroke-dasharray="5,5"/><text x="210" y="180" fill="#48bb78" font-family="sans-serif" font-size="12" text-anchor="middle">Admin Access</text><defs><marker id="arrow_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#e53e3e"/></marker><marker id="arrow_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#48bb78"/></marker></defs></svg>'
  },
  commands: {
    lin: [
      { cmd: 'sqlmap -u "http://target.com/page?id=1"', purpose: 'Automated SQL injection testing', out: 'Parameter id is vulnerable.', note: 'Automates detection and exploitation of SQL injection.', mistake: 'Running sqlmap without permission.' }
    ],
    win: [
      { cmd: 'Test-NetConnection -ComputerName target.com -Port 443', purpose: 'Check TLS port availability', out: 'TcpTestSucceeded : True', note: 'Basic check before analyzing cryptographic configurations.', mistake: 'Assuming open port means secure configuration.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab (DVWA)',
    tools: ['Burp Suite', 'Web Browser'],
    dependencies: ['Damn Vulnerable Web App (DVWA)'],
    safety: ['Perform testing only on authorized lab environments.'],
    scenario: 'GFS requires a demonstration of how Cross-Site Scripting (XSS) can compromise a user session. You will use DVWA to execute a stored XSS attack.',
    objectives: ['Demonstrate Stored XSS and steal a session cookie.'],
    steps: [
      'Step 1: Log in to DVWA and set security level to Low.',
      'Step 2: Navigate to the "XSS (Stored)" page.',
      'Step 3: In the Name field, enter: `hacker`.',
      'Step 4: In the Message field, enter: `<script>alert(document.cookie)</script>`.',
      'Step 5: Click "Sign Guestbook".',
      'Step 6: Observe the alert box displaying the session cookie.'
    ],
    evidence: ['Screenshot of the alert box showing the PHPSESSID cookie.'],
    validation: ['You should see a pop-up alert containing the session cookie string.'],
    troubleshooting: ['If the script does not execute, ensure browser XSS protections are disabled or test on a vulnerable browser version.'],
    mitre: [{ id: 'T1189', name: 'Drive-by Compromise', tactic: 'Initial Access' }],
    cleanup: ['Clear the DVWA database to remove the stored payload.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which OWASP Top 10 vulnerability occurs when untrusted data is sent to an interpreter as part of a command or query?',
      opts: ['Cross-Site Scripting (XSS)', 'Injection', 'Broken Access Control', 'Security Misconfiguration'],
      correct: 1,
      fb: 'Injection flaws (like SQL, NoSQL, OS command, LDAP) happen when untrusted data is executed by an interpreter.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'A user alters the URL parameter `id=10` to `id=11` and accesses another user\\'s data. What type of vulnerability is this?',
      opts: ['Insecure Direct Object Reference (IDOR) / Broken Access Control', 'Cross-Site Scripting (XSS)', 'Server-Side Request Forgery (SSRF)', 'Injection'],
      correct: 0,
      fb: 'This is an example of Broken Access Control (specifically IDOR), where the server fails to verify if the user is authorized to access the requested resource.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which type of XSS is permanently saved on the target server, such as in a database or forum post?',
      opts: ['Reflected XSS', 'DOM-based XSS', 'Stored XSS', 'Blind XSS'],
      correct: 2,
      fb: 'Stored (or Persistent) XSS occurs when a malicious script is injected and stored on the server, serving the payload to subsequent visitors.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'Using parameterized queries is an effective defense against SQL Injection.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'Parameterized queries (prepared statements) ensure that the database treats user input as data, not as executable code.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'What vulnerability allows an attacker to force the web application server to make HTTP requests to an arbitrary domain of the attacker\\'s choosing?',
      opts: ['Cross-Site Request Forgery (CSRF)', 'Server-Side Request Forgery (SSRF)', 'Cross-Site Scripting (XSS)', 'XML External Entities (XXE)'],
      correct: 1,
      fb: 'SSRF occurs when a web application is fetching a remote resource without validating the user-supplied URL.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Leaving default passwords (like admin/admin) unchanged is an example of which OWASP vulnerability?',
      opts: ['Broken Authentication', 'Security Misconfiguration', 'Vulnerable and Outdated Components', 'Cryptographic Failures'],
      correct: 1,
      fb: 'Using default credentials is a classic Security Misconfiguration.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'CSRF (Cross-Site Request Forgery) attacks force an end user to execute unwanted actions on a web application in which they are currently authenticated.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'CSRF targets state-changing requests, tricking the victim\\'s browser into sending a forged request.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which mitigation technique is most effective against Cross-Site Scripting (XSS)?',
      opts: ['Parameterized Queries', 'Output Encoding and Input Validation', 'Enabling TLS', 'Implementing Captchas'],
      correct: 1,
      fb: 'Output encoding ensures that user-supplied data is treated as content rather than executable code by the browser.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Transmitting sensitive data (like passwords) over plain HTTP is an example of:',
      opts: ['Cryptographic Failures', 'Security Misconfiguration', 'Broken Access Control', 'Injection'],
      correct: 0,
      fb: 'Failing to encrypt sensitive data in transit falls under Cryptographic Failures.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'An attacker using a known vulnerability in an older version of Apache Struts is exploiting "Vulnerable and Outdated Components".',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'Using software with known vulnerabilities is exactly what this OWASP category represents.'
    }
  ],
  flashcards: [
    { f: 'SQL Injection (SQLi)', b: 'An attack that injects malicious SQL commands into input fields, allowing unauthorized access to the database.' },
    { f: 'XSS', b: 'Cross-Site Scripting; injecting malicious scripts into trusted websites, executed by the victim\\'s browser.' },
    { f: 'IDOR', b: 'Insecure Direct Object Reference; manipulating an identifier to access unauthorized data.' },
    { f: 'SSRF', b: 'Server-Side Request Forgery; forcing the server to make requests to internal or external resources.' },
    { f: 'CSRF', b: 'Cross-Site Request Forgery; tricking an authenticated user into performing unwanted actions.' }
  ],
  summary: [
    'The OWASP Top 10 is the standard for web application security risks.',
    'Injection flaws occur when untrusted data alters intended commands.',
    'Broken Access Control allows users to bypass authorization.',
    'XSS targets the user\\'s browser by injecting malicious scripts.',
    'Security Misconfiguration is a widespread and easily exploitable risk.'
  ],
  outcomes: [
    'Identify the OWASP Top 10 vulnerabilities.',
    'Explain the mechanics of Injection and XSS attacks.',
    'Propose mitigation strategies for common web application flaws.'
  ],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 60,
    difficulty: "Intermediate",
    prerequisites: ["Web Application Concepts"],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['web-app-hacking-methodology'] = {
  eyebrow: 'Module 14 · Topic 3',
  title: 'Web App Hacking Methodology',
  module: 'Phase 14: Web Application Pentester',
  sub: 'Learn the systematic, step-by-step approach to testing web applications for vulnerabilities.',
  objectives: [
    'Understand the phases of web application penetration testing.',
    'Perform footprinting and reconnaissance on web targets.',
    'Execute vulnerability scanning and manual exploitation.'
  ],
  learn: {
    simple: 'Hacking a web application isn\\'t just about randomly running tools; it requires a structured methodology. The standard methodology involves footprinting the target, identifying entry points, scanning for vulnerabilities, exploiting those vulnerabilities, and finally, maintaining access and reporting. This systematic approach ensures comprehensive coverage.',
    analogy: 'Think of the methodology like casing a bank for a heist. Footprinting is looking up the bank\\'s address and hours. Scanning is checking the locks and finding security cameras. Exploitation is picking the lock or finding an open window.',
    architecture: 'The Web Application Hacking Methodology generally follows these phases: \\n1. Footprinting (Reconnaissance): Gathering information about the target URL, IP addresses, subdomains, and technologies.\\n2. Scanning and Profiling: Crawling the site, mapping directories (using DirBuster or Gobuster), identifying application frameworks, and running automated vulnerability scanners (like Nessus or Nikto).\\n3. Vulnerability Analysis: Manually verifying the scanner findings and identifying logical flaws that scanners miss, intercepting traffic using proxies like Burp Suite.\\n4. Exploitation: Crafting payloads to exploit identified vulnerabilities (e.g., executing SQL injection to dump a database or using XSS to steal cookies).\\n5. Post-Exploitation & Reporting: Documenting findings, calculating risk scores, and providing actionable remediation advice.',
    why: 'A structured methodology ensures that pentesters do not miss critical vulnerabilities. It provides a repeatable, defensible process that organizations rely on for accurate security assessments.'
  },
  enterprise: {
    gfs: 'GFS requires all third-party pentest teams to strictly follow a documented methodology to ensure testing is thorough and does not disrupt critical trading systems.',
    windows: 'During footprinting, a pentester might discover ASP.NET stack traces that reveal internal network paths or SQL Server versions.',
    linux: 'Directory brute-forcing might reveal hidden `.git` directories or backup files (e.g., `config.php.bak`) on an Apache server.'
  },
  workflow: [
    'Step 1: Perform passive reconnaissance (WHOIS, DNS records, OSINT).',
    'Step 2: Perform active reconnaissance (Nmap port scanning, banner grabbing).',
    'Step 3: Map the application (spidering/crawling with Burp Suite or ZAP).',
    'Step 4: Discover hidden content (directory brute-forcing with Gobuster).',
    'Step 5: Test for vulnerabilities manually (intercepting and modifying requests).',
    'Step 6: Document findings and write the penetration test report.'
  ],
  diagram: {
    caption: 'Click to interact with the Hacking Methodology lifecycle',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><circle cx="300" cy="200" r="150" fill="none" stroke="#4a5568" stroke-width="4"/><circle cx="300" cy="50" r="40" fill="#3182ce"/><text x="300" y="55" fill="white" font-family="sans-serif" font-size="12" text-anchor="middle">Footprinting</text><circle cx="440" cy="110" r="40" fill="#dd6b20"/><text x="440" y="115" fill="white" font-family="sans-serif" font-size="12" text-anchor="middle">Scanning</text><circle cx="440" cy="290" r="40" fill="#e53e3e"/><text x="440" y="295" fill="white" font-family="sans-serif" font-size="12" text-anchor="middle">Analysis</text><circle cx="300" cy="350" r="40" fill="#805ad5"/><text x="300" y="355" fill="white" font-family="sans-serif" font-size="12" text-anchor="middle">Exploitation</text><circle cx="160" cy="200" r="40" fill="#38a169"/><text x="160" y="205" fill="white" font-family="sans-serif" font-size="12" text-anchor="middle">Reporting</text><path d="M 335 70 L 410 95" stroke="#718096" stroke-width="2" marker-end="url(#arrow_meth)"/><path d="M 440 150 L 440 250" stroke="#718096" stroke-width="2" marker-end="url(#arrow_meth)"/><path d="M 410 310 L 335 335" stroke="#718096" stroke-width="2" marker-end="url(#arrow_meth)"/><path d="M 265 330 L 185 230" stroke="#718096" stroke-width="2" marker-end="url(#arrow_meth)"/><path d="M 185 170 L 265 70" stroke="#718096" stroke-width="2" marker-end="url(#arrow_meth)"/><defs><marker id="arrow_meth" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#718096"/></marker></defs></svg>'
  },
  commands: {
    lin: [
      { cmd: 'gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt', purpose: 'Directory brute-forcing', out: '/admin (Status: 401)', note: 'Discovers hidden directories and files.', mistake: 'Using a massive wordlist without rate limiting, causing denial of service.' }
    ],
    win: [
      { cmd: 'nslookup -type=any target.com', purpose: 'DNS Footprinting', out: 'Nameservers and MX records', note: 'Basic information gathering.', mistake: 'Relying solely on local DNS caches.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Gobuster', 'Burp Suite'],
    dependencies: [],
    safety: ['Only run directory brute-forcing against authorized targets.'],
    scenario: 'GFS has authorized a pentest on a staging server. You need to map out the application and find hidden administrative interfaces.',
    objectives: ['Perform directory discovery and map the application structure.'],
    steps: [
      'Step 1: Open a terminal in Kali Linux.',
      'Step 2: Run Gobuster to find hidden directories: `gobuster dir -u http://192.168.1.100 -w /usr/share/wordlists/dirb/common.txt`',
      'Step 3: Note any directories returning 200 OK or 301 Redirect (e.g., `/admin`, `/backup`).',
      'Step 4: Configure your browser to use Burp Suite as a proxy.',
      'Step 5: Browse the application normally to populate the Burp Suite site map.',
      'Step 6: Review the Target tab in Burp to analyze the application tree.'
    ],
    evidence: ['Gobuster output showing discovered paths.', 'Burp Suite Site Map screenshot.'],
    validation: ['You should identify at least one hidden directory not linked from the main page.'],
    troubleshooting: ['If Gobuster fails, ensure the target IP is correct and the wordlist path exists.'],
    mitre: [{ id: 'T1595', name: 'Active Scanning', tactic: 'Reconnaissance' }],
    cleanup: ['Stop Gobuster and disable the browser proxy setting.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which phase of the web hacking methodology involves using search engines, WHOIS, and DNS lookups?',
      opts: ['Scanning', 'Footprinting (Reconnaissance)', 'Exploitation', 'Analysis'],
      correct: 1,
      fb: 'Footprinting gathers passive information before interacting deeply with the target.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary purpose of tools like Gobuster or DirBuster?',
      opts: ['To exploit SQL injection', 'To intercept HTTP traffic', 'To brute-force directories and files', 'To encrypt communications'],
      correct: 2,
      fb: 'These tools brute-force URIs to find hidden content on web servers.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'Spidering or crawling a web application is a manual process that cannot be automated.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'Spidering is highly automated using tools like Burp Suite, ZAP, or wget to map the application.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'During which phase would a pentester modify HTTP requests using an intercepting proxy to test for business logic flaws?',
      opts: ['Footprinting', 'Vulnerability Analysis / Manual Testing', 'Reporting', 'Automated Scanning'],
      correct: 1,
      fb: 'Manual testing via an intercepting proxy allows testers to find logical flaws that automated scanners miss.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which HTTP status code during directory brute-forcing indicates a redirect?',
      opts: ['200', '301', '403', '500'],
      correct: 1,
      fb: '3xx codes, like 301 Moved Permanently or 302 Found, indicate redirection.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Automated vulnerability scanners can identify 100% of web application vulnerabilities.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'Scanners often miss complex logical flaws and authorization bypass issues, requiring manual testing.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the final phase of a professional penetration test?',
      opts: ['Exploitation', 'Post-Exploitation', 'Reporting', 'Scanning'],
      correct: 2,
      fb: 'Reporting documents the findings, risks, and remediation steps, delivering value to the client.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'If a pentester discovers an exposed `.git` directory on a web server, what phase are they likely in, and what is the risk?',
      opts: ['Footprinting; Source code disclosure', 'Scanning; Source code disclosure', 'Exploitation; Remote code execution', 'Reporting; Low risk'],
      correct: 1,
      fb: 'Found during scanning/enumeration, an exposed .git directory can allow an attacker to download the entire source code repository.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'A 403 Forbidden status code means the directory or file does not exist.',
      opts: ['True', 'False'],
      correct: 1,
      fb: '403 means the resource exists, but the server is refusing to allow access (permissions issue).'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which technique is used to bypass client-side validation (like HTML5 "required" attributes)?',
      opts: ['Social Engineering', 'SQL Injection', 'Intercepting and modifying requests with a proxy', 'DNS cache poisoning'],
      correct: 2,
      fb: 'Client-side controls can easily be bypassed by intercepting the request after it leaves the browser and altering the data before it reaches the server.'
    }
  ],
  flashcards: [
    { f: 'Footprinting', b: 'The reconnaissance phase of gathering information about a target system or network.' },
    { f: 'Spidering/Crawling', b: 'Automatically discovering all links and resources on a web application.' },
    { f: 'Directory Brute-Forcing', b: 'Using a wordlist to guess the names of hidden directories and files on a web server.' },
    { f: 'Intercepting Proxy', b: 'A tool (like Burp Suite) that sits between the browser and the server to view and modify HTTP traffic.' },
    { f: 'Vulnerability Scanning', b: 'Using automated tools to identify known security weaknesses.' }
  ],
  summary: [
    'A structured methodology is essential for comprehensive web application testing.',
    'Footprinting and scanning map the attack surface and discover hidden endpoints.',
    'Automated scanners are useful but must be supplemented with manual testing.',
    'Intercepting proxies are the most critical tool for analyzing request/response data.',
    'Thorough reporting provides actionable remediation advice to the organization.'
  ],
  outcomes: [
    'Describe the phases of the web application hacking methodology.',
    'Utilize directory brute-forcing tools to discover hidden content.',
    'Explain the importance of manual vulnerability analysis.'
  ],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 50,
    difficulty: "Intermediate",
    prerequisites: ["Web Application Threats"],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['web-app-security-tools'] = {
  eyebrow: 'Module 14 · Topic 4',
  title: 'Web Application Security Tools',
  module: 'Phase 14: Web Application Pentester',
  sub: 'Master the industry-standard tools used for web application penetration testing.',
  objectives: [
    'Configure and use Burp Suite for intercepting and modifying HTTP traffic.',
    'Utilize OWASP ZAP as an alternative web application scanner and proxy.',
    'Understand specialized tools for SQL injection and directory discovery.'
  ],
  learn: {
    simple: 'A web pentester is only as good as their tools. Intercepting proxies like Burp Suite and OWASP ZAP are the core of a pentester\\'s toolkit, allowing them to pause, inspect, and modify traffic between their browser and the web server. Other specialized tools automate specific tasks, like `sqlmap` for databases or `gobuster` for finding hidden files.',
    analogy: 'Using an intercepting proxy is like being a mail sorter who can open, read, change, and reseal letters before they reach their destination. You control everything passing through.',
    architecture: 'Burp Suite Professional is the industry standard. It features the Proxy (for interception), Repeater (for manually modifying and resending requests), Intruder (for brute-forcing and fuzzing parameters), and a powerful automated Scanner. \\n\\nOWASP Zed Attack Proxy (ZAP) is a robust, free, and open-source alternative with similar capabilities. Specialized tools augment these proxies: `sqlmap` automates the complex process of detecting and exploiting SQL injection flaws. `Nikto` is a web server scanner that tests for dangerous files, outdated server software, and specific problems. Integrating these tools allows for comprehensive coverage of the OWASP Top 10.',
    why: 'Mastery of these tools is mandatory for any cybersecurity professional working in web security. They dramatically increase the efficiency of finding and verifying vulnerabilities.'
  },
  enterprise: {
    gfs: 'GFS security engineers use Burp Suite Professional daily to assess custom-built trading applications before they are pushed to the production environment.',
    windows: 'Tools like Burp Suite are cross-platform (Java-based) and run perfectly on Windows pentesting workstations.',
    linux: 'Kali Linux comes pre-installed with the community editions of Burp Suite, OWASP ZAP, sqlmap, and Nikto, making it an ideal pentesting OS.'
  },
  workflow: [
    'Step 1: Configure the browser to route traffic through the proxy (e.g., Burp on 127.0.0.1:8080).',
    'Step 2: Install the proxy\\'s CA certificate in the browser to intercept HTTPS traffic.',
    'Step 3: Browse the target application to populate the Site Map.',
    'Step 4: Send interesting requests to Repeater to manipulate parameters manually.',
    'Step 5: Use Intruder to fuzz specific input fields with payload lists.',
    'Step 6: Run specialized tools (sqlmap, Nikto) against identified targets.'
  ],
  diagram: {
    caption: 'Click to interact with the Intercepting Proxy workflow',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="150" width="100" height="80" fill="#2d3748" rx="10"/><text x="100" y="195" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">Browser</text><rect x="250" y="120" width="100" height="140" fill="#dd6b20" rx="10"/><text x="300" y="180" fill="white" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Burp</text><text x="300" y="200" fill="white" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Suite</text><text x="300" y="230" fill="white" font-family="sans-serif" font-size="10" text-anchor="middle">(Intercepting Proxy)</text><rect x="450" y="150" width="100" height="80" fill="#2d3748" rx="10"/><text x="500" y="195" fill="white" font-family="sans-serif" font-size="14" text-anchor="middle">Web Server</text><path d="M 150 170 L 250 170" stroke="#718096" stroke-width="3" marker-end="url(#arrow_tool)"/><text x="200" y="160" fill="#a0aec0" font-family="sans-serif" font-size="10" text-anchor="middle">Request</text><path d="M 350 170 L 450 170" stroke="#718096" stroke-width="3" stroke-dasharray="4,4" marker-end="url(#arrow_tool)"/><text x="400" y="160" fill="#e2e8f0" font-family="sans-serif" font-size="10" text-anchor="middle">Modified Request</text><path d="M 450 210 L 350 210" stroke="#48bb78" stroke-width="3" marker-end="url(#arrow_tool_g)"/><text x="400" y="230" fill="#a0aec0" font-family="sans-serif" font-size="10" text-anchor="middle">Response</text><path d="M 250 210 L 150 210" stroke="#48bb78" stroke-width="3" marker-end="url(#arrow_tool_g)"/><text x="200" y="230" fill="#a0aec0" font-family="sans-serif" font-size="10" text-anchor="middle">Response</text><defs><marker id="arrow_tool" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#718096"/></marker><marker id="arrow_tool_g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#48bb78"/></marker></defs></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nikto -h http://target.com', purpose: 'Web Server Scanning', out: 'Server is Apache/2.4.41... OSVDB-3092: /cgi-bin/test-cgi found', note: 'Fast scanner for outdated server software and misconfigurations.', mistake: 'Running Nikto creates a massive amount of noisy logs on the target.' }
    ],
    win: [
      { cmd: 'Start-Process "C:\\Program Files\\BurpSuiteCommunity\\BurpSuiteCommunity.exe"', purpose: 'Launch Burp Suite', out: 'GUI opens', note: 'Starting the primary tool on Windows.', mistake: 'Not having Java installed or configured correctly.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Burp Suite', 'Web Browser'],
    dependencies: [],
    safety: ['Do not intercept traffic outside of the lab environment.'],
    scenario: 'GFS needs to verify that client-side validation can be bypassed. You will use Burp Suite Repeater to modify a request and bypass a price check on an e-commerce site.',
    objectives: ['Configure Burp Suite proxy and use Repeater to modify HTTP requests.'],
    steps: [
      'Step 1: Open Burp Suite and navigate to the Proxy -> Intercept tab. Ensure Intercept is ON.',
      'Step 2: Configure your browser to use 127.0.0.1:8080 as an HTTP proxy.',
      'Step 3: Navigate to the target web store and add an item to the cart.',
      'Step 4: The request will freeze in the browser. Look at Burp Suite; the request is intercepted.',
      'Step 5: Right-click the request and select "Send to Repeater".',
      'Step 6: Go to the Repeater tab. Change the "price=100" parameter to "price=1".',
      'Step 7: Click "Send" and analyze the Response to confirm the item was added for $1.'
    ],
    evidence: ['Screenshot of the modified request in Burp Repeater and the successful 200 OK response.'],
    validation: ['You should see the price manipulation reflected in the server response.'],
    troubleshooting: ['If the browser shows an SSL error, ensure the Burp CA certificate is installed in the browser.'],
    mitre: [{ id: 'T1190', name: 'Exploit Public-Facing Application', tactic: 'Initial Access' }],
    cleanup: ['Turn Intercept OFF and remove proxy settings from the browser.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which tool is widely considered the industry standard intercepting proxy for web application pentesting?',
      opts: ['Wireshark', 'Nmap', 'Burp Suite', 'Metasploit'],
      correct: 2,
      fb: 'Burp Suite is the premier tool for intercepting, modifying, and analyzing web traffic.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In Burp Suite, what is the primary function of the "Repeater" tool?',
      opts: ['Automated vulnerability scanning', 'Manually modifying and resending individual HTTP requests', 'Brute-forcing login forms', 'Mapping the application directory structure'],
      correct: 1,
      fb: 'Repeater allows a tester to manually alter request parameters and observe the server\\'s response repeatedly.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'OWASP ZAP is a commercial, paid-only tool.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. OWASP Zed Attack Proxy (ZAP) is a free, open-source web application security scanner.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which command-line tool is specifically designed to automate the detection and exploitation of SQL injection flaws?',
      opts: ['sqlmap', 'Nikto', 'Gobuster', 'Hydra'],
      correct: 0,
      fb: 'sqlmap is a powerful open-source penetration testing tool that automates detecting and exploiting SQL injection flaws.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'When intercepting HTTPS traffic with Burp Suite, why does the browser initially display a certificate warning?',
      opts: ['Burp Suite corrupts the traffic', 'The server is offline', 'The browser does not trust Burp\\'s automatically generated CA certificate', 'HTTPS cannot be intercepted'],
      correct: 2,
      fb: 'Burp acts as a Man-in-the-Middle (MitM). To decrypt HTTPS, it presents its own certificate, which the browser must be configured to trust.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which Burp Suite tool is best suited for fuzzing input fields or brute-forcing passwords by sending numerous modified requests?',
      opts: ['Repeater', 'Intruder', 'Decoder', 'Comparer'],
      correct: 1,
      fb: 'Intruder is a highly configurable tool for automating customized attacks against web applications.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'Nikto is a stealthy tool that bypasses Intrusion Detection Systems (IDS).',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Nikto is notoriously noisy and will trigger almost any IDS/IPS.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary function of the "Decoder" tab in Burp Suite?',
      opts: ['Decrypting SSL traffic', 'Encoding and decoding data (e.g., Base64, URL encoding, HTML encoding)', 'Comparing two different HTTP responses', 'Generating reports'],
      correct: 1,
      fb: 'Decoder is used for manually converting data between common encoding and hashing formats.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Browser Developer Tools (F12) can be used as a basic alternative to intercepting proxies for viewing network requests.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'True. The Network tab in DevTools shows requests and responses, though it lacks the advanced modification features of a proxy.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'If a pentester finds an HTTP request containing `Authorization: Basic YWRtaW46cGFzc3dvcmQ=`, what tool within Burp Suite would quickly reveal the credentials?',
      opts: ['Intruder', 'Scanner', 'Decoder', 'Spider'],
      correct: 2,
      fb: 'The string is Base64 encoded. The Decoder tool can quickly decode it to plain text.'
    }
  ],
  flashcards: [
    { f: 'Burp Suite', b: 'An integrated platform for performing security testing of web applications, featuring an intercepting proxy.' },
    { f: 'OWASP ZAP', b: 'A free, open-source penetration testing tool maintained by OWASP for finding vulnerabilities in web applications.' },
    { f: 'sqlmap', b: 'An open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws.' },
    { f: 'Burp Repeater', b: 'A tool for manually modifying and reissuing individual HTTP requests, and analyzing their responses.' },
    { f: 'Burp Intruder', b: 'A tool for automating customized attacks against web applications, used for fuzzing and brute-forcing.' }
  ],
  summary: [
    'Intercepting proxies (Burp Suite, ZAP) are essential for web application pentesting.',
    'Proxies allow manipulation of HTTP/HTTPS traffic to test for business logic flaws and bypass client-side controls.',
    'Burp Repeater is used for manual testing, while Intruder is used for automated fuzzing.',
    'sqlmap is the premier tool for automating SQL injection attacks.',
    'Installing the proxy CA certificate is necessary to intercept encrypted HTTPS traffic.'
  ],
  outcomes: [
    'Configure and use an intercepting proxy.',
    'Utilize Burp Repeater to manually test for vulnerabilities.',
    'Describe the use cases for sqlmap and Nikto.'
  ],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 60,
    difficulty: "Intermediate",
    prerequisites: ["Web Application Hacking Methodology"],
    lastReviewed: "2026-07-18"
  }
};
"""

def inject_content():
    try:
        with open(TARGET_HTML, 'r', encoding='utf-8') as f:
            content = f.read()

        marker = "// ── TAB WIRING ──"
        if marker not in content:
            print("Error: Marker not found in frontend/index.html")
            sys.exit(1)

        # Inject the new content right before the marker
        updated_content = content.replace(marker, CONTENT + "\n\n" + marker)

        with open(TARGET_HTML, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("Successfully injected Module 14 content into frontend/index.html")

    except Exception as e:
        print(f"Failed to inject content: {e}")
        sys.exit(1)

if __name__ == "__main__":
    inject_content()
