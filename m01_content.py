import os

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"

PAYLOAD = r"""
CONTENT['info-security-overview'] = {
  eyebrow: 'Module 01 · Topic 1',
  title: 'Information Security Overview',
  module: 'Phase 01: Security Analyst Trainee',
  sub: 'Understanding the foundational concepts of information security and the core principles that protect enterprise assets.',
  objectives: ['Understand the CIA Triad and AAA framework', 'Define asset classification and defense in depth', 'Understand risk, threat, and vulnerability concepts', 'Explain Business Continuity and Disaster Recovery'],
  learn: {
    simple: 'Information security is the practice of protecting information by mitigating information risks. It typically involves preventing or at least reducing the probability of unauthorized access, use, disclosure, disruption, deletion, corruption, modification, inspection, recording, or devaluation. The core of this discipline revolves around the CIA Triad: Confidentiality, Integrity, and Availability.',
    analogy: 'Think of information security like a bank vault. Confidentiality ensures only authorized people can see what is inside. Integrity ensures nobody tampers with the money or documents. Availability ensures you can access your assets whenever the bank is open.',
    architecture: 'In an enterprise network, Defense in Depth is implemented by layering security controls. For example, a perimeter firewall (Network Layer), an IPS (Application Layer), Active Directory (Identity Layer), and Endpoint Detection and Response (EDR) on host machines. A Zero Trust architecture assumes breach and verifies every request as though it originates from an open network, regardless of where the request originates or what resource it accesses.',
    why: 'Without a solid understanding of these core principles, technical controls lack context. Knowing what to protect (Assets) and what to protect against (Threats) allows organizations to implement the right countermeasures to manage Risk.'
  },
  enterprise: {
    gfs: 'GFS processes 2.4 million financial transactions daily. A misconfigured database server exposed customer PII and transaction histories. This incident highlights why Confidentiality, Integrity, and Availability are the three pillars of information security at every financial institution.',
    windows: 'Windows environments use Active Directory for AAA, applying Group Policy Objects (GPOs) to enforce security baselines and ensure the CIA Triad is maintained across domains.',
    linux: 'Linux environments leverage PAM (Pluggable Authentication Modules) and file permissions (rwx) to maintain confidentiality and integrity of system files and user data.'
  },
  workflow: [
    'Step 1: Identify and classify assets (Public, Internal, Confidential).',
    'Step 2: Identify threats and vulnerabilities applicable to those assets.',
    'Step 3: Assess the risk (Risk = Threat x Vulnerability x Impact).',
    'Step 4: Implement appropriate security controls to mitigate risk.',
    'Step 5: Monitor and review the security posture continuously.'
  ],
  diagram: {
    caption: 'Click to interact with the CIA Triad diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><g transform="translate(300,200)"><polygon points="0,-120 -103.92,60 103.92,60" fill="none" stroke="#00ffcc" stroke-width="4"/><circle cx="0" cy="-120" r="40" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="0" y="-115" fill="#fff" text-anchor="middle" font-family="monospace" font-size="14">Confidentiality</text><circle cx="-103.92" cy="60" r="40" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="-103.92" y="65" fill="#fff" text-anchor="middle" font-family="monospace" font-size="14">Integrity</text><circle cx="103.92" cy="60" r="40" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="103.92" y="65" fill="#fff" text-anchor="middle" font-family="monospace" font-size="14">Availability</text></g></svg>'
  },
  commands: {
    lin: [
      { cmd: 'chmod 700 /secure_data', purpose: 'Restricts access to the owner, ensuring Confidentiality.', out: 'No output on success', note: 'Essential for protecting sensitive files in multi-user environments.', mistake: 'Using chmod 777 which violates least privilege.' }
    ],
    win: [
      { cmd: 'icacls C:\\Data /grant Administrators:F /inheritance:r', purpose: 'Sets strict permissions on a directory.', out: 'processed file: C:\\Data\\nSuccessfully processed 1 files', note: 'Used to secure NTFS partitions.', mistake: 'Removing all permissions including SYSTEM, breaking OS access.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Foundation',
    duration: '30',
    platform: 'Windows / Linux',
    environment: 'Local Lab',
    tools: ['Asset Inventory System', 'Risk Assessment Template'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not test against production systems.'],
    scenario: 'GFS requires an asset classification exercise. You must categorize GFS assets (databases, APIs, employee laptops, public web servers) into Confidential/Internal/Public tiers and identify applicable controls.',
    objectives: ['Classify enterprise assets accurately', 'Assign appropriate security tiers', 'Map controls to the CIA triad'],
    steps: [
      'Step 1: Review the provided GFS asset list.',
      'Step 2: Assign a classification (Public, Internal, Confidential) to each asset based on its sensitivity.',
      'Step 3: Determine which CIA pillar is most critical for each asset.',
      'Step 4: Propose one technical and one administrative control for the Confidential assets.'
    ],
    evidence: ['Completed Asset Classification matrix.', 'Screenshot of the risk assessment dashboard.'],
    validation: ['You should see: Accurate classification of the core database as Confidential with high Integrity requirements.', 'Verify by: Checking the matrix against the GFS data handling policy.'],
    troubleshooting: ['If an asset seems to fit multiple categories, default to the most restrictive tier.', 'Common error: Classifying public web servers as Confidential.'],
    mitre: [
      { id: 'T1530', name: 'Data from Cloud Storage', tactic: 'Collection' },
      { id: 'T1078', name: 'Valid Accounts', tactic: 'Defense Evasion' }
    ],
    cleanup: ['Save the classification matrix and close the application.', 'No system changes to revert.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which component of the CIA Triad ensures that information is accessible when needed?', opts: ['Confidentiality', 'Integrity', 'Availability', 'Authentication'], correct: 2, fb: 'Availability ensures that authorized users have access to information and associated assets when required.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What does the "AAA" framework stand for?', opts: ['Access, Authorization, Accounting', 'Authentication, Authorization, Accounting', 'Assessment, Auditing, Accountability', 'Authentication, Assessment, Accounting'], correct: 1, fb: 'AAA stands for Authentication, Authorization, and Accounting, which are core security processes.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'A Zero Trust architecture assumes that internal networks are inherently safe.', correct: 'false', fb: 'Zero Trust assumes no network is inherently safe and verifies every request regardless of origin.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Applying multiple layers of security controls to protect an asset is known as:', opts: ['Security Obscurity', 'Defense in Depth', 'Risk Transference', 'Single Sign-On'], correct: 1, fb: 'Defense in Depth is the practice of layering multiple security controls to provide redundancy in case one fails.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which of the following is a potential threat to the Integrity of a database?', opts: ['A DDoS attack', 'Unauthorized read access', 'A SQL injection attack modifying records', 'A power outage'], correct: 2, fb: 'SQL injection modifying records directly impacts the integrity (correctness and trustworthiness) of the data.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Risk is calculated as the product of Threat, Vulnerability, and Impact.', correct: 'true', fb: 'Risk is generally understood as the potential for loss, often expressed as Threat x Vulnerability x Impact.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is an attack surface?', opts: ['The physical perimeter of a building', 'The total sum of vulnerabilities that can be exploited', 'The software used by attackers', 'A defensive barrier'], correct: 1, fb: 'The attack surface is the total sum of vulnerabilities, pathways, or interfaces that an attacker can exploit to enter a system.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Disaster Recovery is primarily concerned with keeping business operations running during a disruption, while Business Continuity is about restoring IT infrastructure after a disaster.', correct: 'false', fb: 'It is the other way around. Business Continuity is keeping the business running, while Disaster Recovery is about restoring IT infrastructure.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which phase of the data lifecycle involves destroying data so it cannot be recovered?', opts: ['Creation', 'Storage', 'Archiving', 'Destruction'], correct: 3, fb: 'Destruction (or purging) is the final phase of the data lifecycle, ensuring data cannot be recovered.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'A Security Operations Center (SOC) is primarily responsible for physical security like building locks and security guards.', correct: 'false', fb: 'A SOC is a centralized unit that deals with security issues on an organizational and technical level, not just physical security.' }
  ],
  flashcards: [
    { f: 'Confidentiality', b: 'Ensuring that information is not disclosed to unauthorized individuals, entities, or processes.' },
    { f: 'Integrity', b: 'Maintaining and assuring the accuracy and completeness of data over its entire lifecycle.' },
    { f: 'Availability', b: 'Ensuring timely and reliable access to and use of information.' },
    { f: 'Defense in Depth', b: 'The coordinated use of multiple security countermeasures to protect the integrity of the information assets.' },
    { f: 'Zero Trust', b: 'A security framework requiring all users to be authenticated, authorized, and continuously validated.' },
    { f: 'Risk', b: 'The potential for loss, damage, or destruction of an asset.' },
    { f: 'Vulnerability', b: 'A weakness in an information system, system security procedures, internal controls, or implementation.' },
    { f: 'Threat', b: 'Any circumstance or event with the potential to adversely impact organizational operations.' },
    { f: 'Authentication', b: 'The process of verifying the identity of a user, process, or device.' },
    { f: 'Accounting', b: 'Tracking user actions and resource consumption on a system to ensure accountability.' }
  ],
  summary: [
    'The CIA Triad (Confidentiality, Integrity, Availability) is the foundation of information security.',
    'Defense in Depth uses multiple layers of security to protect assets.',
    'Risk management involves identifying threats and vulnerabilities to minimize potential impact.',
    'The AAA framework ensures users are who they claim to be, have the right access, and their actions are logged.',
    'Zero Trust architecture assumes that no network is safe and requires continuous verification.'
  ],
  outcomes: [
    'Explain the CIA Triad and its relevance to GFS operations.',
    'Identify and classify enterprise assets based on risk and sensitivity.',
    'Design a basic Defense in Depth strategy.',
    'Understand the core functions of a Security Operations Center (SOC).'
  ]
};

CONTENT['hacker-classes'] = {
  eyebrow: 'Module 01 · Topic 2',
  title: 'Hacker Classes and Threat Actors',
  module: 'Phase 01: Security Analyst Trainee',
  sub: 'Categorizing threat actors, understanding their motivations, and analyzing their tactics, techniques, and procedures (TTPs).',
  objectives: ['Differentiate between White, Black, and Gray Hat hackers', 'Understand Advanced Persistent Threats (APTs) and Nation-State Actors', 'Analyze the Cyber Kill Chain and MITRE ATT&CK framework', 'Perform Threat Actor Profiling'],
  learn: {
    simple: 'Hackers are often classified by their intent and authorization level. "White Hats" are ethical hackers authorized to find vulnerabilities. "Black Hats" are malicious actors who break into systems for personal gain or destruction. "Gray Hats" fall somewhere in between, often hacking without permission but without malicious intent. Beyond these simple terms, modern cybersecurity focuses on "Threat Actors" like organized crime, hacktivists, and nation-states.',
    analogy: 'Imagine a castle. A Black Hat is an invading army trying to breach the walls to steal gold. A White Hat is an inspector hired by the king to find weak spots in the wall and report them. A Gray Hat is a rogue knight who climbs the wall uninvited just to prove they can, then leaves a note on the king\'s throne.',
    architecture: 'Threat actors are tracked using frameworks like the MITRE ATT&CK framework and the Lockheed Martin Cyber Kill Chain. These frameworks break down an attack into phases (e.g., Reconnaissance, Initial Access, Lateral Movement). By understanding a threat actor\'s Tactics, Techniques, and Procedures (TTPs), defenders can implement specific controls to break the kill chain at various stages.',
    why: 'Understanding who is attacking you and why is crucial for effective defense. Different threat actors use different methods; an APT will use slow, stealthy techniques, while a script kiddie will use loud, readily available tools. Profiling helps prioritize defenses.'
  },
  enterprise: {
    gfs: 'GFS SOC detected an advanced persistent threat attempting lateral movement through the payment network. Intelligence analysis revealed the TTPs match a known financial sector threat actor group. Understanding threat actor motivation and methodology is critical for proactive defense.',
    windows: 'In Windows environments, identifying threat actor TTPs often involves analyzing event logs (Event ID 4624, 4688) for signs of credential dumping (e.g., Mimikatz) or living-off-the-land techniques (e.g., PowerShell).',
    linux: 'Linux defenders look for unauthorized SSH keys, anomalous cron jobs, and suspicious binaries in /tmp, which are common techniques used by APTs targeting Linux infrastructure.'
  },
  workflow: [
    'Step 1: Identify the potential threat actor categories (e.g., Organized Crime, Nation-State).',
    'Step 2: Determine their likely motivations (Financial, Espionage, Disruption).',
    'Step 3: Analyze intelligence feeds to understand their known TTPs.',
    'Step 4: Map these TTPs using the MITRE ATT&CK framework.',
    'Step 5: Identify gaps in current defenses against these specific TTPs.',
    'Step 6: Deploy targeted countermeasures to disrupt the actor\'s kill chain.'
  ],
  diagram: {
    caption: 'Click to interact with the Threat Actor Categorization diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><g font-family="monospace" font-size="14" fill="#fff"><rect x="50" y="50" width="150" height="80" rx="10" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="125" y="95" text-anchor="middle">White Hat</text><rect x="225" y="50" width="150" height="80" rx="10" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="300" y="95" text-anchor="middle">Gray Hat</text><rect x="400" y="50" width="150" height="80" rx="10" fill="#1a1a2e" stroke="#ff3366" stroke-width="2"/><text x="475" y="95" text-anchor="middle">Black Hat</text><line x1="125" y1="130" x2="125" y2="180" stroke="#00ffcc" stroke-width="2"/><line x1="475" y1="130" x2="475" y2="180" stroke="#ff3366" stroke-width="2"/><rect x="50" y="180" width="150" height="60" rx="5" fill="#2a2a4a"/><text x="125" y="215" text-anchor="middle">Authorized</text><rect x="400" y="180" width="150" height="60" rx="5" fill="#4a2a2a"/><text x="475" y="215" text-anchor="middle">Malicious</text></g></svg>'
  },
  commands: {
    lin: [
      { cmd: 'lastb', purpose: 'Shows a list of bad login attempts.', out: 'List of failed logins', note: 'Useful for detecting brute-force attacks from script kiddies or automated bots.', mistake: 'Ignoring the output; these logs are early indicators of compromise.' }
    ],
    win: [
      { cmd: 'Get-EventLog -LogName Security -InstanceId 4625', purpose: 'Retrieves failed logon events.', out: 'List of Event ID 4625', note: 'Crucial for detecting brute-force attempts in a Windows domain.', mistake: 'Not configuring the audit policy to log these events in the first place.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Web Browser',
    environment: 'Local Lab',
    tools: ['MITRE ATT&CK Navigator'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.', 'Do not use this profiling data for malicious targeting.'],
    scenario: 'GFS SOC has provided you with an incident report detailing a simulated attack. You must use the MITRE ATT&CK Navigator to map the attack to a known threat group (e.g., FIN7) and identify likely next steps.',
    objectives: ['Map incident indicators to MITRE ATT&CK techniques', 'Identify a specific threat actor profile', 'Predict the adversary\'s next move'],
    steps: [
      'Step 1: Open MITRE ATT&CK Navigator in your browser.',
      'Step 2: Create a new layer based on the Enterprise matrix.',
      'Step 3: Review the incident report: spearphishing attachment used, PowerShell executed, credentials dumped via LSASS.',
      'Step 4: Highlight the corresponding techniques (T1566, T1059, T1003) in the Navigator.',
      'Step 5: Compare the highlighted layer against known financial threat groups (e.g., FIN7, Carbanak) to find a match.'
    ],
    evidence: ['Exported JSON layer from MITRE ATT&CK Navigator.', 'Screenshot of the highlighted matrix.'],
    validation: ['You should see: A strong overlap with FIN7\'s known techniques.', 'Verify by: Checking the threat group profile on the MITRE website.'],
    troubleshooting: ['If techniques don\'t perfectly match, look for broader tactic categories.', 'Common error: Confusing Initial Access techniques with Execution techniques.'],
    mitre: [
      { id: 'TA0043', name: 'Reconnaissance', tactic: 'Reconnaissance' },
      { id: 'TA0001', name: 'Initial Access', tactic: 'Initial Access' }
    ],
    cleanup: ['Close the Navigator tab. No local data to clear.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which type of hacker has authorization to penetrate a system to identify vulnerabilities?', opts: ['Black Hat', 'White Hat', 'Gray Hat', 'Script Kiddie'], correct: 1, fb: 'White Hat hackers are authorized professionals hired to test security.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What term describes an attacker who uses pre-made tools without a deep understanding of how they work?', opts: ['Hacktivist', 'Nation-State', 'Script Kiddie', 'Insider Threat'], correct: 2, fb: 'Script kiddies rely on existing scripts or software to attack networks.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'An Insider Threat can be unintentional, such as an employee accidentally clicking a phishing link.', correct: 'true', fb: 'Insider threats can be malicious or negligent/accidental.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which threat actor group is primarily motivated by ideological or political goals?', opts: ['Organized Crime', 'Nation-State', 'Hacktivist', 'Script Kiddie'], correct: 2, fb: 'Hacktivists launch cyber attacks to promote a political agenda or social change.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'In the Cyber Kill Chain, which phase involves the attacker transmitting the weapon to the target environment?', opts: ['Reconnaissance', 'Weaponization', 'Delivery', 'Installation'], correct: 2, fb: 'The Delivery phase involves transmitting the payload (e.g., via email attachment or USB).' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'The MITRE ATT&CK framework only covers post-compromise behaviors.', correct: 'false', fb: 'MITRE ATT&CK covers both pre-compromise (PRE-ATT&CK) and post-compromise tactics and techniques.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Advanced Persistent Threats (APTs) are typically associated with which type of threat actor?', opts: ['Script Kiddies', 'Nation-State Actors', 'Disgruntled Employees', 'Gray Hats'], correct: 1, fb: 'APTs are usually well-resourced, highly skilled groups, often sponsored by nation-states.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'A Gray Hat hacker might find a vulnerability in a company\'s website and offer to fix it for a fee.', correct: 'true', fb: 'Gray hats often hack without permission but may disclose the flaw responsibly or ask for a bounty.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What does TTP stand for in threat intelligence?', opts: ['Tools, Targets, Protocols', 'Tactics, Techniques, Procedures', 'Threats, Targets, Parameters', 'Time, Threat, Posture'], correct: 1, fb: 'TTPs (Tactics, Techniques, and Procedures) describe the behavior and methodology of a threat actor.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which model is used to represent an intrusion using four nodes: Adversary, Capability, Infrastructure, and Victim?', opts: ['Cyber Kill Chain', 'Diamond Model', 'MITRE ATT&CK', 'STRIDE'], correct: 1, fb: 'The Diamond Model of Intrusion Analysis uses these four core features to analyze events.' }
  ],
  flashcards: [
    { f: 'White Hat', b: 'An ethical hacker who operates with permission to secure systems.' },
    { f: 'Black Hat', b: 'A malicious hacker who exploits systems for personal gain or damage.' },
    { f: 'Gray Hat', b: 'A hacker who operates without permission but usually lacks malicious intent.' },
    { f: 'Script Kiddie', b: 'An unskilled attacker who relies on pre-made tools and scripts.' },
    { f: 'Hacktivist', b: 'An attacker motivated by political, social, or ideological goals.' },
    { f: 'APT (Advanced Persistent Threat)', b: 'A prolonged and targeted cyberattack, often sponsored by a nation-state.' },
    { f: 'Insider Threat', b: 'A security risk originating from within the targeted organization (malicious or accidental).' },
    { f: 'TTPs', b: 'Tactics, Techniques, and Procedures - the behavior profile of a threat actor.' },
    { f: 'Cyber Kill Chain', b: 'A framework developed by Lockheed Martin outlining the stages of a cyberattack.' },
    { f: 'MITRE ATT&CK', b: 'A globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.' }
  ],
  summary: [
    'Hackers are categorized by intent and authorization (White, Black, Gray Hat).',
    'Threat actors have different motivations: financial (Organized Crime), political (Hacktivist), or espionage (Nation-State).',
    'Advanced Persistent Threats (APTs) are stealthy, well-resourced groups that maintain long-term access.',
    'The Cyber Kill Chain describes the phases an attacker goes through to achieve their goal.',
    'MITRE ATT&CK is the industry standard for mapping and understanding adversary TTPs.'
  ],
  outcomes: [
    'Identify the characteristics and motivations of different threat actor categories.',
    'Use the MITRE ATT&CK framework to map adversary behavior.',
    'Explain the stages of the Cyber Kill Chain.',
    'Understand how profiling threat actors helps in prioritizing enterprise defenses.'
  ]
};

CONTENT['ethical-hacking-concepts'] = {
  eyebrow: 'Module 01 · Topic 3',
  title: 'Ethical Hacking Concepts and Scoping',
  module: 'Phase 01: Security Analyst Trainee',
  sub: 'Understanding the rules of engagement, authorization, and the formal structure of a penetration testing engagement.',
  objectives: ['Differentiate between Penetration Testing and Vulnerability Assessments', 'Define Rules of Engagement (RoE) and Scope', 'Understand Red, Blue, and Purple team dynamics', 'Explain reporting standards and responsible disclosure'],
  learn: {
    simple: 'Ethical hacking is not just about breaking into systems; it is a formal, highly regulated process. The defining difference between a malicious hack and an ethical one is *permission*. Before any scanning or exploitation begins, strict legal agreements, such as a Statement of Work (SoW) and Rules of Engagement (RoE), must be established. This ensures the client understands the risks and the hacker stays within legal boundaries.',
    analogy: 'A vulnerability assessment is like walking around a building checking if the doors are locked. A penetration test is like actually trying to pick the lock or break a window to get inside. Doing either without the owner\'s written permission is a crime.',
    architecture: 'In an enterprise, security testing is often divided into teams. The Red Team acts as the adversary, performing stealthy, objective-based attacks. The Blue Team acts as the defenders, detecting and responding to the Red Team. The Purple Team is a collaborative effort where Red and Blue share information in real-time to rapidly improve defenses. All engagements are bound by strict scoping to prevent operational outages.',
    why: 'Without clear scoping and authorization, a penetration test can cause severe business disruption (e.g., crashing a critical database) and expose the tester to criminal liability. Professionalism, clear communication, and robust reporting are what differentiate a professional ethical hacker from a hobbyist.'
  },
  enterprise: {
    gfs: 'GFS Compliance requires an annual penetration test of all customer-facing payment systems. The Security Architecture team must define the Rules of Engagement, scope, and success criteria before any testing begins. A poorly scoped test led to a production outage in 2023.',
    windows: 'When scoping a Windows environment, testers must define whether attacking Active Directory, exploiting Domain Controllers, or using social engineering against employees is permitted.',
    linux: 'For Linux servers, the RoE must specify if Denial of Service (DoS) testing against Apache/Nginx web servers is allowed, as it can disrupt legitimate traffic.'
  },
  workflow: [
    'Step 1: Initial client meeting to understand business objectives.',
    'Step 2: Draft the Statement of Work (SoW) and Non-Disclosure Agreement (NDA).',
    'Step 3: Define the scope (IP ranges, domains, specific applications).',
    'Step 4: Establish the Rules of Engagement (RoE) (testing windows, forbidden techniques).',
    'Step 5: Obtain explicit, written authorization to proceed.',
    'Step 6: Conduct the engagement, strictly adhering to the RoE.',
    'Step 7: Deliver a formal report with findings and remediation steps.'
  ],
  diagram: {
    caption: 'Click to interact with the Security Teams diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><g font-family="monospace" font-size="14" fill="#fff"><circle cx="200" cy="200" r="100" fill="#ff3366" fill-opacity="0.6" stroke="#ff3366" stroke-width="2"/><text x="170" y="205" font-weight="bold">Red Team</text><circle cx="400" cy="200" r="100" fill="#3366ff" fill-opacity="0.6" stroke="#3366ff" stroke-width="2"/><text x="390" y="205" font-weight="bold">Blue Team</text><path d="M 300 130 A 100 100 0 0 0 300 270 A 100 100 0 0 0 300 130 Z" fill="#9933cc" fill-opacity="0.8"/><text x="300" y="205" text-anchor="middle" font-weight="bold">Purple</text><text x="300" y="225" text-anchor="middle" font-weight="bold">Team</text><text x="150" y="240" font-size="10">Attackers</text><text x="410" y="240" font-size="10">Defenders</text></g></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -sV -p- -T4 --exclude 192.168.1.50 <target>', purpose: 'Scans the target while explicitly excluding an out-of-scope IP address.', out: 'Nmap scan report', note: 'Critical for adhering to scoping rules defined in the RoE.', mistake: 'Forgetting the --exclude flag and scanning an out-of-scope production server.' }
    ],
    win: [
      { cmd: 'Test-NetConnection -ComputerName <target> -Port 443', purpose: 'Tests connection to a specific port without intrusive scanning.', out: 'TcpTestSucceeded : True', note: 'A safe way to verify connectivity before launching heavier, potentially disruptive tools.', mistake: 'Running intrusive PowerShell attack scripts before basic connectivity checks.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Foundation',
    duration: '30',
    platform: 'Document Editor',
    environment: 'Local Lab',
    tools: ['RoE Template', 'Text Editor'],
    dependencies: [],
    safety: ['This is a documentation exercise. No active scanning is performed.'],
    scenario: 'You are preparing for an external penetration test for GFS. You must build a Rules of Engagement document defining the scope, out-of-scope systems, testing windows, emergency contacts, and acceptable methodologies.',
    objectives: ['Draft a comprehensive Rules of Engagement (RoE) document', 'Clearly define in-scope and out-of-scope assets', 'Establish communication protocols for the engagement'],
    steps: [
      'Step 1: Open the provided RoE template.',
      'Step 2: Define the target scope: 198.51.100.0/24 subnet.',
      'Step 3: Define out-of-scope assets: specifically exclude the mainframe interface at 198.51.100.15.',
      'Step 4: Set the testing window: Friday 22:00 UTC to Sunday 04:00 UTC.',
      'Step 5: Explicitly forbid Denial of Service (DoS) and physical social engineering attacks.',
      'Step 6: Document emergency contact details for the GFS SOC.'
    ],
    evidence: ['Completed RoE document in PDF format.'],
    validation: ['You should see: A fully populated document ready for client signature.', 'Verify by: Ensuring the out-of-scope IP is explicitly mentioned in the exclusion section.'],
    troubleshooting: ['Ensure all sections of the template are filled; leaving sections blank can lead to legal ambiguity.', 'Common error: Forgetting to specify the timezone for the testing window.'],
    mitre: [],
    cleanup: ['Save the document to your local machine.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'What is the primary difference between a Vulnerability Assessment and a Penetration Test?', opts: ['Vulnerability assessments are faster', 'Penetration tests actively exploit vulnerabilities to prove risk', 'Vulnerability assessments are done by black hats', 'Penetration tests only look at network infrastructure'], correct: 1, fb: 'Vulnerability assessments identify flaws, while penetration tests actively exploit them to demonstrate potential impact.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which document legally protects the ethical hacker and outlines exactly what systems can be tested?', opts: ['Non-Disclosure Agreement (NDA)', 'Rules of Engagement (RoE)', 'Statement of Work (SoW)', 'Service Level Agreement (SLA)'], correct: 1, fb: 'The Rules of Engagement (RoE) document dictates the scope, permissions, and limitations of the penetration test.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'It is acceptable for an ethical hacker to perform a quick port scan on a client\'s network before the RoE is signed, just to prepare.', correct: 'false', fb: 'Absolutely no testing, including scanning, should occur before all legal agreements and authorizations are signed.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which team is responsible for actively defending the network and responding to incidents during a security exercise?', opts: ['Red Team', 'Blue Team', 'Purple Team', 'White Team'], correct: 1, fb: 'The Blue Team is the defensive security team.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the purpose of a Purple Team?', opts: ['To act as referees during a test', 'To manage physical security', 'To facilitate collaboration and knowledge sharing between Red and Blue teams', 'To handle public relations during a breach'], correct: 2, fb: 'The Purple Team ensures that the offensive (Red) and defensive (Blue) teams work together to improve overall security.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'A Non-Disclosure Agreement (NDA) ensures that the ethical hacker will not share confidential client information discovered during the test.', correct: 'true', fb: 'An NDA is a legal contract establishing confidentiality between the tester and the client.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is "Scope Creep" in the context of penetration testing?', opts: ['A stealthy movement technique used by Red Teams', 'When the testing gradually expands beyond the originally agreed-upon boundaries', 'A type of malware', 'The process of scanning a network slowly'], correct: 1, fb: 'Scope creep occurs when the parameters of an engagement slowly expand without formal approval, increasing risk and liability.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Bug bounty programs authorize anyone to test the company\'s systems using any method they choose.', correct: 'false', fb: 'Bug bounties have strict rules of engagement defining what can be tested and what methods are permitted.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'If an ethical hacker discovers evidence of a previous compromise (e.g., active malware) during a penetration test, what is the best immediate action?', opts: ['Exploit the malware to see what it does', 'Ignore it, as it is out of scope', 'Immediately halt testing and report it to the client via emergency contacts', 'Delete the malware'], correct: 2, fb: 'Discovering active compromise requires immediate notification to the client as it may trigger their Incident Response process.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the standard system used to rate the severity of software vulnerabilities?', opts: ['CVE', 'CVSS', 'CWE', 'CAPEC'], correct: 1, fb: 'CVSS (Common Vulnerability Scoring System) provides a way to capture the principal characteristics of a vulnerability and produce a numerical severity score.' }
  ],
  flashcards: [
    { f: 'Rules of Engagement (RoE)', b: 'The document defining the scope, limitations, methodology, and constraints of a penetration test.' },
    { f: 'Red Team', b: 'Offensive security professionals who simulate real-world attacks to test defenses.' },
    { f: 'Blue Team', b: 'Defensive security professionals responsible for maintaining network security and responding to attacks.' },
    { f: 'Purple Team', b: 'A collaborative function that integrates Red and Blue team methodologies to improve defense capabilities.' },
    { f: 'Scope', b: 'The specifically defined targets (IPs, domains, applications) authorized for testing.' },
    { f: 'NDA (Non-Disclosure Agreement)', b: 'A legal contract ensuring confidentiality of information shared during an engagement.' },
    { f: 'Vulnerability Assessment', b: 'The process of identifying and reporting vulnerabilities without actively exploiting them.' },
    { f: 'Penetration Test', b: 'An authorized simulated cyberattack to evaluate the security of a system by exploiting vulnerabilities.' },
    { f: 'CVSS', b: 'Common Vulnerability Scoring System, used to rate the severity of vulnerabilities.' },
    { f: 'Responsible Disclosure', b: 'The practice of reporting a vulnerability to the vendor/owner and giving them time to fix it before making it public.' }
  ],
  summary: [
    'Written authorization and a defined scope are mandatory before any ethical hacking activities begin.',
    'The Rules of Engagement (RoE) dictate how, when, and what can be tested.',
    'Vulnerability assessments identify flaws; penetration tests exploit them to demonstrate impact.',
    'Red Teams attack, Blue Teams defend, and Purple Teams collaborate to maximize learning.',
    'Professional reporting and strict adherence to legal boundaries separate ethical hackers from malicious actors.'
  ],
  outcomes: [
    'Draft and interpret a Rules of Engagement (RoE) document.',
    'Differentiate between vulnerability assessments and penetration tests.',
    'Understand the roles and dynamics of Red, Blue, and Purple teams.',
    'Apply ethical guidelines and responsible disclosure principles.'
  ]
};

CONTENT['hacking-methodologies'] = {
  eyebrow: 'Module 01 · Topic 4',
  title: 'Hacking Methodologies and Frameworks',
  module: 'Phase 01: Security Analyst Trainee',
  sub: 'Mastering the structured approaches and industry-standard frameworks used to execute a professional cyber attack.',
  objectives: ['Learn the 5 phases of the CEH Hacking Methodology', 'Compare the Cyber Kill Chain and MITRE ATT&CK', 'Understand OSSTMM, PTES, and NIST frameworks', 'Apply structured methodology to attack scenarios'],
  learn: {
    simple: 'Hacking is not random; it is highly structured. The CEH defines a 5-phase methodology: Reconnaissance (gathering information), Scanning (probing the network), Gaining Access (exploiting vulnerabilities), Maintaining Access (installing backdoors), and Clearing Tracks (hiding evidence). Using a methodology ensures that tests are thorough, repeatable, and professionally documented.',
    analogy: 'Think of a bank robbery in a movie. Reconnaissance is staking out the bank and checking guard schedules. Scanning is testing the vault doors and checking the alarm wiring. Gaining Access is blowing the vault. Maintaining Access is propping the back door open for tomorrow. Clearing Tracks is wiping the fingerprints and deleting the security footage.',
    architecture: 'In enterprise security, multiple frameworks are used simultaneously. An attacker might follow the CEH methodology for their workflow. The Blue Team might use the Lockheed Martin Cyber Kill Chain to describe the incident at a high level to management. The SOC analysts will use MITRE ATT&CK to tag specific techniques (like T1059 Command and Scripting Interpreter) in their SIEM alerts. Testers may also follow PTES (Penetration Testing Execution Standard) for their engagement structure.',
    why: 'Ad-hoc hacking misses vulnerabilities and lacks reproducibility. Standardized frameworks provide a common language for attackers and defenders, ensuring that security assessments are comprehensive and that incident reports are universally understood.'
  },
  enterprise: {
    gfs: 'After a phishing incident, GFS\'s incident response team uses the MITRE ATT&CK framework to reconstruct the attacker\'s path from initial access through credential theft. Mapping to the Cyber Kill Chain helps identify where defensive controls failed.',
    windows: 'When attacking Windows, the "Maintaining Access" phase often involves creating hidden registry keys for persistence, creating rogue Admin accounts, or manipulating Scheduled Tasks.',
    linux: 'In Linux, "Reconnaissance" might involve querying DNS records and WHOIS, while "Clearing Tracks" involves modifying or deleting the .bash_history file and tampering with /var/log/auth.log.'
  },
  workflow: [
    'Phase 1: Reconnaissance (Footprinting) - Passive and active information gathering.',
    'Phase 2: Scanning - Port scanning, vulnerability scanning, and network mapping.',
    'Phase 3: Enumeration - Extracting specific user names, network shares, and services.',
    'Phase 4: Gaining Access - Exploiting identified vulnerabilities to gain a foothold.',
    'Phase 5: Maintaining Access - Establishing persistence (backdoors, rootkits).',
    'Phase 6: Clearing Tracks - Removing logs and evidence of the intrusion.'
  ],
  diagram: {
    caption: 'Click to interact with the CEH Hacking Methodology diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><g font-family="monospace" font-size="12" fill="#fff"><rect x="50" y="50" width="120" height="50" rx="5" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="110" y="80" text-anchor="middle">1. Recon</text><rect x="220" y="100" width="120" height="50" rx="5" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="280" y="130" text-anchor="middle">2. Scanning</text><rect x="390" y="150" width="120" height="50" rx="5" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="450" y="180" text-anchor="middle">3. Gain Access</text><rect x="220" y="200" width="150" height="50" rx="5" fill="#1a1a2e" stroke="#ff3366" stroke-width="2"/><text x="295" y="230" text-anchor="middle">4. Maintain Access</text><rect x="50" y="250" width="130" height="50" rx="5" fill="#1a1a2e" stroke="#ff3366" stroke-width="2"/><text x="115" y="280" text-anchor="middle">5. Clear Tracks</text><path d="M 170 75 Q 280 75 280 100" fill="none" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/><path d="M 340 125 Q 450 125 450 150" fill="none" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/><path d="M 450 200 Q 450 225 370 225" fill="none" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/><path d="M 220 225 Q 115 225 115 250" fill="none" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/></g></svg>'
  },
  commands: {
    lin: [
      { cmd: 'history -c', purpose: 'Clears the current bash history session.', out: 'No output', note: 'Used during the Clearing Tracks phase. Defenders should forward logs centrally so local deletion is less effective.', mistake: 'Forgetting that .bash_history file still exists on disk until overwritten.' }
    ],
    win: [
      { cmd: 'wevtutil cl Security', purpose: 'Clears the Windows Security Event Log.', out: 'No output', note: 'A loud action used in Clearing Tracks. SOCs should alert immediately if Event ID 1102 (audit log cleared) is detected.', mistake: 'Clearing logs without realizing that the SIEM has already ingested the critical events.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '40',
    platform: 'Web Browser',
    environment: 'Local Lab',
    tools: ['Framework Comparison Chart'],
    dependencies: [],
    safety: ['This is an analytical exercise.'],
    scenario: 'You receive an incident report from the GFS SOC: An attacker researched GFS employees on LinkedIn (A), sent a malicious PDF via email (B), which exploited a zero-day in Adobe Reader (C), installed a scheduled task for persistence (D), and finally deleted Windows event logs (E). You must map this to the CEH Methodology and the Cyber Kill Chain.',
    objectives: ['Map real-world attack steps to standard frameworks', 'Compare the terminology of CEH vs. Kill Chain', 'Identify defensive interventions at each stage'],
    steps: [
      'Step 1: Map (A) LinkedIn research: CEH = Reconnaissance | Kill Chain = Reconnaissance.',
      'Step 2: Map (B) Emailing the PDF: CEH = Reconnaissance/Scanning (borderline) | Kill Chain = Delivery.',
      'Step 3: Map (C) Exploiting the zero-day: CEH = Gaining Access | Kill Chain = Exploitation.',
      'Step 4: Map (D) Scheduled task: CEH = Maintaining Access | Kill Chain = Installation.',
      'Step 5: Map (E) Deleting logs: CEH = Clearing Tracks | Kill Chain = Actions on Objectives.'
    ],
    evidence: ['Completed Framework Mapping table.'],
    validation: ['You should see: Accurate mapping of the incident narrative to both frameworks.', 'Verify by: Ensuring that the terminology used perfectly matches the official framework documentation.'],
    troubleshooting: ['Some actions span multiple phases; focus on the primary objective of the attacker\'s action.', 'Common error: Confusing "Delivery" with "Weaponization" in the Kill Chain.'],
    mitre: [
      { id: 'T1566', name: 'Phishing', tactic: 'Initial Access' },
      { id: 'T1053', name: 'Scheduled Task/Job', tactic: 'Persistence' }
    ],
    cleanup: ['No cleanup required.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which phase of the hacking methodology involves gathering information without directly interacting with the target?', opts: ['Active Reconnaissance', 'Passive Reconnaissance', 'Scanning', 'Enumeration'], correct: 1, fb: 'Passive reconnaissance gathers data from public sources (OSINT) without touching the target\'s network.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'In the CEH methodology, installing a rootkit or backdoor falls under which phase?', opts: ['Gaining Access', 'Maintaining Access', 'Clearing Tracks', 'Scanning'], correct: 1, fb: 'Maintaining Access involves ensuring the attacker can return to the compromised system later.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which penetration testing standard provides comprehensive guidelines consisting of 7 distinct phases, from Pre-engagement Interactions to Reporting?', opts: ['OSSTMM', 'NIST SP 800-115', 'PTES', 'OWASP'], correct: 2, fb: 'PTES (Penetration Testing Execution Standard) is a highly detailed, 7-phase methodology.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Enumeration is the process of extracting user names, machine names, network resources, and shares from a system.', correct: 'true', fb: 'Enumeration is a critical active phase that gathers specific, actionable data for exploitation.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'In the Lockheed Martin Cyber Kill Chain, what happens during the "Weaponization" phase?', opts: ['The payload is delivered to the target', 'The attacker researches the target', 'A malicious payload is coupled with an exploit to create a deliverable weapon', 'The malware executes on the target system'], correct: 2, fb: 'Weaponization occurs on the attacker\'s side, wrapping an exploit and payload into a deliverable format like a PDF.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Clearing tracks only involves deleting log files.', correct: 'false', fb: 'Clearing tracks can involve modifying logs, using rootkits to hide processes, deleting tools, and using covert channels.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which standard focuses primarily on the scientific testing of operational security and provides a quantifiable metric called the RAV (Risk Assessment Value)?', opts: ['PTES', 'OSSTMM', 'NIST', 'ISO 27001'], correct: 1, fb: 'The Open Source Security Testing Methodology Manual (OSSTMM) focuses on measurable, scientific security testing.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'The OWASP Top 10 is primarily a framework used for securing physical facilities.', correct: 'false', fb: 'OWASP (Open Web Application Security Project) focuses specifically on web application security.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which publication is the NIST technical guide to information security testing and assessment?', opts: ['SP 800-53', 'SP 800-115', 'SP 800-30', 'FIPS 140-2'], correct: 1, fb: 'NIST SP 800-115 provides practical guidance on designing and executing security assessments.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'If an attacker uses Alternate Data Streams (ADS) in Windows, which phase of the CEH methodology are they most likely executing?', opts: ['Scanning', 'Enumeration', 'Maintaining Access / Clearing Tracks', 'Reconnaissance'], correct: 2, fb: 'ADS is often used to hide malicious files from casual inspection, aiding in maintaining access and clearing tracks.' }
  ],
  flashcards: [
    { f: 'Passive Reconnaissance', b: 'Gathering information about a target without directly interacting with its systems.' },
    { f: 'Active Reconnaissance', b: 'Probing the target network directly (e.g., port scanning) to gather information.' },
    { f: 'Enumeration', b: 'Systematically extracting specific information like usernames and network shares from a system.' },
    { f: 'Maintaining Access', b: 'The phase where an attacker ensures they can return to a compromised system using backdoors or rootkits.' },
    { f: 'Clearing Tracks', b: 'Removing evidence of the intrusion, such as modifying logs and hiding files.' },
    { f: 'PTES', b: 'Penetration Testing Execution Standard - a comprehensive 7-phase testing framework.' },
    { f: 'OSSTMM', b: 'Open Source Security Testing Methodology Manual - focuses on measurable, scientific testing.' },
    { f: 'Cyber Kill Chain', b: 'Lockheed Martin\'s framework outlining 7 phases of an external cyber attack.' },
    { f: 'OWASP', b: 'Open Web Application Security Project - provides standards and methodologies for web app security.' },
    { f: 'Weaponization', b: 'The phase in the Kill Chain where an exploit and payload are combined into a deliverable weapon.' }
  ],
  summary: [
    'The CEH methodology follows 5 phases: Reconnaissance, Scanning, Gaining Access, Maintaining Access, Clearing Tracks.',
    'Reconnaissance can be passive (no direct contact) or active (probing the target).',
    'The Cyber Kill Chain describes the attacker\'s progression from the defender\'s perspective.',
    'Frameworks like PTES, OSSTMM, and NIST SP 800-115 standardize the penetration testing process.',
    'Applying a methodology ensures testing is thorough, legal, and provides actionable results.'
  ],
  outcomes: [
    'Describe the 5 phases of the CEH hacking methodology.',
    'Map adversary actions to the Lockheed Martin Cyber Kill Chain.',
    'Understand the purpose of industry standards like PTES and OSSTMM.',
    'Identify the transition points between different phases of an attack.'
  ]
};

CONTENT['security-controls'] = {
  eyebrow: 'Module 01 · Topic 5',
  title: 'Information Security Controls',
  module: 'Phase 01: Security Analyst Trainee',
  sub: 'Designing and evaluating the mechanisms used to manage risk and protect enterprise assets.',
  objectives: ['Classify controls by type (Administrative, Technical, Physical)', 'Classify controls by function (Preventive, Detective, Corrective)', 'Implement Defense in Depth strategies', 'Evaluate control effectiveness'],
  learn: {
    simple: 'Security controls are the safeguards or countermeasures deployed to avoid, detect, counteract, or minimize security risks. They are classified by *how* they are implemented (Administrative, Technical, Physical) and by *what* they do (Preventive, Detective, Corrective). A robust security posture uses a mix of all these types to create Defense in Depth.',
    analogy: 'Think of a museum. The policy saying "Do not touch the art" is an Administrative control. The locked glass case around the diamond is a Technical (or logical/physical hybrid) control. The security guard at the door is a Physical control. The glass case is Preventive. The alarm that sounds if the glass breaks is Detective. The backup generator that restores power if the lights go out is Corrective.',
    architecture: 'In enterprise architecture, controls are mapped to frameworks like NIST SP 800-53 or CIS Controls. If a Preventive Technical control (like a Firewall) fails, a Detective Technical control (like an IDS or SIEM) must identify the breach. A Compensating control might be used if a primary control is too expensive or impossible to implement (e.g., using network segmentation for an old, unpatchable medical device).',
    why: 'Relying on a single type of control is a critical failure. Many organizations buy expensive Technical controls (firewalls) but ignore Administrative controls (training), leading to employees easily falling for phishing attacks. Understanding the matrix of controls ensures comprehensive security.'
  },
  enterprise: {
    gfs: 'Following a SOC audit, GFS discovered that while technical controls (firewall, SIEM) were strong, administrative controls (security awareness training, access review procedures) had not been updated in 3 years. This gap allowed a social engineering attack to succeed despite strong technical defenses.',
    windows: 'In Windows, BitLocker is a Technical Preventive control protecting data at rest. Windows Event Forwarding (WEF) is a Technical Detective control aiding the SOC.',
    linux: 'On Linux, SELinux or AppArmor serve as strong Technical Preventive controls, enforcing mandatory access control (MAC) policies that prevent processes from acting outside their intended bounds.'
  },
  workflow: [
    'Step 1: Identify the asset and the specific risk to mitigate.',
    'Step 2: Determine if a Preventive control can stop the threat entirely.',
    'Step 3: Implement Detective controls to alert if the Preventive control fails.',
    'Step 4: Establish Corrective controls to restore normal operations if a breach occurs.',
    'Step 5: Ensure Administrative policies mandate the use of these technical/physical controls.',
    'Step 6: Regularly audit and test the controls for effectiveness.'
  ],
  diagram: {
    caption: 'Click to interact with the Security Controls Matrix',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><g font-family="monospace" font-size="12" fill="#fff"><line x1="150" y1="50" x2="150" y2="350" stroke="#666" stroke-width="2"/><line x1="300" y1="50" x2="300" y2="350" stroke="#666" stroke-width="2"/><line x1="450" y1="50" x2="450" y2="350" stroke="#666" stroke-width="2"/><line x1="50" y1="150" x2="550" y2="150" stroke="#666" stroke-width="2"/><line x1="50" y1="250" x2="550" y2="250" stroke="#666" stroke-width="2"/><text x="100" y="100" font-weight="bold" fill="#00ffcc">Admin</text><text x="100" y="200" font-weight="bold" fill="#00ffcc">Technical</text><text x="100" y="300" font-weight="bold" fill="#00ffcc">Physical</text><text x="225" y="40" font-weight="bold" fill="#ff3366">Preventive</text><text x="375" y="40" font-weight="bold" fill="#ff3366">Detective</text><text x="500" y="40" font-weight="bold" fill="#ff3366">Corrective</text><text x="225" y="100" text-anchor="middle">Policies</text><text x="375" y="100" text-anchor="middle">Audits</text><text x="500" y="100" text-anchor="middle">Disciplinary</text><text x="225" y="200" text-anchor="middle">Firewalls/MFA</text><text x="375" y="200" text-anchor="middle">IDS/SIEM</text><text x="500" y="200" text-anchor="middle">Backups/AV</text><text x="225" y="300" text-anchor="middle">Locks/Fences</text><text x="375" y="300" text-anchor="middle">CCTV/Guards</text><text x="500" y="300" text-anchor="middle">Fire Suppress</text></g></svg>'
  },
  commands: {
    lin: [
      { cmd: 'sudo ufw enable', purpose: 'Enables the Uncomplicated Firewall.', out: 'Firewall is active and enabled on system startup', note: 'A fundamental Technical Preventive control.', mistake: 'Enabling the firewall before allowing SSH access, thereby locking yourself out.' }
    ],
    win: [
      { cmd: 'Auditpol /set /subcategory:"Logon" /success:enable /failure:enable', purpose: 'Enables logon auditing.', out: 'The command was successfully executed.', note: 'A crucial Technical Detective control for identifying unauthorized access attempts.', mistake: 'Logging everything (success/failure for all events) and overwhelming the SIEM with noise.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Web Browser',
    environment: 'Local Lab',
    tools: ['Control Matrix Spreadsheet'],
    dependencies: [],
    safety: ['Analytical exercise only.'],
    scenario: 'GFS needs to secure a new datacenter housing critical financial mainframes. You must design a layered control strategy by selecting appropriate controls across the matrix (Admin/Tech/Phys vs. Prev/Det/Corr).',
    objectives: ['Map specific security tools to their control categories', 'Design a defense-in-depth architecture', 'Identify compensating controls for unmitigated risks'],
    steps: [
      'Step 1: Open the Control Matrix spreadsheet.',
      'Step 2: Assign "Security Awareness Training" to Administrative/Preventive.',
      'Step 3: Assign "Biometric Mantraps" to Physical/Preventive.',
      'Step 4: Assign "Splunk SIEM Alerting" to Technical/Detective.',
      'Step 5: Assign "Automated Server Snapshots" to Technical/Corrective.',
      'Step 6: Propose a Compensating control for an old HVAC system that cannot be patched.'
    ],
    evidence: ['Completed Control Matrix Spreadsheet.'],
    validation: ['You should see: A balanced matrix with controls in every quadrant.', 'Verify by: Ensuring no single point of failure exists; if a preventive control fails, a detective control should catch it.'],
    troubleshooting: ['Some controls blur the lines (e.g., CCTV can be preventive if visible, but is primarily detective). Document your reasoning.', 'Common error: Classifying Backups as Preventive.'],
    mitre: [
      { id: 'D3-AL', name: 'Account Locking', tactic: 'Evict' },
      { id: 'D3-NIA', name: 'Network Intrusion Alerting', tactic: 'Detect' }
    ],
    cleanup: ['Save and close the spreadsheet.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which type of control is implemented through policies, procedures, and training?', opts: ['Technical', 'Administrative', 'Physical', 'Compensating'], correct: 1, fb: 'Administrative (or managerial) controls are directives given by management.' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'A firewall blocking unauthorized inbound traffic is an example of which two control classifications?', opts: ['Technical / Detective', 'Physical / Preventive', 'Technical / Preventive', 'Administrative / Corrective'], correct: 2, fb: 'A firewall is software/hardware (Technical) that stops attacks before they happen (Preventive).' },
    { type: 'true-false', difficulty: 'Foundation', q: 'A security camera (CCTV) is primarily a Physical Corrective control.', correct: 'false', fb: 'CCTV is a Physical Detective control (it records events to be reviewed). It does not correct the incident.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the purpose of a Compensating control?', opts: ['To provide an alternative when a primary control is not feasible', 'To punish employees who violate security policies', 'To automatically fix software bugs', 'To completely eliminate all risk'], correct: 0, fb: 'Compensating controls are used when a required control is too costly or technically impossible to implement.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Restoring a database from a backup after a ransomware attack is an example of using a:', opts: ['Preventive control', 'Detective control', 'Corrective control', 'Deterrent control'], correct: 2, fb: 'Corrective controls aim to restore systems to normal after a security incident has occurred.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'A warning banner displayed before a user logs into a system is considered a Deterrent control.', correct: 'true', fb: 'Deterrent controls aim to discourage individuals from violating security policies.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which of the following best describes the principle of Defense in Depth?', opts: ['Using the strongest encryption algorithm available', 'Layering different types of controls so that if one fails, others remain', 'Purchasing all security tools from a single vendor', 'Hiding the network architecture from attackers'], correct: 1, fb: 'Defense in Depth utilizes multiple layers of overlapping controls (Admin, Tech, Physical).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'An Intrusion Detection System (IDS) alerts the SOC that a port scan is occurring. What type of control is the IDS?', opts: ['Technical Preventive', 'Technical Detective', 'Administrative Detective', 'Physical Corrective'], correct: 1, fb: 'An IDS uses technology to identify and alert on suspicious activity, making it a Technical Detective control.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'Mandatory vacations and job rotation are examples of Technical controls used to prevent fraud.', correct: 'false', fb: 'These are Administrative controls, heavily used in the financial sector to detect and prevent insider fraud.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Under which control category would a business continuity plan (BCP) fall?', opts: ['Administrative Recovery', 'Technical Preventive', 'Physical Detective', 'Compensating'], correct: 0, fb: 'A BCP is a policy/procedure (Administrative) designed to restore business operations (Recovery/Corrective).' }
  ],
  flashcards: [
    { f: 'Administrative Control', b: 'Policies, procedures, and training designed to manage personnel and business practices.' },
    { f: 'Technical Control', b: 'Hardware or software mechanisms used to protect assets (e.g., firewalls, encryption).' },
    { f: 'Physical Control', b: 'Tangible mechanisms that protect physical premises and hardware (e.g., locks, guards).' },
    { f: 'Preventive Control', b: 'Designed to stop a security incident before it occurs.' },
    { f: 'Detective Control', b: 'Designed to identify and record a security incident in progress or after the fact.' },
    { f: 'Corrective Control', b: 'Designed to restore systems and minimize damage after an incident.' },
    { f: 'Deterrent Control', b: 'Designed to discourage malicious activity (e.g., warning signs, visible cameras).' },
    { f: 'Compensating Control', b: 'An alternative control used when a primary control cannot be implemented.' },
    { f: 'Defense in Depth', b: 'The strategy of using multiple, overlapping layers of security.' },
    { f: 'Recovery Control', b: 'Specifically aimed at restoring normal operations after a disaster (often grouped with corrective).' }
  ],
  summary: [
    'Security controls are categorized by type: Administrative, Technical, and Physical.',
    'Controls are also categorized by function: Preventive, Detective, Corrective, Deterrent, and Compensating.',
    'Effective security requires a Defense in Depth strategy, utilizing a mixture of all control types.',
    'A failure in a Preventive control must be caught by a Detective control.',
    'Administrative policies must enforce the use of Technical and Physical controls.'
  ],
  outcomes: [
    'Classify security controls by type and function.',
    'Design a layered security architecture using Defense in Depth.',
    'Identify appropriate compensating controls for specific scenarios.',
    'Understand the relationship between policies and technical implementation.'
  ]
};

CONTENT['security-laws'] = {
  eyebrow: 'Module 01 · Topic 6',
  title: 'Security Laws, Regulations, and Compliance',
  module: 'Phase 01: Security Analyst Trainee',
  sub: 'Navigating the legal and regulatory landscape that dictates enterprise cybersecurity requirements.',
  objectives: ['Understand key global regulations (GDPR, HIPAA, PCI DSS)', 'Differentiate between laws, regulations, and industry standards', 'Understand the implications of non-compliance', 'Map security controls to compliance requirements'],
  learn: {
    simple: 'Cybersecurity is not just about stopping hackers; it is often mandated by law. Laws (like GDPR or HIPAA) are created by governments. Industry standards (like PCI DSS for credit cards) are created by industry bodies. Compliance means proving to an auditor that you meet these legal and regulatory requirements. An ethical hacker must understand these laws to know what data is regulated and how to report vulnerabilities properly.',
    analogy: 'Think of driving a car. Defensive driving techniques are like security best practices (you do them to stay safe). Speed limits and traffic lights are like regulations (you must follow them or get fined). A vehicle safety inspection is like a compliance audit (proving your car meets the legal standards).',
    architecture: 'Enterprise security teams map their technical controls to frameworks like ISO 27001 or the NIST Cybersecurity Framework. These frameworks act as a bridge. For example, by implementing NIST 800-53 controls (access management, encryption), a company can prove they comply with the HIPAA Security Rule. GRC (Governance, Risk, and Compliance) software is used to track these mappings and manage audits.',
    why: 'Non-compliance can destroy a business. GDPR fines can reach 4% of global revenue. Failing a PCI DSS audit means a company can no longer process credit cards. Security professionals must align their technical work with compliance mandates to secure budget and ensure legal operations.'
  },
  enterprise: {
    gfs: 'GFS operates under PCI DSS because it processes cardholder data, and GDPR because it serves EU customers. A single misconfigured API endpoint could result in a GDPR breach notification obligation (72-hour window), PCI DSS Level 1 audit failure, and regulatory fines up to 4% of annual global turnover.',
    windows: 'Windows Server features like BitLocker and Encrypting File System (EFS) are often explicitly deployed to meet the encryption-at-rest requirements mandated by HIPAA and PCI DSS.',
    linux: 'Linux environments use auditd to maintain immutable logs of user commands and file accesses, satisfying the strict auditing and accountability requirements of ISO 27001 and SOC 2.'
  },
  workflow: [
    'Step 1: Identify all applicable laws and regulations based on data types (e.g., PHI, PII, Cardholder Data) and geography.',
    'Step 2: Select a control framework (e.g., NIST CSF, ISO 27001) to structure the security program.',
    'Step 3: Conduct a gap assessment against the requirements.',
    'Step 4: Implement necessary administrative, technical, and physical controls.',
    'Step 5: Continuously monitor compliance and gather evidence.',
    'Step 6: Perform internal audits and engage third-party auditors for official certification.'
  ],
  diagram: {
    caption: 'Click to interact with the Compliance Landscape diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><g font-family="monospace" font-size="12" fill="#fff"><circle cx="300" cy="200" r="140" fill="#1a1a2e" stroke="#00ffcc" stroke-width="2"/><text x="300" y="90" text-anchor="middle" font-weight="bold" fill="#00ffcc">Security Framework (e.g. NIST/ISO)</text><rect x="220" y="130" width="160" height="40" rx="5" fill="#3366ff"/><text x="300" y="155" text-anchor="middle">PCI DSS (Card Data)</text><rect x="220" y="180" width="160" height="40" rx="5" fill="#ff3366"/><text x="300" y="205" text-anchor="middle">HIPAA (Healthcare)</text><rect x="220" y="230" width="160" height="40" rx="5" fill="#9933cc"/><text x="300" y="255" text-anchor="middle">GDPR (EU Privacy)</text><text x="300" y="320" text-anchor="middle" font-size="10">Technical Controls map to these regulations</text></g></svg>'
  },
  commands: {
    lin: [
      { cmd: 'aureport --auth', purpose: 'Generates a report of authentication events from auditd.', out: 'List of logins and failures', note: 'Critical for providing evidence of access control monitoring during a compliance audit.', mistake: 'Failing to configure auditd to forward logs to a centralized, immutable server.' }
    ],
    win: [
      { cmd: 'Get-BitLockerVolume', purpose: 'Checks the encryption status of disk volumes.', out: 'VolumeStatus: FullyEncrypted', note: 'Used to provide immediate evidence to an auditor that data at rest is protected.', mistake: 'Leaving the recovery keys stored in plain text on the same network.' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Document Editor',
    environment: 'Local Lab',
    tools: ['Compliance Gap Assessment Template'],
    dependencies: [],
    safety: ['Analytical exercise only.'],
    scenario: 'GFS is preparing for a joint PCI DSS and GDPR audit. You must review a list of GFS infrastructure components, identify which PCI DSS requirements and GDPR articles apply, document gaps, and recommend remediation.',
    objectives: ['Map technical configurations to legal requirements', 'Identify compliance violations', 'Recommend technical remediation for regulatory gaps'],
    steps: [
      'Step 1: Review Component A: "Unencrypted database storing EU citizen names and credit card numbers".',
      'Step 2: Identify PCI DSS violation: Requirement 3 (Protect stored account data).',
      'Step 3: Identify GDPR violation: Article 32 (Security of processing - encryption).',
      'Step 4: Document the gap: Data at rest is not protected.',
      'Step 5: Recommend remediation: Implement AES-256 encryption on the database volume and restrict key access.'
    ],
    evidence: ['Completed Gap Assessment Report.'],
    validation: ['You should see: Accurate mapping of the unencrypted database to both PCI and GDPR penalties.', 'Verify by: Referencing the official PCI DSS v4.0 documentation.'],
    troubleshooting: ['Remember that GDPR applies to personal data (PII) of EU residents, regardless of where the company is located.', 'Common error: Assuming PCI DSS applies to all employee data (it only applies to the Cardholder Data Environment).'],
    mitre: [
      { id: 'Regulation', name: 'Regulatory Context', tactic: 'N/A - This lab focuses on GRC, not direct MITRE mapping.' }
    ],
    cleanup: ['Save the report.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'Which regulation protects the privacy and security of health information in the United States?', opts: ['PCI DSS', 'GDPR', 'HIPAA', 'FISMA'], correct: 2, fb: 'The Health Insurance Portability and Accountability Act (HIPAA) regulates Protected Health Information (PHI).' },
    { type: 'multiple-choice', difficulty: 'Foundation', q: 'PCI DSS applies to organizations that handle which type of data?', opts: ['Student records', 'Credit card and cardholder data', 'European Union citizen data', 'Government classified information'], correct: 1, fb: 'The Payment Card Industry Data Security Standard applies to any entity that stores, processes, or transmits cardholder data.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'GDPR only applies to companies physically located within the European Union.', correct: 'false', fb: 'GDPR has extraterritorial scope; it applies to any organization processing the data of EU residents, regardless of the organization\'s location.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a core requirement of GDPR regarding data breaches?', opts: ['Notification to authorities within 72 hours of awareness', 'Paying a ransom if demanded', 'Filing a report with the FBI', 'No notification is required if the data was encrypted'], correct: 0, fb: 'Under GDPR, significant breaches must be reported to the supervisory authority within 72 hours.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which law makes it a federal crime to access a protected computer without authorization in the United States?', opts: ['DMCA', 'CFAA', 'GLBA', 'SOX'], correct: 1, fb: 'The Computer Fraud and Abuse Act (CFAA) is the primary federal anti-hacking law in the US.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'ISO 27001 is a mandatory law enacted by the United Nations.', correct: 'false', fb: 'ISO 27001 is an international standard for Information Security Management Systems (ISMS), not a law. It is voluntarily adopted or required by business contracts.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which compliance report focuses on a service organization\'s controls relevant to security, availability, processing integrity, confidentiality, or privacy?', opts: ['SOC 2', 'PCI DSS Level 1', 'FISMA', 'NIST CSF'], correct: 0, fb: 'SOC (System and Organization Controls) 2 reports evaluate an organization\'s information systems relevant to the Trust Services Criteria.' },
    { type: 'true-false', difficulty: 'Foundation', q: 'An ethical hacker performing a penetration test without written authorization could be prosecuted under the CFAA (or local equivalent).', correct: 'true', fb: 'Without authorization, hacking is illegal, regardless of the hacker\'s intent.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Under PCI DSS, which requirement dictates that vendor-supplied default passwords must be changed?', opts: ['Requirement 1', 'Requirement 2', 'Requirement 8', 'Requirement 11'], correct: 1, fb: 'Requirement 2 historically and in v4.0 explicitly focuses on not using vendor-supplied defaults for system passwords and other security parameters.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the purpose of a gap assessment in the context of compliance?', opts: ['To find network vulnerabilities', 'To compare current security controls against the requirements of a regulation or standard', 'To calculate the monetary value of a data breach', 'To test employee awareness through phishing'], correct: 1, fb: 'A gap assessment identifies what is missing between the current state and the required compliant state.' }
  ],
  flashcards: [
    { f: 'HIPAA', b: 'US law governing the protection of Protected Health Information (PHI).' },
    { f: 'PCI DSS', b: 'Payment Card Industry Data Security Standard - applies to cardholder data.' },
    { f: 'GDPR', b: 'General Data Protection Regulation - strict EU privacy law with global reach.' },
    { f: 'CFAA', b: 'Computer Fraud and Abuse Act - the primary US federal anti-hacking law.' },
    { f: 'ISO 27001', b: 'An international standard detailing requirements for an Information Security Management System (ISMS).' },
    { f: 'SOC 2', b: 'An auditing procedure ensuring service providers securely manage data based on Trust Service Criteria.' },
    { f: 'NIST CSF', b: 'Cybersecurity Framework providing a policy framework of computer security guidance.' },
    { f: 'Compliance', b: 'The state of meeting the rules and regulations defined by law or industry standards.' },
    { f: 'Gap Assessment', b: 'An evaluation of current security controls against required regulatory standards.' },
    { f: 'PII', b: 'Personally Identifiable Information - data that can be used to identify a specific individual.' }
  ],
  summary: [
    'Cybersecurity is heavily influenced by legal and regulatory compliance requirements.',
    'Laws like GDPR and HIPAA protect consumer privacy and mandate security controls.',
    'Industry standards like PCI DSS regulate specific types of data (credit cards).',
    'Frameworks like ISO 27001 and NIST help organizations map technical controls to compliance requirements.',
    'Non-compliance can result in severe financial penalties and loss of business operations.'
  ],
  outcomes: [
    'Identify the scope and applicability of major regulations (GDPR, HIPAA, PCI DSS).',
    'Understand the legal implications of unauthorized hacking (CFAA).',
    'Map enterprise technical controls to regulatory requirements.',
    'Explain the importance of Governance, Risk, and Compliance (GRC) in an enterprise.'
  ]
};
"""

try:
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    marker1 = "// ═══════════════════════════════════════════════════════════"
    marker2 = "const CONTENT = {};"
    
    if marker1 in content:
        # Find the first occurrence and replace it with itself + payload
        new_content = content.replace(marker1, marker1 + "\n" + PAYLOAD, 1)
        print("Injected after marker1.")
    elif marker2 in content:
        new_content = content.replace(marker2, marker2 + "\n" + PAYLOAD, 1)
        print("Injected after marker2.")
    else:
        print("Could not find a suitable marker to inject the content.")
        exit(1)
        
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Successfully injected 6 topics into {html_path}")
    
except Exception as e:
    print(f"Error: {e}")
