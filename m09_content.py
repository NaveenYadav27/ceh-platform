import os
import re

CONTENT_JS = r"""
CONTENT['social-engineering-concepts'] = {
  eyebrow: 'Module 09 · Topic 1',
  title: 'Social Engineering Concepts',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Understanding the psychology of persuasion, elicitation, and human manipulation.',
  objectives: ['Understand Cialdini\'s principles of persuasion', 'Identify elicitation techniques used by attackers', 'Explain the psychology behind social engineering attacks'],
  learn: {
    simple: 'Social engineering is the art of manipulating people so they give up confidential information. The types of information these criminals are seeking can vary, but when individuals are targeted the criminals are usually trying to trick you into giving them your passwords or bank information, or access your computer to secretly install malicious software—that will give them access to your passwords and bank information as well as giving them control over your computer.\n\nAttackers use social engineering tactics because it is usually easier to exploit your natural inclination to trust than it is to discover ways to hack your software. For example, it is much easier to fool someone into giving you their password than it is for you to try hacking their password.',
    analogy: 'Imagine a bank vault with an impenetrable steel door and state-of-the-art alarms. A hacker trying to break in is like a burglar trying to drill through the steel. A social engineer, however, just walks up to a security guard, pretends to be a maintenance worker with a clipboard, and asks the guard to hold the door open for them.',
    architecture: 'Social engineering attacks typically follow a life cycle consisting of four phases: Information Gathering (footprinting the target), Relationship Development (establishing trust or creating a pretext), Exploitation (extracting information or gaining access), and Execution (achieving the objective and exiting).\n\nKey psychological principles (Cialdini\'s six principles of influence) are heavily leveraged: Reciprocity (people return favors), Commitment and Consistency (people honor their previous commitments), Social Proof (people do what others do), Authority (people obey authority figures), Liking (people are persuaded by those they like), and Scarcity (perceived scarcity generates demand).\n\nElicitation is a subtle technique where the attacker engages the target in normal conversation to extract information without the target realizing they are being interrogated. Techniques include using false statements to prompt a correction, flattery, or feigning ignorance to encourage the target to "educate" the attacker.',
    why: 'In an enterprise environment, the human element is often the weakest link in the security chain. No amount of firewalls, encryption, or intrusion detection systems can prevent a breach if an employee willingly hands over their credentials or executes a malicious payload because they were tricked by a well-crafted social engineering attack.'
  },
  enterprise: {
    gfs: 'An attacker researches Global Financial Services on LinkedIn, identifying new hires in the IT department. The attacker then calls a new IT administrator, impersonating the VP of Engineering, and urgently requests password reset assistance for a critical trading application, citing an ongoing emergency.',
    windows: 'Windows environments are frequently targeted via social engineering to obtain Active Directory credentials, allowing attackers to move laterally across the network and access sensitive file shares or domain controllers.',
    linux: 'While less commonly targeted for end-user phishing, Linux administrators can be socially engineered into running malicious bash scripts or exposing SSH keys under the guise of urgent system updates or critical patches.'
  },
  workflow: [
    'Step 1: Information Gathering - Attackers collect open-source intelligence (OSINT) about the target.',
    'Step 2: Pretexting - A fabricated scenario is created to engage the target.',
    'Step 3: Engagement - The attacker contacts the target using the pretext.',
    'Step 4: Elicitation - Information is subtly extracted from the target during conversation.',
    'Step 5: Exploitation - The target takes the desired action (e.g., clicking a link, sharing a password).',
    'Step 6: Exit - The attacker gracefully exits the interaction without raising suspicion.'
  ],
  diagram: {
    caption: 'Click to interact with the Social Engineering Attack Lifecycle',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="50" fill="#fff" font-size="20" text-anchor="middle">Social Engineering Lifecycle</text><circle cx="150" cy="150" r="50" fill="#007acc"/><text x="150" y="155" fill="#fff" font-size="12" text-anchor="middle">1. Gather Info</text><path d="M 210 150 L 240 150" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><circle cx="300" cy="150" r="50" fill="#007acc"/><text x="300" y="155" fill="#fff" font-size="12" text-anchor="middle">2. Build Trust</text><path d="M 360 150 L 390 150" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><circle cx="450" cy="150" r="50" fill="#007acc"/><text x="450" y="155" fill="#fff" font-size="12" text-anchor="middle">3. Exploit</text><path d="M 450 210 L 450 240" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><circle cx="450" cy="300" r="50" fill="#007acc"/><text x="450" y="305" fill="#fff" font-size="12" text-anchor="middle">4. Exit</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'maltego', purpose: 'Conduct OSINT gathering on targets', out: 'Visual relationship graphs', note: 'Useful for the Information Gathering phase', mistake: 'Failing to properly scope the target domain' }
    ],
    win: [
      { cmd: 'nltest /domain_trusts', purpose: 'Identify Active Directory trusts', out: 'List of trusted domains', note: 'Helps understand potential targets for lateral movement after a social engineering compromise', mistake: 'Running without domain privileges' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Maltego', 'theHarvester'],
    dependencies: [],
    safety: ['Perform OSINT gathering only on authorized targets or simulated lab domains.'],
    scenario: 'GFS has hired you to assess the publicly available footprint of their executive team to identify potential social engineering risks.',
    objectives: ['Perform OSINT gathering using theHarvester', 'Identify target email addresses and subdomains'],
    steps: [
      'Step 1: Open terminal in Kali Linux.',
      'Step 2: Run `theHarvester -d gfs.local -l 500 -b google` to search for emails.',
      'Step 3: Analyze the output for patterns in email address formats.',
      'Step 4: Use Maltego to visualize relationships between identified personnel.'
    ],
    evidence: ['Terminal output showing discovered email addresses.', 'Maltego graph export.'],
    validation: ['You should see: A list of email addresses associated with the target domain.'],
    troubleshooting: ['If theHarvester fails, check your internet connection and API keys if configured.'],
    mitre: [{ id: 'T1592', name: 'Gather Victim Host Information', tactic: 'Reconnaissance' }],
    cleanup: ['Close Maltego and clear terminal history.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of Cialdini\'s principles of persuasion relies on the target\'s desire to do what others are doing?',
      opts: ['Scarcity', 'Authority', 'Social Proof', 'Reciprocity'],
      correct: 2,
      fb: 'Social Proof is the principle where people look to the actions and behaviors of others to determine their own.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary goal of the "Elicitation" technique in social engineering?',
      opts: ['To infect the target with malware', 'To subtly extract information during normal conversation', 'To create a sense of urgency', 'To bypass physical security controls'],
      correct: 1,
      fb: 'Elicitation involves guiding a conversation to extract information without the target realizing they are being interrogated.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker offers a free IT health check to a company and later asks for sensitive network diagrams. Which principle of persuasion is being used?',
      opts: ['Liking', 'Reciprocity', 'Authority', 'Commitment'],
      correct: 1,
      fb: 'Reciprocity exploits the human tendency to return a favor or feel indebted after receiving something for free.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'The "Scarcity" principle creates a false sense of urgency, pressuring the target to act quickly.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'True. Scarcity implies limited time or resources, rushing the target\'s decision-making process.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which phase of the social engineering lifecycle involves creating a fabricated scenario to engage the target?',
      opts: ['Information Gathering', 'Pretexting / Relationship Development', 'Exploitation', 'Execution'],
      correct: 1,
      fb: 'Pretexting is the act of creating a fabricated scenario to establish trust and engage the target.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which psychological principle is an attacker exploiting when they impersonate a CEO or law enforcement officer?',
      opts: ['Social Proof', 'Liking', 'Authority', 'Consistency'],
      correct: 2,
      fb: 'The Authority principle leverages the natural human tendency to obey or comply with requests from perceived figures of authority.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Elicitation techniques are always aggressive and confrontational to force the target to answer.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Elicitation relies on subtlety, natural conversation, and non-threatening approaches to lower the target\'s guard.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'A social engineer intentionally makes a false statement, hoping the target will correct them and reveal sensitive info. What is this technique called?',
      opts: ['Flattery', 'False statement / Deliberate false statement', 'Feigned ignorance', 'Mirroring'],
      correct: 1,
      fb: 'Using a deliberate false statement prompts the natural human urge to correct mistakes, often leading to the disclosure of accurate, sensitive information.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why is social engineering often considered more dangerous than technical hacking?',
      opts: ['It requires expensive zero-day exploits', 'It bypasses technical security controls by exploiting human psychology', 'It only targets legacy systems', 'It is fully automated and requires no human interaction'],
      correct: 1,
      fb: 'Social engineering targets the human element, which can often bypass complex technical controls like firewalls and encryption.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker asks a target for a small, seemingly harmless favor. Later, they ask for a larger, more sensitive favor. Which principle is this?',
      opts: ['Commitment and Consistency', 'Scarcity', 'Social Proof', 'Authority'],
      correct: 0,
      fb: 'Commitment and Consistency relies on the fact that once people commit to a small action, they are more likely to agree to subsequent, larger requests to remain consistent in their behavior.'
    }
  ],
  flashcards: [
    { f: 'Elicitation', b: 'The subtle extraction of information during a seemingly normal conversation.' },
    { f: 'Pretexting', b: 'Creating a fabricated scenario to engage a target and establish trust.' },
    { f: 'Reciprocity', b: 'A psychological principle where people feel obligated to return a favor.' },
    { f: 'Authority Principle', b: 'Exploiting the human tendency to obey figures of perceived power or authority.' },
    { f: 'Social Proof', b: 'A psychological phenomenon where people assume the actions of others in an attempt to reflect correct behavior.' }
  ],
  summary: [
    'Social engineering manipulates human psychology to bypass technical security controls.',
    'The lifecycle includes Information Gathering, Relationship Development, Exploitation, and Execution.',
    'Cialdini\'s six principles of persuasion (Authority, Reciprocity, Scarcity, etc.) are commonly exploited.',
    'Elicitation is a subtle way to extract information without direct interrogation.',
    'Defending against social engineering requires robust security awareness training for all employees.'
  ],
  outcomes: [
    'Explain the core concepts and psychology behind social engineering.',
    'Identify Cialdini\'s six principles of persuasion in real-world scenarios.',
    'Describe the phases of a social engineering attack lifecycle.',
    'Recognize common elicitation techniques.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Basic understanding of cybersecurity principles'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['phishing-campaigns'] = {
  eyebrow: 'Module 09 · Topic 2',
  title: 'Phishing Campaigns & Variants',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Exploring spear-phishing, whaling, vishing, smishing, and clone phishing.',
  objectives: ['Differentiate between various types of phishing attacks', 'Understand how to set up and analyze a phishing campaign', 'Identify indicators of a phishing attempt'],
  learn: {
    simple: 'Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message. The recipient is then tricked into clicking a malicious link, which can lead to the installation of malware, the freezing of the system as part of a ransomware attack, or the revealing of sensitive information.',
    analogy: 'Phishing is like casting a wide net into the ocean hoping to catch any fish (sending thousands of generic emails). Spear-phishing is like using a specialized spear to hunt a specific type of fish (targeting a specific individual or organization). Whaling is like hunting for Moby Dick (targeting a high-profile executive like a CEO).',
    architecture: 'Phishing campaigns require infrastructure, typically consisting of registered look-alike domains (typosquatting), spoofed email headers, and a payload delivery mechanism (such as a credential harvesting login page or a malicious document attachment).\n\nSpear-phishing uses gathered OSINT to highly personalize the attack, increasing success rates. Whaling targets C-level executives who hold significant authority and access. Vishing (Voice Phishing) uses phone calls, often combined with caller ID spoofing and deepfake audio. Smishing (SMS Phishing) leverages text messages, exploiting the higher trust and click rates associated with mobile devices.\n\nClone phishing involves taking a legitimate, previously delivered email containing an attachment or link, and replacing it with a malicious version, then sending it from a spoofed address claiming it is an "updated" version.',
    why: 'Phishing remains the most common initial access vector for ransomware and data breaches in enterprise environments. Understanding the mechanics of these campaigns is critical for developing effective email filtering rules and training employees to recognize sophisticated lures.'
  },
  enterprise: {
    gfs: 'GFS employees receive an SMS message claiming to be from the IT Helpdesk, warning that their multi-factor authentication (MFA) token has expired and providing a link to a fake login portal designed to steal their credentials.',
    windows: 'Windows environments must utilize advanced threat protection features in Exchange/O365, such as Safe Links and Safe Attachments, to detect and neutralize sophisticated phishing payloads before they reach the user.',
    linux: 'Security analysts use Linux-based tools like GoPhish to simulate phishing campaigns against the organization, identifying susceptible user groups and measuring the effectiveness of security awareness training.'
  },
  workflow: [
    'Step 1: Domain Registration - Register a look-alike domain (e.g., gfs-portal.com instead of gfs.com).',
    'Step 2: Infrastructure Setup - Configure mail servers, SPF/DKIM records, and landing pages.',
    'Step 3: Target Selection - Identify specific targets (Spear-phishing) or acquire a large email list.',
    'Step 4: Lure Creation - Craft a compelling email, SMS, or voice script based on a credible pretext.',
    'Step 5: Delivery - Send the phishing messages to the targets.',
    'Step 6: Harvesting - Collect credentials or execute payloads when targets interact with the lure.'
  ],
  diagram: {
    caption: 'Click to interact with the Phishing Attack Vectors diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="50" fill="#fff" font-size="20" text-anchor="middle">Phishing Attack Vectors</text><rect x="50" y="100" width="120" height="60" rx="10" fill="#d9534f"/><text x="110" y="135" fill="#fff" font-size="14" text-anchor="middle">Phishing (Email)</text><rect x="240" y="100" width="120" height="60" rx="10" fill="#f0ad4e"/><text x="300" y="135" fill="#fff" font-size="14" text-anchor="middle">Vishing (Voice)</text><rect x="430" y="100" width="120" height="60" rx="10" fill="#5cb85c"/><text x="490" y="135" fill="#fff" font-size="14" text-anchor="middle">Smishing (SMS)</text><rect x="240" y="250" width="120" height="60" rx="10" fill="#0275d8"/><text x="300" y="285" fill="#fff" font-size="14" text-anchor="middle">Target Victim</text><path d="M 110 160 L 240 250" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><path d="M 300 160 L 300 250" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><path d="M 490 160 L 360 250" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/></svg>'
  },
  commands: {
    lin: [
      { cmd: 'setoolkit', purpose: 'Launch Social-Engineer Toolkit', out: 'SET Menu', note: 'Automates phishing and payload generation', mistake: 'Running outside an authorized campaign' },
      { cmd: 'gophish', purpose: 'Launch GoPhish framework', out: 'Web UI started', note: 'Used for managing large-scale simulated phishing campaigns', mistake: 'Exposing the admin interface to the public internet' }
    ],
    win: [
      { cmd: 'Get-MessageTrace', purpose: 'Trace phishing emails in Exchange/O365', out: 'Email routing logs', note: 'Crucial for incident response to phishing', mistake: 'Searching without specific sender/recipient filters' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['SET', 'Gophish'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment against authorized targets.'],
    scenario: 'You are tasked with demonstrating the risk of credential harvesting to GFS management by creating a simulated phishing campaign using the Social-Engineer Toolkit (SET).',
    objectives: ['Clone a legitimate website login page using SET', 'Harvest credentials submitted to the cloned page'],
    steps: [
      'Step 1: Open terminal in Kali Linux and type `setoolkit`.',
      'Step 2: Select [1] Social-Engineering Attacks.',
      'Step 3: Select [2] Website Attack Vectors.',
      'Step 4: Select [3] Credential Harvester Attack Method.',
      'Step 5: Select [2] Site Cloner and input the URL of a test portal (e.g., a local lab web server).',
      'Step 6: Access your Kali machine\'s IP from a victim VM and enter test credentials.',
      'Step 7: View the harvested credentials in the SET terminal.'
    ],
    evidence: ['Terminal output from SET showing the cloned site and captured credentials.'],
    validation: ['You should see: "POSSIBLE USERNAME FIELD FOUND" followed by the entered credentials in plain text.'],
    troubleshooting: ['If the site fails to clone, ensure Apache is not already running on port 80 (`systemctl stop apache2`).'],
    mitre: [{ id: 'T1566', name: 'Phishing', tactic: 'Initial Access' }],
    cleanup: ['Exit SET (Ctrl+C) to stop the credential harvesting server.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which type of phishing attack specifically targets high-profile individuals, such as CEOs or CFOs?',
      opts: ['Spear-phishing', 'Smishing', 'Whaling', 'Vishing'],
      correct: 2,
      fb: 'Whaling is a highly targeted phishing attack aimed at senior executives (the "whales") who have significant access to sensitive data and funds.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker sends a fraudulent SMS message containing a malicious link. What is this attack called?',
      opts: ['Vishing', 'Smishing', 'Spear-phishing', 'Clone phishing'],
      correct: 1,
      fb: 'Smishing (SMS Phishing) uses text messages as the primary delivery vector.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'How does spear-phishing differ from traditional phishing?',
      opts: ['Spear-phishing uses voice calls', 'Spear-phishing targets specific individuals or organizations using customized information', 'Spear-phishing is always automated and random', 'Spear-phishing only targets mobile devices'],
      correct: 1,
      fb: 'Spear-phishing is highly targeted and relies on OSINT to personalize the message for a specific victim, making it much more convincing.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Vishing involves using voice communication, such as telephone calls, to deceive victims.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'True. Vishing stands for Voice Phishing.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker intercepts a legitimate email, modifies the attachment to include malware, and resends it from a spoofed address. What is this called?',
      opts: ['Whaling', 'Clone phishing', 'Smishing', 'Typosquatting'],
      correct: 1,
      fb: 'Clone phishing involves copying a legitimate, previously delivered email and replacing links or attachments with malicious versions.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which tool is commonly used in Kali Linux to easily clone websites for credential harvesting?',
      opts: ['Nmap', 'Metasploit', 'Social-Engineer Toolkit (SET)', 'Wireshark'],
      correct: 2,
      fb: 'SET includes a Credential Harvester Attack Method that easily clones websites and hosts them to capture submitted credentials.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which DNS records are crucial for validating email senders and mitigating domain spoofing in phishing attacks?',
      opts: ['A and AAAA', 'SPF, DKIM, and DMARC', 'CNAME and PTR', 'NS and SOA'],
      correct: 1,
      fb: 'Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and DMARC help verify the sender\'s identity and prevent spoofing.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Phishing campaigns only aim to steal credentials; they are never used to distribute malware or ransomware.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Phishing is a primary vector for delivering malware, including ransomware, often via malicious attachments or links.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the purpose of typosquatting in a phishing campaign?',
      opts: ['To crash the victim\'s mail server', 'To register domains that look visually similar to legitimate domains (e.g., paypa1.com)', 'To bypass spam filters using encryption', 'To intercept SMS messages'],
      correct: 1,
      fb: 'Typosquatting relies on users making typographical errors or failing to notice slight variations in a domain name.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is a common indicator of a phishing email?',
      opts: ['Use of a legitimate corporate signature', 'Proper spelling and grammar', 'Generic greetings (e.g., "Dear Customer") and a sense of extreme urgency', 'The email comes from an internal, verified domain'],
      correct: 2,
      fb: 'Phishing emails often use generic greetings because they are sent in bulk, and rely on urgency to force the user to act before thinking.'
    }
  ],
  flashcards: [
    { f: 'Spear-Phishing', b: 'A highly targeted phishing attack aimed at specific individuals or organizations.' },
    { f: 'Whaling', b: 'A form of spear-phishing that specifically targets high-profile executives.' },
    { f: 'Smishing', b: 'Phishing attacks conducted via SMS or text messages.' },
    { f: 'Vishing', b: 'Voice phishing; using telephone calls to deceive targets.' },
    { f: 'Clone Phishing', b: 'Copying a legitimate email and replacing its contents with malicious links or attachments.' }
  ],
  summary: [
    'Phishing is a broad term for deceptive communications designed to steal data or install malware.',
    'Spear-phishing and whaling are targeted variants that yield higher success rates.',
    'Vishing and smishing utilize voice and SMS channels, bypassing traditional email security controls.',
    'Clone phishing leverages trust in previously legitimate email threads.',
    'Effective defense requires technical controls (SPF/DKIM/DMARC) combined with user awareness training.'
  ],
  outcomes: [
    'Differentiate between phishing, spear-phishing, whaling, vishing, and smishing.',
    'Understand the infrastructure required to launch a phishing campaign.',
    'Identify common indicators of phishing attempts.',
    'Demonstrate the ability to clone a site for credential harvesting in a lab environment.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Basic understanding of email protocols (SMTP)'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['insider-threats'] = {
  eyebrow: 'Module 09 · Topic 3',
  title: 'Insider Threats & Indicators',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Analyzing malicious vs negligent insiders and recognizing indicators of compromise.',
  objectives: ['Differentiate between types of insider threats', 'Identify behavioral and technical indicators of insider threats', 'Understand strategies for mitigating insider risks'],
  learn: {
    simple: 'An insider threat is a security risk that originates from within the targeted organization. It involves a current or former employee, contractor, or business partner who has inside information concerning the organization\'s security practices, data, and computer systems. The threat can involve fraud, the theft of confidential or commercially valuable information, the theft of intellectual property, or the sabotage of computer systems.',
    analogy: 'Defending against external threats is like building a strong wall around a castle. However, an insider threat is like having a knight already inside the castle walls who decides to open the gates for the enemy or set fire to the keep. The wall cannot stop them because they already have the keys.',
    architecture: 'Insider threats are generally categorized into three types: Malicious Insiders (intentional harm, often motivated by financial gain, revenge, or espionage), Negligent Insiders (careless employees who unintentionally cause breaches through poor security hygiene, such as falling for phishing or mishandling data), and Compromised Insiders (legitimate accounts taken over by external attackers).\n\nDetecting insider threats requires User and Entity Behavior Analytics (UEBA). UEBA establishes a baseline of normal behavior for each user and entity on the network. When a user deviates from their baseline (e.g., logging in at unusual hours, downloading massive amounts of data, accessing files unrelated to their role), the system flags the anomalous activity.\n\nTechnical indicators include unusual privilege escalation, use of unauthorized software (shadow IT), and data exfiltration patterns. Behavioral indicators include expressions of extreme dissatisfaction, sudden changes in financial status, or conflicts with coworkers.',
    why: 'Insider threats are among the most difficult to detect and prevent because the attacker already has legitimate access to systems and data. In an enterprise, a single malicious insider can bypass multi-million dollar perimeter defenses and cause catastrophic damage to the business.'
  },
  enterprise: {
    gfs: 'A senior developer at Global Financial Services, recently passed over for a promotion, begins quietly copying proprietary algorithmic trading code to a personal USB drive before their planned resignation.',
    windows: 'In Windows environments, insider threats are mitigated by implementing the Principle of Least Privilege (PoLP) via Active Directory group policies and utilizing tools like Microsoft Defender for Endpoint to monitor unusual file access patterns.',
    linux: 'Linux systems monitor insider activity through auditd and centralized syslogging, tracking commands executed by privileged users (sudoers) and alerting on unauthorized access to sensitive configuration files like /etc/shadow.'
  },
  workflow: [
    'Step 1: Baseline Establishment - Use UEBA to determine normal user behavior patterns.',
    'Step 2: Access Control - Implement the Principle of Least Privilege and Role-Based Access Control (RBAC).',
    'Step 3: Monitoring - Continuously monitor for behavioral anomalies (e.g., large data transfers).',
    'Step 4: Alerting - Generate alerts when a user significantly deviates from their baseline.',
    'Step 5: Investigation - Security analysts review the alerts and context (e.g., HR records regarding termination).',
    'Step 6: Mitigation - Revoke access and involve HR/Legal if malicious activity is confirmed.'
  ],
  diagram: {
    caption: 'Click to interact with the Insider Threat Matrix',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="40" fill="#fff" font-size="20" text-anchor="middle">Types of Insider Threats</text><circle cx="150" cy="200" r="80" fill="#d9534f" opacity="0.8"/><text x="150" y="195" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Malicious</text><text x="150" y="215" fill="#fff" font-size="12" text-anchor="middle">Intentional Harm</text><circle cx="300" cy="200" r="80" fill="#f0ad4e" opacity="0.8"/><text x="300" y="195" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Negligent</text><text x="300" y="215" fill="#fff" font-size="12" text-anchor="middle">Careless Mistakes</text><circle cx="450" cy="200" r="80" fill="#5cb85c" opacity="0.8"/><text x="450" y="195" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Compromised</text><text x="450" y="215" fill="#fff" font-size="12" text-anchor="middle">Account Takeover</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'aureport -x', purpose: 'Generate a summary of executable events from audit logs', out: 'Auditd executable report', note: 'Helps identify unusual commands run by insiders', mistake: 'Failing to configure auditd rules properly' }
    ],
    win: [
      { cmd: 'Get-WinEvent -LogName Security | Where-Object {$_.Id -eq 4624}', purpose: 'View successful logon events', out: 'List of logon events', note: 'Useful for detecting off-hours access', mistake: 'Running without administrative privileges' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['auditd', 'Splunk (or basic grep)'],
    dependencies: [],
    safety: ['Perform monitoring on authorized systems only.'],
    scenario: 'You suspect an employee is accessing sensitive HR files outside of their normal duties. You must review Linux audit logs to confirm their actions.',
    objectives: ['Configure auditd to monitor a specific directory', 'Identify unauthorized access in the logs'],
    steps: [
      'Step 1: Open terminal in Linux.',
      'Step 2: Add an audit rule for the sensitive directory: `auditctl -w /opt/hr_data -p warx -k hr_monitor`.',
      'Step 3: Simulate an insider by reading a file in that directory: `cat /opt/hr_data/salaries.txt`.',
      'Step 4: Search the audit logs for the key: `ausearch -k hr_monitor`.',
      'Step 5: Review the output to identify the user ID (uid) and command (exe) used.'
    ],
    evidence: ['Terminal output showing the auditctl configuration.', 'Output from ausearch detailing the file access event.'],
    validation: ['You should see: An audit record detailing the uid of the user who accessed the file and the timestamp.'],
    troubleshooting: ['If auditctl returns an error, ensure the auditd service is running (`systemctl status auditd`).'],
    mitre: [{ id: 'T1078', name: 'Valid Accounts', tactic: 'Defense Evasion, Persistence, Privilege Escalation, Initial Access' }],
    cleanup: ['Remove the audit rule: `auditctl -W /opt/hr_data -p warx -k hr_monitor`.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following best describes a negligent insider?',
      opts: ['An employee who steals data to sell to a competitor', 'An employee who accidentally emails sensitive data to the wrong recipient', 'An external hacker who compromises an employee\'s account', 'A former employee who leaves a logic bomb in the network'],
      correct: 1,
      fb: 'Negligent insiders cause harm through carelessness or ignorance of security policies, not through malicious intent.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'A disgruntled employee downloads a large volume of intellectual property shortly before resigning. What type of threat is this?',
      opts: ['Negligent Insider', 'Compromised Insider', 'Malicious Insider', 'External Threat'],
      correct: 2,
      fb: 'Malicious insiders intentionally harm the organization, often for financial gain, revenge, or corporate espionage.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What technology is primarily used to detect anomalous behavior by analyzing patterns in user activity?',
      opts: ['Firewall', 'User and Entity Behavior Analytics (UEBA)', 'Antivirus', 'Intrusion Prevention System (IPS)'],
      correct: 1,
      fb: 'UEBA establishes a baseline of normal behavior and alerts on deviations, making it effective for spotting insider threats.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Insider threats are generally easier to detect than external threats because the attackers use known methods.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Insider threats are harder to detect because the attacker already possesses legitimate credentials and access to the network.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is a behavioral indicator of a potential malicious insider?',
      opts: ['Logging in during normal business hours', 'Frequently working late hours or accessing systems remotely at odd times', 'Updating passwords regularly', 'Attending security awareness training'],
      correct: 1,
      fb: 'Unusual access patterns, such as working odd hours without authorization, can indicate an insider attempting to operate unnoticed.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What principle is most effective at limiting the damage an insider can cause?',
      opts: ['Security by Obscurity', 'Principle of Least Privilege (PoLP)', 'Defense in Depth', 'Open Design'],
      correct: 1,
      fb: 'The Principle of Least Privilege ensures users only have the minimum access necessary to perform their jobs, limiting what an insider can steal or damage.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'A compromised insider is an employee who willingly sells their credentials to an external attacker.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. A compromised insider refers to an innocent employee whose account has been taken over by an external attacker (e.g., via phishing). An employee selling credentials is a malicious insider.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which technical indicator might suggest data exfiltration by an insider?',
      opts: ['A sudden spike in outbound network traffic to a personal cloud storage site', 'Frequent password resets', 'High CPU utilization on a domain controller', 'Multiple failed login attempts'],
      correct: 0,
      fb: 'Large outbound data transfers, especially to unauthorized external storage, strongly indicate potential data theft.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why should HR and IT collaborate closely regarding insider threats?',
      opts: ['To ensure employees have fast computers', 'Because HR holds the encryption keys', 'To ensure immediate access revocation during terminations or hostile departures', 'To manage the corporate firewall'],
      correct: 2,
      fb: 'Promptly revoking access during offboarding is critical to preventing departing employees from becoming malicious insiders.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In Linux, what service is commonly used to track detailed user access to specific files and directories?',
      opts: ['iptables', 'auditd', 'cron', 'systemd'],
      correct: 1,
      fb: 'The audit daemon (auditd) allows administrators to create rules that log detailed information about file access and command execution.'
    }
  ],
  flashcards: [
    { f: 'Malicious Insider', b: 'An individual who intentionally exploits their legitimate access to harm the organization.' },
    { f: 'Negligent Insider', b: 'An individual who accidentally exposes the organization to risk through carelessness.' },
    { f: 'Compromised Insider', b: 'An employee whose credentials have been stolen by an external attacker.' },
    { f: 'UEBA', b: 'User and Entity Behavior Analytics; uses machine learning to detect anomalous user activity.' },
    { f: 'Principle of Least Privilege', b: 'Granting users only the minimum access rights necessary to perform their jobs.' }
  ],
  summary: [
    'Insider threats fall into three categories: Malicious, Negligent, and Compromised.',
    'They are difficult to detect because the threat actor has legitimate access.',
    'Behavioral indicators include odd working hours, sudden financial changes, or expressing extreme grievances.',
    'Technical indicators include unusual data access, large outbound transfers, and privilege escalation.',
    'Mitigation relies on the Principle of Least Privilege, UEBA, and tight integration between HR and IT for offboarding.'
  ],
  outcomes: [
    'Differentiate between malicious, negligent, and compromised insiders.',
    'Recognize common behavioral and technical indicators of compromise.',
    'Understand how UEBA is used to establish baselines and detect anomalies.',
    'Configure basic audit logging in Linux to monitor sensitive files.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Understanding of access control models'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['impersonation'] = {
  eyebrow: 'Module 09 · Topic 4',
  title: 'Impersonation & Physical Social Engineering',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Mastering pretexting, tailgating, dumpster diving, and shoulder surfing.',
  objectives: ['Identify physical social engineering techniques', 'Understand the mechanics of pretexting and impersonation', 'Implement physical security controls against social engineering'],
  learn: {
    simple: 'Impersonation occurs when a social engineer pretends to be someone else to gain trust or access. This can happen over the phone, via email, or in person. Physical social engineering involves exploiting human behavior to bypass physical security barriers, such as doors and locked cabinets. Common techniques include following someone through a secure door (tailgating), looking over someone\'s shoulder to steal passwords (shoulder surfing), or searching through trash for sensitive documents (dumpster diving).',
    analogy: 'Tailgating is like holding the door open for someone carrying heavy boxes; your politeness overrides your security awareness. Dumpster diving is like trying to reconstruct a shredded puzzle to see the full picture of an organization\'s secrets.',
    architecture: 'Pretexting is the foundation of impersonation. It involves creating a highly detailed, fabricated scenario (the pretext) that justifies the attacker\'s presence or request. The attacker must adopt the persona completely, including terminology, authority level, and demeanor.\n\nPhysical exploitation leverages natural human politeness. Tailgating (or piggybacking) involves an attacker closely following an authorized employee into a restricted area. The difference is that in piggybacking, the employee knows the person is following and allows it (often out of politeness), whereas in tailgating, the employee may be unaware.\n\nDumpster diving exploits the failure to properly destroy sensitive information. Attackers look for organizational charts, memos, passwords written on sticky notes, and hardware like old hard drives. Shoulder surfing requires direct observation, often aided by binoculars or hidden cameras, to capture credentials entered on keyboards or keypads.',
    why: 'An enterprise can have perfect digital security, but if an attacker can physically walk into the server room by wearing a fake maintenance uniform and holding a clipboard, all digital defenses are bypassed. Physical security is the foundation of all cybersecurity.'
  },
  enterprise: {
    gfs: 'An attacker wearing an internet service provider uniform arrives at a Global Financial Services branch office, claiming they need to check the main distribution frame. Due to a busy schedule, the receptionist allows them into the server room without verifying their work order.',
    windows: 'To combat shoulder surfing in Windows environments, GFS enforces screen timeouts and requires employees to lock their workstations (Win+L) immediately when stepping away from their desks.',
    linux: 'Physical access to a Linux terminal can allow an attacker to reboot the system into single-user mode, granting root access without a password, highlighting the critical need to secure physical hardware.'
  },
  workflow: [
    'Step 1: Reconnaissance - Observe physical security controls (cameras, guards, badge readers).',
    'Step 2: Pretext Development - Create a believable persona (e.g., delivery driver, IT auditor).',
    'Step 3: Props and Costuming - Acquire necessary uniforms, fake badges, or clipboards.',
    'Step 4: Execution (Tailgating/Impersonation) - Approach the target facility and bypass the perimeter.',
    'Step 5: Objective Achievement - Plant a rogue device, steal documents, or access an unlocked terminal.',
    'Step 6: Egress - Leave the facility confidently without drawing attention.'
  ],
  diagram: {
    caption: 'Click to interact with Physical Social Engineering Threats',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="50" fill="#fff" font-size="20" text-anchor="middle">Physical Security Exploits</text><rect x="50" y="100" width="150" height="80" rx="10" fill="#007acc"/><text x="125" y="135" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Tailgating</text><text x="125" y="155" fill="#fff" font-size="12" text-anchor="middle">Following authorized personnel</text><rect x="225" y="100" width="150" height="80" rx="10" fill="#007acc"/><text x="300" y="135" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Dumpster Diving</text><text x="300" y="155" fill="#fff" font-size="12" text-anchor="middle">Scavenging trashed data</text><rect x="400" y="100" width="150" height="80" rx="10" fill="#007acc"/><text x="475" y="135" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Shoulder Surfing</text><text x="475" y="155" fill="#fff" font-size="12" text-anchor="middle">Direct observation</text><rect x="225" y="250" width="150" height="80" rx="10" fill="#d9534f"/><text x="300" y="285" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Impersonation</text><text x="300" y="305" fill="#fff" font-size="12" text-anchor="middle">Using a Pretext (Uniform/Badge)</text><path d="M 300 250 L 300 180" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/></svg>'
  },
  commands: {
    lin: [
      { cmd: 'macchanger', purpose: 'Spoof MAC address', out: 'New MAC assigned', note: 'Useful if attempting to bypass physical network port security (NAC) after gaining entry', mistake: 'Spoofing a MAC address that is currently active on the network' }
    ],
    win: [
      { cmd: 'rundll32.exe user32.dll,LockWorkStation', purpose: 'Lock the Windows session', out: 'Session locked', note: 'Essential command to mitigate physical access threats when leaving a desk', mistake: 'Relying solely on a long timeout period instead of manual locking' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['macchanger'],
    dependencies: [],
    safety: ['Only alter MAC addresses on networks you have permission to test.'],
    scenario: 'During a physical penetration test at GFS, you have successfully tailgated into an office area. You find an open ethernet port, but Network Access Control (NAC) restricts access to known MAC addresses. You must spoof a known printer\'s MAC address to gain network access.',
    objectives: ['Identify your current MAC address', 'Use macchanger to spoof a specific MAC address'],
    steps: [
      'Step 1: Open terminal in Kali Linux.',
      'Step 2: Check current MAC address: `ip link show eth0`.',
      'Step 3: Bring the interface down: `sudo ip link set eth0 down`.',
      'Step 4: Spoof the MAC address of the target printer (e.g., 00:11:22:33:44:55): `sudo macchanger -m 00:11:22:33:44:55 eth0`.',
      'Step 5: Bring the interface up: `sudo ip link set eth0 up`.',
      'Step 6: Verify the change: `ip link show eth0`.'
    ],
    evidence: ['Terminal output showing the original MAC and the new spoofed MAC.'],
    validation: ['You should see: "New MAC: 00:11:22:33:44:55" in the macchanger output.'],
    troubleshooting: ['If the interface fails to come up, restart NetworkManager (`sudo systemctl restart NetworkManager`).'],
    mitre: [{ id: 'T1562.001', name: 'Disable or Modify Tools', tactic: 'Defense Evasion' }],
    cleanup: ['Restore original MAC: `sudo macchanger -p eth0` and bring interface up.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker wearing a delivery uniform closely follows an employee through a secure badge-access door without swiping their own badge. What is this technique called?',
      opts: ['Dumpster Diving', 'Tailgating', 'Shoulder Surfing', 'Phishing'],
      correct: 1,
      fb: 'Tailgating (or piggybacking) involves following an authorized person into a restricted area to bypass physical security controls.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which physical security control is specifically designed to prevent tailgating?',
      opts: ['CCTV Cameras', 'Mantrap', 'Shredders', 'Biometric Scanners'],
      correct: 1,
      fb: 'A mantrap is a small space with two sets of interlocking doors, designed so that only one person can pass through at a time, preventing tailgating.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary objective of dumpster diving in social engineering?',
      opts: ['To install malware on discarded hard drives', 'To recover sensitive information such as organizational charts, passwords, or memos', 'To physically destroy the company\'s trash compactors', 'To bypass firewall rules'],
      correct: 1,
      fb: 'Dumpster diving is a reconnaissance technique used to gather discarded but sensitive information that can aid in further attacks.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Shoulder surfing only occurs in physical proximity and cannot be done remotely.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Shoulder surfing can be done from a distance using binoculars, high-resolution cameras, or CCTV feeds.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a "pretext" in the context of impersonation?',
      opts: ['The malicious payload delivered via USB', 'A fabricated scenario or persona created to gain trust and extract information', 'The physical badge used to clone access', 'The process of locking a workstation'],
      correct: 1,
      fb: 'Pretexting is the act of creating an invented scenario to engage a targeted victim in a manner that increases the chance they will divulge information.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'How can an organization best defend against dumpster diving?',
      opts: ['Installing mantraps', 'Enforcing screen locks', 'Implementing a strict shredding policy for all printed documents', 'Using MAC address filtering'],
      correct: 2,
      fb: 'A strict shredding policy (using cross-cut shredders) ensures that sensitive documents cannot be reconstructed if retrieved from the trash.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker looks over an employee\'s shoulder while they type their password at a coffee shop. What is this called?',
      opts: ['Elicitation', 'Tailgating', 'Shoulder Surfing', 'Pretexting'],
      correct: 2,
      fb: 'Shoulder surfing is the direct observation of a target entering sensitive information.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Impersonation attacks only happen in person.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Impersonation can occur via email (CEO fraud), over the phone (vishing), or in person.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why might an attacker use the `macchanger` tool after gaining physical access to an office?',
      opts: ['To decrypt a hard drive', 'To bypass Network Access Control (NAC) by spoofing an authorized device\'s MAC address', 'To launch a phishing campaign', 'To lock the user\'s screen'],
      correct: 1,
      fb: 'If a network restricts access based on MAC addresses, an attacker can spoof the MAC of an authorized device (like a printer) to gain connectivity.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is the best defense against tailgating if physical modifications like mantraps are not possible?',
      opts: ['Installing heavier doors', 'Creating a culture where employees are trained and empowered to challenge unbadged individuals', 'Placing security cameras in the break room', 'Requiring complex passwords'],
      correct: 1,
      fb: 'Empowering employees to challenge strangers is the most effective administrative control against tailgating.'
    }
  ],
  flashcards: [
    { f: 'Tailgating', b: 'Following an authorized person into a secure area without authorization.' },
    { f: 'Mantrap', b: 'A physical security control consisting of two interlocking doors to prevent tailgating.' },
    { f: 'Dumpster Diving', b: 'Searching through trash to find sensitive organizational information.' },
    { f: 'Shoulder Surfing', b: 'Directly observing someone entering sensitive information, such as passwords or PINs.' },
    { f: 'MAC Spoofing', b: 'Changing a device\'s Media Access Control address to bypass network access controls.' }
  ],
  summary: [
    'Physical social engineering bypasses digital controls by exploiting human nature and physical vulnerabilities.',
    'Pretexting involves creating a detailed, believable persona to gain trust and access.',
    'Tailgating is a common method for entering secure facilities without a badge.',
    'Dumpster diving yields valuable OSINT if proper document destruction policies are not followed.',
    'Defenses include mantraps, strict shredding policies, privacy screens, and employee empowerment to challenge strangers.'
  ],
  outcomes: [
    'Describe the mechanisms of physical social engineering attacks like tailgating and dumpster diving.',
    'Explain the role of pretexting in successful impersonation.',
    'Identify appropriate physical and administrative controls to mitigate physical security threats.',
    'Demonstrate the ability to bypass basic MAC filtering using macchanger.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Understanding of physical security principles'],
    lastReviewed: '2026-07-18'
  }
};
"""

target_file = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'

try:
    with open(target_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    if '// ── TAB WIRING ──' in html_content:
        # Avoid duplicating if already injected
        if "CONTENT['social-engineering-concepts'] =" in html_content:
            print("Content already seems to be injected.")
        else:
            html_content = html_content.replace('// ── TAB WIRING ──', CONTENT_JS + '\n// ── TAB WIRING ──')
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print("Successfully injected Module 09 content into index.html")
    else:
        print("Error: Could not find '// ── TAB WIRING ──' in the target file.")
except FileNotFoundError:
    print(f"Error: Target file not found at {target_file}")
except Exception as e:
    print(f"An error occurred: {e}")
