"""
CEH Platform — Content Injection Script
Fills in all tab content for:
- Module 01 Topics 4-6 (add diagram + enterprise + pitfalls)
- Module 02 Full (6 topics, all 8 tabs)
- Module 03 Full (5 topics, all 8 tabs)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

INJECT_BEFORE = '// ==========================================================\n// AUTO-STUB GENERATOR'

# ─────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────
ok = []
fail = []

def add_content(js_block):
    global html
    pos = html.find(INJECT_BEFORE)
    if pos == -1:
        fail.append('INJECT_BEFORE marker not found')
        return False
    html = html[:pos] + js_block + '\n\n' + html[pos:]
    return True

# =================================================================
# MODULE 01 — TOPIC 4: hacking-methodologies
# Add diagram + enterprise + pitfalls
# =================================================================
ANCHOR_M01T4 = "    learn: { simple: 'A hacking methodology is a step-by-step blueprint"
PREFIX_M01T4 = """    diagram:{
      title:'CEH 5-Phase Attack Methodology',
      steps:[
        {icon:'\U0001f50d',label:'Phase 1 — Reconnaissance',desc:'Passive and active information gathering: OSINT, WHOIS, DNS, social media, Shodan, Google Dorking. No direct contact with target.'},
        {icon:'\U0001f4e1',label:'Phase 2 — Scanning',desc:'Active probing: port scanning (Nmap), vulnerability scanning (Nessus), OS fingerprinting, service version detection, network mapping.'},
        {icon:'\U0001f513',label:'Phase 3 — Gaining Access',desc:'Exploiting discovered vulnerabilities: password cracking, buffer overflows, social engineering, web app attacks, privilege escalation.'},
        {icon:'\U0001f50f',label:'Phase 4 — Maintaining Access',desc:'Establishing persistence: backdoors, rootkits, scheduled tasks, remote access trojans (RATs). Evading AV/EDR detection.'},
        {icon:'\U0001f9f9',label:'Phase 5 — Covering Tracks',desc:'Erasing evidence: deleting logs, clearing bash_history, timestomping, using covert channels, removing malware artifacts.'}
      ]
    },
    enterprise:{
      role:'You are the Red Team Lead at GlobalFinSec Corp simulating an APT attack.',
      situation:'The CISO has approved a 2-week purple team exercise to test detection capabilities across all 5 phases of the CEH methodology. The Blue Team knows an exercise is happening, but not when or how.',
      challenge:'Execute a realistic kill chain against the test environment (192.168.50.0/24) mapping every action to a CEH phase and a MITRE ATT&CK technique.',
      steps:[
        'Phase 1 — Recon: Run theHarvester and Maltego to map employee names, emails, and LinkedIn profiles. Passive only.',
        'Phase 2 — Scan: Run nmap -sS -sV -O -A 192.168.50.0/24 to map open ports and service versions.',
        'Phase 3 — Gain Access: Use Metasploit to exploit an unpatched EternalBlue (MS17-010) on a test Windows host.',
        'Phase 4 — Maintain Access: Deploy a Meterpreter reverse shell and set up a scheduled task for persistence.',
        'Phase 5 — Cover Tracks: Clear the Windows Event Log (wevtutil cl System), delete prefetch files, timestomp artifacts.'
      ],
      outcome:'The exercise revealed the Blue Team detected Phases 2 and 3 (Nmap scan and exploit) but completely missed Phases 1, 4, and 5. Post-exercise, SIEM rules were added for PowerShell execution and scheduled task creation.',
      lesson:'Defenders must monitor all 5 phases, not just the exploit. Recon and post-exploitation are the most commonly undetected phases in real-world attacks.'
    },
    pitfalls:[
      {icon:'\u26a0\ufe0f',title:'Skipping the Methodology and Going Straight to Exploitation',desc:'New penetration testers often skip recon and scanning, jumping directly to running Metasploit. This leads to noisy, incomplete, and incomplete assessments.',fix:'Always follow the methodology in order. Thorough recon reveals attack surface that scanning alone misses.'},
      {icon:'\U0001f534',title:'Confusing MITRE ATT&CK with the CEH Kill Chain',desc:'MITRE ATT&CK has 14 Tactics, CEH has 5 phases. Students mix them up in exams and real assessments.',fix:'CEH 5 phases = strategic overview. MITRE ATT&CK = granular technique library. Use both together: CEH phase identifies "where you are," ATT&CK identifies "how you do it."'},
      {icon:'\u26d4',title:'Not Clearing Tracks During a Real Engagement',desc:'Leaving Nmap logs, Metasploit sessions, and dropped files on a client system is unprofessional and creates security risks.',fix:'Always clean up artifacts at the end of an engagement. Document what was placed on systems and have a cleanup checklist in your methodology.'},
      {icon:'\U0001f3ad',title:'Treating the Cyber Kill Chain and CEH Methodology as Identical',desc:'The Lockheed Martin Cyber Kill Chain is 7 steps focused on the attacker; CEH methodology is 5 phases focused on the pen tester. They overlap but differ.',fix:'Know both: CEH methodology for exam and engagement planning; Cyber Kill Chain for understanding and disrupting real attacker behavior.'}
    ],
    """
if ANCHOR_M01T4 in html:
    html = html.replace(ANCHOR_M01T4, PREFIX_M01T4 + ANCHOR_M01T4, 1)
    ok.append('M01T4 hacking-methodologies enriched')
else:
    fail.append('M01T4 anchor not found')

# =================================================================
# MODULE 01 — TOPIC 5: security-controls
# Add diagram + enterprise + pitfalls
# =================================================================
ANCHOR_M01T5 = "    learn: { simple: 'Security controls are safeguards or countermeasures"
PREFIX_M01T5 = """    diagram:{
      title:'Defense in Depth — Layered Security Control Model',
      steps:[
        {icon:'\U0001f4dc',label:'Administrative Controls (Policies)',desc:'Policies, procedures, security awareness training, background checks, NDAs, acceptable use policies. The human and process layer.'},
        {icon:'\U0001f6aa',label:'Physical Controls (Barriers)',desc:'Fences, locks, biometric access, security guards, CCTV, mantrap entry systems. Prevent unauthorized physical access.'},
        {icon:'\U0001f4bb',label:'Technical Controls — Perimeter',desc:'Firewalls, IDS/IPS, DMZ, VPN gateways, network segmentation. The first technical line of defense.'},
        {icon:'\U0001f512',label:'Technical Controls — Endpoint',desc:'Antivirus, EDR, host-based firewalls, disk encryption (BitLocker/FileVault), patch management, application whitelisting.'},
        {icon:'\U0001f4ca',label:'Detective Controls — Monitoring',desc:'SIEM, log management, DLP, UEBA, network traffic analysis. Detect anomalies during or after an incident.'},
        {icon:'\U0001f527',label:'Corrective & Recovery Controls',desc:'Incident response playbooks, backup and restore, disaster recovery plans, business continuity. Minimize damage and restore operations.'}
      ]
    },
    enterprise:{
      role:'You are the Information Security Manager at GlobalFinSec Corp.',
      situation:'A ransomware attack encrypted 200 workstations across two branch offices. Post-incident review revealed: no endpoint EDR, backups existed but had never been tested, and there was no formal incident response plan.',
      challenge:'Design a layered Defense in Depth architecture that would have prevented or contained this ransomware attack.',
      steps:[
        'Administrative: Mandate quarterly phishing simulation training (ransomware enters via phishing in 91% of cases).',
        'Technical - Perimeter: Deploy email filtering (ATP) with attachment sandboxing to block malicious Office macros.',
        'Technical - Endpoint: Deploy EDR (CrowdStrike/Defender for Endpoint) with behavioral ransomware detection.',
        'Detective: Configure SIEM alerts for mass file encryption events (high write IOPS + file extension changes).',
        'Recovery: Implement 3-2-1 backup rule: 3 copies, 2 different media, 1 offsite. Test restoration monthly.'
      ],
      outcome:'Post-implementation, a second ransomware attempt 6 months later was detected at the email gateway (ATP blocked the macro), and EDR quarantined the sample on the one endpoint that clicked through within 8 seconds.',
      lesson:'Defense in Depth means no single control failure causes a breach. Every layer buys time for detection and response.'
    },
    pitfalls:[
      {icon:'\u26a0\ufe0f',title:'Relying on a Single Control Type',desc:'Organizations often deploy only technical controls (firewall, antivirus) while ignoring administrative controls (training, policies). When the firewall is bypassed, nothing stops the attacker.',fix:'Implement all three control types: Administrative, Technical, and Physical. A policy without a technical enforcement mechanism is just a wish.'},
      {icon:'\U0001f534',title:'Confusing Control Type with Control Function',desc:'Students mix up "what kind" (Admin/Technical/Physical) with "what it does" (Preventive/Detective/Corrective). A firewall is Technical + Preventive. An audit log is Technical + Detective.',fix:'Always classify controls on both axes: Type (Admin/Technical/Physical) AND Function (Preventive/Detective/Corrective/Deterrent/Recovery/Compensating).'},
      {icon:'\u26d4',title:'Deploying Compensating Controls Permanently',desc:'Compensating controls are meant to be temporary substitutes when primary controls cannot be implemented. Organizations often leave them in place indefinitely.',fix:'Document compensating controls with a sunset date and remediation plan. Review quarterly. Replace with primary controls as soon as feasible.'},
      {icon:'\U0001f3ad',title:'Never Testing Recovery Controls',desc:'Organizations have backups but never test restoration. Backups that fail during a ransomware recovery are a critical control failure.',fix:'Test backup restoration on a quarterly schedule. Simulate complete system recovery in a staging environment. Backup integrity without restoration testing is false assurance.'}
    ],
    """
if ANCHOR_M01T5 in html:
    html = html.replace(ANCHOR_M01T5, PREFIX_M01T5 + ANCHOR_M01T5, 1)
    ok.append('M01T5 security-controls enriched')
else:
    fail.append('M01T5 anchor not found')

# =================================================================
# MODULE 01 — TOPIC 6: security-laws
# Add diagram + enterprise + pitfalls
# =================================================================
ANCHOR_M01T6 = "    learn: { simple: 'Information security laws are government-enforced rules"
PREFIX_M01T6 = """    diagram:{
      title:'Regulatory Compliance Framework Hierarchy',
      steps:[
        {icon:'\U0001f1ea\U0001f1fa',label:'GDPR (EU) — Privacy Law',desc:'General Data Protection Regulation. Applies to any org processing EU citizen data. Max fine: 4% of global annual revenue or €20M. Right to be forgotten, data portability, 72-hour breach notification.'},
        {icon:'\U0001f3e5',label:'HIPAA (USA) — Healthcare Data',desc:'Health Insurance Portability and Accountability Act. Protects electronic Protected Health Information (ePHI). Applies to covered entities and business associates. Fines up to $1.9M/year.'},
        {icon:'\U0001f4b3',label:'PCI-DSS — Payment Card Data',desc:'Payment Card Industry Data Security Standard. Mandatory for any entity storing, processing, or transmitting cardholder data. 12 core requirements including encryption, access control, and quarterly scans.'},
        {icon:'\U0001f4bc',label:'SOX (USA) — Corporate Finance',desc:'Sarbanes-Oxley Act. Requires accurate financial reporting controls for publicly traded US companies. IT controls for financial systems are audited annually.'},
        {icon:'\U0001f4cb',label:'ISO/IEC 27001 — ISMS Standard',desc:'International standard for Information Security Management Systems. Certification demonstrates systematic approach to managing sensitive information. Risk-based framework with 93 controls in Annex A.'},
        {icon:'\U0001f5a5\ufe0f',label:'NIST CSF — Cybersecurity Framework',desc:'US NIST Cybersecurity Framework: Identify, Protect, Detect, Respond, Recover. Voluntary guidance for critical infrastructure. Widely adopted as a baseline globally.'}
      ]
    },
    enterprise:{
      role:'You are the Chief Information Security Officer (CISO) at GlobalFinSec Corp.',
      situation:'GlobalFinSec processes credit card payments for 2 million EU customers and stores electronic health insurance records for their employee benefits program. A breach has just been discovered — 500,000 customer records were accessed by an unauthorized party.',
      challenge:'Identify which regulatory frameworks are triggered, what the notification deadlines are, and what the maximum financial exposure is.',
      steps:[
        'Identify frameworks: GDPR (EU customer data) + HIPAA (employee health insurance ePHI) + PCI-DSS (credit card data) are all triggered.',
        'GDPR: 72-hour breach notification to the supervisory authority (Article 33). Notify affected individuals "without undue delay."',
        'HIPAA: 60-day notification to HHS Office for Civil Rights + affected individuals. If >500 individuals, notify prominent media.',
        'PCI-DSS: Immediately notify your acquiring bank and card brands (Visa/Mastercard). Engage a PCI Forensic Investigator (PFI).',
        'Calculate exposure: GDPR max = 4% of global revenue. PCI-DSS = $5,000-$100,000/month fines + potential card brand termination.'
      ],
      outcome:'GlobalFinSec notified authorities within 68 hours (GDPR compliant), engaged a PFI for PCI-DSS forensics, and avoided the maximum fines by demonstrating existing controls and rapid response. Total regulatory fines: €2.1M (reduced from potential €15M).',
      lesson:'Multi-framework compliance is not a checklist exercise — it requires a unified data classification policy that maps every data type to its regulatory requirements before a breach occurs.'
    },
    pitfalls:[
      {icon:'\u26a0\ufe0f',title:'Treating GDPR as Europe-Only',desc:'Organizations outside the EU assume GDPR does not apply to them. If you process data of EU residents — regardless of where you are located — GDPR applies to you.',fix:'Audit your entire data pipeline. If any EU resident data is processed, stored, or transmitted by your systems, GDPR compliance is mandatory.'},
      {icon:'\U0001f534',title:'Confusing ISO 27001 Certification with PCI-DSS Compliance',desc:'ISO 27001 is a framework for information security management. PCI-DSS is a specific standard for cardholder data. They are complementary but neither substitutes for the other.',fix:'Map your compliance requirements by data type. Credit card data = PCI-DSS. Personal data of EU citizens = GDPR. Patient health data = HIPAA. Each may require separate controls.'},
      {icon:'\u26d4',title:'Missing Breach Notification Deadlines',desc:'GDPR requires 72-hour notification. HIPAA requires 60 days. Many organizations lack incident response plans that include regulatory notification procedures, missing these deadlines and incurring additional fines.',fix:'Build regulatory notification timelines into your Incident Response Plan. Create notification templates in advance. Designate a DPO (Data Protection Officer) for GDPR compliance.'},
      {icon:'\U0001f3ad',title:'Achieving Compliance Once, Then Neglecting It',desc:'Compliance is treated as a one-time project. Frameworks like PCI-DSS require quarterly vulnerability scans and annual penetration tests. Letting these lapse creates non-compliance.',fix:'Build compliance into operational BAU (business as usual). Use GRC tools (Archer, ServiceNow) to automate compliance tracking and schedule recurring control assessments.'}
    ],
    """
if ANCHOR_M01T6 in html:
    html = html.replace(ANCHOR_M01T6, PREFIX_M01T6 + ANCHOR_M01T6, 1)
    ok.append('M01T6 security-laws enriched')
else:
    fail.append('M01T6 anchor not found')

# =================================================================
# MODULE 02 — Full Content Injection
# All 6 topics before the auto-stub generator
# =================================================================

MODULE02_CONTENT = """
// =================================================================
// MODULE 02 — Footprinting & Reconnaissance
// =================================================================

CONTENT['footprinting-concepts'] = {
  module:'Module 02 \u00b7 Footprinting & Reconnaissance',
  title:'Footprinting Concepts',
  sub:'Understanding the target landscape before the first packet is sent.',
  killchain:{phase:'Reconnaissance',mitre:'TA0043 \u2014 Reconnaissance',desc:'Footprinting is the first and most critical phase \u2014 the quality of your intelligence determines the success of every subsequent phase.'},
  learn:{
    simple:'Footprinting is the process of systematically collecting information about a target organization \u2014 its infrastructure, employees, technologies, and security posture \u2014 before any attack or test begins.',
    analogy:'Think of footprinting like a detective building a case file before making an arrest. They don\'t burst through the door immediately \u2014 they stake out the building, interview neighbors, check public records, and photograph entrances. Only then do they plan the operation.',
    why:'Without footprinting, a penetration tester is blind. They might exploit a vulnerability on a test server while missing a critical production database. Footprinting ensures complete scope coverage and reduces noise during active testing.',
    architecture:'Footprinting is divided into Passive (no direct contact with target \u2014 OSINT, WHOIS, DNS, social media, job postings) and Active (direct contact \u2014 ping sweeps, traceroutes, port scanning). CEH methodology demands passive footprinting first to avoid detection.'
  },
  diagram:{
    title:'Footprinting Intelligence Collection Pyramid',
    steps:[
      {icon:'\U0001f30e',label:'Public OSINT',desc:'Start with fully public sources: company website, LinkedIn, job postings, news articles, SEC filings, GitHub repositories.'},
      {icon:'\U0001f4c4',label:'WHOIS & DNS Records',desc:'Query WHOIS databases for domain registration details (registrant, admin contact, name servers). DNS records reveal mail servers (MX), subdomains (A/CNAME), zone transfers.'},
      {icon:'\U0001f50d',label:'Search Engine Footprinting',desc:'Google Dorking, Bing, DuckDuckGo. Find exposed documents, login pages, error messages, cached pages, directory listings.'},
      {icon:'\U0001f4f1',label:'Social Media Intelligence',desc:'LinkedIn employee profiles reveal technology stack (Java developer, AWS engineer), org chart, key personnel, and corporate culture.'},
      {icon:'\U0001f4e7',label:'Email Footprinting',desc:'Identify email format (firstname.lastname@company.com). Tools: Hunter.io, theHarvester. Email headers reveal internal mail server IPs.'},
      {icon:'\U0001f5fa\ufe0f',label:'Network Footprinting',desc:'Traceroute, Nmap host discovery, BGP routing analysis. Map the network perimeter, identify ISPs, cloud providers, CDNs.'}
    ]
  },
  enterprise:{
    role:'You are the External Red Team Operator at GlobalFinSec Corp.',
    situation:'You have been given written authorization to perform a Black Box external penetration test. You know only the company name: GlobalFinSec Corp. You must build a complete intelligence dossier before active testing begins.',
    challenge:'Using only passive footprinting techniques, construct a complete target profile including: IP ranges, employee names, technology stack, and potential entry points.',
    steps:[
      'WHOIS: whois globalfinsec.com \u2014 note registrant details, registration date, name servers.',
      'DNS: dig globalfinsec.com ANY \u2014 discover all DNS records including MX (mail servers), SPF records, subdomains.',
      'theHarvester: theHarvester -d globalfinsec.com -b google,linkedin \u2014 collect employee emails and names.',
      'LinkedIn: Search "GlobalFinSec" on LinkedIn \u2014 map org chart, technology mentions in profiles, recent job postings.',
      'Shodan: shodan search "globalfinsec.com" \u2014 find exposed services, server banners, TLS certificates with subdomains.',
      'Document: Create a target profile: IP ranges, email format, identified employees, tech stack (Apache 2.4, PHP 7.4, MySQL).'
    ],
    outcome:'After 4 hours of passive footprinting, you identified: 3 external IPs, 12 subdomains including dev.globalfinsec.com and staging.globalfinsec.com, the email format (firstname.l@globalfinsec.com), 47 employee LinkedIn profiles, and the technology stack (AWS EC2, Nginx, Node.js).',
    lesson:'A complete passive footprinting phase is what separates a professional penetration test from a noisy automated scan. The staging subdomain discovered through Shodan was the actual entry point.'
  },
  tools:[
    {name:'theHarvester',cmd:'theHarvester -d target.com -b google,linkedin,bing',desc:'Email and subdomain OSINT collection'},
    {name:'Maltego',cmd:'maltego',desc:'Visual OSINT mapping and relationship analysis'},
    {name:'Shodan',cmd:'shodan search "target.com"',desc:'Internet-connected device discovery'},
    {name:'WHOIS',cmd:'whois target.com',desc:'Domain registration information lookup'}
  ],
  commands:{
    win:['nslookup target.com','nslookup -type=MX target.com','tracert target.com','ping -n 4 target.com'],
    lin:['whois target.com','dig target.com ANY','dig +short MX target.com','traceroute target.com','host -t ns target.com']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Skipping Passive Footprinting and Going Straight to Active Scanning',desc:'Active scanning (Nmap, ping sweeps) immediately alerts IDS/IPS and can violate scope boundaries. Many testers skip recon and start scanning.',fix:'Always exhaust passive footprinting before any active technique. You should know more about the target from OSINT alone than most of their own IT staff.'},
    {icon:'\U0001f534',title:'Missing Subdomain Discovery',desc:'Many testers only test the main domain. Subdomains (dev., staging., admin., api.) are where the most critical vulnerabilities hide and are frequently out of hardening scope.',fix:'Always perform comprehensive subdomain enumeration: Sublist3r, Amass, dnsx, Certificate Transparency logs (crt.sh).'},
    {icon:'\u26d4',title:'Ignoring Job Postings as Intelligence',desc:'Job postings are goldmines: "We use Java Spring Boot on AWS with Postgres" tells you the exact stack. "Seeking Splunk admin" tells you what SIEM they run.',fix:'Systematically scrape job postings from LinkedIn, Indeed, and the company careers page. Every technology mention is an intelligence data point.'},
    {icon:'\U0001f3ad',title:'Not Verifying Information Before Acting On It',desc:'WHOIS data may be outdated. DNS records may point to decommissioned servers. Acting on unverified intelligence wastes time and creates false findings.',fix:'Cross-reference information from multiple sources. If WHOIS says one thing and Shodan says another, investigate before drawing conclusions.'}
  ],
  lab:{
    title:'Lab: Build a Full Target Intelligence Dossier',
    difficulty:'Beginner',
    duration:'45 min',
    objectives:['Perform passive OSINT footprinting on a designated practice target','Discover subdomains, emails, and technology stack','Produce a written intelligence report'],
    steps:[
      'Run: whois scanme.nmap.org and record registrant, name servers, and creation date.',
      'Run: dig scanme.nmap.org ANY to discover all DNS record types.',
      'Run: theHarvester -d nmap.org -b bing -l 200 to find emails and subdomains.',
      'Visit crt.sh and search for "%.nmap.org" to find subdomains via Certificate Transparency logs.',
      'Search Shodan: shodan search "hostname:nmap.org" and record exposed services.',
      'Compile your findings into a written dossier: IP ranges, subdomains, emails, technology stack, key personnel.'
    ],
    validation:'Your dossier should include: at least 3 subdomains, the primary IP address, the web server software, and at least 2 email addresses or employee names.'
  },
  quiz:[
    {q:'What is the primary goal of footprinting?',opts:['Exploiting vulnerabilities','Collecting information about the target without triggering alerts','Cracking passwords','Establishing persistence'],correct:1,fb:'Footprinting is the intelligence-gathering phase designed to build a complete picture of the target before any active testing begins.'},
    {q:'Which type of footprinting involves no direct interaction with the target system?',opts:['Active footprinting','Passive footprinting','Network footprinting','Physical footprinting'],correct:1,fb:'Passive footprinting uses only publicly available information (OSINT) and never directly contacts the target, making it undetectable.'},
    {q:'Which DNS record type is used to find a domain\'s mail servers?',opts:['A record','CNAME record','MX record','PTR record'],correct:2,fb:'MX (Mail Exchange) records specify the mail servers responsible for accepting email on behalf of a domain.'},
    {q:'What information does WHOIS provide about a domain?',opts:['Website source code','Registrant name, address, registration date, name servers','Employee passwords','Internal network topology'],correct:1,fb:'WHOIS databases contain domain registration information including registrant details, registration/expiration dates, and authoritative name servers.'},
    {q:'Which tool is specifically designed for visual OSINT mapping and relationship analysis?',opts:['Nmap','Maltego','Wireshark','Metasploit'],correct:1,fb:'Maltego is a powerful OSINT and link analysis tool that creates visual graphs of relationships between entities (domains, emails, people, organizations).'},
    {q:'A DNS zone transfer (AXFR) reveals:',opts:['Encrypted password hashes','All DNS records for a domain, exposing complete network infrastructure','Credit card numbers','Source code of web applications'],correct:1,fb:'A zone transfer copies the entire DNS database for a zone. Misconfigured DNS servers that allow public zone transfers expose all subdomains, IP addresses, and internal hostnames.'},
    {q:'Which command performs reverse DNS lookup to find the hostname associated with an IP?',opts:['nslookup -type=A 8.8.8.8','dig -x 8.8.8.8','ping 8.8.8.8','traceroute 8.8.8.8'],correct:1,fb:'dig -x performs reverse DNS lookup using PTR records. nslookup -type=PTR 8.8.8.8 is the Windows equivalent.'},
    {q:'What is "Google Dorking"?',opts:['A type of SQL injection','Using advanced Google search operators to find sensitive information','A network scanning technique','A social engineering attack'],correct:1,fb:'Google Dorking uses advanced search operators (site:, filetype:, intitle:, inurl:) to find sensitive information exposed on public websites that Google has indexed.'},
    {q:'theHarvester is primarily used for:',opts:['Cracking WPA2 passwords','Collecting emails, subdomains, and employee names from public sources','Buffer overflow exploitation','Network packet capture'],correct:1,fb:'theHarvester is an OSINT tool that queries search engines, PGP key servers, and other sources to collect email addresses, subdomains, hosts, and employee names.'},
    {q:'Which Shodan search query finds servers with a specific hostname?',opts:['shodan host: target.com','shodan search "hostname:target.com"','shodan query hostname target.com','shodan -h target.com'],correct:1,fb:'The Shodan search filter "hostname:target.com" returns all indexed hosts associated with that hostname. Other useful filters: port:, org:, ssl.cert.subject.cn:.'}
  ],
  flashcards:[
    {f:'Footprinting',b:'The first phase of hacking \u2014 systematically collecting information about a target organization before any attack or penetration test.'},
    {f:'Passive Footprinting',b:'Intelligence gathering using only publicly available sources with NO direct contact with the target. Completely undetectable.'},
    {f:'Active Footprinting',b:'Intelligence gathering that involves direct interaction with the target (ping, traceroute, DNS queries to target\'s servers). May trigger IDS alerts.'},
    {f:'WHOIS',b:'A protocol and database system that stores domain registration information: registrant, admin contact, name servers, registration dates.'},
    {f:'MX Record',b:'Mail Exchange DNS record. Specifies the mail server(s) responsible for accepting email for a domain.'},
    {f:'Zone Transfer (AXFR)',b:'A DNS mechanism to replicate the full DNS database. A misconfigured server allowing public zone transfers exposes all subdomains and internal IPs.'},
    {f:'theHarvester',b:'OSINT tool for collecting email addresses, subdomains, employee names, and IP addresses from public search engines and sources.'},
    {f:'Google Dork',b:'Advanced Google search using operators (site:, filetype:, intitle:, inurl:) to find sensitive or hidden information indexed by Google.'}
  ],
  ctf:{
    scenario:'You run: dig axfr @ns1.globalfinsec-lab.com globalfinsec-lab.com and receive a successful zone transfer listing all internal subdomains. One subdomain is "flag.globalfinsec-lab.com" with the TXT record containing the flag. What is the flag?',
    hint:'Zone transfers expose TXT records. The flag is in the format CEH{...}.',
    flag:'CEH{f00tpr1nt_c0nc3pts_2026}',
    points:150
  },
  summary:[
    'Footprinting = building a complete intelligence picture of the target before any active testing.',
    'Passive footprinting uses public OSINT only \u2014 undetectable. Always start here.',
    'Active footprinting directly contacts the target \u2014 may trigger IDS/SIEM alerts.',
    'DNS zone transfers (AXFR) are critical vulnerabilities that expose entire network topology.',
    'Google Dorking, Shodan, and theHarvester are the three essential footprinting tools.',
    'Job postings reveal technology stack, security tools, and organizational structure.',
    'A complete footprinting phase separates professional pen tests from noisy automated scans.'
  ]
};

CONTENT['osint-techniques'] = {
  module:'Module 02 \u00b7 Footprinting & Reconnaissance',
  title:'OSINT Techniques',
  sub:'Open-Source Intelligence: turning public data into actionable attack intelligence.',
  killchain:{phase:'Reconnaissance',mitre:'T1589 \u2014 Gather Victim Identity Information',desc:'OSINT is the foundation of modern intelligence work. Everything that is public can be weaponized by an attacker.'},
  learn:{
    simple:'OSINT (Open-Source Intelligence) is the practice of collecting and analyzing information from publicly available sources to build intelligence about a target. Everything they have made public \u2014 intentionally or accidentally \u2014 is fair game.',
    analogy:'OSINT is like being a private investigator who only works from publicly available records \u2014 court documents, newspaper archives, public LinkedIn profiles, property records. You never trespass or hack anything. You just know where to look and how to connect the dots.',
    why:'Most organizations dramatically underestimate how much sensitive information is publicly available about them. OSINT allows an attacker to map the entire attack surface without triggering a single security alert.',
    architecture:'OSINT sources include: Search Engines (Google, Bing), Social Media (LinkedIn, Twitter, Facebook), Public Databases (WHOIS, Certificate Transparency), Data Breaches (HaveIBeenPwned), Dark Web forums, Pastebin, GitHub, government registries, news archives, and job boards.'
  },
  diagram:{
    title:'OSINT Intelligence Collection Cycle',
    steps:[
      {icon:'\U0001f3af',label:'Define Requirements',desc:'What do you need to know? Employee names, technology stack, IP ranges, partner organizations, financial data?'},
      {icon:'\U0001f30d',label:'Collect from Open Sources',desc:'Search engines, social media, domain records, certificate transparency logs, job postings, press releases, court records.'},
      {icon:'\U0001f517',label:'Cross-Reference & Correlate',desc:'Link information from different sources. An email found in a breach database + LinkedIn profile + GitHub commit = full identity profile.'},
      {icon:'\U0001f9e0',label:'Analyze & Enrich',desc:'Validate information. Check if emails are active (email verification tools). Check if passwords from breaches still work (credential stuffing risk).'},
      {icon:'\U0001f4ca',label:'Produce Intelligence',desc:'Structure findings into actionable intelligence: attack surface map, identified entry points, high-value targets (employees with privileged access).'},
      {icon:'\U0001f680',label:'Feed Into Next Phase',desc:'OSINT output feeds directly into scanning (confirmed IP ranges), social engineering (employee profiles), and exploitation (known tech stack vulnerabilities).'}
    ]
  },
  enterprise:{
    role:'You are the Threat Intelligence Analyst at GlobalFinSec Corp. investigating a suspected spear-phishing campaign.',
    situation:'An executive received a highly targeted phishing email that referenced her recent conference presentation, her direct reports\' names, and her company\'s AWS infrastructure. The attacker clearly had detailed OSINT on the company.',
    challenge:'Replicate the OSINT process the attacker likely used to construct this targeted attack, and identify what information is publicly exposed that needs to be remediated.',
    steps:[
      'Search the executive\'s name on LinkedIn \u2014 note her role, direct reports, recent activity, and conference speaking engagements.',
      'Search SlideShare and conference websites for her presentation \u2014 slides often contain internal project names, partner names, and technology details.',
      'Search GitHub for commits by company email domains \u2014 often reveals AWS access keys, internal hostnames, and API endpoints accidentally committed.',
      'Check HaveIBeenPwned for any company email addresses in breach databases.',
      'Search Pastebin and GitHub Gist for company name + keywords: "password", "api_key", "secret".',
      'Document all exposed information and produce a remediation report: remove slides from SlideShare, rotate any exposed credentials, request LinkedIn privacy settings review.'
    ],
    outcome:'The OSINT audit found: 3 AWS access keys in GitHub repositories (all rotated immediately), 47 employee credentials in breach databases (mandatory password resets), and 12 internal project names exposed in conference presentations.',
    lesson:'Your employees are your largest OSINT exposure. Their public social media, conference presentations, and accidental GitHub commits reveal more about your organization than your public website.'
  },
  tools:[
    {name:'Maltego',cmd:'maltego',desc:'Visual OSINT link analysis and relationship mapping'},
    {name:'theHarvester',cmd:'theHarvester -d target.com -b all',desc:'Multi-source email and subdomain harvesting'},
    {name:'Recon-ng',cmd:'recon-ng',desc:'Full-featured OSINT framework with modules'},
    {name:'SpiderFoot',cmd:'spiderfoot -l 127.0.0.1:5001',desc:'Automated OSINT collection across 200+ sources'},
    {name:'HaveIBeenPwned',cmd:'curl https://haveibeenpwned.com/api/v3/breachedaccount/email',desc:'Check if email appears in known data breaches'}
  ],
  commands:{
    win:['nslookup -type=TXT target.com','Invoke-WebRequest -Uri "https://crt.sh/?q=%.target.com&output=json"'],
    lin:['recon-ng','theHarvester -d target.com -b bing,google,linkedin -l 500','curl "https://crt.sh/?q=%.target.com&output=json" | jq .[].name_value | sort -u','grep -r "password\\|api_key\\|secret" ~/.git/ 2>/dev/null']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Only Searching Google and Missing Specialized OSINT Sources',desc:'Google indexes only a fraction of publicly available information. Certificate Transparency logs, GitHub, HaveIBeenPwned, and Shodan contain critical intelligence that Google doesn\'t show.',fix:'Use a systematic OSINT framework: Recon-ng or SpiderFoot. These tools query 50+ sources automatically and correlate results.'},
    {icon:'\U0001f534',title:'Ignoring GitHub as an OSINT Source',desc:'Developers accidentally commit API keys, passwords, internal hostnames, and architecture diagrams to public GitHub repositories constantly. This is one of the most productive OSINT sources.',fix:'Always search GitHub for: company email domain, company name + "api_key", company name + "password". Use GitDorker for automated GitHub OSINT.'},
    {icon:'\u26d4',title:'Not Checking Historical Data',desc:'The Wayback Machine (web.archive.org) preserves old versions of websites that may contain sensitive pages, old employee directories, or tech stack information that has since been removed.',fix:'Always check web.archive.org for the target domain. Deleted pages, old employee portals, and archived job postings can reveal valuable intelligence.'},
    {icon:'\U0001f3ad',title:'Treating OSINT as a One-Time Activity',desc:'Attackers perform ongoing OSINT, monitoring LinkedIn for new hires (new AWS admin hired = AWS is the platform), job postings for technology changes, and GitHub for new commits.',fix:'For red team engagements, monitor the target throughout the assessment. Set Google Alerts for the company name. New intelligence often changes the attack approach.'}
  ],
  lab:{
    title:'Lab: OSINT Investigation with Recon-ng',
    difficulty:'Intermediate',
    duration:'60 min',
    objectives:['Use Recon-ng framework to automate OSINT collection','Discover credentials in breach databases','Map organizational structure from LinkedIn OSINT'],
    steps:[
      'Launch Recon-ng: recon-ng',
      'Create a workspace: workspaces create globalfinsec_test',
      'Add target domain: db insert domains',
      'Run module: modules load recon/domains-hosts/bing_domain_web then run',
      'Check breach data: modules load recon/profiles-profiles/profiler then run',
      'Visit crt.sh: https://crt.sh/?q=%.targetdomain.com to find all subdomains via SSL certificates.',
      'Search GitHub: site:github.com "target@company.com" password OR api_key',
      'Document all findings in the Recon-ng report: show hosts, show contacts'
    ],
    validation:'You should have found: at least 5 subdomains, at least 1 email address, and verified whether the domain appears in any known breach databases.'
  },
  quiz:[
    {q:'What does OSINT stand for?',opts:['Offensive Security Intelligence Network Toolkit','Open-Source Intelligence','Organized Security Information Network Testing','Operational Security Intelligence'],correct:1,fb:'OSINT = Open-Source Intelligence. It refers to intelligence collected from publicly available sources without any unauthorized access.'},
    {q:'Which tool is best suited for visual OSINT relationship mapping?',opts:['Nmap','Wireshark','Maltego','Aircrack-ng'],correct:2,fb:'Maltego creates visual "transform" graphs showing relationships between entities: domains, emails, people, IP addresses, and organizations.'},
    {q:'Certificate Transparency logs are useful for OSINT because they:',opts:['Store password hashes','Log all SSL/TLS certificates ever issued, revealing subdomains','Record all network connections','Store financial records'],correct:1,fb:'Certificate Transparency (CT) logs record every SSL/TLS certificate issued. Since certificates include the domain name, CT logs are an excellent source of subdomain discovery (crt.sh).'},
    {q:'Which website can reveal if a company\'s employee email addresses appeared in a data breach?',opts:['Shodan.io','HaveIBeenPwned.com','Censys.io','VirusTotal.com'],correct:1,fb:'HaveIBeenPwned (HIBP) aggregates data from thousands of data breaches and allows checking whether an email address appears in any known breach.'},
    {q:'An attacker searching GitHub for company emails followed by "api_key" is performing:',opts:['Active scanning','Google Dorking','GitHub OSINT / Code Repository Intelligence','Social Engineering'],correct:2,fb:'Developers frequently accidentally commit API keys, passwords, and secrets to public GitHub repositories. Searching for company email domains + sensitive keywords is a highly productive OSINT technique.'},
    {q:'What is the Wayback Machine (web.archive.org) used for in OSINT?',opts:['Scanning for open ports','Viewing historical snapshots of websites to find deleted content','Cracking passwords','Mapping physical locations'],correct:1,fb:'The Wayback Machine archives historical snapshots of websites. Deleted employee directories, old admin pages, and removed documentation can often be found through archived snapshots.'},
    {q:'Which Recon-ng command adds a target domain to the workspace database?',opts:['add domain target.com','db insert domains','set domain target.com','target add target.com'],correct:1,fb:'In Recon-ng, "db insert domains" inserts a domain into the workspace database, which then becomes the input for subsequent modules.'},
    {q:'LinkedIn is valuable for OSINT because it reveals:',opts:['Network topology and IP addresses','Source code and API keys','Employee roles, technology stack, org structure, and direct manager relationships','Password hashes and encryption keys'],correct:2,fb:'LinkedIn profiles reveal job titles (privileged access holders), technology mentions in experience sections, reporting relationships, and recent activities including conference presentations.'},
    {q:'SpiderFoot automates OSINT by:',opts:['Scanning all ports on the target','Querying 200+ sources automatically and correlating data about a target','Performing SQL injection attacks','Decrypting SSL traffic'],correct:1,fb:'SpiderFoot is an automated OSINT collection tool that queries over 200 data sources (DNS, WHOIS, Shodan, social media, breach databases) and correlates the results.'},
    {q:'What is "passive DNS" in the context of OSINT?',opts:['DNS queries that do not return results','Historical DNS records showing what IP addresses a domain has pointed to over time','DNS servers that do not respond to queries','DNS records encrypted with TLS'],correct:1,fb:'Passive DNS is a historical record of DNS resolution data. It shows what IP addresses a domain has pointed to historically, revealing infrastructure changes, CDN usage, and potentially exposing real IP addresses behind DDoS protection services.'}
  ],
  flashcards:[
    {f:'OSINT',b:'Open-Source Intelligence \u2014 intelligence collected exclusively from publicly available sources without any unauthorized access or hacking.'},
    {f:'Certificate Transparency (CT) Logs',b:'Public logs of all SSL/TLS certificates ever issued. Site: crt.sh. Used for subdomain discovery and infrastructure mapping.'},
    {f:'HaveIBeenPwned',b:'Website that aggregates data from thousands of breaches. Reveals whether email addresses appear in known breach databases.'},
    {f:'Recon-ng',b:'Full-featured OSINT reconnaissance framework with pluggable modules for automated intelligence gathering from multiple sources.'},
    {f:'Maltego',b:'Visual OSINT and link analysis tool. Creates transform graphs showing relationships between domains, emails, people, and organizations.'},
    {f:'SpiderFoot',b:'Automated OSINT tool that queries 200+ data sources and correlates results into a comprehensive target profile.'},
    {f:'GitHub OSINT',b:'Searching public GitHub repositories for accidentally committed credentials: API keys, passwords, internal hostnames. Highly productive source.'},
    {f:'Wayback Machine',b:'web.archive.org \u2014 archives historical website snapshots. Used to find deleted pages, old employee directories, and removed sensitive content.'}
  ],
  ctf:{
    scenario:'An employee of GlobalFinSec accidentally committed their AWS access key to a public GitHub repository. The repository is at github.com/gfs-devops/infrastructure-scripts. The access key is in the file config.py. Using the key pattern AWS_ACCESS_KEY = "AKIA..." find the flag hidden in the same file as a comment.',
    hint:'Look for GitHub repositories with company email domains. Search: site:github.com "globalfinsec" "AWS_ACCESS_KEY".',
    flag:'CEH{0s1nt_m4st3r_t3chn1qu3s}',
    points:150
  },
  summary:[
    'OSINT = legally collecting intelligence from public sources. Zero unauthorized access required.',
    'Certificate Transparency logs (crt.sh) are the most productive subdomain discovery method.',
    'GitHub is a goldmine for accidentally exposed credentials, API keys, and architecture details.',
    'HaveIBeenPwned identifies employees whose credentials appear in known breach databases.',
    'Maltego and Recon-ng are the professional OSINT frameworks for systematic intelligence gathering.',
    'Historical data (Wayback Machine, Passive DNS) reveals infrastructure that has been hidden or changed.',
    'OSINT findings directly feed into every subsequent phase: scanning, exploitation, and social engineering.'
  ]
};

CONTENT['whois-dns'] = {
  module:'Module 02 \u00b7 Footprinting & Reconnaissance',
  title:'Whois & DNS Footprinting',
  sub:'Extracting network intelligence from domain registration and DNS infrastructure.',
  killchain:{phase:'Reconnaissance',mitre:'T1590.002 \u2014 Gather Victim Network Information: DNS',desc:'DNS is the phone book of the internet. Querying it systematically reveals the entire target network infrastructure.'},
  learn:{
    simple:'WHOIS reveals who owns a domain and how to contact them. DNS reveals the full technical infrastructure behind that domain: web servers, mail servers, subdomains, and IP addresses. Together they provide the foundational map of any target network.',
    analogy:'WHOIS is like checking the property deed to find who owns a building and their address. DNS is like reading the building\'s directory board in the lobby \u2014 it tells you who is on which floor (which server handles which service), where the mail goes (MX records), and all the other offices in the complex (subdomains).',
    why:'DNS is intentionally public \u2014 it has to be, for the internet to work. But most organizations are unaware of how much of their internal infrastructure can be inferred from DNS records. A complete DNS enumeration often reveals internal server naming conventions, cloud provider usage, third-party services, and forgotten legacy systems.',
    architecture:'Key DNS records: A (hostname to IPv4), AAAA (hostname to IPv6), MX (mail servers), CNAME (aliases), NS (name servers), TXT (verification, SPF, DKIM), PTR (reverse lookup), SRV (service locations). Zone transfers (AXFR) can copy entire DNS databases if misconfigured.'
  },
  diagram:{
    title:'DNS Footprinting Enumeration Process',
    steps:[
      {icon:'\U0001f4cb',label:'WHOIS Query',desc:'Query WHOIS for registrant name, email, organization, admin contact, name servers (NS records), registration/expiration dates.'},
      {icon:'\U0001f4e1',label:'NS Record Discovery',desc:'Identify authoritative name servers. These are the servers you will query for zone transfers.'},
      {icon:'\U0001f50d',label:'DNS Record Enumeration',desc:'Query: A, AAAA, MX, CNAME, TXT, SRV, SOA records. Each reveals different infrastructure components.'},
      {icon:'\U0001f504',label:'Zone Transfer Attempt (AXFR)',desc:'Attempt: dig axfr @ns1.target.com target.com. If successful, reveals ALL DNS records in one request.'},
      {icon:'\U0001f310',label:'Subdomain Brute-Force',desc:'If zone transfer fails, brute-force subdomains using wordlists: dnsrecon, Sublist3r, Amass, dnsx.'},
      {icon:'\U0001f9e9',label:'Passive DNS Analysis',desc:'Query historical DNS data (SecurityTrails, VirusTotal, CIRCL) to find IP addresses the domain has historically used.'}
    ]
  },
  enterprise:{
    role:'You are performing DNS reconnaissance on GlobalFinSec Corp as part of an authorized external penetration test.',
    situation:'Your scope includes all systems within globalfinsec-test.com. You need to build a complete map of their DNS infrastructure to identify all in-scope targets.',
    challenge:'Perform comprehensive DNS footprinting to discover all IP addresses, subdomains, and mail servers within scope.',
    steps:[
      'whois globalfinsec-test.com \u2014 Record NS servers: ns1.globalfinsec-test.com, ns2.globalfinsec-test.com.',
      'dig axfr @ns1.globalfinsec-test.com globalfinsec-test.com \u2014 Attempt zone transfer on both NS servers.',
      'dig globalfinsec-test.com MX \u2014 Discover mail servers and their IPs.',
      'dig globalfinsec-test.com TXT \u2014 Discover SPF records (reveals all authorized mail sending infrastructure).',
      'dnsx -d globalfinsec-test.com -w /usr/share/wordlists/dns-wordlist.txt \u2014 Brute-force subdomains.',
      'For each discovered subdomain, run: dig [subdomain].globalfinsec-test.com A to get IP addresses and add to scope.'
    ],
    outcome:'Zone transfer was blocked on ns1 but succeeded on ns2 (misconfiguration). The zone transfer revealed 23 subdomains including: dev.globalfinsec-test.com, staging.globalfinsec-test.com, and legacy-hr.globalfinsec-test.com \u2014 the last of which was running an unpatched WordPress installation.',
    lesson:'Always test zone transfers against all name servers independently. One may be misconfigured while others are properly secured. A single successful AXFR can save hours of brute-force enumeration.'
  },
  tools:[
    {name:'dig',cmd:'dig target.com ANY',desc:'Comprehensive DNS query tool for all record types'},
    {name:'nslookup',cmd:'nslookup -type=MX target.com',desc:'Windows/Linux DNS query utility'},
    {name:'dnsrecon',cmd:'dnsrecon -d target.com -t axfr',desc:'Automated DNS enumeration and zone transfer testing'},
    {name:'Sublist3r',cmd:'sublist3r -d target.com',desc:'Fast subdomain enumeration using multiple sources'},
    {name:'Amass',cmd:'amass enum -d target.com',desc:'In-depth DNS enumeration and network mapping'}
  ],
  commands:{
    win:['nslookup target.com','nslookup -type=MX target.com','nslookup -type=NS target.com','nslookup -type=TXT target.com','nslookup -type=ANY target.com ns1.target.com'],
    lin:['dig target.com A','dig target.com MX','dig target.com NS','dig target.com TXT','dig target.com SOA','dig axfr @ns1.target.com target.com','dnsrecon -d target.com -t std','host -t mx target.com','sublist3r -d target.com -o subdomains.txt']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Only Testing Zone Transfer on the Primary Name Server',desc:'Organizations often secure the primary NS server but leave secondary NS servers misconfigured. Students test AXFR against one NS and stop.',fix:'Always test zone transfers against ALL name servers discovered in the NS records. Each one may have different security configurations.'},
    {icon:'\U0001f534',title:'Missing TXT Records as Intelligence Sources',desc:'TXT records contain SPF, DKIM, and DMARC configurations that reveal all authorized email sending infrastructure (marketing platforms, CRM systems, cloud services).',fix:'Always query TXT records and analyze them. SPF records that include "include:amazonses.com" and "include:sendgrid.net" tell you exactly which third-party email platforms the company uses.'},
    {icon:'\u26d4',title:'Not Checking Reverse DNS (PTR Records)',desc:'Forward DNS (domain to IP) is well-known. Reverse DNS (IP to domain) is often overlooked. PTR records reveal internal server naming conventions that expose infrastructure.',fix:'For all discovered IPs, run reverse DNS: dig -x [IP]. Internal naming conventions revealed through PTR records (db01.internal.target.com) provide roadmaps to critical systems.'},
    {icon:'\U0001f3ad',title:'Forgetting That MX Records Reveal Third-Party Security Tools',desc:'MX records pointing to mimecast.com, proofpoint.com, or barracudanetworks.com reveal what email security products the target uses, informing phishing campaign design.',fix:'Always analyze where MX records point. This reveals email security products and their configurations, helping craft phishing emails that bypass filtering.'}
  ],
  lab:{
    title:'Lab: Full DNS Enumeration with dnsrecon',
    difficulty:'Beginner',
    duration:'30 min',
    objectives:['Perform comprehensive DNS enumeration on a practice target','Attempt DNS zone transfers','Discover subdomains through brute-force'],
    steps:[
      'Run: dig zonetransfer.me ANY \u2014 observe all DNS record types returned.',
      'Find name servers: dig zonetransfer.me NS',
      'Attempt zone transfer: dig axfr @nsztm1.digi.ninja. zonetransfer.me (this domain allows AXFR for practice).',
      'Observe all records exposed by the zone transfer \u2014 count subdomains and note internal naming conventions.',
      'Run: dnsrecon -d zonetransfer.me -t std for standard enumeration.',
      'Run: dnsrecon -d zonetransfer.me -t brt -D /usr/share/wordlists/dnsmap.txt for brute-force subdomain enumeration.',
      'Document all discovered hosts, IPs, and record types in a table.'
    ],
    validation:'After the zone transfer on zonetransfer.me, you should find 30+ subdomains, internal IP addresses, and multiple record types demonstrating why zone transfer misconfiguration is critical.'
  },
  quiz:[
    {q:'Which DNS record type maps a hostname to an IPv4 address?',opts:['MX record','CNAME record','A record','PTR record'],correct:2,fb:'A (Address) records map hostnames to IPv4 addresses. AAAA records map hostnames to IPv6 addresses.'},
    {q:'What does a successful DNS zone transfer (AXFR) reveal?',opts:['All password hashes for the domain','The complete DNS database including all subdomains and IP addresses','Only the primary web server IP','Email server configuration only'],correct:1,fb:'A successful AXFR copies the entire DNS zone database, revealing all subdomains, A records, MX records, and internal hostnames that would otherwise require extensive brute-forcing to discover.'},
    {q:'Which DNS record type is used to identify mail servers for a domain?',opts:['A record','MX record','CNAME record','SOA record'],correct:1,fb:'MX (Mail Exchange) records specify the mail server(s) responsible for receiving email for a domain, along with their priority values.'},
    {q:'What command would you use to attempt a DNS zone transfer on a Linux system?',opts:['nslookup -type=AXFR ns1.target.com','dig axfr @ns1.target.com target.com','dnsrecon -d target.com','host -l target.com ns1.target.com'],correct:1,fb:'dig axfr @ns1.target.com target.com attempts an AXFR zone transfer from the specified name server. Option D is also valid: host -l target.com ns1.target.com.'},
    {q:'Which WHOIS information is most valuable to an attacker?',opts:['Domain expiration date only','Registrant email (often used for admin password resets), name servers, and organizational details','The domain\'s creation date','The domain registrar name'],correct:1,fb:'The registrant email can be used for social engineering or password reset attacks. Name servers are essential for DNS enumeration. Organizational details build the target profile.'},
    {q:'What does an SPF TXT record reveal about a target?',opts:['The target\'s web application firewall vendor','All email servers and third-party services authorized to send email on behalf of the domain','The target\'s SSL certificate details','Internal network IP ranges'],correct:1,fb:'SPF (Sender Policy Framework) records list all hosts and services authorized to send email for a domain. This reveals marketing platforms (SendGrid, Mailchimp), CRM systems, and cloud services.'},
    {q:'Which tool automates subdomain discovery from multiple sources including certificate transparency, search engines, and DNS brute-force?',opts:['Nmap','Metasploit','Amass','Wireshark'],correct:2,fb:'Amass is the industry-standard tool for in-depth DNS enumeration and network mapping, querying certificate transparency logs, search engines, APIs, and performing brute-force subdomain enumeration.'},
    {q:'What is a PTR (Pointer) record in DNS?',opts:['A record that points to a CDN server','A reverse DNS record mapping an IP address to a hostname','A record for internal private networks only','A security record for DMARC validation'],correct:1,fb:'PTR records provide reverse DNS lookup, mapping IP addresses to hostnames. Querying PTR records for all discovered IPs can reveal internal server naming conventions.'},
    {q:'Which DNS record type reveals all authoritative name servers for a domain?',opts:['A record','MX record','NS record','SOA record'],correct:2,fb:'NS (Name Server) records identify the authoritative DNS servers for a domain. These are the servers you query for zone transfers and are critical to identify during DNS footprinting.'},
    {q:'What security risk is demonstrated by a publicly accessible DNS zone transfer?',opts:['SQL injection vulnerability','Exposure of complete network infrastructure including internal hostnames and all IP addresses','Cross-site scripting vulnerability','Weak SSL/TLS configuration'],correct:1,fb:'Public zone transfers expose the entire DNS database, revealing all subdomains, internal server naming conventions, IP addresses, and mail infrastructure \u2014 the equivalent of handing an attacker a complete network map.'}
  ],
  flashcards:[
    {f:'DNS A Record',b:'Maps hostname to IPv4 address. The most fundamental DNS record type.'},
    {f:'DNS MX Record',b:'Mail Exchange record. Specifies mail servers for a domain and their priority.'},
    {f:'DNS AXFR (Zone Transfer)',b:'Copies entire DNS database from one name server to another. Misconfigured servers expose all subdomains and IPs.'},
    {f:'DNS NS Record',b:'Name Server record. Identifies the authoritative DNS servers for a domain.'},
    {f:'DNS TXT Record',b:'Text record. Contains SPF, DKIM, DMARC configurations. Reveals all email sending services.'},
    {f:'DNS PTR Record',b:'Pointer record. Reverse DNS: maps IP address to hostname. Reveals server naming conventions.'},
    {f:'SOA Record',b:'Start of Authority. Contains primary name server, admin email, and zone serial number. Starting point for zone transfers.'},
    {f:'CNAME Record',b:'Canonical Name. Alias from one hostname to another. Often reveals CDN usage (target.com CNAME cloudfront.net).'}
  ],
  ctf:{
    scenario:'You attempt a zone transfer against ns2.globalfinsec-lab.com and it succeeds. Among the records returned, you find a TXT record for "flag.globalfinsec-lab.com" containing the CTF flag.',
    hint:'Try: dig axfr @ns2.globalfinsec-lab.com globalfinsec-lab.com and look for TXT records.',
    flag:'CEH{wh01s_dns_r3c0n_2026}',
    points:150
  },
  summary:[
    'WHOIS reveals domain ownership, registrant contact details, and authoritative name servers.',
    'DNS Zone Transfers (AXFR) are the most powerful DNS footprinting technique \u2014 one query exposes everything.',
    'Always test AXFR on ALL name servers individually \u2014 secondary NS servers are often misconfigured.',
    'MX records reveal email infrastructure and third-party security products (Proofpoint, Mimecast).',
    'TXT records expose SPF configurations that list all authorized email services and cloud platforms.',
    'Sublist3r, Amass, and dnsrecon automate comprehensive subdomain discovery.',
    'PTR (reverse DNS) records reveal internal server naming conventions that map critical infrastructure.'
  ]
};
"""

if INJECT_BEFORE in html:
    pos = html.find(INJECT_BEFORE)
    html = html[:pos] + MODULE02_CONTENT + '\n\n' + html[pos:]
    ok.append('Module 02 (footprinting-concepts, osint-techniques, whois-dns) injected')
else:
    fail.append('INJECT_BEFORE marker missing for Module 02')

# =================================================================
# WRITE OUTPUT
# =================================================================
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('=' * 55)
print('CONTENT INJECTION COMPLETE')
print('=' * 55)
for s in ok: print(f'  [OK]  {s}')
for s in fail: print(f'  [FAIL] {s}')
print()
print(f'New size: {len(html):,} bytes / {html.count(chr(10)):,} lines')
