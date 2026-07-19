import os
import sys

CONTENT = """
CONTENT['web-server-concepts'] = {
  eyebrow: 'Module 13 · Topic 1',
  title: 'Web Server Concepts',
  module: 'Phase 13: Web Application Pentester',
  sub: 'Understanding the foundational architecture and operation of web servers.',
  objectives: ['Understand web server architecture', 'Identify key components of a web server', 'Explain the HTTP request/response process'],
  learn: {
    simple: 'Web servers are software and hardware systems that serve content to the World Wide Web. They process HTTP requests from clients and return HTTP responses, typically containing HTML pages, images, or other web resources. Understanding how they work is fundamental to discovering and exploiting their vulnerabilities.',
    analogy: 'Think of a web server as a librarian. You (the client) ask for a specific book (the URL). The librarian checks the catalog (the routing/configuration), finds the book on the shelf (the file system or database), and hands it to you (the response).',
    architecture: 'At a high level, a web server consists of a physical server, an operating system, and web server software (like Apache, Nginx, or IIS). When a client sends an HTTP request, the web server software parses the request, determines the appropriate handler (e.g., static file serving or dynamic content generation via PHP/Python), processes the request, and formulates an HTTP response. The architecture often includes load balancers, reverse proxies, and application servers working in tandem to handle high traffic and complex processing.',
    why: 'In enterprise cybersecurity, web servers are often public-facing and form the perimeter of the network. A compromised web server can lead to data breaches, defacement, or serve as a pivot point to attack internal networks.'
  },
  enterprise: {
    gfs: 'Global Financial Services relies on hundreds of web servers to handle customer banking portals, API endpoints, and internal employee dashboards.',
    windows: 'Windows environments typically use Internet Information Services (IIS). IIS integrates tightly with Windows Server and Active Directory for authentication.',
    linux: 'Linux environments predominantly use Apache or Nginx. Nginx is favored for its asynchronous event-driven architecture, making it highly efficient for serving static content and acting as a reverse proxy.'
  },
  workflow: ['Step 1: Client resolves DNS to get IP address.', 'Step 2: Client establishes TCP connection (and TLS if HTTPS).', 'Step 3: Client sends HTTP request.', 'Step 4: Web server processes request.', 'Step 5: Web server sends HTTP response.', 'Step 6: Client renders the response.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a2e"/><text x="50%" y="50%" font-size="24" fill="white" text-anchor="middle">Web Server Architecture Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'curl -I http://target.com', purpose: 'Fetch HTTP Headers', out: 'Server banner and header details', note: 'Useful for identifying server version', mistake: 'Missing the -I flag returns full page content instead of just headers' }
    ],
    win: [
      { cmd: 'Invoke-WebRequest -Uri http://target.com -Method Default', purpose: 'Fetch web page details', out: 'HTML content and headers', note: 'PowerShell alternative to curl', mistake: 'Not handling self-signed certificates' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['curl', 'netcat'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS needs to audit the headers of a newly deployed web application.',
    objectives: ['Identify web server version from HTTP headers'],
    steps: ['Step 1: Run `curl -I http://target-web-server`.', 'Step 2: Analyze the Server header in the response.'],
    evidence: ['Terminal output showing the Server header.'],
    validation: ['You should see the web server version (e.g., Apache/2.4.41).'],
    troubleshooting: ['If connection refused, check if the web server is running.'],
    mitre: [{ id: 'T1592', name: 'Gather Victim Host Information', tactic: 'Reconnaissance' }],
    cleanup: ['No specific cleanup required.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which of the following is a common web server software for Windows?',
      opts: ['Apache', 'Nginx', 'IIS', 'Lighttpd'],
      correct: 2,
      fb: 'Internet Information Services (IIS) is the standard web server for Windows environments.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'What is the default port for HTTP traffic?',
      opts: ['21', '22', '80', '443'],
      correct: 2,
      fb: 'Port 80 is the default port for HTTP traffic, while 443 is for HTTPS.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which HTTP method is typically used to request a web page?',
      opts: ['POST', 'GET', 'PUT', 'DELETE'],
      correct: 1,
      fb: 'The GET method requests a representation of the specified resource.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does a 404 HTTP status code mean?',
      opts: ['OK', 'Forbidden', 'Not Found', 'Internal Server Error'],
      correct: 2,
      fb: '404 indicates that the server cannot find the requested resource.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which architectural component is often placed in front of a web server to distribute traffic?',
      opts: ['Database server', 'Load balancer', 'File server', 'Mail server'],
      correct: 1,
      fb: 'A load balancer distributes network traffic across multiple servers.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the purpose of the Server HTTP header?',
      opts: ['To define the character set', 'To indicate the software used by the origin server', 'To set a cookie', 'To specify cache directives'],
      correct: 1,
      fb: 'The Server header contains information about the software used by the origin server.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which protocol secures HTTP traffic?',
      opts: ['FTP', 'SSH', 'TLS/SSL', 'IPsec'],
      correct: 2,
      fb: 'TLS/SSL is used to encrypt and secure HTTP traffic, making it HTTPS.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'In the context of Nginx, what is its primary architecture type?',
      opts: ['Process-driven', 'Thread-driven', 'Event-driven', 'Connection-driven'],
      correct: 2,
      fb: 'Nginx is known for its asynchronous, event-driven architecture.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'Apache is only available on Linux operating systems.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'Apache is cross-platform and can also be run on Windows and other OSs.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'A reverse proxy sits behind a web server to manage database connections.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'A reverse proxy typically sits IN FRONT of web servers to direct client requests to the appropriate backend server.'
    }
  ],
  flashcards: [
    { f: 'Web Server', b: 'Software or hardware that serves web content to clients over HTTP/HTTPS.' },
    { f: 'IIS', b: 'Internet Information Services, a web server software created by Microsoft for Windows.' },
    { f: 'Nginx', b: 'A popular open-source web server known for high performance and acting as a reverse proxy.' }
  ],
  summary: ['Web servers are the foundation of the World Wide Web.', 'Understanding HTTP requests and responses is crucial.', 'Common web servers include Apache, Nginx, and IIS.', 'Web servers are a common target for cyber attacks.', 'Load balancers and proxies are often part of web server architecture.'],
  outcomes: ['Identify web server components.', 'Explain HTTP request methods.', 'Differentiate between common web server software.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['web-server-attacks'] = {
  eyebrow: 'Module 13 · Topic 2',
  title: 'Web Server Attacks',
  module: 'Phase 13: Web Application Pentester',
  sub: 'Exploring common attack vectors targeting web server infrastructure.',
  objectives: ['Identify common web server attacks', 'Understand Denial of Service (DoS) against web servers', 'Explain directory traversal attacks'],
  learn: {
    simple: 'Web server attacks target the underlying infrastructure rather than just the application running on it. These attacks aim to exploit misconfigurations, software vulnerabilities, or logical flaws to gain unauthorized access, cause denial of service, or deface the website. Attackers use various techniques like directory traversal to access unauthorized files, or DoS attacks to exhaust server resources.',
    analogy: 'Imagine a bank building (the web server). An attacker might try to pick the locks on the back door (exploiting a vulnerability), impersonate a security guard (authentication bypass), or block the main entrance with a large crowd so legitimate customers cannot enter (Denial of Service).',
    architecture: 'Web servers process incoming requests based on specific rules and configurations. Attacks often involve crafting malicious HTTP requests that manipulate these rules. For instance, a directory traversal attack (`../`) tricks the server into accessing files outside the web root. Buffer overflow attacks send more data than the server expects, causing it to crash or execute arbitrary code. HTTP request smuggling exploits discrepancies in how frontend proxies and backend servers parse HTTP requests.',
    why: 'Web servers are high-value targets because they often host sensitive data and provide a gateway to internal corporate networks. Understanding these attacks is essential for securing the perimeter.'
  },
  enterprise: {
    gfs: 'At Global Financial Services, an unpatched web server could lead to a massive data breach, exposing customer financial records and severely damaging the company reputation.',
    windows: 'IIS servers can be targeted by specific attacks like the MS15-034 HTTP.sys remote code execution vulnerability if not properly patched.',
    linux: 'Apache servers can be vulnerable to attacks like Slowloris, which exhausts connection pools, or exploits targeting specific Apache modules (e.g., mod_cgi).'
  },
  workflow: ['Step 1: Attacker identifies target web server.', 'Step 2: Attacker probes for vulnerabilities (e.g., misconfigurations, outdated software).', 'Step 3: Attacker crafts a malicious payload.', 'Step 4: Attacker sends payload in an HTTP request.', 'Step 5: Server executes payload or crashes.', 'Step 6: Attacker achieves objective (access, DoS, etc.).'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a2e"/><text x="50%" y="50%" font-size="24" fill="white" text-anchor="middle">Directory Traversal Attack Flow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'curl "http://target.com/page.php?file=../../../../etc/passwd"', purpose: 'Directory Traversal Attempt', out: 'Contents of /etc/passwd if vulnerable', note: 'Basic test for local file inclusion/directory traversal', mistake: 'Not URL encoding characters if required by a WAF' }
    ],
    win: [
      { cmd: 'Invoke-WebRequest -Uri "http://target.com/page.php?file=..\\\\..\\\\..\\\\..\\\\Windows\\\\win.ini"', purpose: 'Directory Traversal on Windows', out: 'Contents of win.ini if vulnerable', note: 'Windows uses backslashes for paths', mistake: 'Forgetting to test both forward and backslashes' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['curl', 'Burp Suite'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS suspects an internal file server is vulnerable to directory traversal.',
    objectives: ['Execute a successful directory traversal attack to read a local file.'],
    steps: ['Step 1: Access the vulnerable web application.', 'Step 2: Identify a parameter that fetches a file.', 'Step 3: Manipulate the parameter using `../` to access `/etc/passwd`.'],
    evidence: ['Screenshot of the `/etc/passwd` contents displayed in the browser or terminal.'],
    validation: ['You should see the system user list, starting with `root:x:0:0:root:/root:/bin/bash`.'],
    troubleshooting: ['If it fails, try URL encoding the `../` payload as `%2e%2e%2f`.'],
    mitre: [{ id: 'T1190', name: 'Exploit Public-Facing Application', tactic: 'Initial Access' }],
    cleanup: ['Report the vulnerability to the lab administrator.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which attack aims to make a web server unavailable to legitimate users?',
      opts: ['SQL Injection', 'Cross-Site Scripting', 'Denial of Service (DoS)', 'Directory Traversal'],
      correct: 2,
      fb: 'DoS attacks aim to overwhelm the server, making it unavailable.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the goal of a Directory Traversal attack?',
      opts: ['To execute code on the server', 'To access files outside the web root', 'To inject malicious scripts into a webpage', 'To steal session cookies'],
      correct: 1,
      fb: 'Directory traversal aims to read files on the server that should not be accessible.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which attack involves sending partial HTTP requests to exhaust server connections?',
      opts: ['SYN Flood', 'Ping of Death', 'Slowloris', 'Smurf Attack'],
      correct: 2,
      fb: 'Slowloris keeps connections open by sending partial HTTP requests slowly.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Website defacement typically involves:',
      opts: ['Stealing the database', 'Altering the visual appearance of the site', 'Overwhelming the server with traffic', 'Intercepting user communications'],
      correct: 1,
      fb: 'Defacement is the unauthorized modification of a websites appearance.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'HTTP Request Smuggling exploits discrepancies between:',
      opts: ['The client browser and the server', 'A frontend proxy and a backend server', 'Two different backend servers', 'The web server and the database'],
      correct: 1,
      fb: 'It exploits how different servers (like a proxy and a backend) interpret ambiguous HTTP requests.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'A vulnerability in a web server software itself (like an unpatched Apache version) is an example of:',
      opts: ['A logical flaw', 'An infrastructure vulnerability', 'A client-side vulnerability', 'A social engineering attack'],
      correct: 1,
      fb: 'Unpatched server software is an infrastructure-level vulnerability.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which character sequence is typically used in a basic Directory Traversal attack?',
      opts: ['//', '..', '../', '!!'],
      correct: 2,
      fb: 'The `../` sequence is used to move up one directory level.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What type of attack leverages thousands of compromised computers to attack a single web server?',
      opts: ['DoS', 'DDoS', 'Phishing', 'Man-in-the-Middle'],
      correct: 1,
      fb: 'Distributed Denial of Service (DDoS) uses multiple sources to overwhelm a target.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'Web server defacement is usually harmless and only affects the sites appearance.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'While it changes appearance, it often indicates a deeper compromise (like server root access) and damages reputation.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Directory traversal attacks can be completely prevented by simply filtering the `../` string.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'Attackers can use encodings (like `%2e%2e%2f`) or other path manipulation techniques to bypass simple string filters.'
    }
  ],
  flashcards: [
    { f: 'DoS Attack', b: 'Denial of Service; an attack meant to shut down a machine or network, making it inaccessible.' },
    { f: 'Directory Traversal', b: 'An exploit that allows an attacker to access restricted directories and files outside of the web root.' },
    { f: 'Slowloris', b: 'A type of DoS attack that relies on keeping many connections to the target web server open and holding them open as long as possible.' }
  ],
  summary: ['Web server attacks target the infrastructure and software.', 'Directory traversal aims to read unauthorized files.', 'DoS attacks seek to exhaust server resources.', 'Web server software vulnerabilities must be patched promptly.', 'Misconfigurations can lead to severe security breaches.'],
  outcomes: ['Describe directory traversal attacks.', 'Explain the mechanics of a Slowloris attack.', 'Identify the impact of web server defacement.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['web-server-attack-methodology'] = {
  eyebrow: 'Module 13 · Topic 3',
  title: 'Web Server Attack Methodology',
  module: 'Phase 13: Web Application Pentester',
  sub: 'The structured approach attackers use to compromise web servers.',
  objectives: ['Understand the phases of a web server attack', 'Explain information gathering techniques', 'Describe exploitation and post-exploitation steps'],
  learn: {
    simple: 'A web server attack methodology provides a structured approach for penetration testers (and attackers) to identify and exploit vulnerabilities systematically. It typically involves information gathering (reconnaissance), web server footprinting, vulnerability scanning, exploitation, and post-exploitation. Following a methodology ensures thorough testing and minimizes the chance of missing critical flaws.',
    analogy: 'Think of a web server attack methodology like planning a bank heist. First, you scout the location (Information Gathering). Then, you check the doors and windows (Footprinting & Scanning). Next, you pick a lock (Exploitation). Finally, you enter the vault and hide your tracks (Post-Exploitation).',
    architecture: 'The methodology begins with passive and active reconnaissance to identify the web servers IP address, domain, and open ports. Footprinting involves identifying the web server software, version, and operating system (OS banner grabbing). Vulnerability scanning uses automated tools to find known flaws in the identified software. Exploitation involves using specialized tools or manual techniques to leverage those flaws. Post-exploitation includes maintaining access, privilege escalation, and covering tracks.',
    why: 'In enterprise cybersecurity, having a formal methodology is crucial for conducting comprehensive penetration tests. It ensures consistent, repeatable, and thorough assessments of web server security posture.'
  },
  enterprise: {
    gfs: 'GFS employs a strict penetration testing methodology to regularly assess its web infrastructure, ensuring compliance with financial regulations.',
    windows: 'When targeting Windows environments, the methodology often focuses on identifying IIS versions and enumerating accessible ASP.NET applications.',
    linux: 'For Linux environments, the methodology heavily involves identifying specific Apache/Nginx modules and looking for misconfigured permissions on configuration files.'
  },
  workflow: ['Step 1: Information Gathering (Whois, DNS records).', 'Step 2: Web Server Footprinting (Banner grabbing, discovering hidden paths).', 'Step 3: Vulnerability Scanning (Using tools like Nikto or Nessus).', 'Step 4: Exploitation (Exploiting identified vulnerabilities).', 'Step 5: Maintaining Access (Web shells, backdoors).', 'Step 6: Covering Tracks (Clearing logs).'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a2e"/><text x="50%" y="50%" font-size="24" fill="white" text-anchor="middle">Attack Methodology Stages</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -sV -p 80,443 target.com', purpose: 'Port and Version Scanning', out: 'Open ports and service versions', note: 'Essential for the footprinting phase', mistake: 'Scanning without authorization' }
    ],
    win: [
      { cmd: 'Test-NetConnection -ComputerName target.com -Port 80', purpose: 'Check port accessibility', out: 'TCP connection status', note: 'Basic connectivity check in Windows', mistake: 'Assuming a closed port means the server is down' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nmap', 'Netcat', 'Searchsploit'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS has tasked you with executing the first three phases of the web server attack methodology against a staging server.',
    objectives: ['Perform footprinting and identify a vulnerability.'],
    steps: ['Step 1: Use `nmap -sV` to identify the web server version.', 'Step 2: Use `searchsploit <version>` to find known exploits.', 'Step 3: Document your findings.'],
    evidence: ['Nmap output showing the server version and Searchsploit output showing related exploits.'],
    validation: ['You should successfully identify a specific CVE associated with the running web server version.'],
    troubleshooting: ['If nmap shows filtered ports, check if a firewall is blocking the scan.'],
    mitre: [{ id: 'T1592', name: 'Gather Victim Host Information', tactic: 'Reconnaissance' }],
    cleanup: ['No specific cleanup required.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Which phase of the web server attack methodology involves banner grabbing?',
      opts: ['Exploitation', 'Web Server Footprinting', 'Covering Tracks', 'Post-Exploitation'],
      correct: 1,
      fb: 'Banner grabbing is a key technique in Web Server Footprinting to identify server software and versions.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary purpose of vulnerability scanning?',
      opts: ['To exploit the server', 'To identify known security flaws in the server software', 'To delete log files', 'To perform a DoS attack'],
      correct: 1,
      fb: 'Vulnerability scanning automates the process of finding known flaws based on identified versions.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Uploading a web shell occurs during which phase?',
      opts: ['Information Gathering', 'Scanning', 'Maintaining Access (Post-Exploitation)', 'Footprinting'],
      correct: 2,
      fb: 'A web shell provides persistent access to the compromised server, a core post-exploitation goal.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is an active footprinting technique?',
      opts: ['Searching Google for the target domain', 'Querying the Whois database', 'Sending HTTP OPTIONS requests to the server', 'Looking up DNS records'],
      correct: 2,
      fb: 'Sending requests directly to the target server is an active technique.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Why do attackers cover their tracks?',
      opts: ['To improve server performance', 'To evade detection and maintain access', 'To patch the vulnerability they used', 'To make the website look better'],
      correct: 1,
      fb: 'Covering tracks delays incident response and helps the attacker maintain persistence.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which nmap flag is used specifically for service version detection during footprinting?',
      opts: ['-sS', '-sV', '-O', '-p-'],
      correct: 1,
      fb: 'The -sV flag instructs nmap to probe open ports to determine service and version info.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a common method for covering tracks on a Linux web server?',
      opts: ['Installing an antivirus', 'Clearing the /var/log/apache2/access.log file', 'Restarting the server', 'Changing the website background'],
      correct: 1,
      fb: 'Attackers manipulate or clear log files in /var/log to hide their activities.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Exploitation is the process of:',
      opts: ['Finding out the IP address', 'Taking advantage of a vulnerability to gain unauthorized access', 'Scanning for open ports', 'Registering a domain name'],
      correct: 1,
      fb: 'Exploitation is the actual execution of an attack against a identified vulnerability.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Information gathering should always involve direct interaction with the target web server.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'Passive information gathering avoids direct interaction to remain undetected.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'A web shell allows an attacker to execute OS commands on the compromised server via a web browser.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'A web shell acts as a command-line interface accessible over the web.'
    }
  ],
  flashcards: [
    { f: 'Footprinting', b: 'The process of gathering information about a target network and its environment.' },
    { f: 'Banner Grabbing', b: 'A technique used to glean information about a computer system on a network and the services running on its open ports.' },
    { f: 'Web Shell', b: 'A malicious script uploaded to a web server to grant the attacker remote administrative control.' }
  ],
  summary: ['A structured methodology is essential for thorough web server testing.', 'Footprinting identifies the server OS, software, and version.', 'Vulnerability scanning automates flaw discovery.', 'Exploitation leverages flaws to gain access.', 'Post-exploitation involves maintaining access and covering tracks.'],
  outcomes: ['List the phases of a web server attack.', 'Differentiate between passive and active footprinting.', 'Explain the purpose of a web shell.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['web-server-security-tools'] = {
  eyebrow: 'Module 13 · Topic 4',
  title: 'Web Server Security Tools',
  module: 'Phase 13: Web Application Pentester',
  sub: 'Tools used to identify vulnerabilities and secure web servers.',
  objectives: ['Identify key web server security tools', 'Understand the function of a Web Application Firewall (WAF)', 'Learn to use web server vulnerability scanners'],
  learn: {
    simple: 'Securing web servers requires a combination of proactive scanning tools and defensive mechanisms. Security tools help identify vulnerabilities before attackers do. Scanners like Nikto or Nessus automate the discovery of known flaws, while defensive tools like Web Application Firewalls (WAFs) monitor and filter incoming HTTP traffic to block malicious requests in real-time.',
    analogy: 'Security tools are like the security systems of a building. Vulnerability scanners are the inspectors checking for broken locks or open windows. The Web Application Firewall (WAF) is the security guard at the door checking everyones ID and bags before letting them in.',
    architecture: 'Vulnerability scanners operate by sending hundreds or thousands of crafted HTTP requests to the target server, looking for specific responses that indicate a known vulnerability (e.g., an outdated software version or an exposed sensitive directory). A WAF, on the other hand, sits inline between the client and the web server. It analyzes the Layer 7 (HTTP) payload against a set of rules (like the OWASP Core Rule Set) to identify and block attacks like SQL injection, cross-site scripting, and directory traversal.',
    why: 'In an enterprise, automated tools are necessary to keep up with the scale of web infrastructure and the constant release of new vulnerabilities. WAFs provide a critical layer of defense, often offering virtual patching while systems await formal updates.'
  },
  enterprise: {
    gfs: 'GFS uses enterprise-grade WAFs in front of all customer portals and runs weekly automated vulnerability scans across its entire public IP space.',
    windows: 'Windows servers often utilize tools like Microsoft Baseline Security Analyzer (MBSA) or integrate with Azure Web Application Firewall.',
    linux: 'Linux environments frequently deploy open-source WAFs like ModSecurity integrated with Apache or Nginx to inspect traffic.'
  },
  workflow: ['Step 1: Configure vulnerability scanner with target IP/URL.', 'Step 2: Run the scan against the web server.', 'Step 3: Analyze the scan report for actionable vulnerabilities.', 'Step 4: Patch software or reconfigure the server to fix vulnerabilities.', 'Step 5: Configure WAF rules to block exploits related to any unpatchable flaws.', 'Step 6: Monitor WAF logs for blocked attacks.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a2e"/><text x="50%" y="50%" font-size="24" fill="white" text-anchor="middle">WAF Deployment Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nikto -h http://target.com', purpose: 'Comprehensive Web Server Scan', out: 'List of potential vulnerabilities and misconfigurations', note: 'Nikto is very noisy and easily detected by IPS/WAF', mistake: 'Running it on a production server during peak hours' }
    ],
    win: [
      { cmd: 'Get-WebConfigurationProperty -Filter //security/requestFiltering -Name *', purpose: 'Check IIS Request Filtering', out: 'Request filtering rules', note: 'Request filtering acts as a basic built-in WAF for IIS', mistake: 'Overly restrictive rules breaking legitimate application functionality' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Beginner',
    duration: '30',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nikto'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires a baseline vulnerability scan of a new Apache server before it goes live.',
    objectives: ['Execute a Nikto scan against a target web server.'],
    steps: ['Step 1: Open a terminal in Kali Linux.', 'Step 2: Run `nikto -h http://target-web-server`.', 'Step 3: Review the output for outdated software warnings or exposed directories.'],
    evidence: ['Terminal output showing the Nikto scan results.'],
    validation: ['You should see a list of findings, including the server header and any identified issues.'],
    troubleshooting: ['If Nikto cannot connect, verify the target IP address and ensure the web server is running.'],
    mitre: [{ id: 'T1595', name: 'Active Scanning', tactic: 'Reconnaissance' }],
    cleanup: ['No specific cleanup required.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'What does WAF stand for?',
      opts: ['Web Access Filter', 'Wide Area Firewall', 'Web Application Firewall', 'Wireless Access Feature'],
      correct: 2,
      fb: 'WAF stands for Web Application Firewall, which filters HTTP traffic.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following tools is a popular open-source web server scanner?',
      opts: ['Wireshark', 'Nikto', 'Snort', 'John the Ripper'],
      correct: 1,
      fb: 'Nikto is a well-known open-source web server vulnerability scanner.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'At which OSI layer does a Web Application Firewall primarily operate?',
      opts: ['Layer 3 (Network)', 'Layer 4 (Transport)', 'Layer 7 (Application)', 'Layer 2 (Data Link)'],
      correct: 2,
      fb: 'A WAF inspects HTTP/HTTPS traffic, which operates at Layer 7.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a primary benefit of using a WAF?',
      opts: ['It speeds up the web server.', 'It provides "virtual patching" against known vulnerabilities.', 'It encrypts the hard drive.', 'It prevents physical access to the server.'],
      correct: 1,
      fb: 'A WAF can block exploits targeting a vulnerability before the underlying software is patched.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'Vulnerability scanners like Nikto are considered:',
      opts: ['Stealthy', 'Noisy', 'Defensive only', 'Invisible to logs'],
      correct: 1,
      fb: 'Scanners generate thousands of requests quickly, making them "noisy" and easily detectable in logs.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'ModSecurity is an example of a:',
      opts: ['Network Firewall', 'Intrusion Detection System', 'Web Application Firewall', 'Vulnerability Scanner'],
      correct: 2,
      fb: 'ModSecurity is a popular open-source Web Application Firewall.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which tool would be BEST suited for intercepting and modifying HTTP requests manually?',
      opts: ['Nmap', 'Burp Suite', 'Nikto', 'Ping'],
      correct: 1,
      fb: 'Burp Suite is an intercepting proxy used for manual web application testing.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Beginner',
      q: 'What is the first step in securing a web server after a fresh installation?',
      opts: ['Run Nikto', 'Change default passwords and remove default pages', 'Install a WAF', 'Perform a DoS attack'],
      correct: 1,
      fb: 'Removing default configurations and credentials is a critical first step.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'A WAF replaces the need for a traditional network firewall.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'They serve different purposes. A network firewall blocks ports/IPs, while a WAF inspects application-layer traffic.'
    },
    {
      type: 'true-false',
      difficulty: 'Beginner',
      q: 'Vulnerability scanners only find vulnerabilities; they do not fix them.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'Scanners report issues, but remediation (fixing) requires manual intervention or patching.'
    }
  ],
  flashcards: [
    { f: 'WAF', b: 'Web Application Firewall; filters, monitors, and blocks HTTP traffic to and from a web service.' },
    { f: 'Nikto', b: 'An open-source web server scanner which performs comprehensive tests against web servers for multiple items.' },
    { f: 'Virtual Patching', b: 'Implementing a security policy at the WAF level to block an exploit without modifying the application code itself.' }
  ],
  summary: ['Security tools are essential for identifying and mitigating web server risks.', 'Nikto is a popular scanner for finding web server misconfigurations.', 'WAFs provide Layer 7 defense against common web attacks.', 'Virtual patching via WAF can protect servers while waiting for updates.', 'A defense-in-depth strategy requires both network firewalls and WAFs.'],
  outcomes: ['Explain the function of a Web Application Firewall.', 'Describe how vulnerability scanners operate.', 'Differentiate between a network firewall and a WAF.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};
"""

target_html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'

try:
    with open(target_html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    marker = '// ── TAB WIRING ──'
    if marker in html_content:
        new_html = html_content.replace(marker, CONTENT + '\\n' + marker)
        with open(target_html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Injected successfully.")
    else:
        print("Marker not found.")
except FileNotFoundError:
    print(f"File not found: {target_html_path}")
except Exception as e:
    print(f"Error: {e}")
