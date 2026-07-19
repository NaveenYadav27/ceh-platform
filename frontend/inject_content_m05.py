"""
CEH Platform — Content Injection Script
Fills in all tab content for:
- Module 05 Full (3 topics, all 8 tabs)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

INJECT_BEFORE = '// ==========================================================\n// AUTO-STUB GENERATOR'

ok = []
fail = []

MODULE05_CONTENT = """
// =================================================================
// MODULE 05 — Vulnerability Analysis
// =================================================================

CONTENT['vuln-concepts'] = {
  module:'Module 05 \u00b7 Vulnerability Analysis',
  title:'Vulnerability Analysis Concepts',
  sub:'Identifying the weaknesses in the armor.',
  killchain:{phase:'Vulnerability Analysis',mitre:'TA0046 \u2014 Discovery',desc:'Once services are enumerated, attackers map them to known flaws. This phase transitions reconnaissance into actionable exploit selection.'},
  learn:{
    simple:'Vulnerability analysis is the process of discovering weaknesses in systems, applications, and networks that an attacker could exploit. It involves comparing the software versions found during enumeration against databases of known flaws.',
    analogy:'If scanning is finding an unlocked door, vulnerability analysis is noticing that the door lock is a model known to be easily picked with a standard paperclip, or that the hinges are mounted on the outside where they can be unscrewed.',
    why:'You cannot randomly throw exploits at a target and hope they work; that is noisy and often crashes the system (Denial of Service). Vulnerability analysis ensures you select the exact exploit designed for the specific flaw present on the target.',
    architecture:'Vulnerabilities generally fall into three categories: Design Flaws (inherently insecure protocols like Telnet), Implementation Flaws (coding errors like Buffer Overflows or SQL Injection), and Operational Flaws (misconfigurations like default passwords or open shares).'
  },
  diagram:{
    title:'The Vulnerability Lifecycle',
    steps:[
      {icon:'\U0001f50d',label:'1. Discovery',desc:'A researcher or attacker finds a new flaw in software.'},
      {icon:'\u26a0\ufe0f',label:'2. Zero-Day Phase',desc:'The flaw is actively exploited in the wild before the vendor knows about it or has created a patch.'},
      {icon:'\U0001f4e3',label:'3. Disclosure & CVE',desc:'The flaw is publicly disclosed and assigned a CVE (Common Vulnerabilities and Exposures) tracking number.'},
      {icon:'\U0001f4a3',label:'4. Exploit Publishing',desc:'Proof-of-Concept (PoC) exploit code is published on Exploit-DB or added to Metasploit.'},
      {icon:'\U0001f6e1\ufe0f',label:'5. Patch Release',desc:'The vendor releases a security update fixing the flaw.'},
      {icon:'\u23f1\ufe0f',label:'6. The Patch Gap',desc:'The critical window between when the patch is released and when organizations actually install it. This is when most breaches occur.'}
    ]
  },
  enterprise:{
    role:'You are the Vulnerability Management Lead at GlobalFinSec Corp.',
    situation:'Your automated weekly vulnerability scan completes and generates a 500-page PDF report detailing 12,000 "Critical" and "High" vulnerabilities across the enterprise.',
    challenge:'The IT patching team cannot patch 12,000 vulnerabilities this week. You must prioritize the findings based on true enterprise risk.',
    steps:[
      'Filter out False Positives: Verify if the scanner flagged a vulnerability based solely on the banner, even if a backported patch was applied.',
      'Contextualize Asset Value: Prioritize the 50 vulnerabilities affecting external-facing web servers and Domain Controllers over the 11,000 affecting isolated internal print servers.',
      'Check Exploitability: Prioritize vulnerabilities that have known, weaponized exploit code in Metasploit over theoretical vulnerabilities.',
      'Check Mitigating Controls: Lower the priority of a vulnerability if a Web Application Firewall (WAF) or IPS is already actively blocking the exploit signature.'
    ],
    outcome:'By applying context (asset value, exploitability, mitigating controls), you reduced the 12,000 "critical" findings to 14 "immediate action required" vulnerabilities. The IT team patched those 14 within 48 hours, significantly reducing actual enterprise risk without burning out the staff.',
    lesson:'Vulnerability scanning without contextual analysis is just noise. True vulnerability management is risk-based prioritization, not just running a tool and handing over a PDF.'
  },
  tools:[
    {name:'NVD (National Vulnerability Database)',cmd:'nvd.nist.gov',desc:'The US government repository of standards-based vulnerability management data'},
    {name:'Exploit-DB',cmd:'exploit-db.com',desc:'An archive of public exploits and corresponding vulnerable software'},
    {name:'SearchSploit',cmd:'searchsploit apache 2.4',desc:'Command-line search tool for Exploit-DB'}
  ],
  commands:{
    win:['Rem - Primarily browser-based research for manual analysis'],
    lin:['searchsploit vsftpd 2.3.4','nmap --script=vuln target']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Treating Vulnerability Scanning as Penetration Testing',desc:'Running Nessus and handing the client the automated PDF report is not a penetration test. It is a vulnerability assessment.',fix:'A penetration test involves exploiting those vulnerabilities to prove the risk and impact. Vulnerability scanning is just one phase of the assessment.'},
    {icon:'\U0001f534',title:'Trusting Automated Scanners Blindly (False Positives)',desc:'Scanners often rely on banner grabbing. If an admin backported a patch (fixed the code but didn\'t update the version number), the scanner will falsely report the system as vulnerable.',fix:'Always manually verify critical vulnerabilities. If a scanner says a server is vulnerable to MS17-010, verify it manually or safely test the exploit.'},
    {icon:'\u26d4',title:'Ignoring "Low" or "Informational" Findings',desc:'Scanners might flag an open SMB share or a verbose error message as "Low" severity.',fix:'Attackers chain "Low" severity findings together. An informational finding (verbose error leaking a path) combined with a low finding (open share) can lead to a critical compromise.'}
  ],
  lab:{
    title:'Lab: Manual Vulnerability Research',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Map a discovered service to a known exploit','Use SearchSploit','Understand Exploit-DB'],
    steps:[
      'Assume your Nmap scan from Module 3 discovered "vsftpd 2.3.4" running on port 21.',
      'Open a terminal and run: searchsploit vsftpd 2.3.4',
      'Note the exploit name (Backdoor Command Execution) and the path to the exploit script.',
      'Open a web browser and go to www.exploit-db.com.',
      'Search for "vsftpd 2.3.4". Read the exploit code (usually Ruby or Python) to see how it works.',
      'Search the National Vulnerability Database (NVD) for CVE-2011-2523 to read the official description of this flaw.'
    ],
    validation:'You should understand the workflow of taking a service version (from Nmap), searching for it in an exploit database, and finding the specific CVE and exploit code.'
  },
  quiz:[
    {q:'What is the primary difference between a Vulnerability Assessment and a Penetration Test?',opts:['A Vulnerability Assessment is illegal; a Penetration Test is authorized','A Vulnerability Assessment identifies and reports potential flaws; a Penetration Test actively exploits those flaws to prove the risk','A Penetration Test is automated; a Vulnerability Assessment is manual','There is no difference; the terms are synonymous'],correct:1,fb:'Vulnerability assessments stop at discovery and reporting. Penetration tests go a step further by actively exploiting the vulnerabilities (weaponization) to demonstrate actual impact.'},
    {q:'What is a "Zero-Day" vulnerability?',opts:['A vulnerability that has zero impact on the system','A flaw that has been patched for zero days','A vulnerability that is known to the vendor but has not yet been patched, or is actively being exploited before the vendor is even aware of it','A vulnerability that takes zero days to exploit'],correct:2,fb:'A zero-day means the vendor has had "zero days" to fix the issue. There is no patch available, making it highly dangerous.'},
    {q:'Which of the following is an example of a "Design Flaw" vulnerability?',opts:['A buffer overflow in a C program','A web application vulnerable to SQL Injection','An administrator leaving the default password on a router','The use of the Telnet protocol, which transmits all data in plaintext by default'],correct:3,fb:'Telnet is functioning exactly as it was designed to. The flaw is in the fundamental design of the protocol (lack of encryption), not an error in the code (implementation) or a misconfiguration (operational).'},
    {q:'What is a "False Positive" in the context of vulnerability scanning?',opts:['When a scanner fails to find a vulnerability that actually exists','When a scanner reports a vulnerability that does not actually exist on the target system','When an exploit fails to work','When a system is secure'],correct:1,fb:'A false positive occurs when the scanner incorrectly flags a secure system as vulnerable. This often happens if the scanner relies solely on checking version banners and misses that a patch was backported.'},
    {q:'Why do attackers rely on resources like Exploit-DB?',opts:['To download viruses and malware to infect their own machines','To find pre-written Proof-of-Concept (PoC) exploit code for specific software versions discovered during enumeration','To scan targets automatically','To generate phishing emails'],correct:1,fb:'Exploit-DB is an archive of public exploits. Instead of writing custom exploit code from scratch for every vulnerability, attackers search Exploit-DB for existing code matching the target\'s software version.'},
    {q:'Which command-line tool allows you to search a local copy of the Exploit-DB archive?',opts:['Nmap','Metasploit','SearchSploit','Wireshark'],correct:2,fb:'SearchSploit is a command-line search utility for Exploit-DB that allows you to take an offline copy of the database and search it quickly on your Kali machine.'},
    {q:'What is the "Patch Gap"?',opts:['The time it takes to download a patch','The space on a hard drive reserved for updates','The critical window of time between when a vendor releases a patch and when an organization actually installs it','A vulnerability in a patch management system'],correct:2,fb:'The Patch Gap is when most systems are compromised. Once a patch is released, attackers reverse-engineer it to figure out what the flaw was, write an exploit, and attack organizations that haven\'t installed the patch yet.'},
    {q:'If a vulnerability scanner identifies 10,000 vulnerabilities, how should an enterprise prioritize remediation?',opts:['Patch all "Low" vulnerabilities first because they are easiest','Patch them in alphabetical order','Prioritize based on Asset Value (external vs internal), Exploitability (is there a known exploit?), and Mitigating Controls','Run the scanner again until the number goes down'],correct:2,fb:'True vulnerability management is risk-based. A "Critical" vulnerability on an internal print server is less risk to the enterprise than a "High" vulnerability on the public-facing e-commerce database.'},
    {q:'What type of vulnerability is caused by an administrator failing to change the factory default credentials on an IoT device?',opts:['Design Flaw','Implementation Flaw','Operational Flaw (Misconfiguration)','Zero-Day'],correct:2,fb:'The software code isn\'t broken (Implementation), and the protocol isn\'t flawed (Design). The error was made by the human operator failing to configure it securely.'},
    {q:'How do vulnerability scanners primarily identify flaws without crashing the system?',opts:['By running exploits against every port','By comparing the service banners and versions found against a database of known vulnerable versions','By deleting files and seeing if the system recovers','By asking the administrator for a list of vulnerabilities'],correct:1,fb:'Most automated scanners are non-intrusive. They grab banners, extract configuration details, and compare that data against a massive database of signatures to infer if a vulnerability exists.'}
  ],
  flashcards:[
    {f:'Vulnerability Assessment',b:'Identifying, quantifying, and ranking vulnerabilities. Does not involve active exploitation.'},
    {f:'Penetration Test',b:'Actively exploiting vulnerabilities to prove risk and demonstrate impact.'},
    {f:'Zero-Day',b:'A vulnerability actively exploited in the wild before a patch exists or before the vendor is aware.'},
    {f:'False Positive',b:'A scanner incorrectly reporting that a vulnerability exists when the system is actually secure.'},
    {f:'Exploit-DB',b:'A public archive of exploits and vulnerable software. Used to find pre-written PoC code.'},
    {f:'SearchSploit',b:'Command-line tool to search a local copy of Exploit-DB.'},
    {f:'Patch Gap',b:'The time between a patch being released and an organization installing it. The window of highest risk.'},
    {f:'Operational Flaw',b:'A vulnerability caused by misconfiguration, such as leaving default passwords or open shares.'}
  ],
  ctf:{
    scenario:'You discover a server running "vsftpd 2.3.4". You want to find an exploit for it quickly using the command line on your Kali Linux machine. What tool do you use to search your local copy of Exploit-DB?',
    hint:'It is a combination of the words Search and Exploit.',
    flag:'CEH{vuln_4ss3ssm3nt_c0r3}',
    points:150
  },
  summary:[
    'Vulnerability Analysis maps enumerated services to known flaws.',
    'It is distinct from Penetration Testing (which requires exploitation).',
    'Zero-days have no patch; the Patch Gap is the window when most exploits occur.',
    'SearchSploit and Exploit-DB are the primary resources for finding weaponized code.',
    'Scanners generate False Positives (especially with backported patches).',
    'Enterprise vulnerability management requires prioritizing patches based on business risk and asset context, not just CVSS scores.'
  ]
};

CONTENT['cve-cvss'] = {
  module:'Module 05 \u00b7 Vulnerability Analysis',
  title:'CVE & CVSS Scoring',
  sub:'The universal language of vulnerabilities.',
  killchain:{phase:'Vulnerability Analysis',mitre:'TA0046 \u2014 Discovery',desc:'Understanding CVE and CVSS allows attackers to quickly identify the most devastating flaws and defenders to prioritize their patching efforts.'},
  learn:{
    simple:'CVE (Common Vulnerabilities and Exposures) is a dictionary of publicly known security vulnerabilities, giving each one a unique ID (e.g., CVE-2017-0144). CVSS (Common Vulnerability Scoring System) is the formula used to score the severity of that vulnerability from 0.0 to 10.0.',
    analogy:'CVE is like a catalog of car parts, where every defective brake pad gets a specific part number so mechanics worldwide know exactly what is broken. CVSS is the safety rating (from 1 to 10) telling the mechanic whether the car is safe to drive (1) or will explode immediately (10).',
    why:'Before CVE, every security vendor called vulnerabilities by different names, making communication impossible. The CVE system provides a standard identifier. The CVSS score removes subjective opinions ("I think this is bad") and replaces it with an objective metric based on how the vulnerability is exploited and its impact.',
    architecture:'A CVSS v3/v4 score is calculated from Base Metrics (Attack Vector, Attack Complexity, Privileges Required, User Interaction) and Impact Metrics (Confidentiality, Integrity, Availability). A CVSS 10.0 is the worst-case scenario: Network exploitable, low complexity, no privileges required, total system compromise.'
  },
  diagram:{
    title:'Deconstructing a CVSS Score (e.g., Log4Shell CVE-2021-44228)',
    steps:[
      {icon:'\U0001f310',label:'Attack Vector (AV)',desc:'Network (N) vs Local (L) vs Physical (P). Log4Shell is Network (N), meaning it can be exploited remotely over the internet.'},
      {icon:'\U0001f9e9',label:'Attack Complexity (AC)',desc:'Low (L) vs High (H). Log4Shell is Low (L), meaning it does not require complex conditions or timing to exploit.'},
      {icon:'\U0001f511',label:'Privileges Required (PR)',desc:'None (N) vs Low (L) vs High (H). Log4Shell is None (N), meaning an unauthenticated attacker can trigger it.'},
      {icon:'\U0001f464',label:'User Interaction (UI)',desc:'None (N) vs Required (R). Log4Shell is None (N), meaning no one has to click a link for it to work.'},
      {icon:'\U0001f4a5',label:'Impact: C/I/A',desc:'Confidentiality, Integrity, Availability. Log4Shell is High (H) for all three, resulting in total system compromise.'},
      {icon:'\U0001f4ca',label:'Final Score',desc:'Because it is Network, Low Complexity, No Privs, No Interaction, and High Impact across the board, it scores a 10.0 (Critical).'}
    ]
  },
  enterprise:{
    role:'You are the CISO of GlobalFinSec Corp.',
    situation:'Your vulnerability scanner reports two vulnerabilities on an internal database server. Vuln A has a CVSS Base Score of 9.8. Vuln B has a CVSS Base Score of 7.5.',
    challenge:'Determine which vulnerability to patch first, knowing that you can adjust the CVSS Base Score with Environmental Metrics.',
    steps:[
      'Analyze Vuln A (CVSS 9.8): It is an RCE (Remote Code Execution) vulnerability. However, it requires the attacker to be on the local subnet (Attack Vector: Adjacent).',
      'Analyze Vuln B (CVSS 7.5): It is a Privilege Escalation vulnerability. It requires local access (Attack Vector: Local) but allows a low-privilege user to become Domain Admin.',
      'Apply Environmental Context: The database server is highly isolated. No regular users are on its subnet. Therefore, Vuln A (Adjacent) is very difficult to reach.',
      'However, GlobalFinSec relies heavily on contractors who have low-level access to the database server. Vuln B (Privilege Escalation) is highly likely to be exploited by an insider.'
    ],
    outcome:'You used the CVSS Environmental Metrics to lower the score of Vuln A (due to network isolation) and raise the priority of Vuln B (due to business context). You patched Vuln B first, preventing an insider threat from achieving Domain Admin.',
    lesson:'The CVSS Base Score (what you see in the news) assumes the worst-case scenario. True enterprise security requires adjusting the Base Score with Temporal (is there an exploit available?) and Environmental (is the system isolated?) metrics.'
  },
  tools:[
    {name:'NVD (National Vulnerability Database)',cmd:'nvd.nist.gov',desc:'Searchable database of all CVEs and their CVSS scores'},
    {name:'CVSS Calculator',cmd:'www.first.org/cvss/calculator',desc:'Web tool to calculate custom CVSS scores based on environmental factors'}
  ],
  commands:{
    win:['Rem - Conceptual framework, no specific command-line tools'],
    lin:['Rem - Conceptual framework, no specific command-line tools']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Treating CVSS as a Risk Score',desc:'CVSS measures Severity, not Risk. A CVSS 10.0 vulnerability on a disconnected, powered-off laptop in a safe has high severity but zero business risk.',fix:'Risk = Threat x Vulnerability x Impact. Use CVSS to understand the vulnerability, but use business context to determine the actual risk.'},
    {icon:'\U0001f534',title:'Ignoring Temporal Metrics',desc:'A vulnerability might score a 9.0 when discovered. But if no exploit code is ever written, the actual threat is lower.',fix:'Use CVSS Temporal metrics to adjust the score based on Exploit Code Maturity. If a weaponized Metasploit module exists, the priority increases.'},
    {icon:'\u26d4',title:'Panicking over "Critical" Scores without Checking the Attack Vector',desc:'The media panics over every 9.0+ CVSS score. However, if the Attack Vector is "Physical" (requires the attacker to plug a USB drive into the server), the threat to a cloud environment is zero.',fix:'Always read the CVSS string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H). The "AV" (Attack Vector) tells you how close the attacker needs to be.'}
  ],
  lab:{
    title:'Lab: Decoding a CVSS String',
    difficulty:'Beginner',
    duration:'15 min',
    objectives:['Understand the CVSS v3.1 vector string','Calculate a score using FIRST.org'],
    steps:[
      'Open a web browser and navigate to the FIRST.org CVSS v3.1 Calculator (first.org/cvss/calculator/3.1).',
      'Input the following string manually by clicking the buttons: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N',
      'This represents Cross-Site Scripting (XSS). Notice the Attack Vector (Network), Privileges Required (None), User Interaction (Required - someone must click a link).',
      'Observe the final Base Score (6.1 - Medium).',
      'Change the Attack Vector to "Local" and observe how the score drops.',
      'Change the Impact (C/I/A) to "High" and observe how the score rises.'
    ],
    validation:'You should understand how changing individual variables (like whether user interaction is required) dramatically alters the final severity score of a vulnerability.'
  },
  quiz:[
    {q:'What does CVE stand for?',opts:['Critical Vulnerability Evaluation','Common Vulnerabilities and Exposures','Computer Virus Execution','Central Vulnerability Engine'],correct:1,fb:'CVE stands for Common Vulnerabilities and Exposures. It is a dictionary that provides a standardized identifier for publicly known vulnerabilities.'},
    {q:'What is the primary purpose of the CVSS (Common Vulnerability Scoring System)?',opts:['To assign a standardized name to a vulnerability','To provide an objective, numerical score reflecting the severity of a vulnerability','To automatically patch systems','To generate exploit code'],correct:1,fb:'While CVE provides the name, CVSS provides the score (0.0 to 10.0), allowing organizations to objectively assess severity and prioritize patching.'},
    {q:'In a CVSS v3.1 score, what does an Attack Vector (AV) of "Network" mean?',opts:['The vulnerability can be exploited remotely over the internet or a wide area network','The attacker must be on the same local subnet (e.g., connected to the same switch)','The attacker must have physical access to the machine','The vulnerability only affects network switches'],correct:0,fb:'An Attack Vector of Network (N) is the most dangerous, as the attacker can launch the exploit from anywhere in the world.'},
    {q:'Which of the following scenarios describes a CVSS "User Interaction" requirement of "None"?',opts:['An attacker sends a phishing email and the victim clicks a link','An attacker sends a malformed packet to a web server, which crashes immediately without any user action','An administrator must log in for the payload to execute','A user must download and run a malicious PDF'],correct:1,fb:'"None" means the vulnerability can be exploited solely by the attacker\'s actions, requiring no participation or mistakes from a victim user. These are highly prized by attackers for automated worms.'},
    {q:'What are the three components of the CVSS Impact Metric?',opts:['Attack Vector, Complexity, Privileges','Confidentiality, Integrity, Availability (The CIA Triad)','Exploitability, Remediation, Report Confidence','Scope, User Interaction, Timing'],correct:1,fb:'The impact of a vulnerability is measured by how much it compromises the CIA Triad. A remote code execution (RCE) flaw usually scores High in all three.'},
    {q:'If a vulnerability requires an attacker to already possess a valid user account on the system to exploit it, which CVSS metric is affected?',opts:['Attack Vector','User Interaction','Privileges Required','Scope'],correct:2,fb:'The Privileges Required (PR) metric determines if the attacker needs Low (standard user) or High (administrator) privileges before launching the exploit. "None" means unauthenticated attackers can use it.'},
    {q:'What is the highest possible CVSS Base Score?',opts:['5.0','10.0','100.0','It is infinite'],correct:1,fb:'The CVSS scale runs from 0.0 (None) to 10.0 (Critical). A 10.0 typically represents a remotely exploitable, unauthenticated vulnerability resulting in total system compromise.'},
    {q:'Why might a CISO adjust a CVSS Base Score using Environmental Metrics?',opts:['Because the Base Score is always wrong','To account for the specific security controls (like firewalls or isolation) deployed in their specific organization that might mitigate the vulnerability','To hide vulnerabilities from auditors','To increase the CVSS score to get more budget'],correct:1,fb:'The Base Score assumes the worst-case scenario. Environmental Metrics allow an organization to lower the score if they have compensating controls (e.g., the vulnerable system is air-gapped).'},
    {q:'What does the CVSS Temporal Metric "Exploit Code Maturity" assess?',opts:['How old the vulnerability is','Whether reliable, weaponized exploit code is publicly available (e.g., in Metasploit) or if it is just a theoretical concept','The age of the attacker','How long the system has been unpatched'],correct:1,fb:'A vulnerability might have a high Base Score, but if no one has figured out how to write a working exploit for it (Exploit Code Maturity is Unproven), the immediate threat is lower.'},
    {q:'A vulnerability scanner reports a CVSS 9.8 vulnerability. You investigate and find the Attack Vector is "Physical". What does this mean for a cloud-hosted web server?',opts:['It is in immediate danger of a remote attack','It must be patched within 1 hour','The vulnerability poses almost zero risk, because an attacker cannot physically touch a cloud server in an AWS data center','The cloud provider is breached'],correct:2,fb:'Physical Attack Vectors require inserting a USB drive or typing on the local keyboard. For a cloud server, this is impossible, demonstrating why you must read the CVSS vector string, not just the number.'}
  ],
  flashcards:[
    {f:'CVE',b:'Common Vulnerabilities and Exposures. A standardized dictionary providing a unique ID for known vulnerabilities.'},
    {f:'CVSS',b:'Common Vulnerability Scoring System. A numerical score (0.0 to 10.0) reflecting the severity of a vulnerability.'},
    {f:'Attack Vector (AV)',b:'CVSS metric. Determines how close the attacker needs to be: Network (N), Adjacent (A), Local (L), Physical (P).'},
    {f:'Privileges Required (PR)',b:'CVSS metric. Determines if the attacker needs authentication: None (N), Low (L), High (H).'},
    {f:'User Interaction (UI)',b:'CVSS metric. Determines if a victim must click a link or open a file (Required) or if it can be automated (None).'},
    {f:'CVSS Impact Metrics',b:'Measures the effect on Confidentiality, Integrity, and Availability (CIA Triad).'},
    {f:'CVSS Environmental Metrics',b:'Used by defenders to adjust the Base Score based on their specific network architecture and mitigating controls.'},
    {f:'CVSS Temporal Metrics',b:'Adjusts the score based on factors that change over time, primarily the availability of weaponized exploit code.'}
  ],
  ctf:{
    scenario:'You are analyzing a vulnerability with the vector string: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H. Based on the PR metric (PR:N), does the attacker need to log in to exploit this?',
    hint:'PR stands for Privileges Required. N stands for None.',
    flag:'CEH{cv3_cvss_nvd_2026}',
    points:150
  },
  summary:[
    'CVE provides the Name (Identity). CVSS provides the Number (Severity).',
    'CVSS is scored from 0.0 to 10.0 (Critical).',
    'The CVSS Base Score assumes a worst-case scenario without any defensive controls.',
    'Attack Vector (Network) + Privileges (None) + User Interaction (None) creates the most dangerous vulnerabilities (Worms).',
    'Defenders must use Environmental and Temporal metrics to translate CVSS Severity into actual business Risk.',
    'Always read the Vector String (AV:N/AC:L...), never just the final number.'
  ]
};

CONTENT['nessus-openvas'] = {
  module:'Module 05 \u00b7 Vulnerability Analysis',
  title:'Automated Vulnerability Scanners',
  sub:'Deploying Nessus and OpenVAS at scale.',
  killchain:{phase:'Vulnerability Analysis',mitre:'T1595.002 \u2014 Active Scanning: Vulnerability Scanning',desc:'Automated scanners drastically reduce the time required to map thousands of services to known CVEs across massive enterprise networks.'},
  learn:{
    simple:'Automated vulnerability scanners (like Nessus, OpenVAS, and Qualys) are software tools that scan networks, discover live hosts and open ports, and then query those ports with thousands of specific probes to identify known vulnerabilities (CVEs) and misconfigurations.',
    analogy:'If Nmap is walking down a hallway checking which doors are unlocked, Nessus is a robot walking down the hallway with a ring of 100,000 specific keys, trying every single key in every single unlocked door, and writing a report on which keys worked.',
    why:'Manual vulnerability research (taking an Nmap version and searching Exploit-DB) is required for targeted penetration testing, but it does not scale. To secure an enterprise with 5,000 servers, you must use automated scanners to identify the baseline vulnerabilities quickly.',
    architecture:'Scanners use "Plugins" or "Signatures" (small scripts). When a scan runs, the engine matches discovered services (e.g., Apache) with all plugins related to Apache. It sends the probe, analyzes the response against the signature, and flags a vulnerability if it matches.'
  },
  diagram:{
    title:'How Vulnerability Scanners Work',
    steps:[
      {icon:'\U0001f4e1',label:'1. Ping Sweep',desc:'Scanner identifies live hosts on the target network.'},
      {icon:'\U0001f513',label:'2. Port Scan',desc:'Scanner identifies open TCP and UDP ports on live hosts.'},
      {icon:'\U0001f4c4',label:'3. Service Enumeration',desc:'Scanner grabs banners to identify the software and OS running.'},
      {icon:'\U0001f9e9',label:'4. Plugin Selection',desc:'Scanner selects relevant vulnerability signatures (e.g., skips IIS plugins if the server is Apache).'},
      {icon:'\U0001f4a3',label:'5. Vulnerability Probing',desc:'Scanner sends specific, safe probes to verify if the vulnerability exists (without actually exploiting it).'},
      {icon:'\U0001f4ca',label:'6. Reporting',desc:'Scanner generates a report grouping vulnerabilities by severity (Critical, High, Medium, Low) and providing CVSS scores.'}
    ]
  },
  enterprise:{
    role:'You are a Vulnerability Management Engineer at GlobalFinSec Corp.',
    situation:'You run a weekly unauthenticated Nessus scan across the server subnet. It consistently reports 50 "Medium" vulnerabilities related to outdated software versions, but no "Critical" vulnerabilities.',
    challenge:'The CISO believes the network is secure. You know unauthenticated scans provide a false sense of security. You must prove the value of Authenticated (Credentialed) scanning.',
    steps:[
      'Run the baseline: Execute the standard unauthenticated Nessus scan on a test server.',
      'Configure Credentials: Create a dedicated service account with local administrator rights on the test server.',
      'Configure Nessus: Add the service account credentials to the Nessus scan policy (Credentialed Scan).',
      'Run Credentialed Scan: Execute the scan again.',
      'Compare Results: The unauthenticated scan found 5 vulnerabilities (mostly web server banners). The authenticated scan found 142 vulnerabilities, including 3 Criticals (missing Windows KBs, outdated local Adobe Reader, and an insecure local privilege escalation flaw).'
    ],
    outcome:'You presented the comparison to the CISO. Unauthenticated scans only see the outside of the server (the ports). Authenticated scans log into the server, read the registry, check installed software, and read configuration files. The CISO mandated authenticated scanning across the enterprise.',
    lesson:'Unauthenticated vulnerability scanning is only good for finding perimeter flaws. To truly understand enterprise risk, you must perform Authenticated (Credentialed) scanning.'
  },
  tools:[
    {name:'Nessus',cmd:'(Web GUI)',desc:'The industry standard commercial vulnerability scanner (Tenable)'},
    {name:'OpenVAS (Greenbone)',cmd:'(Web GUI)',desc:'The most popular open-source, full-featured vulnerability scanner'},
    {name:'Qualys',cmd:'(Cloud GUI)',desc:'Enterprise cloud-based vulnerability management platform'},
    {name:'Nexpose / InsightVM',cmd:'(Web GUI)',desc:'Rapid7\'s enterprise vulnerability scanner'}
  ],
  commands:{
    win:['Rem - Scanners are operated via Web GUI, not command line'],
    lin:['Rem - OpenVAS/Nessus services are started via systemctl, operated via browser']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Relying on Unauthenticated Scans',desc:'Unauthenticated scans only see what an external attacker sees. They miss 90% of internal vulnerabilities (missing OS patches, outdated local software, insecure permissions).',fix:'Always configure Authenticated (Credentialed) scans using SSH keys (Linux) or SMB credentials (Windows) for accurate enterprise vulnerability management.'},
    {icon:'\U0001f534',title:'Scanning Fragile Systems with Default Policies',desc:'Running a default Nessus "Full Scan" against legacy mainframes, IoT devices, or SCADA equipment will almost certainly crash them due to the aggressive probing.',fix:'Create custom, lightweight scan policies for fragile systems. Disable aggressive plugins (like brute-forcing or DoS checks) and slow down the scan timing.'},
    {icon:'\u26d4',title:'Handing a 500-Page Report to IT',desc:'Exporting a Nessus PDF and throwing it over the fence to the sysadmin team destroys relationships and guarantees nothing gets patched.',fix:'Analyze the report. Filter out false positives. Group the fixes (e.g., "Applying this one Windows cumulative update fixes 80 of these CVEs"). Provide actionable, prioritized remediation plans.'}
  ],
  lab:{
    title:'Lab: Authenticated vs Unauthenticated Scanning',
    difficulty:'Intermediate',
    duration:'45 min',
    objectives:['Configure a basic vulnerability scan','Understand the difference credentials make','Analyze scan results'],
    steps:[
      'If you have access to Nessus Essentials or OpenVAS (Greenbone):',
      'Create a new scan policy targeting a vulnerable VM (e.g., Metasploitable).',
      'Run the scan WITHOUT credentials. Note the number of Critical and High vulnerabilities found.',
      'Edit the scan policy. Go to the Credentials tab and add the SSH username/password for the target VM.',
      'Run the scan again WITH credentials.',
      'Compare the reports. The credentialed scan will list vulnerabilities in local packages (e.g., outdated kernel, vulnerable local sudo configuration) that the unauthenticated scan could not see.'
    ],
    validation:'You should observe a massive increase in findings during the authenticated scan, proving that logging into the box provides the only accurate vulnerability assessment.'
  },
  quiz:[
    {q:'What is the primary function of an automated vulnerability scanner like Nessus?',opts:['To actively exploit systems and gain root access','To map network topology','To discover live hosts, open ports, and probe services against a database of known signatures to identify vulnerabilities','To encrypt network traffic'],correct:2,fb:'Scanners automate the discovery phase and match found services against a massive database of plugins/signatures (CVEs). They do not exploit the vulnerabilities.'},
    {q:'Which of the following is an open-source alternative to the commercial Nessus scanner?',opts:['Qualys','Nexpose','OpenVAS (Greenbone)','Burp Suite'],correct:2,fb:'OpenVAS started as a fork of the Nessus engine when Nessus became closed-source commercial software. It is the premier open-source vulnerability scanner.'},
    {q:'What is a "Credentialed" (or Authenticated) vulnerability scan?',opts:['A scan performed by a certified professional','A scan where the scanner is provided with usernames and passwords (or SSH keys) to log into the target systems and check local registries and files','A scan that only targets password login portals','A scan that requires a license key'],correct:1,fb:'Credentialed scans allow the scanner to log into the target (via SSH or SMB), enabling it to check installed software versions, missing patches, and local configurations that are invisible from the outside.'},
    {q:'Why might a vulnerability scanner cause a Denial of Service (DoS) on a legacy network?',opts:['Because scanners are malware','Because the aggressive probing of thousands of ports and malformed packets can overwhelm fragile or older systems (like SCADA or IoT)','Because scanners intentionally shut down systems they find vulnerable','Because scanners encrypt the hard drives'],correct:1,fb:'Vulnerability scanners are noisy and aggressive. Sending thousands of malformed packets to a fragile legacy system can easily crash its network stack or the service itself.'},
    {q:'In Nessus, what is a "Plugin"?',opts:['A browser extension for viewing reports','A small script or signature that checks for a specific vulnerability or misconfiguration','A hardware dongle required to run the software','A module that exploits the target'],correct:1,fb:'Scanners use a library of Plugins (Tenable/Nessus) or NVTs (Network Vulnerability Tests in OpenVAS). Each plugin contains the logic to test for one specific vulnerability (e.g., a plugin to check for MS17-010).'},
    {q:'If you need to scan a highly fragile medical device network, how should you adjust your vulnerability scanner settings?',opts:['Enable the "Aggressive" profile','Enable brute-force plugins','Create a custom policy that disables DoS plugins, disables brute-forcing, and reduces the scan speed/concurrent connections','Scan it during peak operational hours'],correct:2,fb:'Fragile networks require custom, gentle scan policies to prevent disruption to critical services.'},
    {q:'What is a major limitation of Unauthenticated vulnerability scans?',opts:['They are illegal','They can only find vulnerabilities on the perimeter/network services and cannot see missing local OS patches or local software flaws','They take weeks to run','They require root access'],correct:1,fb:'An unauthenticated scan only sees what is listening on open ports. It cannot see if Adobe Reader is outdated on the hard drive, or if a Windows patch from last Tuesday was missed.'},
    {q:'When a vulnerability scanner flags a web server as vulnerable based ONLY on the "Server: Apache/2.2.14" banner, what is the primary risk of this finding?',opts:['It might trigger an exploit','It is likely a False Positive if the administrator backported security patches without changing the version banner','It will crash the server','It proves the server is compromised'],correct:1,fb:'Linux distributions (like Debian/RedHat) often "backport" security fixes into older software versions without changing the main version number. Scanners relying only on banners will flag this as a false positive.'},
    {q:'How does a vulnerability scanner differ from a port scanner (like basic Nmap)?',opts:['Port scanners find vulnerabilities; vulnerability scanners find ports','Port scanners stop at identifying open ports and services; vulnerability scanners actively probe those services with thousands of specific tests to identify known CVEs','Vulnerability scanners are much faster','There is no difference'],correct:1,fb:'Nmap tells you "Apache 2.4 is running on port 80." Nessus goes further by sending specific payloads to check if that Apache 2.4 instance is vulnerable to 50 different known CVEs.'},
    {q:'Which phase of the ethical hacking methodology relies heavily on the output of automated vulnerability scanners?',opts:['Reconnaissance','Scanning / Vulnerability Analysis','Maintaining Access','Covering Tracks'],correct:1,fb:'Vulnerability scanners are the primary tool used during the Vulnerability Analysis phase to map enumerated services to actionable exploits.'}
  ],
  flashcards:[
    {f:'Vulnerability Scanner',b:'Automated tool (Nessus, OpenVAS, Qualys) that probes networks to identify missing patches and known CVEs.'},
    {f:'Credentialed Scan',b:'An authenticated scan where the scanner logs into the target (SSH/SMB) to accurately check local files, registries, and missing patches.'},
    {f:'Unauthenticated Scan',b:'A scan without login credentials. Can only identify vulnerabilities visible from the network perimeter (open ports).'},
    {f:'Plugin / Signature',b:'The individual script within a scanner that tests for one specific vulnerability.'},
    {f:'OpenVAS',b:'The leading open-source, full-featured vulnerability scanner.'},
    {f:'Nessus',b:'The industry-standard commercial vulnerability scanner by Tenable.'},
    {f:'False Positive (Scanning)',b:'When a scanner flags a secure system as vulnerable, often because it relied solely on checking version banners instead of behavior.'},
    {f:'Fragile Systems (SCADA/IoT)',b:'Systems that can easily crash during automated vulnerability scanning. Require custom, slow, gentle scan policies.'}
  ],
  ctf:{
    scenario:'You configure Nessus to log into a Windows target using SMB credentials to perform a highly accurate scan of missing registry patches. What type of scan is this?',
    hint:'It requires credentials. It is an _______ scan.',
    flag:'CEH{n3ssus_0p3nv4s_sc4n}',
    points:150
  },
  summary:[
    'Automated scanners (Nessus, OpenVAS, Qualys) map enumerated services to known CVEs at scale.',
    'Scanners use plugins/signatures to probe for specific vulnerabilities.',
    'Credentialed (Authenticated) scans log into the target and are required for accurate enterprise assessments.',
    'Unauthenticated scans only see perimeter flaws and generate high rates of False Positives.',
    'Always use custom, gentle policies when scanning fragile SCADA, medical, or legacy systems.',
    'Vulnerability scanning is not penetration testing; it is the prerequisite step before exploitation.'
  ]
};
"""

if INJECT_BEFORE in html:
    pos = html.find(INJECT_BEFORE)
    html = html[:pos] + MODULE05_CONTENT + '\n\n' + html[pos:]
    ok.append('Module 05 (vuln-concepts, cve-cvss, nessus-openvas) injected')
else:
    fail.append('INJECT_BEFORE marker missing for Module 05')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('=' * 55)
print('MODULE 05 CONTENT INJECTION COMPLETE')
print('=' * 55)
for s in ok: print(f'  [OK]  {s}')
for s in fail: print(f'  [FAIL] {s}')
print()
print(f'New size: {len(html):,} bytes / {html.count(chr(10)):,} lines')
