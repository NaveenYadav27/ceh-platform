"""
CEH Platform — Content Injection Script
Fills in all tab content for:
- Module 02 Remaining Topics: google-hacking, shodan-recon, social-media-recon
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

INJECT_BEFORE = '// ==========================================================\n// AUTO-STUB GENERATOR'

ok = []
fail = []

MODULE02_REMAINING_CONTENT = """
CONTENT['google-hacking'] = {
  module:'Module 02 \u00b7 Footprinting & Reconnaissance',
  title:'Google Hacking (Google Dorks)',
  sub:'Weaponizing search engines to discover exposed sensitive data.',
  killchain:{phase:'Reconnaissance',mitre:'T1593.002 \u2014 Search Open Technical Databases',desc:'Search engines crawl everything without context. Google Dorking leverages advanced search operators to filter this massive dataset for exposed files and vulnerabilities.'},
  learn:{
    simple:'Google Hacking (or Google Dorking) involves using advanced search operators (like "site:", "filetype:", "intitle:") to find information that organizations accidentally exposed to the internet and Google indexed.',
    analogy:'Imagine Google is a massive library containing every document on earth, but everything is thrown into a single pile. A normal search is digging through the pile. Google Dorking is using a magnet to instantly pull out only the documents labeled "Confidential" or "Password".',
    why:'Many web administrators incorrectly assume that if a page is not linked anywhere on their site, no one will find it (Security through Obscurity). But Google\'s crawlers find these pages. Google Dorking allows attackers to find these hidden pages without touching the target\'s servers.',
    architecture:'Google crawlers (Googlebot) continuously index the web. They read HTML, PDF, Word, Excel, and text files. When a site misconfigures permissions (e.g., directory listing enabled), Google indexes all files in the directory. Attackers use specific query syntax to filter Google\'s index for specific file types or URL patterns.'
  },
  diagram:{
    title:'Common Google Dork Operators',
    steps:[
      {icon:'\U0001f310',label:'site:',desc:'Restricts results to a specific domain or top-level domain. Example: site:target.com'},
      {icon:'\U0001f4c4',label:'filetype: / ext:',desc:'Restricts results to a specific file extension (pdf, doc, xls, txt, sql, env). Example: filetype:sql'},
      {icon:'\U0001f516',label:'intitle:',desc:'Finds pages with a specific word in the HTML <title> tag. Example: intitle:"index of"'},
      {icon:'\U0001f517',label:'inurl:',desc:'Finds pages with a specific string in the URL path. Example: inurl:admin'},
      {icon:'\U0001f4dd',label:'intext:',desc:'Finds pages containing specific text in the body of the page. Example: intext:"password"'},
      {icon:'\U0001f504',label:'Combining Operators',desc:'The real power is combining them. Example: site:target.com filetype:pdf intitle:"confidential"'}
    ]
  },
  enterprise:{
    role:'You are performing an OSINT assessment for GlobalFinSec Corp.',
    situation:'The company claims they have strict data loss prevention (DLP) controls and nothing sensitive is publicly exposed on their domains.',
    challenge:'Use Google Dorking to verify if any sensitive files, passwords, or misconfigured directories are indexed by Google on globalfinsec-test.com.',
    steps:[
      'Search for exposed database backups: site:globalfinsec-test.com filetype:sql intext:password',
      'Search for exposed directory listings (often containing old files): site:globalfinsec-test.com intitle:"index of"',
      'Search for exposed environment configuration files (which contain API keys): site:globalfinsec-test.com ext:env',
      'Search for exposed Excel spreadsheets that might contain employee data: site:globalfinsec-test.com filetype:xls OR filetype:xlsx',
      'Search for login portals hidden on subdomains: site:globalfinsec-test.com inurl:login OR inurl:admin'
    ],
    outcome:'The search site:globalfinsec-test.com intitle:"index of" ext:sql revealed an open directory on an old marketing server containing a backup file named "users_2023.sql". The file contained 5,000 customer email addresses and plaintext passwords.',
    lesson:'Web application firewalls (WAF) do not protect against Google Dorking because the query is sent to Google, not the company\'s servers. If it\'s indexed, it\'s compromised.'
  },
  tools:[
    {name:'Google Search',cmd:'site:target.com filetype:pdf',desc:'The primary tool for Google Hacking'},
    {name:'Google Hacking Database (GHDB)',cmd:'https://www.exploit-db.com/google-hacking-database',desc:'A repository of thousands of known Google Dorks'},
    {name:'theHarvester',cmd:'theHarvester -d target.com -b google',desc:'Automates Google searches for emails and subdomains'}
  ],
  commands:{
    win:['Rem - No specific Windows command line tools, use a web browser for Google Dorking'],
    lin:['Rem - No specific Linux command line tools, use a web browser for Google Dorking']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Relying on robots.txt for Security',desc:'Administrators often put sensitive directories in robots.txt (e.g., Disallow: /admin/). This tells legitimate crawlers not to index it, but it also provides a map for attackers of exactly where the sensitive files are.',fix:'Do not use robots.txt for security. Use proper authentication and authorization controls (like .htaccess or application-level login) to protect sensitive directories.'},
    {icon:'\U0001f534',title:'Assuming "Unlinked" Means "Hidden"',desc:'Putting a file at /secret_backup_2024.zip without linking to it anywhere does not make it hidden. Crawlers can guess URLs, or users might accidentally share the link on public forums.',fix:'Never rely on Security through Obscurity. If a file is sensitive, it must be protected by authentication, regardless of whether it is linked.'},
    {icon:'\u26d4',title:'Forgetting to Check Document Metadata',desc:'Even if a PDF is meant to be public, its metadata might contain the author\'s internal username, the software version used to create it, or internal network paths.',fix:'Use tools like ExifTool or FOCA to analyze metadata of public documents found via Google Dorking before publishing them.'},
    {icon:'\U0001f3ad',title:'Ignoring Cached Pages',desc:'An administrator might realize a sensitive file is public and delete it from the server. But Google caches pages. An attacker can view the "Cached" version in Google search results long after the file is gone.',fix:'If sensitive data is indexed, you must use Google Search Console to explicitly request removal of the URL from Google\'s cache and index.'}
  ],
  lab:{
    title:'Lab: Discover Exposed Files using Google Dorks',
    difficulty:'Beginner',
    duration:'30 min',
    objectives:['Use basic Google Dork operators','Combine operators to find specific file types','Understand the Google Hacking Database (GHDB)'],
    steps:[
      'Open Google in a web browser.',
      'Search for exposed directory listings containing music files: intitle:"index of" "mp3"',
      'Search for exposed password files on educational domains: site:.edu filetype:txt inurl:passwords',
      'Search for exposed environment files (often containing API keys): filetype:env "DB_PASSWORD"',
      'Visit the Exploit-DB Google Hacking Database (GHDB).',
      'Browse the categories (e.g., "Files Containing Passwords") and test one of the suggested dorks on a bug bounty program target (if authorized).'
    ],
    validation:'You should be able to successfully construct a query combining site:, filetype:, and intitle: to find a specific type of document on a specific domain.'
  },
  quiz:[
    {q:'Which Google search operator restricts results to a specific domain?',opts:['inurl:','intitle:','site:','domain:'],correct:2,fb:'The site: operator (e.g., site:example.com) restricts the search results to only pages indexed from that specific domain or its subdomains.'},
    {q:'If you want to find exposed database backup files, which operator would you use?',opts:['filetype:sql','intext:backup','intitle:database','inurl:db'],correct:0,fb:'The filetype: operator (or ext:) searches for specific file extensions. filetype:sql is commonly used to find exposed SQL database dumps.'},
    {q:'What does the operator intitle:"index of" typically reveal?',opts:['Web application source code','Misconfigured web servers allowing directory browsing','Database schema definitions','Encrypted password hashes'],correct:1,fb:'"Index of" is the default title generated by Apache and other web servers when directory listing is enabled, allowing users to see all files in a directory.'},
    {q:'Why do attackers look at robots.txt files during footprinting?',opts:['To find out which crawler the site uses','To bypass the web application firewall','Because administrators often list sensitive directories they want hidden from search engines','To execute cross-site scripting (XSS) attacks'],correct:2,fb:'Administrators often use robots.txt to tell crawlers not to index sensitive directories (e.g., Disallow: /admin-panel/). Attackers read robots.txt to find exactly where those sensitive directories are.'},
    {q:'Which of the following is a complete Google Dork that would search for PDF documents containing the word "confidential" only on government (.gov) websites?',opts:['site:.gov filetype:pdf intitle:confidential','site:.gov inurl:pdf "confidential"','site:.gov filetype:pdf "confidential"','inurl:.gov filetype:pdf text:confidential'],correct:2,fb:'site:.gov restricts to government domains, filetype:pdf restricts to PDF files, and "confidential" searches for that specific word in the text or title.'},
    {q:'What is the GHDB?',opts:['Google Hacking Database - A repository of known, effective Google Dorks for finding vulnerabilities','Global Hacker Database - A list of known threat actors','General HTTP Debugging Browser - A tool for intercepting web traffic','Google Host Directory Board - A DNS enumeration tool'],correct:0,fb:'The Google Hacking Database (GHDB), hosted by Exploit-DB, is a categorized collection of Google search queries that can uncover sensitive data and vulnerable applications.'},
    {q:'How can an attacker view a sensitive page that was recently deleted from the target server but is still showing up in Google search results?',opts:['By using the inurl: operator','By viewing Google\'s Cached version of the page','By performing a DNS zone transfer','By using the filetype:bak operator'],correct:1,fb:'Google stores a snapshot (cache) of each page it crawls. Even if the page is deleted from the live server, the cached version remains available until Google re-crawls the site and updates its index.'},
    {q:'Which tool automatically extracts metadata (like usernames, software versions, internal paths) from documents found via Google Hacking?',opts:['Nmap','Wireshark','FOCA (Fingerprinting Organizations with Collected Archives)','Metasploit'],correct:2,fb:'FOCA is a tool specifically designed to analyze metadata from documents (PDF, DOCX, etc.) downloaded from a target\'s website, revealing internal network information.'},
    {q:'What does the operator inurl:admin do?',opts:['Logs into the admin panel automatically','Searches for pages where the URL contains the word "admin"','Restricts the search to only administrator-owned domains','Finds files created by the administrator'],correct:1,fb:'The inurl: operator restricts results to pages where the specified string appears somewhere in the URL path.'},
    {q:'Is Google Hacking illegal?',opts:['Yes, it is a form of unauthorized access (hacking)','No, because it only queries Google\'s public index, not the target\'s servers','Yes, but only if you use the GHDB','No, as long as you do not click on the search results'],correct:1,fb:'Google Hacking itself is generally considered legal passive reconnaissance, as you are simply querying Google\'s public search engine. However, accessing or downloading the sensitive files you find without authorization may violate laws.'}
  ],
  flashcards:[
    {f:'Google Dorking',b:'Using advanced search operators to find sensitive information indexed by search engines.'},
    {f:'site:',b:'Google operator that restricts search results to a specific domain or top-level domain (e.g., site:example.com).'},
    {f:'filetype: / ext:',b:'Google operator that restricts results to a specific file extension (e.g., filetype:pdf).'},
    {f:'intitle:',b:'Google operator that finds pages with a specific word in the HTML <title> tag.'},
    {f:'inurl:',b:'Google operator that finds pages with a specific string in the URL path.'},
    {f:'GHDB',b:'Google Hacking Database. A repository of known, effective search queries for uncovering vulnerabilities and sensitive data.'},
    {f:'Directory Listing',b:'A web server misconfiguration (often found with intitle:"index of") that displays all files in a directory.'},
    {f:'FOCA',b:'Fingerprinting Organizations with Collected Archives. A tool for extracting metadata from documents found on a target site.'}
  ],
  ctf:{
    scenario:'A company accidentally left their database backups exposed on their web server with directory listing enabled. The backups are stored in a folder named "db_backups" and the files have a .sql extension.',
    hint:'Construct a Google dork using intitle: and ext:.',
    flag:'CEH{g00gl3_d0rk_m4st3r_2026}',
    points:150
  },
  summary:[
    'Google Dorking uses advanced operators to find sensitive data indexed by search engines.',
    'site:, filetype:, intitle:, and inurl: are the most common and powerful operators.',
    'Directory listings (intitle:"index of") often expose backup files, source code, and configuration files.',
    'Robots.txt should not be used to hide sensitive files, as attackers read it to find them.',
    'Google\'s cache can expose sensitive data even after it has been deleted from the target server.',
    'Document metadata (analyzable with FOCA or ExifTool) reveals internal usernames and software versions.',
    'The GHDB is a valuable resource for finding effective Google Dorks.'
  ]
};

CONTENT['shodan-recon'] = {
  module:'Module 02 \u00b7 Footprinting & Reconnaissance',
  title:'Shodan & IoT Footprinting',
  sub:'The search engine for the Internet of Things (IoT) and internet-connected devices.',
  killchain:{phase:'Reconnaissance',mitre:'T1595.002 \u2014 Active Scanning: Vulnerability Scanning',desc:'Shodan constantly scans the internet, grabbing banners and service information. Attackers use it to find vulnerable devices without scanning the target themselves.'},
  learn:{
    simple:'While Google crawls websites (HTML), Shodan crawls ports and services (banners, headers, device responses). Shodan is a search engine for internet-connected devices: webcams, routers, industrial control systems (SCADA), medical devices, and servers.',
    analogy:'Google is like the yellow pages, listing businesses and their public descriptions. Shodan is like a master list of every building\'s security system, back doors, and open windows. It tells you exactly what hardware and software is running behind the IP address.',
    why:'Scanning a target network directly (e.g., with Nmap) is noisy and often blocked by firewalls or detected by IDS. Shodan has already scanned the internet for you. You can query Shodan\'s database to find vulnerable devices on the target\'s IP range without ever sending a packet to the target.',
    architecture:'Shodan operates a network of global crawlers that continuously scan the IPv4 and IPv6 address space on various ports. When they find an open port, they grab the banner (the response the service sends when connected, like "SSH-2.0-OpenSSH_7.2p2"). This banner information is indexed and made searchable.'
  },
  diagram:{
    title:'Shodan Intelligence Gathering',
    steps:[
      {icon:'\U0001f310',label:'Shodan Crawlers',desc:'Shodan continuously scans the internet, probing open ports and grabbing service banners.'},
      {icon:'\U0001f4c4',label:'Banner Indexing',desc:'The banners (containing software versions, server types, device models) are indexed into a searchable database.'},
      {icon:'\U0001f50d',label:'Attacker Query',desc:'The attacker queries Shodan (e.g., "org:TargetCorp port:22") instead of scanning the target directly.'},
      {icon:'\U0001f4f1',label:'Vulnerability Identification',desc:'Shodan cross-references grabbed banners with known CVEs to flag vulnerable devices.'},
      {icon:'\U0001f5fa\ufe0f',label:'IoT Discovery',desc:'Attackers find misconfigured webcams, industrial control systems, and routers exposed to the internet.'}
    ]
  },
  enterprise:{
    role:'You are performing OSINT on GlobalFinSec Corp.',
    situation:'GlobalFinSec recently acquired a small regional bank. The parent company\'s infrastructure is secure, but you need to footprint the newly acquired subsidiary\'s IP space (192.168.100.0/24 \u2014 simulated public IPs for this example).',
    challenge:'Use Shodan to identify any exposed services or vulnerable devices in the subsidiary\'s IP range without performing active scanning.',
    steps:[
      'Search by IP range: net:192.168.100.0/24',
      'Filter for specific vulnerable services (e.g., RDP): net:192.168.100.0/24 port:3389',
      'Look for exposed webcams or IoT devices: net:192.168.100.0/24 "default password"',
      'Check for known vulnerabilities: net:192.168.100.0/24 vuln:CVE-2019-0708 (BlueKeep)',
      'Search by organization name to find assets not in the known IP range: org:"Acquired Regional Bank"'
    ],
    outcome:'The Shodan query net:192.168.100.0/24 port:3389 revealed three servers with Remote Desktop Protocol exposed to the internet. One of them was flagged by Shodan as vulnerable to BlueKeep (CVE-2019-0708). You gained this intelligence without sending a single packet to the target network.',
    lesson:'Acquisitions often introduce legacy, insecure infrastructure. Attackers use Shodan to find the weakest link in a corporate conglomerate\'s perimeter, completely bypassing the parent company\'s strong defenses.'
  },
  tools:[
    {name:'Shodan Web Interface',cmd:'https://www.shodan.io',desc:'The primary search engine interface'},
    {name:'Shodan CLI',cmd:'shodan search "apache"',desc:'Command-line interface for Shodan (requires API key)'},
    {name:'Censys',cmd:'https://censys.io',desc:'A similar search engine for internet-connected devices and certificates'}
  ],
  commands:{
    win:['Rem - Use a web browser or install the Python Shodan CLI library'],
    lin:['shodan init [API_KEY]','shodan search "org:TargetCorp"','shodan host 8.8.8.8','shodan stats port:22']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Assuming Internal Devices Cannot Be Found on Shodan',desc:'Organizations often think their internal webcams or printers are safe. If port forwarding is misconfigured on the edge router, those internal devices become public and Shodan will index them.',fix:'Regularly search Shodan for your own IP ranges and organization name to ensure no internal devices have been accidentally exposed to the internet.'},
    {icon:'\U0001f534',title:'Relying Solely on Port Numbers',desc:'Searching for port:80 assumes HTTP is running on standard ports. Services are often moved to non-standard ports (e.g., HTTP on 8080 or SSH on 2222).',fix:'Search by service banner or product name rather than just port number. Shodan identifies services regardless of the port they run on.'},
    {icon:'\u26d4',title:'Forgetting the API',desc:'Using the Shodan web interface is slow for large assessments. Failing to use the Shodan API or CLI means missing out on automation and bulk data analysis.',fix:'Obtain a Shodan API key and learn to use the Shodan command-line tool or Python library to script searches and integrate results into other tools.'}
  ],
  lab:{
    title:'Lab: Device Discovery with Shodan',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Understand basic Shodan search filters','Identify exposed IoT devices','Find vulnerable services on specific IP ranges'],
    steps:[
      'Open shodan.io (create a free account if necessary).',
      'Search for exposed webcams: "Server: SQ-WEBCAM" or "webcamXP"',
      'Search for exposed industrial control systems (SCADA/ICS): port:502 (Modbus protocol)',
      'Search for a specific organization: org:"Google"',
      'Search for a specific IP address: host 8.8.8.8 (using the web interface or CLI if installed)',
      'Notice the information provided: open ports, banners, geographic location, and associated CVEs.'
    ],
    validation:'You should be able to successfully construct a Shodan query using filters like port: and org: to find specific types of devices.'
  },
  quiz:[
    {q:'How does Shodan differ from Google?',opts:['Shodan is illegal to use','Shodan crawls web pages (HTML), Google crawls open ports','Google crawls web pages (HTML), Shodan crawls open ports and service banners','Shodan is only for the dark web'],correct:2,fb:'Google indexes the content of web pages. Shodan indexes the banners (metadata) returned by services running on open ports across the internet.'},
    {q:'What is a "banner" in the context of Shodan?',opts:['An advertisement on a website','The text response a service sends when a connection is made (e.g., software version)','A flag captured in a CTF','A type of firewall rule'],correct:1,fb:'A banner is the text returned by a service (like SSH, FTP, or a web server) when a client connects. It often contains the software name and version number.'},
    {q:'Which Shodan filter restricts results to a specific organization or company name?',opts:['company:','org:','domain:','target:'],correct:1,fb:'The org: filter (e.g., org:"GlobalFinSec") searches for IPs registered to a specific organization.'},
    {q:'Why is Shodan considered a "passive" footprinting tool from the attacker\'s perspective?',opts:['Because Shodan doesn\'t find vulnerabilities','Because the attacker queries Shodan\'s database, rather than sending packets directly to the target','Because Shodan only works on local networks','Because it requires no internet connection'],correct:1,fb:'While Shodan\'s crawlers actively scan the internet, an attacker using Shodan is only interacting with Shodan\'s database. No traffic goes directly from the attacker to the target.'},
    {q:'Which of the following is an example of an IoT device frequently found exposed on Shodan?',opts:['A disconnected laptop','An air-gapped server','An unauthenticated IP security camera','A password-protected encrypted hard drive'],correct:2,fb:'Internet of Things (IoT) devices, such as IP cameras, smart home hubs, and default-configured routers, are frequently exposed to the internet and easily found on Shodan.'},
    {q:'What does the Shodan filter vuln: do?',opts:['Exploits the target','Searches for devices known to be affected by a specific CVE (Common Vulnerabilities and Exposures)','Scans the target for all vulnerabilities','Downloads a vulnerability scanner'],correct:1,fb:'The vuln: filter (requires a paid Shodan account or academic access) allows searching for devices that Shodan has identified as vulnerable to a specific CVE (e.g., vuln:CVE-2014-0160 for Heartbleed).'},
    {q:'If you wanted to find exposed Remote Desktop Protocol (RDP) servers, which Shodan query would you use?',opts:['rdp:open','port:3389','service:rdp','protocol:remote_desktop'],correct:1,fb:'RDP typically runs on TCP port 3389. Searching port:3389 will return devices with this port open and the RDP service banner.'},
    {q:'Which tool is a major alternative/competitor to Shodan for internet-wide scanning and device search?',opts:['Censys','Nmap','Wireshark','Metasploit'],correct:0,fb:'Censys (censys.io) is another search engine that continuously scans the internet, indexing devices, services, and TLS/SSL certificates.'},
    {q:'What is SCADA/ICS?',opts:['A type of malware','Supervisory Control and Data Acquisition / Industrial Control Systems (often found exposed on Shodan)','A web application firewall','A secure encryption protocol'],correct:1,fb:'SCADA/ICS refers to systems that control industrial processes (power grids, water treatment, manufacturing). Finding these exposed on Shodan is a critical security risk.'},
    {q:'How can an organization prevent their devices from appearing on Shodan?',opts:['They cannot prevent it','Place devices behind a firewall and do not expose ports to the public internet','Add the devices to a robots.txt file','Ask Shodan to remove them'],correct:1,fb:'Shodan scans public IP addresses. If a device is properly placed behind a firewall with no port forwarding or public IP exposure, Shodan\'s crawlers cannot reach it.'}
  ],
  flashcards:[
    {f:'Shodan',b:'A search engine for internet-connected devices (IoT, servers, routers) that indexes service banners rather than web page content.'},
    {f:'Banner',b:'The text response sent by a service when a connection is made, often revealing software names and version numbers.'},
    {f:'org: (Shodan Filter)',b:'Restricts Shodan search results to IP addresses registered to a specific organization.'},
    {f:'port: (Shodan Filter)',b:'Restricts Shodan search results to devices with a specific port open (e.g., port:22 for SSH).'},
    {f:'IoT (Internet of Things)',b:'Non-standard computing devices (cameras, smart appliances, sensors) connected to the internet, frequently found exposed on Shodan.'},
    {f:'Censys',b:'Another internet-wide scanning search engine, similar to Shodan, particularly strong in indexing TLS/SSL certificates.'},
    {f:'Passive Reconnaissance (via Shodan)',b:'Gathering information about a target by querying Shodan\'s database, avoiding direct interaction with the target\'s network.'},
    {f:'SCADA/ICS',b:'Industrial Control Systems used in manufacturing and infrastructure. Finding these exposed on Shodan indicates a severe security risk.'}
  ],
  ctf:{
    scenario:'You use Shodan to footprint a target organization. You search for their registered IP range and find an exposed IP camera running on port 8081. The banner reveals the camera model.',
    hint:'Think about the Shodan filter used to search for specific devices or organizations.',
    flag:'CEH{sh0d4n_10t_r3c0n_2026}',
    points:150
  },
  summary:[
    'Shodan is a search engine for devices, not websites. It indexes open ports and service banners.',
    'Using Shodan is a form of passive footprinting, as the attacker queries a database, not the target.',
    'Shodan is heavily used to find exposed IoT devices, industrial control systems (SCADA), and vulnerable servers.',
    'Key filters include port:, org:, net:, and vuln:.',
    'Banners reveal software versions, which can be cross-referenced with exploit databases.',
    'Censys is a prominent alternative to Shodan.',
    'Devices properly secured behind firewalls without public exposure will not appear on Shodan.'
  ]
};

CONTENT['social-media-recon'] = {
  module:'Module 02 \u00b7 Footprinting & Reconnaissance',
  title:'Social Media Reconnaissance',
  sub:'Exploiting the human element for organizational intelligence.',
  killchain:{phase:'Reconnaissance',mitre:'T1593.001 \u2014 Search Open Websites/Domains: Social Media',desc:'Social media provides the human context necessary for effective social engineering and reveals technical details employees accidentally share.'},
  learn:{
    simple:'Social Media Reconnaissance is the process of gathering intelligence from platforms like LinkedIn, Twitter, Facebook, and Instagram. It focuses on people \u2014 employees, their roles, relationships, and the information they inadvertently share about their employer.',
    analogy:'If network scanning is looking at a building\'s floor plan, social media recon is reading the diaries of everyone who works there. You learn who has the keys, who is disgruntled, what software they complain about using, and when the security guard goes on break.',
    why:'Humans are the weakest link in security. Social media reveals the organizational chart, reporting structures, and technical stack (from resumes/profiles). This information is gold for crafting highly targeted spear-phishing campaigns (Social Engineering).',
    architecture:'Intelligence is divided into two categories: Technical (software versions, infrastructure details found in job descriptions or employee skills) and Human (names, roles, email formats, relationships, travel schedules, interests). Attackers use automated tools to scrape this data and build comprehensive profiles.'
  },
  diagram:{
    title:'Social Media Intelligence Value',
    steps:[
      {icon:'\U0001f4bc',label:'LinkedIn',desc:'The most valuable platform. Reveals organizational structure, employee roles, technology stacks (skills section), and job openings.'},
      {icon:'\U0001f4e4',label:'Twitter / X',desc:'Reveals real-time activities, complaints about internal tools, conference attendance, and professional networks.'},
      {icon:'\U0001f465',label:'Facebook / Instagram',desc:'Reveals personal interests, family members, pets (often used as passwords), and out-of-office travel schedules.'},
      {icon:'\U0001f4bb',label:'GitHub / StackOverflow',desc:'Reveals code snippets, internal naming conventions, and technical problems employees are actively trying to solve.'},
      {icon:'\U0001f4c4',label:'Glassdoor',desc:'Reveals internal culture, disgruntled employees (prime targets for insider threat recruitment), and management changes.'}
    ]
  },
  enterprise:{
    role:'You are a Red Team operator preparing a spear-phishing campaign against GlobalFinSec Corp.',
    situation:'Your objective is to gain initial access to the internal network by compromising a mid-level IT administrator\'s workstation.',
    challenge:'Use social media reconnaissance to identify a target, understand their role, and craft a convincing spear-phishing pretext.',
    steps:[
      'Search LinkedIn for "GlobalFinSec" and filter by "Information Technology". Identify a target: "John Doe, Systems Administrator".',
      'Review John\'s LinkedIn profile: He lists "AWS Cloud Migration" and "VMware vSphere" as current projects.',
      'Search Twitter for John\'s handle. Discover he recently tweeted about attending the "CloudSec 2024" conference in Las Vegas.',
      'Find his manager on LinkedIn: "Jane Smith, Director of IT Operations".',
      'Craft Pretext: Create a spoofed email from "Jane Smith" to John Doe with the subject "CloudSec 2024 Expense Report Issue", attaching a malicious Excel macro document labeled "Expense_Revisions.xlsm".'
    ],
    outcome:'The highly targeted spear-phishing email bypassed the spam filters. Because the email referenced John\'s actual manager and a conference he actually attended, he opened the attachment and enabled macros, granting the Red Team a reverse shell on his workstation.',
    lesson:'Generic phishing has a low success rate. Spear-phishing fueled by social media reconnaissance has a terrifyingly high success rate because it exploits trust and context.'
  },
  tools:[
    {name:'Sherlock',cmd:'python3 sherlock username',desc:'Hunts for a specific username across hundreds of social media sites'},
    {name:'theHarvester',cmd:'theHarvester -d target.com -b linkedin',desc:'Gathers employee names from LinkedIn associated with a domain'},
    {name:'Maltego',cmd:'maltego',desc:'Visualizes social networks and organizational relationships'},
    {name:'Social-Engineer Toolkit (SET)',cmd:'setoolkit',desc:'Used later in the attack phase to craft the phishing emails based on recon'}
  ],
  commands:{
    win:['Rem - Primarily browser-based research or Python scripts like Sherlock'],
    lin:['python3 sherlock user_handle','theHarvester -d target.com -b linkedin']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Ignoring Job Postings',desc:'Job postings are written by HR, often detailing exactly what technologies, firewalls, and SIEMs the company uses ("Seeking candidate with 5 years experience in Palo Alto Firewalls and Splunk").',fix:'Monitor target job postings continuously. They provide a free inventory of the target\'s security and IT stack.'},
    {icon:'\U0001f534',title:'Underestimating Background Details in Photos',desc:'Employees post "first day at work" photos showing their ID badges (which can be cloned), their desk (showing Post-it notes with passwords), or whiteboards with network diagrams in the background.',fix:'Implement strict policies regarding photography in office spaces. Educate employees on OPSEC (Operational Security) regarding what they post online.'},
    {icon:'\u26d4',title:'Focusing Only on Executives',desc:'Executives are often highly trained against phishing. Mid-level IT staff, HR personnel, and executive assistants have extensive access but are often softer targets.',fix:'Map the entire organization. Assistants have access to the CEO\'s calendar and inbox. IT Helpdesk has admin rights to all workstations.'}
  ],
  lab:{
    title:'Lab: Profiling a Target via Social Media',
    difficulty:'Beginner',
    duration:'30 min',
    objectives:['Map an organizational structure using LinkedIn','Identify potential spear-phishing targets','Correlate usernames across platforms using Sherlock'],
    steps:[
      'Open LinkedIn and search for a large, well-known organization (e.g., a major retailer).',
      'Filter employees by the "Information Technology" department.',
      'Identify the reporting structure: Find a Helpdesk Analyst, an IT Manager, and a CISO.',
      'Note the specific technologies listed in their "Experience" and "Skills" sections.',
      'Install Sherlock (if on a Linux VM): git clone https://github.com/sherlock-project/sherlock.git',
      'Run Sherlock on a known public figure\'s username to see how it finds their accounts across various platforms.'
    ],
    validation:'You should be able to construct a small org chart (Manager -> Employee) and list at least three specific technologies the organization uses, based purely on employee LinkedIn profiles.'
  },
  quiz:[
    {q:'Which social media platform is generally considered the most valuable for mapping an organization\'s technical stack and reporting structure?',opts:['Facebook','Twitter','LinkedIn','Instagram'],correct:2,fb:'LinkedIn is a professional networking site where users voluntarily list their employer, job title, reporting relationships, and the specific technologies they work with (their skills).'},
    {q:'What is the primary goal of Social Media Reconnaissance for an attacker?',opts:['To deface the company\'s social media pages','To gather personal and professional information to craft highly targeted social engineering (spear-phishing) attacks','To crack employee passwords directly','To find IP addresses for network scanning'],correct:1,fb:'While social media can reveal technical details, its primary value is providing the human context (relationships, interests, events) needed to make a spear-phishing email convincing.'},
    {q:'Which open-source tool searches for a specific username across hundreds of different social media platforms?',opts:['Nmap','theHarvester','Sherlock','John the Ripper'],correct:2,fb:'Sherlock is a powerful command-line tool that takes a username and checks for its existence across a vast number of social networks and websites, helping correlate identities.'},
    {q:'Why are corporate job postings considered a valuable OSINT source?',opts:['They contain employee passwords','They often list the specific technologies, firewalls, and software the company uses, revealing their internal tech stack','They provide the IP addresses of internal servers','They contain the company\'s financial records'],correct:1,fb:'Job postings often include detailed requirements (e.g., "Must have experience configuring Cisco ASA firewalls and managing Active Directory"), giving attackers a blueprint of the target\'s infrastructure.'},
    {q:'What is "Spear-Phishing"?',opts:['A generic, mass-emailed scam','A highly targeted phishing attack aimed at a specific individual, utilizing personal details gathered through recon','A physical attack involving unauthorized entry','A type of denial-of-service attack'],correct:1,fb:'Spear-phishing uses the intelligence gathered during social media recon (manager\'s name, recent projects, attended conferences) to craft a customized, highly believable malicious email.'},
    {q:'If an attacker uses LinkedIn to find the name of the IT Director, and then emails an IT Helpdesk employee pretending to be that Director to request a password reset, what type of attack is this?',opts:['Whaling','Pretexting / Impersonation (Social Engineering)','SQL Injection','Cross-Site Scripting'],correct:1,fb:'The attacker is using the organizational structure discovered on LinkedIn to create a convincing pretext (impersonating an authority figure) to manipulate an employee.'},
    {q:'What security risk is associated with employees posting "First Day at Work" photos at their desks?',opts:['No risk, it improves morale','The photos might inadvertently capture ID badges, whiteboards with passwords, or internal network diagrams','It consumes excessive corporate bandwidth','It violates copyright laws'],correct:1,fb:'Background details in photos (whiteboards, sticky notes on monitors, ID badge designs) frequently leak sensitive physical and digital security information. This is an OPSEC (Operational Security) failure.'},
    {q:'Which site is particularly useful for finding disgruntled employees who might be susceptible to insider threat recruitment?',opts:['GitHub','StackOverflow','Glassdoor','Pinterest'],correct:2,fb:'Glassdoor hosts anonymous employee reviews. Attackers analyze these reviews to understand corporate culture, identify internal conflicts, and spot potentially disgruntled employees.'},
    {q:'What information can an attacker glean from a developer\'s StackOverflow questions?',opts:['The developer\'s home address','The specific coding problems, technologies, and internal naming conventions used within the company','The company\'s marketing strategy','The CEO\'s travel schedule'],correct:1,fb:'Developers often post code snippets or describe specific technical environments when asking for help on StackOverflow, accidentally revealing internal architecture and vulnerabilities.'},
    {q:'What is OPSEC?',opts:['Open Source Email Collection','Operational Security - The process of identifying and protecting generally unclassified information that could be useful to an adversary','Organizational Phishing Security Education Course','Online Profile Scanning and Enumeration Check'],correct:1,fb:'Operational Security (OPSEC) involves recognizing what public information (like social media posts) could be pieced together by an adversary to form a threat, and taking steps to protect that information.'}
  ],
  flashcards:[
    {f:'Social Media Recon',b:'Gathering intelligence from social platforms to understand a target\'s organizational structure, employee roles, and technology stack.'},
    {f:'Spear-Phishing',b:'A highly targeted phishing attack crafted using personal and professional details gathered during social media reconnaissance.'},
    {f:'LinkedIn (for OSINT)',b:'The primary source for mapping corporate hierarchies and identifying specific technologies used by an organization.'},
    {f:'Sherlock',b:'An open-source tool used to hunt down a specific username across hundreds of different social media sites and platforms.'},
    {f:'Job Postings (OSINT)',b:'Publicly available job descriptions that inadvertently reveal the specific hardware, software, and security tools an organization uses.'},
    {f:'OPSEC',b:'Operational Security. The practice of protecting seemingly harmless pieces of public information that an adversary could piece together.'},
    {f:'Glassdoor (for OSINT)',b:'Used to gauge corporate culture and identify potentially disgruntled employees susceptible to insider threat recruitment.'},
    {f:'Pretexting',b:'A social engineering technique where an attacker creates a fabricated scenario (based on recon data) to manipulate a target into divulging information.'}
  ],
  ctf:{
    scenario:'You are profiling a target company. You find a Reddit account belonging to one of their SysAdmins. They use the same username on all platforms. Use a tool to find their GitHub account and find the flag in their bio.',
    hint:'The tool Sherlock is used to find accounts with the same username across different platforms.',
    flag:'CEH{s0c14l_m3d14_0s1nt_2026}',
    points:150
  },
  summary:[
    'Social media recon focuses on the human element, providing the context needed for social engineering.',
    'LinkedIn is the most critical platform for mapping organizational structure and identifying technology stacks.',
    'Job postings are a free inventory of a target\'s internal security and IT infrastructure.',
    'Automated tools like Sherlock help correlate identities across multiple platforms.',
    'Spear-phishing relies entirely on the quality of intelligence gathered during this phase.',
    'Poor OPSEC by employees (backgrounds in photos, complaining on Twitter) creates significant vulnerabilities.',
    'Developers posting on StackOverflow or GitHub often leak internal architecture details.'
  ]
};
"""

if INJECT_BEFORE in html:
    pos = html.find(INJECT_BEFORE)
    html = html[:pos] + MODULE02_REMAINING_CONTENT + '\n\n' + html[pos:]
    ok.append('Module 02 remaining topics (google-hacking, shodan-recon, social-media-recon) injected')
else:
    fail.append('INJECT_BEFORE marker missing for Module 02 remaining')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('=' * 55)
print('MODULE 02 CONTENT INJECTION COMPLETE')
print('=' * 55)
for s in ok: print(f'  [OK]  {s}')
for s in fail: print(f'  [FAIL] {s}')
print()
print(f'New size: {len(html):,} bytes / {html.count(chr(10)):,} lines')
