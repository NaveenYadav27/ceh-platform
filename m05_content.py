import sys
import os

file_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')

payload = r"""
CONTENT['vuln-concepts'] = {
  eyebrow: 'Module 05 · Topic 1',
  title: 'Vulnerability Concepts & Assessment Phases',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Master the fundamentals of vulnerability management, assessment methodologies, and threat modeling.',
  objectives: [
    'Understand the vulnerability management lifecycle',
    'Differentiate between active and passive vulnerability assessments',
    'Apply threat modeling and vulnerability tree analysis'
  ],
  learn: {
    simple: 'Vulnerability assessment is the systematic review of security weaknesses in an information system. It evaluates if the system is susceptible to any known vulnerabilities, assigns severity levels, and recommends remediation or mitigation, if and whenever needed. This phase forms the backbone of a proactive defense strategy.',
    analogy: 'Think of a vulnerability assessment like a home inspector checking a house before you buy it. They do not break down the door (that would be penetration testing), but they check if the locks are flimsy, if the windows can be easily opened from the outside, and if the alarm system actually works.',
    architecture: 'At a technical level, vulnerability management involves continuous asset discovery, enumeration, scanning, and remediation. Scanners map network topologies and compare service banners, configuration files, and software versions against a database of known vulnerabilities (like CVEs). In enterprise environments, this data is ingested into SIEMs and SOAR platforms for correlation with threat intelligence feeds. Tree analysis is often employed to map potential attack vectors, evaluating the root node (ultimate goal of the attacker) and the leaf nodes (specific conditions required to achieve the goal).',
    why: 'In enterprise environments like GFS, new vulnerabilities are disclosed daily. Without a continuous vulnerability assessment program, the attack surface grows unmonitored. Understanding these concepts enables security teams to prioritize patching based on actual business risk rather than just technical severity.'
  },
  enterprise: {
    gfs: 'Global Financial Services (GFS) processes thousands of transactions per second. A vulnerability in their core transaction processing engine must be identified and scored using a standardized framework before it can be actively exploited by threat actors.',
    windows: 'Windows environments rely on Microsoft Defender Vulnerability Management and SCCM for centralized patch assessment and deployment across thousands of endpoints.',
    linux: 'Linux server farms often utilize tools like OpenSCAP to ensure compliance with STIGs and identify package vulnerabilities across various distributions (RHEL, Ubuntu).'
  },
  workflow: [
    'Step 1: Asset Inventory - Identify all hardware and software assets.',
    'Step 2: Threat Modeling - Identify potential threats and prioritize them.',
    'Step 3: Vulnerability Scanning - Use automated tools to scan for known vulnerabilities.',
    'Step 4: Vulnerability Assessment - Analyze the scan results for false positives.',
    'Step 5: Remediation - Apply patches or implement workarounds.',
    'Step 6: Verification - Rescan to ensure the vulnerability is resolved.'
  ],
  diagram: {
    caption: 'Click to interact with the vulnerability assessment lifecycle diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a2e"/><circle cx="300" cy="200" r="100" fill="#16213e" stroke="#e94560" stroke-width="4"/><text x="300" y="200" fill="#fff" font-size="20" text-anchor="middle" dominant-baseline="middle">Lifecycle</text><circle cx="300" cy="50" r="40" fill="#0f3460"/><text x="300" y="55" fill="#fff" font-size="12" text-anchor="middle">Discover</text><circle cx="450" cy="200" r="40" fill="#0f3460"/><text x="450" y="205" fill="#fff" font-size="12" text-anchor="middle">Assess</text><circle cx="300" cy="350" r="40" fill="#0f3460"/><text x="300" y="355" fill="#fff" font-size="12" text-anchor="middle">Report</text><circle cx="150" cy="200" r="40" fill="#0f3460"/><text x="150" y="205" fill="#fff" font-size="12" text-anchor="middle">Remediate</text><path d="M300 90 L300 100" stroke="#e94560" stroke-width="2" marker-end="url(#arrow)"/></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap --script vuln <target>', purpose: 'Run NSE scripts to detect vulnerabilities', out: 'List of detected CVEs and vulnerabilities', note: 'Active scanning that generates noise', mistake: 'Running in production without authorization' }
    ],
    win: [
      { cmd: 'Get-HotFix', purpose: 'Check installed patches', out: 'List of KBs', note: 'Native way to check for missing patches', mistake: 'Assuming installed patches mean no vulnerabilities exist' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nmap', 'Searchsploit'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS requires an initial assessment of a newly acquired subsidiary\'s public-facing servers. You need to map the attack surface without causing disruption.',
    objectives: ['Perform a passive vulnerability assessment', 'Execute an active vulnerability scan'],
    steps: [
      'Step 1: Perform a passive recon using `whois <target>` to gather domain info.',
      'Step 2: Run a basic active scan using `nmap -sV --script vuln <target>`.'
    ],
    evidence: ['Terminal output showing service versions and NSE script results.'],
    validation: ['You should see: State: OPEN, Service: http, Vulnerability: ...'],
    troubleshooting: ['If nmap is too slow, adjust timing with -T4.'],
    mitre: [{ id: 'T1595', name: 'Active Scanning', tactic: 'Reconnaissance' }],
    cleanup: ['Remove any scan reports generated.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which phase of the vulnerability management lifecycle involves applying patches?',
      opts: ['Discovery', 'Assessment', 'Remediation', 'Verification'],
      correct: 2,
      fb: 'Remediation is the process of fixing the identified vulnerabilities, often through patching or configuration changes.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary difference between active and passive vulnerability scanning?',
      opts: ['Active scanning uses more bandwidth', 'Passive scanning interacts directly with the target', 'Active scanning interacts directly with the target to identify weaknesses', 'There is no difference'],
      correct: 2,
      fb: 'Active scanning sends packets to the target and analyzes the responses to find vulnerabilities, while passive scanning monitors network traffic without directly probing the host.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In vulnerability tree analysis, what does the root node represent?',
      opts: ['The underlying vulnerability', 'The ultimate goal of the attacker', 'A specific exploit', 'A mitigation strategy'],
      correct: 1,
      fb: 'The root node in a threat or vulnerability tree represents the ultimate goal or top-level event an attacker wants to achieve.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is an example of an active vulnerability assessment tool?',
      opts: ['Wireshark', 'Nessus', 'Snort', 'Zeek'],
      correct: 1,
      fb: 'Nessus is an active vulnerability scanner that probes hosts for weaknesses.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why might an organization choose passive scanning over active scanning?',
      opts: ['It provides more detailed vulnerability data', 'It is less likely to disrupt fragile legacy systems', 'It can automatically patch systems', 'It is faster at discovering new devices'],
      correct: 1,
      fb: 'Passive scanning does not send active probes, making it safer for delicate IT or OT environments that might crash during active scans.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary purpose of vulnerability assessment?',
      opts: ['To exploit identified vulnerabilities', 'To identify and quantify security weaknesses in an environment', 'To monitor network traffic for intrusions', 'To prevent DDOS attacks'],
      correct: 1,
      fb: 'Vulnerability assessment is the systematic review of security weaknesses, not the exploitation of them (which is penetration testing).'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which action is typically performed during the Verification phase of the vulnerability management lifecycle?',
      opts: ['Applying a security patch', 'Rescanning the system to ensure the vulnerability is closed', 'Creating an asset inventory', 'Assigning a CVSS score'],
      correct: 1,
      fb: 'Verification involves validating that the remediation efforts were successful, usually by rescanning.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which type of vulnerability assessment relies on intercepting network traffic to deduce vulnerabilities?',
      opts: ['Active Assessment', 'Credentialed Assessment', 'Passive Assessment', 'Host-based Assessment'],
      correct: 2,
      fb: 'Passive assessment involves sniffing network traffic to deduce operating systems, applications, and potential vulnerabilities without sending active probes.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a false positive in the context of a vulnerability scan?',
      opts: ['A vulnerability that exists but is not detected', 'A reported vulnerability that does not actually exist on the system', 'A vulnerability that cannot be exploited', 'A vulnerability with a CVSS score of 0.0'],
      correct: 1,
      fb: 'A false positive occurs when the scanner incorrectly identifies a vulnerability that is not present.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following describes a credentialed (authenticated) scan?',
      opts: ['Scanning the system from the outside without logging in', 'Scanning the system using valid user credentials to accurately assess installed software and configurations', 'Scanning only web applications', 'Scanning network devices without SNMP'],
      correct: 1,
      fb: 'Credentialed scans log into the target system using valid credentials to provide a deeper, more accurate assessment of vulnerabilities, missing patches, and configurations.'
    }
  ],
  flashcards: [
    { f: 'Active Scanning', b: 'Directly interacting with a target to identify open ports, services, and vulnerabilities.' },
    { f: 'Passive Scanning', b: 'Monitoring network traffic to infer vulnerabilities without directly probing the target.' },
    { f: 'Vulnerability Tree Analysis', b: 'A visual representation of the attack paths an adversary could take to achieve a specific goal.' }
  ],
  summary: [
    'Vulnerability assessment is a continuous lifecycle, not a one-time event.',
    'Active scanning probes targets directly, while passive scanning monitors traffic.',
    'Threat modeling helps prioritize vulnerabilities based on business risk.',
    'False positives must be filtered out during the assessment phase.',
    'Verification ensures that remediation efforts were effective.'
  ],
  outcomes: [
    'Explain the phases of the vulnerability management lifecycle.',
    'Differentiate between active and passive scanning techniques.',
    'Understand how to utilize threat modeling and tree analysis.'
  ],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: ["Networking Basics", "Linux CLI"],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['cve-cvss'] = {
  eyebrow: 'Module 05 · Topic 2',
  title: 'CVEs, CVSS Scoring & Exploit Databases',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Learn how vulnerabilities are standardized, scored, and cataloged globally.',
  objectives: [
    'Understand the CVE naming convention and structure',
    'Calculate and interpret CVSS v3.1 and v4 scores',
    'Navigate and utilize exploit databases'
  ],
  learn: {
    simple: 'When a new vulnerability is discovered, it needs a standard identifier so everyone knows what is being discussed. The Common Vulnerabilities and Exposures (CVE) system provides this. Once identified, the vulnerability is scored using the Common Vulnerability Scoring System (CVSS) to determine its severity, helping organizations prioritize which flaws to fix first.',
    analogy: 'Think of a CVE like a disease\'s scientific name (e.g., COVID-19), ensuring doctors worldwide know exactly what they are treating. CVSS is like the triage system in an emergency room, determining who needs immediate attention (Critical/High) versus who can wait (Low).',
    architecture: 'The CVE list is maintained by MITRE and serves as a dictionary of publicly known vulnerabilities. CVSS provides a numerical score reflecting the severity, utilizing Base, Temporal, and Environmental metrics. CVSS v3.1 relies heavily on the Attack Vector, Attack Complexity, Privileges Required, and User Interaction metrics. CVSS v4 introduces finer granularity, including metrics for Attack Requirements and explicit assessments of Impact on the Vulnerable System vs. Subsequent Systems. Exploit databases (like Exploit-DB) map these CVEs to actual Proof of Concept (PoC) code.',
    why: 'In an enterprise environment, thousands of vulnerabilities may exist. Security teams cannot patch everything simultaneously. CVSS provides the quantifiable metric needed for risk-based vulnerability management, ensuring resources are directed toward patching critical flaws that pose the most immediate threat to the business.'
  },
  enterprise: {
    gfs: 'GFS vulnerability management dashboards ingest data from Nessus. An alert triggers for a CVE with a CVSS v4 score of 9.8 (Critical) on the VPN gateway, prompting an immediate out-of-band patching protocol.',
    windows: 'Microsoft Security Response Center (MSRC) publishes Security Update Guides detailing CVEs patched during Patch Tuesday, along with their respective CVSS scores.',
    linux: 'Linux administrators rely on resources like the NVD (National Vulnerability Database) and distribution-specific security advisories (e.g., Ubuntu USN) to track CVEs affecting their kernel or user-space applications.'
  },
  workflow: [
    'Step 1: Identification - A vulnerability scanner identifies a flaw and references its CVE ID.',
    'Step 2: Research - The security analyst looks up the CVE in the NVD to understand its impact.',
    'Step 3: Scoring - Review the CVSS Base score and adjust using Environmental metrics specific to the organization.',
    'Step 4: Exploitability - Check databases like Exploit-DB or GitHub to see if a weaponized exploit exists.',
    'Step 5: Prioritization - Rank the vulnerability for patching based on the adjusted score and exploit availability.'
  ],
  diagram: {
    caption: 'Click to interact with the CVSS v3.1 metric breakdown',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a2e"/><text x="300" y="50" fill="#fff" font-size="20" text-anchor="middle">CVSS v3.1 Base Metrics</text><rect x="50" y="100" width="150" height="200" fill="#16213e" stroke="#0f3460" stroke-width="2"/><text x="125" y="130" fill="#e94560" font-size="16" text-anchor="middle">Exploitability</text><text x="125" y="170" fill="#fff" font-size="12" text-anchor="middle">- Attack Vector (AV)</text><text x="125" y="200" fill="#fff" font-size="12" text-anchor="middle">- Attack Complexity (AC)</text><text x="125" y="230" fill="#fff" font-size="12" text-anchor="middle">- Privileges Required (PR)</text><text x="125" y="260" fill="#fff" font-size="12" text-anchor="middle">- User Interaction (UI)</text><rect x="400" y="100" width="150" height="200" fill="#16213e" stroke="#0f3460" stroke-width="2"/><text x="475" y="130" fill="#e94560" font-size="16" text-anchor="middle">Impact</text><text x="475" y="170" fill="#fff" font-size="12" text-anchor="middle">- Confidentiality (C)</text><text x="475" y="200" fill="#fff" font-size="12" text-anchor="middle">- Integrity (I)</text><text x="475" y="230" fill="#fff" font-size="12" text-anchor="middle">- Availability (A)</text><path d="M200 200 L400 200" stroke="#e94560" stroke-width="4" marker-end="url(#arrow)"/></svg>'
  },
  commands: {
    lin: [
      { cmd: 'searchsploit apache 2.4', purpose: 'Search Exploit-DB for specific service vulnerabilities', out: 'List of exploits and corresponding EDB-IDs', note: 'Can use -m to mirror the exploit to local dir', mistake: 'Not running `searchsploit -u` to update the local database first' }
    ],
    win: [
      { cmd: 'Invoke-WebRequest -Uri "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228"', purpose: 'Query NVD API for CVE details', out: 'JSON response with CVSS data', note: 'Requires parsing the JSON object', mistake: 'Not handling API rate limits' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '30',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Searchsploit', 'Curl'],
    dependencies: ['exploitdb package'],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'You have identified a server running ProFTPD 1.3.5. You need to look up its CVE and find a proof of concept exploit.',
    objectives: ['Query Exploit-DB using Searchsploit', 'Identify the corresponding CVE for an exploit'],
    steps: [
      'Step 1: Update the exploit database using `searchsploit -u`.',
      'Step 2: Search for exploits using `searchsploit proftpd 1.3.5`.',
      'Step 3: Copy the exploit to your directory using `searchsploit -m <path-to-exploit>`.'
    ],
    evidence: ['Terminal output showing the matched exploits and the copied file.'],
    validation: ['You should see: Exploit copied to current directory.'],
    troubleshooting: ['If searchsploit fails, ensure the exploitdb package is installed (`apt install exploitdb`).'],
    mitre: [{ id: 'T1588', name: 'Obtain Capabilities', tactic: 'Resource Development' }],
    cleanup: ['Remove downloaded exploits from your workspace.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which organization maintains the CVE list?',
      opts: ['NIST', 'NSA', 'MITRE', 'CISA'],
      correct: 2,
      fb: 'The Common Vulnerabilities and Exposures (CVE) program is sponsored by CISA and operated by the MITRE Corporation.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In CVSS v3.1, what does an Attack Vector (AV) of Network (N) mean?',
      opts: ['The vulnerability requires local access', 'The vulnerability is exploitable remotely over a network', 'The vulnerability requires physical access', 'The vulnerability can only be exploited via Bluetooth'],
      correct: 1,
      fb: 'An Attack Vector of Network means the vulnerability is bound to the network stack and can be exploited remotely.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the highest possible CVSS score?',
      opts: ['10.0', '100.0', '9.9', '5.0'],
      correct: 0,
      fb: 'The CVSS scale ranges from 0.0 to 10.0, with 10.0 representing a critical severity vulnerability.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which CVSS metric group represents characteristics of a vulnerability that change over time?',
      opts: ['Base Metrics', 'Temporal Metrics', 'Environmental Metrics', 'Impact Metrics'],
      correct: 1,
      fb: 'Temporal metrics represent characteristics that change over time, such as the availability of an exploit or a patch.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the purpose of Exploit-DB?',
      opts: ['To provide a score for vulnerabilities', 'To serve as an archive of public exploits and vulnerable software', 'To automatically patch systems', 'To scan networks for vulnerabilities'],
      correct: 1,
      fb: 'Exploit-DB is an archive of public exploits and corresponding vulnerable software, maintained by Offensive Security.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In CVSS, which metric evaluates the impact on the system\'s data integrity?',
      opts: ['Confidentiality', 'Integrity', 'Availability', 'Attack Complexity'],
      correct: 1,
      fb: 'The Integrity metric measures the impact to trustworthiness and veracity of information on the vulnerable system.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does a CVSS v3.1 score of 7.5 typically map to in qualitative severity ratings?',
      opts: ['Low', 'Medium', 'High', 'Critical'],
      correct: 2,
      fb: 'In CVSS v3.0/v3.1, scores from 7.0 to 8.9 are rated as High severity.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following describes the \'Privileges Required (PR)\' metric in CVSS?',
      opts: ['Whether the attacker needs a specialized tool', 'The level of privileges an attacker must possess before successfully exploiting the vulnerability', 'Whether a user must click a link', 'The amount of time required to develop an exploit'],
      correct: 1,
      fb: 'Privileges Required (PR) captures the level of access (e.g., None, Low, High) required for an attacker to execute an exploit.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What command-line tool in Kali Linux allows offline searching of Exploit-DB?',
      opts: ['nmap', 'searchsploit', 'msfconsole', 'hydra'],
      correct: 1,
      fb: 'Searchsploit is a command-line search tool for Exploit-DB that allows you to easily search for exploits offline.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'CVSS v4 introduced a new assessment of impact. What does it explicitly differentiate?',
      opts: ['Base vs Temporal', 'Impact on the Vulnerable System vs. Subsequent Systems', 'Windows vs Linux', 'Local vs Remote'],
      correct: 1,
      fb: 'CVSS v4 explicitly assesses impact metrics for the Vulnerable System separately from Subsequent Systems.'
    }
  ],
  flashcards: [
    { f: 'CVE', b: 'Common Vulnerabilities and Exposures: A dictionary of publicly known information security vulnerabilities and exposures.' },
    { f: 'CVSS', b: 'Common Vulnerability Scoring System: A framework for rating the severity of vulnerabilities.' },
    { f: 'Temporal Metrics', b: 'CVSS metrics that change over time, such as exploit code maturity and remediation level.' }
  ],
  summary: [
    'CVE provides standard nomenclature for vulnerabilities.',
    'CVSS offers a numerical severity score from 0.0 to 10.0.',
    'CVSS base scores reflect intrinsic qualities, while temporal and environmental scores refine it for specific contexts.',
    'Exploit databases bridge the gap between abstract vulnerability listings and actual threat capabilities.',
    'Searchsploit is the primary CLI tool for offline Exploit-DB queries.'
  ],
  outcomes: [
    'Read and interpret a CVE entry.',
    'Calculate a CVSS score using Base metrics.',
    'Use searchsploit to find relevant exploits.'
  ],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: ["Understanding of vulnerabilities"],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['nessus-openvas'] = {
  eyebrow: 'Module 05 · Topic 3',
  title: 'Vulnerability Scanners: Nessus & OpenVAS',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Deploy and configure enterprise-grade vulnerability scanners to identify network weaknesses.',
  objectives: [
    'Configure and execute unauthenticated and authenticated vulnerability scans',
    'Compare Nessus and OpenVAS architectures',
    'Analyze and interpret vulnerability scan reports'
  ],
  learn: {
    simple: 'Vulnerability scanners are automated tools that probe a network or host to identify known security weaknesses. Nessus is a leading commercial scanner (with a free Essentials version), while OpenVAS is a powerful open-source alternative. These tools automate the process of checking thousands of CVEs against your systems.',
    analogy: 'Imagine a vulnerability scanner as an automated security guard walking through a massive office building. They check every single door and window (ports) to see if they are locked. If they have the master keys (authenticated scan), they also go inside every room to check the safes and file cabinets (local configurations).',
    architecture: 'Scanners work by utilizing a feed of vulnerability signatures (plugins or NVTs). An unauthenticated scan identifies services over the network and guesses vulnerabilities based on banners and responses. An authenticated (credentialed) scan logs into the target via SSH or SMB/WMI, providing a highly accurate inventory of installed packages, missing patches, and misconfigurations. The architecture usually involves a scanner engine, a management console, and a regularly updated database of vulnerability checks.',
    why: 'In enterprise security at GFS, relying on manual vulnerability checks is impossible given the scale. Scanners provide the automation necessary to identify critical misconfigurations and missing patches before an attacker can exploit them. Analyzing the output (and filtering false positives) is a core skill for any SOC or vulnerability management team.'
  },
  enterprise: {
    gfs: 'GFS utilizes Nessus Professional for credentialed scans across its Windows server infrastructure to ensure compliance with CIS benchmarks and to identify missing critical patches.',
    windows: 'Windows hosts are typically scanned via SMB using a dedicated service account. WMI is often queried by the scanner to determine the patch level (KBs installed) and registry settings.',
    linux: 'Linux hosts are scanned via SSH. The scanner authenticates, runs commands to list installed packages (e.g., `dpkg -l` or `rpm -qa`), and compares the versions against known vulnerabilities.'
  },
  workflow: [
    'Step 1: Deployment - Install the scanner and update the vulnerability plugins/NVTs.',
    'Step 2: Target Definition - Define the IP range or specific hosts to be scanned.',
    'Step 3: Policy Configuration - Create a scan policy (e.g., Basic Network Scan, Credentialed Patch Audit).',
    'Step 4: Credential Configuration - (Optional but recommended) Input SSH/SMB credentials for deeper analysis.',
    'Step 5: Execution - Run the scan during an approved maintenance window.',
    'Step 6: Analysis - Review the report, filter false positives, and export for remediation.'
  ],
  diagram: {
    caption: 'Click to interact with the Authenticated Scanning workflow',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a2e"/><rect x="50" y="150" width="120" height="100" rx="10" fill="#16213e" stroke="#e94560" stroke-width="3"/><text x="110" y="195" fill="#fff" font-size="16" text-anchor="middle">Scanner</text><text x="110" y="215" fill="#aaa" font-size="12" text-anchor="middle">(Nessus/OpenVAS)</text><rect x="430" y="150" width="120" height="100" rx="10" fill="#16213e" stroke="#0f3460" stroke-width="3"/><text x="490" y="195" fill="#fff" font-size="16" text-anchor="middle">Target Host</text><text x="490" y="215" fill="#aaa" font-size="12" text-anchor="middle">(Windows/Linux)</text><path d="M170 170 L430 170" stroke="#4ecca3" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)"/><text x="300" y="160" fill="#4ecca3" font-size="12" text-anchor="middle">1. Authenticate (SSH/SMB)</text><path d="M170 200 L430 200" stroke="#e94560" stroke-width="2" marker-end="url(#arrow)"/><text x="300" y="195" fill="#e94560" font-size="12" text-anchor="middle">2. Query local registry/packages</text><path d="M430 230 L170 230" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><text x="300" y="225" fill="#fff" font-size="12" text-anchor="middle">3. Return data for analysis</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'sudo gvm-start', purpose: 'Start the Greenbone Vulnerability Management (OpenVAS) services', out: 'Services started message', note: 'Requires OpenVAS to be fully configured', mistake: 'Failing to update feeds (`greenbone-feed-sync`) before scanning' }
    ],
    win: [
      { cmd: 'net start "Tenable Nessus"', purpose: 'Start the Nessus service on Windows', out: 'The Tenable Nessus service was started successfully.', note: 'Requires Administrator privileges', mistake: 'Trying to access the web interface before the service fully starts' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['OpenVAS/Greenbone'],
    dependencies: ['gvm package installed and initialized'],
    safety: ['Perform this lab only in an authorized environment. Active scans can disrupt services.'],
    scenario: 'GFS has tasked you with setting up an open-source vulnerability scanning capability. You need to configure OpenVAS, update its feeds, and perform an unauthenticated scan of a test server.',
    objectives: ['Start and access the GVM web interface', 'Configure a target and a scanning task', 'Analyze the resulting report'],
    steps: [
      'Step 1: Ensure feeds are up to date by running `sudo greenbone-feed-sync`.',
      'Step 2: Start the services with `sudo gvm-start`.',
      'Step 3: Access the web interface at `https://127.0.0.1:9392`.',
      'Step 4: Navigate to Configuration > Targets and create a new target with the lab IP.',
      'Step 5: Navigate to Scans > Tasks, create a new task using the "Full and fast" configuration, and start it.'
    ],
    evidence: ['A PDF or CSV export of the vulnerability scan report.'],
    validation: ['You should see: Task status changes to Done, and a report is generated with identified vulnerabilities.'],
    troubleshooting: ['If gvm-start fails, check the logs in `/var/log/gvm/`. Initialization (`gvm-setup`) must be run first.'],
    mitre: [{ id: 'T1595', name: 'Active Scanning', tactic: 'Reconnaissance' }],
    cleanup: ['Delete the task and target from the GVM interface.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary advantage of an authenticated (credentialed) vulnerability scan over an unauthenticated scan?',
      opts: ['It runs faster over the network', 'It does not require any passwords', 'It provides a highly accurate inventory of installed software and missing local patches', 'It cannot be detected by an IDS'],
      correct: 2,
      fb: 'Authenticated scans log into the system, allowing the scanner to accurately check registry keys, package managers, and file versions without guessing.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which protocol is most commonly used by vulnerability scanners to perform credentialed scans on Linux systems?',
      opts: ['SMB', 'RDP', 'SSH', 'FTP'],
      correct: 2,
      fb: 'SSH (Secure Shell) is the standard protocol used to authenticate and execute commands securely on Linux targets.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In Nessus, what are the scripts that check for specific vulnerabilities called?',
      opts: ['NVTs', 'Plugins', 'Modules', 'Exploits'],
      correct: 1,
      fb: 'Nessus uses \'Plugins\', which are scripts written in NASL (Nessus Attack Scripting Language) to check for vulnerabilities.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is OpenVAS currently known as within its enterprise framework?',
      opts: ['Metasploit', 'Nessus Essentials', 'Greenbone Vulnerability Management (GVM)', 'Qualys'],
      correct: 2,
      fb: 'OpenVAS is the scanner component, but the entire framework is managed via Greenbone Vulnerability Management (GVM).'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which port does the Nessus web interface typically run on by default?',
      opts: ['443', '8080', '8834', '9392'],
      correct: 2,
      fb: 'By default, the Nessus web management interface is accessible via HTTPS on port 8834.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a common risk of running a highly aggressive, unauthenticated vulnerability scan against legacy systems?',
      opts: ['The scanner will definitely exploit the system', 'The system may crash or experience a denial of service due to unexpected traffic', 'The scanner will permanently lock all user accounts', 'There is no risk'],
      correct: 1,
      fb: 'Aggressive scanning can send malformed packets or overwhelming traffic that fragile or legacy services cannot handle, causing a denial of service.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'To perform an authenticated scan on a Windows environment, which of the following is typically required by the scanner?',
      opts: ['SSH access', 'Administrator credentials and access to the ADMIN$ share via SMB', 'Telnet access', 'An installed agent on every machine'],
      correct: 1,
      fb: 'Windows authenticated scans typically rely on SMB access, utilizing an Administrator account to access the remote registry and ADMIN$ share.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What are NVTs in the context of OpenVAS?',
      opts: ['Network Vulnerability Tests', 'Node Validation Tokens', 'New Vulnerability Threats', 'Network Verification Tools'],
      correct: 0,
      fb: 'NVTs stand for Network Vulnerability Tests; they are the routines used by OpenVAS to detect specific vulnerabilities.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'When a scanner reports a vulnerability based solely on an HTTP Server header version (e.g., Apache/2.2.14), what is the most likely cause of a false positive?',
      opts: ['The port is actually closed', 'The system administrator has backported security patches without changing the version banner', 'The scanner cannot read HTTP', 'Apache has no vulnerabilities'],
      correct: 1,
      fb: 'Linux distributions (like Debian/RHEL) often "backport" security fixes into older software versions without changing the main version number, leading to banner-grabbing false positives.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is an essential step BEFORE running a vulnerability scan?',
      opts: ['Exploiting the target', 'Obtaining proper authorization and defining the scope', 'Turning off all firewalls on the network', 'Publishing the target IPs online'],
      correct: 1,
      fb: 'Scanning without explicit authorization is illegal and against ethical hacking principles. Scope definition is critical.'
    }
  ],
  flashcards: [
    { f: 'Authenticated Scan', b: 'A scan where the tool logs into the target system using provided credentials to conduct a deep, highly accurate assessment.' },
    { f: 'Unauthenticated Scan', b: 'A scan conducted over the network without credentials, relying on port scanning, banner grabbing, and network responses.' },
    { f: 'Nessus Plugins', b: 'Scripts used by Nessus to identify a specific vulnerability or gather information about a target.' }
  ],
  summary: [
    'Nessus and OpenVAS/GVM are industry-standard vulnerability scanning platforms.',
    'Authenticated scans provide significantly more accurate results and fewer false positives than unauthenticated scans.',
    'Windows targets generally require SMB/WMI access for credentialed scans, while Linux targets require SSH.',
    'Scanning can disrupt fragile systems; authorization and scheduling (maintenance windows) are crucial.',
    'Scanners rely on regularly updated feeds (Plugins/NVTs) to detect the latest vulnerabilities.'
  ],
  outcomes: [
    'Explain the difference between authenticated and unauthenticated scans.',
    'Identify the default ports and management interfaces for Nessus and OpenVAS.',
    'Recognize the risks associated with active vulnerability scanning.'
  ],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 60,
    difficulty: "Intermediate",
    prerequisites: ["Understanding of CVEs"],
    lastReviewed: "2026-07-18"
  }
};
"""

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    marker = "// ── TAB WIRING ──"
    if marker not in content:
        print(f"Marker '{marker}' not found in index.html!")
        sys.exit(1)
        
    new_content = content.replace(marker, payload + "\n" + marker)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print("Content successfully injected into index.html")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
