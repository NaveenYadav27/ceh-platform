import os
import json

file_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'

payload = """
CONTENT['footprinting-concepts'] = {
  eyebrow: 'Module 02 · Topic 1',
  title: 'Footprinting Concepts',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Understanding what an external attacker can see.',
  objectives: ['Understand Active vs Passive Footprinting', 'Learn Information Gathering methodologies', 'Identify Network mapping and OS identification techniques'],
  learn: {
    simple: 'Footprinting is the first step of any attack or defense strategy. It involves gathering as much information as possible about a target system or network to identify vulnerabilities and map the attack surface. Passive footprinting relies on public data, while active footprinting involves direct interaction.',
    analogy: 'Think of footprinting like casing a bank before a heist. Passive footprinting is observing the bank from across the street. Active footprinting is walking inside and checking the locks.',
    architecture: 'In an enterprise environment, footprinting involves mapping external IP ranges, identifying open ports and services, discovering employee information, and analyzing organizational structures. This data is used to build a comprehensive threat model and identify potential entry points for attackers. The methodology typically follows: Open Source Intelligence (OSINT), Network Enumeration, and Vulnerability Scanning.',
    why: 'For a SOC analyst, understanding footprinting is crucial because it reveals what information is publicly available to attackers, allowing the organization to proactively reduce its attack surface and mitigate risks before exploitation occurs.'
  },
  enterprise: {
    gfs: 'GFS SOC needs to understand what an external attacker can see. You are tasked with mapping the external perimeter passively to avoid triggering alarms.',
    windows: 'Windows environments often expose information through DNS records, NetBIOS, and active directory structures if not properly secured.',
    linux: 'Linux environments might expose information through banner grabbing on services like SSH, HTTP, or FTP, revealing OS versions and configurations.'
  },
  workflow: ['Step 1: Define the scope and objectives of the footprinting exercise.', 'Step 2: Gather public information using search engines and OSINT tools.', 'Step 3: Enumerate network ranges and DNS records.', 'Step 4: Identify active systems and open ports (if active footprinting is authorized).', 'Step 5: Analyze the gathered data to build a threat model and identify vulnerabilities.', 'Step 6: Document findings and recommend mitigation strategies.'],
  diagram: {
    caption: 'Click to interact with the footprinting methodology diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#0A1128"/><text x="300" y="200" fill="#00FF88" text-anchor="middle" font-family="monospace">Footprinting Methodology Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'whois target.com', purpose: 'Gather domain registration info', out: 'Domain registrar and contact details', note: 'Useful for finding administrative contacts', mistake: 'Running against unauthorized targets' }
    ],
    win: [
      { cmd: 'Resolve-DnsName target.com', purpose: 'Resolve DNS records', out: 'IP addresses and DNS info', note: 'Native PowerShell alternative to nslookup', mistake: 'Misinterpreting internal vs external DNS results' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['whois', 'nslookup', 'recon-ng'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not test against production systems.'],
    scenario: 'GFS SOC needs to understand what an external attacker can see. You are tasked with mapping the external perimeter passively to avoid triggering alarms.',
    objectives: ['Perform passive footprinting on a simulated target', 'Gather domain and network information without direct interaction'],
    steps: ['Step 1: Use `whois target.com` to gather registration data.', 'Step 2: Use `nslookup` to enumerate DNS records.', 'Step 3: Analyze the gathered information to map the target attack surface.'],
    evidence: ['Terminal output from whois and nslookup.', 'Summary report of the target attack surface.'],
    validation: ['You should see: Domain registration details and DNS records', 'Verify by: Checking the output against known target information'],
    troubleshooting: ['If whois fails, ensure you have internet connectivity.', 'Common error: Connection timed out (check network settings)'],
    mitre: [{ id: 'TA0043', name: 'Reconnaissance', tactic: 'Reconnaissance' }],
    cleanup: ['Remove any temporary files generated during the lab.', 'Restore original configuration.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What is the primary difference between active and passive footprinting?', opts: ['Active footprinting requires internet access, passive does not', 'Active footprinting involves direct interaction with the target, passive relies on public data', 'Active footprinting is legal, passive is illegal', 'Active footprinting is faster than passive footprinting'], correct: 1, fb: 'Active footprinting interacts with the target system directly, while passive footprinting uses publicly available information without direct contact.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is an objective of footprinting?', opts: ['Exploiting a vulnerability', 'Network mapping', 'Deploying malware', 'Cracking passwords'], correct: 1, fb: 'Network mapping is a key objective of footprinting to understand the target infrastructure.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Passive footprinting always triggers IDS/IPS alerts on the target network.', correct: 'false', fb: 'Passive footprinting relies on public data and does not interact directly with the target, thus avoiding detection.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which technique involves gathering information about competitors to gain a business advantage?', opts: ['Competitive Intelligence', 'Social Engineering', 'Dumpster Diving', 'Phishing'], correct: 0, fb: 'Competitive Intelligence is the process of gathering and analyzing information about competitors.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'OS identification is a common objective of footprinting.', correct: 'true', fb: 'Identifying the operating systems in use helps attackers tailor their exploits and attacks.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which phase of hacking does footprinting belong to?', opts: ['Reconnaissance', 'Scanning', 'Gaining Access', 'Maintaining Access'], correct: 0, fb: 'Footprinting is synonymous with Reconnaissance, the first phase of hacking.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Footprinting can reveal organizational structures and employee details.', correct: 'true', fb: 'Information gathering often uncovers organizational charts, employee names, and contact info.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is the MITRE ATT&CK tactic associated with footprinting?', opts: ['TA0040', 'TA0043', 'TA0001', 'TA0002'], correct: 1, fb: 'TA0043 corresponds to the Reconnaissance tactic in the MITRE ATT&CK framework.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'WHOIS queries are considered a form of active footprinting.', correct: 'false', fb: 'WHOIS queries interact with public registries, not the target system directly, so they are considered passive footprinting.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why is footprinting important for a SOC analyst?', opts: ['To launch attacks against competitors', 'To understand what information is publicly exposed', 'To encrypt organizational data', 'To manage employee passwords'], correct: 1, fb: 'SOC analysts use footprinting to identify exposed information and reduce the organization attack surface.' }
  ],
  flashcards: [
    { f: 'Active Footprinting', b: 'Information gathering that involves direct interaction with the target system.' },
    { f: 'Passive Footprinting', b: 'Information gathering using publicly available resources without interacting directly with the target.' },
    { f: 'Competitive Intelligence', b: 'The legal and ethical process of gathering information about competitors to gain a business advantage.' },
    { f: 'Network Mapping', b: 'The process of identifying devices and their connectivity on a network.' },
    { f: 'OS Identification', b: 'Determining the operating system running on a target device, often through banner grabbing.' },
    { f: 'Attack Surface', b: 'The total sum of vulnerabilities that can be exploited to carry out a security attack.' },
    { f: 'Reconnaissance', b: 'The preliminary phase of an attack where information is gathered about the target.' },
    { f: 'OSINT', b: 'Open Source Intelligence; data collected from publicly available sources.' },
    { f: 'WHOIS', b: 'A query and response protocol widely used for querying databases that store registered users of an Internet resource.' },
    { f: 'TA0043', b: 'The MITRE ATT&CK tactic ID for Reconnaissance.' }
  ],
  summary: ['Footprinting is the first step in hacking and defense.', 'Passive footprinting avoids direct contact with the target.', 'Active footprinting involves direct interaction and risks detection.', 'Objectives include network mapping and OS identification.', 'Understanding the attack surface is crucial for SOC analysts.'],
  outcomes: ['Explain the difference between active and passive footprinting.', 'Identify the main objectives of footprinting.', 'Apply footprinting techniques to gather organizational data.', 'Analyze the attack surface from an external perspective.', 'Relate footprinting concepts to the MITRE ATT&CK framework.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['osint-techniques'] = {
  eyebrow: 'Module 02 · Topic 2',
  title: 'OSINT Techniques',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Leveraging Open Source Intelligence frameworks.',
  objectives: ['Master Open Source Intelligence gathering', 'Utilize tools like Maltego and Recon-ng', 'Extract data from public records and job postings'],
  learn: {
    simple: 'Open Source Intelligence (OSINT) involves collecting and analyzing publicly available data to gather actionable intelligence. This includes searching public records, analyzing social media, reviewing job postings, and using specialized OSINT frameworks to automate data collection.',
    analogy: 'OSINT is like being an investigative journalist piecing together a story using only public documents, interviews, and published articles, without breaking into any offices.',
    architecture: 'OSINT relies on a vast array of public sources, including search engines, social networks, government databases, and archive services. Automated tools like Recon-ng provide a modular framework to query these sources efficiently, while tools like Maltego offer visual link analysis to uncover hidden relationships between entities (e.g., domains, IPs, individuals).',
    why: 'In enterprise security, OSINT helps identify leaked credentials, exposed infrastructure, and potential physical or social engineering vectors before adversaries can exploit them.'
  },
  enterprise: {
    gfs: 'Threat Intel discovered GFS internal network topologies leaked in an old job posting on an IT board.',
    windows: 'OSINT can reveal details about internal Windows domains, naming conventions, and software versions used within the organization.',
    linux: 'Job postings for Linux administrators often reveal specific distributions, orchestration tools (e.g., Kubernetes), and configurations used by the company.'
  },
  workflow: ['Step 1: Define the target organization and OSINT objectives.', 'Step 2: Utilize search engines for initial data gathering.', 'Step 3: Analyze job postings and public records for internal details.', 'Step 4: Use Archive.org to view historical website versions.', 'Step 5: Run automated frameworks like Recon-ng to gather domain info.', 'Step 6: Map relationships using visual tools like Maltego.', 'Step 7: Consolidate findings into an intelligence report.'],
  diagram: {
    caption: 'Click to interact with the OSINT workflow diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#0A1128"/><text x="300" y="200" fill="#00FF88" text-anchor="middle" font-family="monospace">OSINT Workflow Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'recon-ng', purpose: 'Launch Recon-ng framework', out: 'Recon-ng interactive prompt', note: 'Requires API keys for some modules', mistake: 'Running modules without configuring API keys' }
    ],
    win: [
      { cmd: 'Invoke-WebRequest -Uri "http://archive.org"', purpose: 'Fetch webpage content', out: 'HTML content of the page', note: 'Useful for basic scraping in PowerShell', mistake: 'Not handling redirects or SSL errors' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Recon-ng', 'Maltego'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not test against production systems.'],
    scenario: 'Threat Intel discovered GFS internal network topologies leaked in an old job posting on an IT board. You need to use OSINT tools to find more leaked data.',
    objectives: ['Use Recon-ng to gather organizational data', 'Analyze public records and archives for leaked info'],
    steps: ['Step 1: Launch recon-ng and create a new workspace.', 'Step 2: Use the hackertarget module to enumerate subdomains.', 'Step 3: Search Archive.org for historical data of the target domain.'],
    evidence: ['Screenshot of Recon-ng module output.', 'List of discovered subdomains and historical data.'],
    validation: ['You should see: Discovered subdomains and leaked info', 'Verify by: Reviewing the Recon-ng database'],
    troubleshooting: ['If modules fail, check your internet connection and API keys.', 'Common error: Module not found (use marketplace install)'],
    mitre: [{ id: 'T1593', name: 'Search Open Websites/Domains', tactic: 'Reconnaissance' }],
    cleanup: ['Remove the Recon-ng workspace created for the lab.', 'Clear any downloaded temporary files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What does OSINT stand for?', opts: ['Open Source Internet Networking Tools', 'Open Source Intelligence', 'Operational System Integration', 'Outsourced Intelligence Network'], correct: 1, fb: 'OSINT stands for Open Source Intelligence, which is data collected from publicly available sources.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is known for visual link analysis in OSINT?', opts: ['Nmap', 'Metasploit', 'Maltego', 'Wireshark'], correct: 2, fb: 'Maltego is a powerful OSINT tool used for visual link analysis and mapping relationships.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Job postings can accidentally leak sensitive internal network details.', correct: 'true', fb: 'Job descriptions often list specific technologies, software versions, and network structures, which can be valuable to attackers.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is the purpose of Recon-ng?', opts: ['To crack passwords', 'To exploit vulnerabilities', 'To automate OSINT gathering', 'To launch DDoS attacks'], correct: 2, fb: 'Recon-ng is a full-featured Web Reconnaissance framework designed to automate OSINT gathering.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Archive.org can be used to view past versions of websites that may contain removed sensitive data.', correct: 'true', fb: 'The Wayback Machine on Archive.org stores historical snapshots of websites, often preserving data that has since been deleted.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which of the following is NOT a typical source for OSINT?', opts: ['Public records', 'Social media', 'Internal HR databases', 'Data brokers'], correct: 2, fb: 'Internal HR databases are private and not considered publicly available open sources.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Data brokers aggregate public and non-public data, which can be useful for OSINT.', correct: 'true', fb: 'Data brokers collect vast amounts of information about individuals and organizations, often accessible for a fee or partially public.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which MITRE ATT&CK technique corresponds to searching open websites and domains?', opts: ['T1590', 'T1593', 'T1596', 'T1589'], correct: 1, fb: 'T1593 is the technique ID for Search Open Websites/Domains.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'OSINT activities are generally considered illegal.', correct: 'false', fb: 'OSINT uses publicly available information, so it is generally legal and ethical when used appropriately.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why might an attacker analyze a company\'s job postings?', opts: ['To apply for a job', 'To identify the software and systems in use', 'To find the CEO\'s email', 'To determine the company\'s stock price'], correct: 1, fb: 'Job postings often reveal the specific technologies and infrastructure an organization uses.' }
  ],
  flashcards: [
    { f: 'OSINT', b: 'Open Source Intelligence; gathering data from public sources.' },
    { f: 'Maltego', b: 'An interactive data mining tool that renders directed graphs for link analysis.' },
    { f: 'Recon-ng', b: 'A full-featured Web Reconnaissance framework written in Python.' },
    { f: 'Archive.org', b: 'A non-profit library offering free universal access to historical web pages.' },
    { f: 'Data Broker', b: 'A business that collects personal information about consumers and sells that information.' },
    { f: 'Public Records', b: 'Documents or pieces of information that are not considered confidential and are available to the public.' },
    { f: 'Link Analysis', b: 'A data analysis technique used to evaluate relationships (connections) between nodes (objects).' },
    { f: 'T1593', b: 'MITRE ATT&CK ID for Search Open Websites/Domains.' },
    { f: 'Wayback Machine', b: 'A digital archive of the World Wide Web created by the Internet Archive.' },
    { f: 'Information Leakage', b: 'The accidental disclosure of sensitive information to unauthorized parties.' }
  ],
  summary: ['OSINT leverages public data for intelligence gathering.', 'Tools like Maltego and Recon-ng automate and visualize OSINT.', 'Job postings often leak internal technology details.', 'Archive.org is useful for finding historical, deleted data.', 'OSINT is a crucial first step in footprinting.'],
  outcomes: ['Define OSINT and its role in cybersecurity.', 'Identify common sources of OSINT.', 'Use Recon-ng to gather domain information.', 'Analyze job postings for information leakage.', 'Explain the value of historical web archives in reconnaissance.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['whois-dns'] = {
  eyebrow: 'Module 02 · Topic 3',
  title: 'WHOIS & DNS Enumeration',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Mapping domains, subdomains, and DNS infrastructure.',
  objectives: ['Perform WHOIS lookups', 'Understand DNS record types', 'Execute DNS zone transfers and subdomain enumeration'],
  learn: {
    simple: 'WHOIS and DNS enumeration are essential for mapping an organization\'s digital footprint. WHOIS provides registration details for a domain, while DNS enumeration reveals IP addresses, mail servers, and subdomains associated with the target.',
    analogy: 'WHOIS is like looking up the owner of a building in public property records. DNS enumeration is like getting the building\'s directory to find out what departments are on which floors.',
    architecture: 'DNS (Domain Name System) translates human-readable domain names into IP addresses. Attackers enumerate DNS to find targets. Key records include A (IPv4), AAAA (IPv6), MX (Mail Exchange), NS (Name Server), and TXT (Text records, often containing SPF/DKIM info). Zone transfers (AXFR) are intended for DNS server replication but, if misconfigured, can leak the entire DNS zone file to an attacker.',
    why: 'For an enterprise, misconfigured DNS can expose hidden subdomains (e.g., test environments, admin portals) and reveal internal network structures. Securing DNS and preventing unauthorized zone transfers is critical.'
  },
  enterprise: {
    gfs: 'GFS acquired a startup. You must map all subdomains and DNS records of the acquired company to fold them into the SOC monitoring perimeter.',
    windows: 'Windows DNS Server requires specific configuration to restrict zone transfers and secure DNS dynamic updates in an Active Directory environment.',
    linux: 'BIND and dnsmasq are common Linux DNS servers; their configuration files must be audited to prevent AXFR leaks and secure DNSSEC.'
  },
  workflow: ['Step 1: Perform a WHOIS lookup on the target domain.', 'Step 2: Identify authoritative Name Servers (NS records).', 'Step 3: Query for common DNS records (A, MX, TXT).', 'Step 4: Attempt a DNS Zone Transfer (AXFR) against the authoritative servers.', 'Step 5: Perform subdomain bruteforcing or fuzzing to find hidden hosts.', 'Step 6: Analyze TXT records for potential misconfigurations or sensitive data.', 'Step 7: Document the discovered infrastructure.'],
  diagram: {
    caption: 'Click to interact with the DNS Enumeration diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#0A1128"/><text x="300" y="200" fill="#00FF88" text-anchor="middle" font-family="monospace">DNS Enumeration Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'dig axfr @ns1.target.com target.com', purpose: 'Attempt a DNS zone transfer', out: 'Full list of DNS records or transfer failed', note: 'Only works if the DNS server is misconfigured', mistake: 'Not querying the authoritative name server' }
    ],
    win: [
      { cmd: 'Resolve-DnsName -Name target.com -Type TXT', purpose: 'Query TXT records', out: 'TXT record data (e.g., SPF)', note: 'Useful for finding email security configurations', mistake: 'Forgetting to specify the record type' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['dig', 'nslookup', 'fierce', 'sublist3r'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not test against production systems.'],
    scenario: 'GFS acquired a startup. You must map all subdomains and DNS records of the acquired company to fold them into the SOC monitoring perimeter.',
    objectives: ['Enumerate DNS records for a target domain', 'Perform subdomain bruteforcing to uncover hidden assets'],
    steps: ['Step 1: Use `dig target.com ANY` to find basic DNS records.', 'Step 2: Use `fierce --domain target.com` to attempt zone transfers and bruteforce subdomains.', 'Step 3: Use `sublist3r -d target.com` to find subdomains using OSINT.'],
    evidence: ['Terminal output showing discovered subdomains and DNS records.', 'Screenshot of the Fierce tool output.'],
    validation: ['You should see: A list of subdomains and associated IP addresses', 'Verify by: Checking the output against expected lab targets'],
    troubleshooting: ['If dig fails, check your DNS resolver configuration.', 'Common error: Connection timed out (firewall blocking DNS queries)'],
    mitre: [{ id: 'T1590', name: 'Gather Victim Network Information', tactic: 'Reconnaissance' }],
    cleanup: ['Remove any output files generated by the enumeration tools.', 'Restore original configuration.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which DNS record type specifies the mail servers for a domain?', opts: ['A', 'MX', 'NS', 'TXT'], correct: 1, fb: 'The MX (Mail Exchange) record directs email to the servers for a domain.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a DNS Zone Transfer (AXFR)?', opts: ['A mechanism to replicate DNS databases across servers', 'A method to encrypt DNS traffic', 'A technique to hide subdomains', 'A type of Denial of Service attack'], correct: 0, fb: 'AXFR is used to replicate DNS data between servers. If misconfigured, it can leak the entire zone to attackers.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'A WHOIS query reveals the IP addresses of all subdomains.', correct: 'false', fb: 'WHOIS provides domain registration info (owner, contacts, registrars), not specific IP addresses of subdomains.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which tool is specifically designed for DNS enumeration and subdomain discovery?', opts: ['Nmap', 'Fierce', 'Wireshark', 'Metasploit'], correct: 1, fb: 'Fierce is a reconnaissance tool used to locate non-contiguous IP space and subdomains.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'TXT records can contain SPF information used for email authentication.', correct: 'true', fb: 'TXT records are commonly used to store SPF, DKIM, and DMARC policies.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What does an A record do in DNS?', opts: ['Maps a domain name to an IPv4 address', 'Maps a domain name to an IPv6 address', 'Specifies the authoritative name server', 'Stores text information'], correct: 0, fb: 'The A record maps a hostname to a 32-bit IPv4 address.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Subdomain bruteforcing relies solely on querying authoritative name servers.', correct: 'false', fb: 'Subdomain bruteforcing uses wordlists to guess subdomains and queries standard DNS resolvers to see if they exist.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is the purpose of DNSSEC?', opts: ['To encrypt all DNS traffic', 'To provide cryptographic authentication of DNS data', 'To prevent WHOIS lookups', 'To speed up DNS resolution'], correct: 1, fb: 'DNSSEC adds cryptographic signatures to DNS records to ensure their authenticity and integrity.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'The `dig` command can be used to perform DNS queries on Linux.', correct: 'true', fb: '`dig` (Domain Information Groper) is a flexible tool for interrogating DNS name servers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which MITRE ATT&CK technique involves gathering network information like DNS records?', opts: ['T1590', 'T1593', 'T1596', 'T1589'], correct: 0, fb: 'T1590 corresponds to Gather Victim Network Information.' }
  ],
  flashcards: [
    { f: 'WHOIS', b: 'A protocol used to query databases that store registered users or assignees of an Internet resource.' },
    { f: 'A Record', b: 'A DNS record that maps a hostname to an IPv4 address.' },
    { f: 'MX Record', b: 'A DNS record that specifies the mail servers responsible for accepting email on behalf of a domain.' },
    { f: 'NS Record', b: 'A DNS record that indicates which name servers are authoritative for the zone.' },
    { f: 'TXT Record', b: 'A DNS record that provides text information to sources outside your domain, often used for SPF.' },
    { f: 'AXFR', b: 'Asynchronous Full Transfer Zone; a type of DNS transaction used for replicating DNS databases.' },
    { f: 'DNSSEC', b: 'Domain Name System Security Extensions; a suite of specifications for securing certain kinds of information provided by DNS.' },
    { f: 'Sublist3r', b: 'A python tool designed to enumerate subdomains of websites using OSINT.' },
    { f: 'Fierce', b: 'A reconnaissance tool for locating non-contiguous IP space and subdomains.' },
    { f: 'T1590', b: 'MITRE ATT&CK ID for Gather Victim Network Information.' }
  ],
  summary: ['WHOIS provides domain registration and ownership details.', 'DNS enumeration maps the target network infrastructure.', 'Zone transfers (AXFR) should be restricted to authorized servers.', 'Subdomain bruteforcing uncovers hidden assets.', 'Tools like dig, fierce, and sublist3r are essential for DNS recon.'],
  outcomes: ['Execute WHOIS queries to find domain contacts.', 'Identify and explain different DNS record types.', 'Perform a DNS zone transfer to discover network topology.', 'Use automated tools to enumerate subdomains.', 'Secure DNS configurations against enumeration attacks.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['google-hacking'] = {
  eyebrow: 'Module 02 · Topic 4',
  title: 'Google Hacking (Dorks)',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Finding exposed files and directories using advanced search operators.',
  objectives: ['Master Google Dorks and advanced operators', 'Search for exposed directories and sensitive files', 'Utilize the Google Hacking Database (GHDB)'],
  learn: {
    simple: 'Google Hacking, or Google Dorking, involves using advanced search operators to find information that is publicly available but often unintentionally exposed. This can include sensitive documents, passwords, or exposed directories.',
    analogy: 'Google Hacking is like knowing the secret Dewey Decimal codes to find restricted books in a public library that the librarian forgot to lock away.',
    architecture: 'Search engines continuously index the web. If a web server is misconfigured (e.g., directory listing enabled) or if sensitive files (like .env or config.php) are placed in public web folders, Google will index them. Advanced operators like site:, inurl:, intitle:, and filetype: allow attackers to filter search results to pinpoint these exact vulnerabilities.',
    why: 'Enterprises often accidentally expose sensitive data due to misconfigured cloud storage (like AWS S3 buckets) or web servers. SOC analysts use Google Dorks to proactively find and remediate these exposures before attackers do.'
  },
  enterprise: {
    gfs: 'An auditor used Google Dorks to find a publicly exposed AWS S3 bucket containing GFS customer data indexed by a search engine.',
    windows: 'Google Dorks can uncover exposed Windows IIS directory listings or inadvertently published RDP connection files (.rdp).',
    linux: 'Linux web servers (Apache/Nginx) with directory listing enabled can expose sensitive configuration files or bash history files (.bash_history) to search engines.'
  },
  workflow: ['Step 1: Identify the target domain (e.g., target.com).', 'Step 2: Use the `site:` operator to restrict searches to the target.', 'Step 3: Combine with `filetype:` to search for specific sensitive files (e.g., pdf, sql, env).', 'Step 4: Use `intitle:"index of"` to find exposed directories.', 'Step 5: Reference the GHDB for pre-built queries targeting specific vulnerabilities.', 'Step 6: Analyze the results and report any exposed sensitive data.', 'Step 7: Remediate the exposure by configuring web server access controls or robots.txt.'],
  diagram: {
    caption: 'Click to interact with the Google Hacking workflow diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#0A1128"/><text x="300" y="200" fill="#00FF88" text-anchor="middle" font-family="monospace">Google Hacking Workflow Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'curl -s "https://www.google.com/search?q=site:target.com+filetype:pdf"', purpose: 'Fetch Google search results via CLI', out: 'HTML of search results', note: 'Google often blocks automated queries with CAPTCHAs', mistake: 'Not handling CAPTCHAs or rate limiting' }
    ],
    win: [
      { cmd: 'Invoke-WebRequest -Uri "https://www.google.com/search?q=site:target.com+intitle:index.of"', purpose: 'Search for directory listings', out: 'HTML response containing search results', note: 'Browser automation is often better for this', mistake: 'Triggering anti-bot mechanisms' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Web Browser', 'GHDB'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not test against production systems.'],
    scenario: 'An auditor used Google Dorks to find a publicly exposed AWS S3 bucket containing GFS customer data. You need to verify what other data is exposed.',
    objectives: ['Craft advanced Google queries to find exposed files', 'Locate directory listings on a target domain'],
    steps: ['Step 1: Open a web browser and navigate to Google.', 'Step 2: Search for `site:target.com intitle:"index of"` to find open directories.', 'Step 3: Search for `site:target.com filetype:env` to find exposed environment variables.'],
    evidence: ['Screenshots of Google search results showing exposed data.', 'List of identified exposed files.'],
    validation: ['You should see: Search results highlighting exposed directories or files', 'Verify by: Clicking the links to confirm the exposure (in the lab environment)'],
    troubleshooting: ['If Google blocks your query, try completing the CAPTCHA or using a different IP.', 'Common error: Too many requests (Google rate limiting)'],
    mitre: [{ id: 'T1593.002', name: 'Search Engines', tactic: 'Reconnaissance' }],
    cleanup: ['Clear browser history and cache.', 'Restore original configuration.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which Google operator restricts search results to a specific domain?', opts: ['inurl:', 'intitle:', 'site:', 'filetype:'], correct: 2, fb: 'The `site:` operator limits search results to the specified domain or URL.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the GHDB?', opts: ['Google Hardware Database', 'Google Hacking Database', 'Global Host Discovery Bot', 'Generic Hacking Data Broker'], correct: 1, fb: 'The Google Hacking Database (GHDB) is an index of search queries designed to uncover sensitive information publicly available on the web.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Google Dorks can be used to find exposed passwords.', correct: 'true', fb: 'By searching for specific file types or keywords (like "password" or "db_password"), attackers can find exposed credential files.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which query is best for finding directory listings?', opts: ['site:example.com "directory"', 'intitle:"index of" site:example.com', 'inurl:index site:example.com', 'filetype:dir site:example.com'], correct: 1, fb: '`intitle:"index of"` is the classic dork used to find web servers with directory listing enabled.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Using Google Dorks is illegal.', correct: 'false', fb: 'Google Dorking itself is just advanced searching and is legal. However, accessing or exploiting the sensitive data found may be illegal.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which operator finds pages with a specific word in the URL?', opts: ['site:', 'inurl:', 'intitle:', 'filetype:'], correct: 1, fb: 'The `inurl:` operator restricts results to pages containing the specified word in the URL.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'The `robots.txt` file can prevent Google from indexing sensitive directories.', correct: 'true', fb: 'Webmasters use `robots.txt` to tell search engine crawlers which pages or files they should or should not request.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What MITRE ATT&CK technique covers the use of search engines for reconnaissance?', opts: ['T1593.001', 'T1593.002', 'T1590', 'T1596'], correct: 1, fb: 'T1593.002 specifically relates to using Search Engines for reconnaissance.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Google Dorks can only find text files.', correct: 'false', fb: 'The `filetype:` operator can search for various file types, including pdf, docx, sql, and xls.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why might an attacker search for `filetype:sql`?', opts: ['To find database backups containing sensitive data', 'To execute SQL injection', 'To find SQL tutorials', 'To connect to a database server directly'], correct: 0, fb: 'Searching for SQL files often reveals database dumps or backups that were accidentally left in publicly accessible web folders.' }
  ],
  flashcards: [
    { f: 'Google Dorking', b: 'Using advanced search operators to find information that is not easily accessible through simple searches.' },
    { f: 'site:', b: 'Search operator that limits results to a specific domain or website.' },
    { f: 'filetype:', b: 'Search operator that restricts results to a specific file extension (e.g., pdf, doc, sql).' },
    { f: 'intitle:', b: 'Search operator that returns pages with the specified keyword in the HTML title tag.' },
    { f: 'inurl:', b: 'Search operator that returns pages with the specified keyword in the URL.' },
    { f: 'GHDB', b: 'Google Hacking Database; a collection of advanced search queries that uncover sensitive data.' },
    { f: 'Directory Listing', b: 'A web server misconfiguration that displays a list of all files in a directory when no index file is present.' },
    { f: 'robots.txt', b: 'A text file webmasters create to instruct web robots how to crawl pages on their website.' },
    { f: 'T1593.002', b: 'MITRE ATT&CK ID for Search Engines.' },
    { f: 'Information Exposure', b: 'The accidental disclosure of sensitive information, often leading to data breaches.' }
  ],
  summary: ['Google Dorks use advanced operators to find hidden data.', 'Common operators include site:, filetype:, intitle:, and inurl:.', 'The GHDB provides a catalog of queries for specific vulnerabilities.', 'Exposed directory listings and config files are common targets.', 'Proactive dorking helps organizations identify and secure exposed data.'],
  outcomes: ['Construct advanced Google search queries using operators.', 'Locate exposed sensitive files and directories.', 'Utilize the Google Hacking Database (GHDB) for reconnaissance.', 'Analyze the risks associated with information exposure.', 'Implement measures to prevent sensitive data from being indexed.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['shodan-recon'] = {
  eyebrow: 'Module 02 · Topic 5',
  title: 'Shodan & Infrastructure Recon',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Searching for internet-connected devices and exposed infrastructure.',
  objectives: ['Navigate Shodan and Censys', 'Fingerprint exposed infrastructure', 'Identify vulnerable embedded devices'],
  learn: {
    simple: 'While Google indexes webpages, search engines like Shodan and Censys index internet-connected devices. They scan the internet for open ports, grab banners, and categorize devices like routers, webcams, industrial control systems (ICS), and servers.',
    analogy: 'If Google is the phonebook for websites, Shodan is the phonebook for all the physical devices plugged into the internet.',
    architecture: 'Shodan works by continuously scanning the entire IPv4 space. It connects to open ports and records the response (the banner). This banner often contains the software version, operating system, and configuration details. Attackers use this data to find specific vulnerable systems globally, such as unpatched VPN appliances or databases exposed without authentication.',
    why: 'Enterprises often have "shadow IT" — devices deployed without security oversight. Shodan helps SOC analysts identify these rogue devices and exposed services (like RDP or unauthenticated databases) before they are exploited.'
  },
  enterprise: {
    gfs: 'A rogue IT admin deployed an unmanaged VPN appliance in a GFS branch office. It was found via Shodan before an attacker exploited it.',
    windows: 'Shodan frequently indexes exposed Windows servers running RDP (port 3389) or SMB (port 445), which are prime targets for ransomware.',
    linux: 'Exposed Linux servers often show up on Shodan running vulnerable versions of SSH, Apache, or unauthenticated Redis databases.'
  },
  workflow: ['Step 1: Access Shodan or Censys web interfaces or APIs.', 'Step 2: Construct queries using filters like `org:`, `port:`, or `country:`.', 'Step 3: Analyze the returned banners to identify the device type and software version.', 'Step 4: Cross-reference the software version with vulnerability databases (CVEs).', 'Step 5: Identify default credentials or unauthenticated access.', 'Step 6: Report exposed infrastructure for immediate remediation.', 'Step 7: Implement continuous monitoring of the organization IP space.'],
  diagram: {
    caption: 'Click to interact with the Shodan Recon workflow diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#0A1128"/><text x="300" y="200" fill="#00FF88" text-anchor="middle" font-family="monospace">Shodan Recon Workflow Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'shodan search org:"Target Inc"', purpose: 'Search Shodan via CLI for an organization', out: 'List of IPs and services belonging to the org', note: 'Requires the Shodan CLI tool and API key', mistake: 'Not refining the query, returning too many results' }
    ],
    win: [
      { cmd: 'Invoke-WebRequest -Uri "https://api.shodan.io/shodan/host/8.8.8.8?key=YOUR_API_KEY"', purpose: 'Query Shodan API for a specific IP', out: 'JSON data detailing open ports and banners', note: 'Easy to automate with PowerShell scripts', mistake: 'Exposing the API key in public scripts' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Shodan CLI', 'Web Browser'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not test against production systems.'],
    scenario: 'A rogue IT admin deployed an unmanaged VPN appliance in a GFS branch office. You need to use Shodan to find it.',
    objectives: ['Use Shodan to identify exposed services on a specific IP range', 'Analyze service banners to determine software versions'],
    steps: ['Step 1: Use the Shodan CLI to initialize your API key (`shodan init`).', 'Step 2: Run `shodan search net:192.168.1.0/24` (use a public lab IP range).', 'Step 3: Analyze the results for exposed RDP or vulnerable web services.'],
    evidence: ['Terminal output of the Shodan search results.', 'Detailed host information for an exposed device.'],
    validation: ['You should see: A list of devices, open ports, and banners', 'Verify by: Checking the banner details for known software versions'],
    troubleshooting: ['If the Shodan CLI fails, ensure your API key is correct.', 'Common error: Invalid API key or plan limits exceeded'],
    mitre: [{ id: 'T1596', name: 'Search Open Technical Databases', tactic: 'Reconnaissance' }],
    cleanup: ['Remove the Shodan API key from the local configuration if on a shared machine.', 'Restore original configuration.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What is Shodan primarily designed to search for?', opts: ['Webpages and documents', 'Internet-connected devices and infrastructure', 'Social media profiles', 'Dark web forums'], correct: 1, fb: 'Shodan indexes internet-connected devices like routers, webcams, and servers, not typical webpages.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a "banner" in the context of Shodan?', opts: ['An advertisement on a webpage', 'The response sent by a service when a connection is made', 'A graphic used in an attack', 'A type of firewall'], correct: 1, fb: 'A banner is the text returned by a service (like SSH or HTTP) upon connection, often revealing the software version.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Shodan can be used to find systems vulnerable to specific exploits.', correct: 'true', fb: 'By searching for specific software versions in banners, attackers can locate systems vulnerable to known exploits (CVEs).' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which Shodan filter restricts results to a specific company or organization?', opts: ['net:', 'port:', 'org:', 'country:'], correct: 2, fb: 'The `org:` filter limits results to IPs registered to a specific organization.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Censys is another search engine similar to Shodan that indexes internet-connected devices.', correct: 'true', fb: 'Censys, like Shodan, scans the internet and provides data on hosts and networks.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Why is finding default credentials relevant when using Shodan?', opts: ['To log into the Shodan website', 'Many IoT devices found on Shodan use factory default passwords', 'To encrypt data', 'To bypass firewalls'], correct: 1, fb: 'Many devices discovered by Shodan, like webcams or routers, are deployed with default credentials, making them easy targets.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Shodan actively exploits vulnerabilities during its scanning process.', correct: 'false', fb: 'Shodan only grabs banners and records responses; it does not attempt to exploit vulnerabilities.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which MITRE ATT&CK technique involves using platforms like Shodan?', opts: ['T1590', 'T1593', 'T1596', 'T1589'], correct: 2, fb: 'T1596 is the technique for Search Open Technical Databases.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Shodan requires an API key for advanced searches and CLI usage.', correct: 'true', fb: 'While basic searches are free, an account and API key are required for advanced filters and programmatic access.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is "Shadow IT"?', opts: ['IT systems deployed in the dark web', 'Hardware or software used without approval or knowledge of the IT department', 'Encrypted IT communications', 'A hacking group'], correct: 1, fb: 'Shadow IT refers to systems deployed without IT oversight, which are often discovered by attackers using Shodan.' }
  ],
  flashcards: [
    { f: 'Shodan', b: 'A search engine that lets the user find specific types of computers connected to the internet using a variety of filters.' },
    { f: 'Banner Grabbing', b: 'A technique used to gain information about a computer system on a network and the services running on its open ports.' },
    { f: 'Censys', b: 'A search engine for internet-connected devices, similar to Shodan, focusing on security.' },
    { f: 'Shadow IT', b: 'Information technology systems deployed by departments other than the central IT department, often lacking security.' },
    { f: 'IoT', b: 'Internet of Things; physical devices embedded with sensors and software that connect to the internet.' },
    { f: 'org:', b: 'Shodan search filter used to find devices belonging to a specific organization.' },
    { f: 'port:', b: 'Shodan search filter used to find devices with a specific open port.' },
    { f: 'T1596', b: 'MITRE ATT&CK ID for Search Open Technical Databases.' },
    { f: 'CVE', b: 'Common Vulnerabilities and Exposures; a list of publicly disclosed cybersecurity vulnerabilities.' },
    { f: 'Default Credentials', b: 'Factory-set usernames and passwords on devices that are often unchanged before deployment.' }
  ],
  summary: ['Shodan and Censys index internet-connected devices.', 'They rely on banner grabbing to identify software versions.', 'These tools are excellent for discovering Shadow IT.', 'Many exposed IoT devices suffer from default credentials.', 'Using filters like org: and port: refines reconnaissance.'],
  outcomes: ['Navigate Shodan to find exposed internet infrastructure.', 'Analyze service banners to fingerprint device types and software.', 'Use Shodan search filters to target specific organizations or ports.', 'Explain the risks associated with Shadow IT and exposed devices.', 'Integrate Shodan data into threat intelligence reports.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['social-media-recon'] = {
  eyebrow: 'Module 02 · Topic 6',
  title: 'Social Media & People Recon',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Gathering identity information for social engineering campaigns.',
  objectives: ['Extract metadata from public files and photos', 'Utilize theHarvester for email gathering', 'Prepare data for Social Engineering attacks'],
  learn: {
    simple: 'Social media reconnaissance involves gathering information about individuals working at a target organization. This includes finding email addresses, job titles, relationships, and even metadata from uploaded photos, all to craft convincing social engineering or phishing attacks.',
    analogy: 'People recon is like a con artist learning everything about their mark\'s hobbies, friends, and schedule before approaching them with a tailored scam.',
    architecture: 'Attackers use tools like theHarvester to scrape search engines and LinkedIn for employee names and email formats. They also analyze metadata (EXIF data) from public photos, which can reveal GPS coordinates, camera types, and software used. This data builds a psychological profile of the target, making spear-phishing highly effective.',
    why: 'Humans are often the weakest link in enterprise security. By understanding what employee information is publicly exposed, an organization can provide targeted security awareness training and tighten social media policies to reduce phishing success rates.'
  },
  enterprise: {
    gfs: 'Attackers successfully phished a GFS executive by referencing a recent vacation photo posted on social media.',
    windows: 'Employee information gathered via social media is often used to bruteforce Windows Active Directory accounts or craft targeted spear-phishing emails containing malicious Office documents.',
    linux: 'While less direct, knowing the IT staff\'s names and roles can help attackers tailor phishing emails designed to steal SSH keys or Linux server credentials.'
  },
  workflow: ['Step 1: Identify key personnel (executives, IT admins) at the target organization.', 'Step 2: Use LinkedIn to map out the organizational structure and employee roles.', 'Step 3: Run `theHarvester` to scrape email addresses associated with the target domain.', 'Step 4: Analyze social media profiles (Twitter, Facebook, Instagram) for personal interests.', 'Step 5: Download publicly available documents/photos and extract EXIF/metadata.', 'Step 6: Combine the technical and personal data to craft a spear-phishing pretext.', 'Step 7: Launch the social engineering campaign (in a simulated environment).'],
  diagram: {
    caption: 'Click to interact with the Social Media Recon workflow diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#0A1128"/><text x="300" y="200" fill="#00FF88" text-anchor="middle" font-family="monospace">Social Media Recon Workflow Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'theHarvester -d target.com -b google,linkedin', purpose: 'Scrape emails and names', out: 'List of employee emails and subdomains', note: 'Search engines frequently update, which can break scrapers', mistake: 'Not updating the tool before running' }
    ],
    win: [
      { cmd: 'exiftool image.jpg', purpose: 'Extract EXIF metadata from a photo', out: 'List of metadata (GPS, camera info, dates)', note: 'Requires exiftool to be installed on Windows', mistake: 'Assuming all photos have EXIF data (social media sites often strip it)' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['theHarvester', 'exiftool'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not test against production systems or real individuals.'],
    scenario: 'Attackers are preparing a phishing campaign against GFS. You need to identify what employee information is publicly accessible to preempt the attack.',
    objectives: ['Use theHarvester to gather employee email addresses', 'Extract metadata from a provided sample image'],
    steps: ['Step 1: Run `theHarvester -d target.com -b all` to collect email addresses.', 'Step 2: Download the sample image provided in the lab environment.', 'Step 3: Run `exiftool sample.jpg` to view the metadata and identify GPS coordinates.'],
    evidence: ['Terminal output showing collected email addresses.', 'Terminal output showing the EXIF data extracted from the image.'],
    validation: ['You should see: A list of emails and image metadata', 'Verify by: Checking the GPS coordinates on a map to find the location'],
    troubleshooting: ['If theHarvester returns no results, try a different data source (-b parameter).', 'Common error: Missing dependencies for exiftool'],
    mitre: [{ id: 'T1589', name: 'Gather Victim Identity Information', tactic: 'Reconnaissance' }],
    cleanup: ['Delete the sample image and tool output files.', 'Restore original configuration.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What is the primary goal of social media reconnaissance?', opts: ['To gain administrative access to servers', 'To gather identity information for social engineering', 'To perform a Denial of Service attack', 'To find open network ports'], correct: 1, fb: 'The goal is to gather information about people to craft convincing social engineering or phishing attacks.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used to scrape email addresses and employee names from search engines?', opts: ['Nmap', 'theHarvester', 'Metasploit', 'Wireshark'], correct: 1, fb: 'theHarvester is designed to gather emails, subdomains, hosts, employee names, and open ports from different public sources.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Social media sites like Facebook and Twitter always leave EXIF data intact on uploaded photos.', correct: 'false', fb: 'Most major social media platforms strip EXIF data (like GPS coordinates) from photos upon upload for privacy reasons.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What type of data does `exiftool` extract?', opts: ['Network traffic', 'Database passwords', 'Metadata from files and images', 'Website HTML code'], correct: 2, fb: 'exiftool reads, writes, and edits meta information (EXIF, IPTC, XMP, etc.) in a wide variety of files.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'LinkedIn is a valuable resource for mapping an organization\'s structure and finding key personnel.', correct: 'true', fb: 'LinkedIn profiles provide job titles, employment history, and connections, making it easy to map organizational hierarchies.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Spear-phishing relies heavily on data gathered during which phase?', opts: ['Exploitation', 'Reconnaissance / Information Gathering', 'Covering Tracks', 'Maintaining Access'], correct: 1, fb: 'Spear-phishing requires detailed knowledge about the target, which is gathered during the reconnaissance phase.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Metadata in a PDF document can reveal the software used to create it and the author\'s name.', correct: 'true', fb: 'Document metadata often includes the author\'s username, software version, and creation dates, which can be useful for attackers.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which MITRE ATT&CK technique involves gathering identity information?', opts: ['T1590', 'T1593', 'T1596', 'T1589'], correct: 3, fb: 'T1589 is the technique ID for Gather Victim Identity Information.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'TheHarvester only uses Google as a data source.', correct: 'false', fb: 'TheHarvester supports multiple data sources, including Bing, LinkedIn, Baidu, and various APIs.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can organizations defend against social media reconnaissance?', opts: ['By blocking all internet access', 'By implementing strict social media policies and awareness training', 'By using stronger encryption algorithms', 'By updating their antivirus software'], correct: 1, fb: 'Training employees on what not to share and enforcing social media policies are the best defenses against people recon.' }
  ],
  flashcards: [
    { f: 'Social Engineering', b: 'The psychological manipulation of people into performing actions or divulging confidential information.' },
    { f: 'Phishing', b: 'A fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity in an electronic communication.' },
    { f: 'Spear-Phishing', b: 'A targeted phishing attack directed at a specific individual or organization.' },
    { f: 'theHarvester', b: 'A tool for gathering e-mail accounts, subdomain names, and employee names from public sources.' },
    { f: 'EXIF Data', b: 'Exchangeable Image File Format; metadata embedded in digital photos, often including GPS coordinates.' },
    { f: 'Metadata', b: 'Data that provides information about other data (e.g., author, date created, file size).' },
    { f: 'exiftool', b: 'A command-line application used to read, write, and manipulate image, audio, and video metadata.' },
    { f: 'T1589', b: 'MITRE ATT&CK ID for Gather Victim Identity Information.' },
    { f: 'Pretexting', b: 'The act of creating an invented scenario to persuade a targeted victim to release information or perform an action.' },
    { f: 'OSINT', b: 'Open Source Intelligence; the foundation for gathering data used in social media reconnaissance.' }
  ],
  summary: ['People recon targets employees for social engineering.', 'LinkedIn is a primary source for mapping organizational structures.', 'Tools like theHarvester automate email and name gathering.', 'EXIF data in photos can reveal sensitive location information.', 'Employee awareness is the main defense against people recon.'],
  outcomes: ['Identify key personnel and organizational structures using social media.', 'Extract email addresses and subdomains using theHarvester.', 'Analyze image and document metadata using exiftool.', 'Design a spear-phishing pretext based on gathered OSINT.', 'Propose security awareness training topics to mitigate social engineering risks.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};
"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "// ── TAB WIRING ──"
if target in content:
    content = content.replace(target, payload + "\\n" + target)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully injected payload.")
else:
    print("Could not find the target string in index.html")
