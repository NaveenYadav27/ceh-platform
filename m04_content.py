import os

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"

if not os.path.exists(html_path):
    print(f"Error: Could not find {html_path}")
    exit(1)

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

payload = """
CONTENT['enumeration-overview'] = {
  eyebrow: 'Module 04 · Topic 1',
  title: 'Enumeration Overview',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Extracting valuable information from active network connections.',
  objectives: ['Understand Enumeration Concepts', 'Identify Active Connections', 'Extract Useful Data'],
  learn: {
    simple: 'Enumeration is the systematic process of extracting usernames, machine names, network resources, shares, and services from a system. Unlike scanning, which is discovering what ports are open, enumeration involves actively establishing connections to the target to gather detailed information.',
    analogy: 'If scanning is walking through a neighborhood to see which houses have open windows, enumeration is knocking on the door, talking to the inhabitants, and asking for a list of everyone who lives there and what rooms they occupy.',
    architecture: 'In an enterprise environment, enumeration leverages protocols that are designed to share information, such as SMB, SNMP, LDAP, and DNS. Attackers abuse these administrative and management protocols to map out the internal network structure, identify high-value targets, and discover potential vulnerabilities or misconfigurations. The data gathered during enumeration is critical for planning targeted attacks.',
    why: 'Enumeration provides the necessary details to move from a general understanding of the network to planning specific, targeted exploits. It transforms IP addresses and open ports into actionable intelligence.'
  },
  enterprise: {
    gfs: 'At Global Financial Services (GFS), enumerating the internal network could reveal the location of the core banking databases, Active Directory domain controllers, and file shares containing sensitive financial reports.',
    windows: 'In a Windows enterprise, enumeration often targets NetBIOS and SMB to extract user lists, group memberships, and shared folder permissions.',
    linux: 'In a Linux environment, enumeration might focus on NFS exports, SNMP strings, and SSH configurations.'
  },
  workflow: ['Step 1: Identify target systems and open ports from previous scanning phases.', 'Step 2: Determine the services running on those ports (e.g., SMB on 139/445).', 'Step 3: Select appropriate enumeration tools based on the identified services.', 'Step 4: Execute enumeration commands to extract data (users, shares, etc.).', 'Step 5: Document the findings systematically.', 'Step 6: Analyze the gathered information to identify potential attack vectors.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f8f9fa"/><text x="50%" y="50%" font-family="Arial" font-size="24" text-anchor="middle" fill="#333">Enumeration Workflow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'enum4linux -a target', purpose: 'Enumerate SMB', out: 'Users and shares', note: 'Essential for Windows targets', mistake: 'Running without credentials when null sessions are disabled' }
    ],
    win: [
      { cmd: 'net view \\\\target', purpose: 'View shares', out: 'List of shares', note: 'Native alternative', mistake: 'Requires SMB access' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['enum4linux', 'nmap'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'As a security analyst at GFS, you need to map out the publicly accessible services on a newly deployed server.',
    objectives: ['Identify open ports and services.', 'Extract initial system information.'],
    steps: ['Step 1: Run an Nmap scan to identify services.', 'Step 2: Use specific enumeration tools based on Nmap results.'],
    evidence: ['Output showing open ports and services.'],
    validation: ['You should see: detailed service information'],
    troubleshooting: ['If scan fails, check network connectivity.'],
    mitre: [{ id: 'T1087', name: 'Account Discovery', tactic: 'Discovery' }],
    cleanup: ['Remove any temporary files or scan results.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary goal of enumeration?', opts: ['Discovering open ports', 'Extracting detailed system information', 'Exploiting a vulnerability', 'Cracking passwords'], correct: 1, fb: 'Enumeration involves actively connecting to gather detailed info.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is NOT typically a target for enumeration?', opts: ['Usernames', 'Network shares', 'Routing tables', 'Encrypted database contents'], correct: 3, fb: 'Enumeration targets structure and metadata, not typically the raw encrypted contents directly.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does enumeration differ from scanning?', opts: ['Scanning is active, enumeration is passive', 'Enumeration is active, scanning is passive', 'Enumeration gathers more detailed data than scanning', 'There is no difference'], correct: 2, fb: 'Enumeration builds on scanning by gathering more detailed, specific information.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol is often targeted for enumeration in Windows environments?', opts: ['SSH', 'SMB', 'FTP', 'SMTP'], correct: 1, fb: 'SMB is commonly used in Windows for file sharing and is a prime target for enumeration.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: Enumeration always requires valid credentials.', opts: ['True', 'False'], correct: 1, fb: 'Many enumeration techniques (like null sessions) do not require valid credentials.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What kind of information can be gathered using SNMP enumeration?', opts: ['System uptime and interfaces', 'Plaintext passwords', 'Active Directory user hashes', 'SQL database schema'], correct: 0, fb: 'SNMP provides management information like uptime, interfaces, and routing info.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why is enumeration important for a penetration test?', opts: ['It proves the system is vulnerable.', 'It identifies potential attack vectors.', 'It automatically patches systems.', 'It generates the final report.'], correct: 1, fb: 'Enumeration identifies the specific users, shares, and services that can be targeted.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which phase of the ethical hacking methodology comes immediately after enumeration?', opts: ['Reconnaissance', 'Scanning', 'Vulnerability Analysis', 'Covering Tracks'], correct: 2, fb: 'After enumerating targets, you analyze them for vulnerabilities.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a "null session"?', opts: ['An encrypted connection', 'An anonymous connection to an IPC$ share', 'A connection using the Administrator account', 'A dropped connection'], correct: 1, fb: 'A null session is an unauthenticated connection to a Windows IPC$ share.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used for SNMP enumeration?', opts: ['enum4linux', 'snmpwalk', 'nmap', 'netcat'], correct: 1, fb: 'snmpwalk is a standard tool for querying SNMP enabled devices.' }
  ],
  flashcards: [
    { f: 'Enumeration', b: 'The active process of extracting detailed information from a target system.' },
    { f: 'Null Session', b: 'An unauthenticated connection to a Windows system, often used for enumeration.' }
  ],
  summary: ['Enumeration is an active information gathering process.', 'It builds upon the results of network scanning.', 'Targets include users, shares, and services.', 'Commonly enumerated protocols include SMB, SNMP, and LDAP.', 'The gathered data is crucial for identifying attack vectors.'],
  outcomes: ['Explain the purpose of enumeration.', 'Identify key protocols targeted during enumeration.', 'Describe the difference between scanning and enumeration.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['netbios-smb'] = {
  eyebrow: 'Module 04 · Topic 2',
  title: 'NetBIOS and SMB Enumeration',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Targeting Windows file sharing and naming services.',
  objectives: ['Understand NetBIOS and SMB', 'Perform Null Sessions', 'Enumerate Windows Shares'],
  learn: {
    simple: 'NetBIOS and Server Message Block (SMB) are protocols heavily used in Windows environments for file and printer sharing. Enumerating these services can reveal a wealth of information, including user lists, groups, password policies, and shared resources.',
    analogy: 'Enumerating SMB is like checking the directory board in an office building to find out who works where and which meeting rooms are currently open.',
    architecture: 'NetBIOS provides naming services (port 137 UDP), datagram services (port 138 UDP), and session services (port 139 TCP). SMB (often running directly over TCP port 445) is the application-layer network protocol used for shared access to files. Historically, Windows allowed "null sessions" (anonymous connections to the IPC$ share), which attackers use to extract sensitive domain information without authentication.',
    why: 'In enterprise environments, SMB is ubiquitous. Misconfigured shares or legacy systems allowing null sessions provide attackers with the perfect foothold to map the domain and identify privileged accounts.'
  },
  enterprise: {
    gfs: 'At GFS, enumerating SMB could expose an unprotected share containing server configuration scripts or a list of domain administrator accounts.',
    windows: 'Windows Server environments rely on SMB for Active Directory replication and Group Policy distribution, making it a critical enumeration target.',
    linux: 'Linux systems running Samba can also be targeted for SMB enumeration.'
  },
  workflow: ['Step 1: Identify systems listening on TCP 139 and 445.', 'Step 2: Attempt to establish a null session using tools like smbclient or rpcclient.', 'Step 3: If successful, enumerate user accounts and groups.', 'Step 4: List available network shares.', 'Step 5: Check permissions on identified shares.', 'Step 6: Document any sensitive information found.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f8f9fa"/><text x="50%" y="50%" font-family="Arial" font-size="24" text-anchor="middle" fill="#333">SMB Enumeration</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'enum4linux -a target', purpose: 'Enumerate SMB', out: 'Users and shares', note: 'Essential for Windows targets', mistake: 'Running without credentials when null sessions are disabled' },
      { cmd: 'smbclient -L //10.0.0.5 -N', purpose: 'List shares anonymously', out: 'Available SMB shares', note: 'Uses a null password (-N)', mistake: 'Assuming all listed shares are accessible' }
    ],
    win: [
      { cmd: 'net view \\\\target', purpose: 'View shares', out: 'List of shares', note: 'Native alternative', mistake: 'Requires SMB access' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['enum4linux', 'smbclient'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS requires an audit of legacy file servers to identify overly permissive SMB shares.',
    objectives: ['Enumerate SMB shares.', 'Identify anonymous access capabilities.'],
    steps: ['Step 1: Use enum4linux to gather basic SMB info.', 'Step 2: Use smbclient to list shares anonymously.'],
    evidence: ['Terminal output showing enumerated users and shares.'],
    validation: ['You should see: a list of shares and user details'],
    troubleshooting: ['If connection times out, verify firewall settings on the target.'],
    mitre: [{ id: 'T1087', name: 'Account Discovery', tactic: 'Discovery' }],
    cleanup: ['Remove any temporary files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which port is typically used by SMB over TCP?', opts: ['21', '80', '139', '445'], correct: 3, fb: 'SMB often runs directly over TCP port 445.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a primary tool for enumerating SMB on Linux?', opts: ['snmpwalk', 'enum4linux', 'dnsenum', 'nikto'], correct: 1, fb: 'enum4linux is specifically designed for enumerating information from Windows and Samba systems.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which command lists shares anonymously using smbclient?', opts: ['smbclient -L //target -N', 'smbclient //target -U admin', 'smbclient -M target', 'smbclient -c ls'], correct: 0, fb: 'The -L flag lists shares, and -N specifies no password (anonymous).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does IPC$ represent in Windows?', opts: ['Internet Protocol Configuration', 'Inter-Process Communication share', 'Internal Private Connection', 'Internet Protocol Connection'], correct: 1, fb: 'IPC$ is the Inter-Process Communication share used for null sessions.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which piece of information is LEAST likely to be gathered via basic SMB enumeration?', opts: ['Usernames', 'Network shares', 'Password policies', 'Database contents'], correct: 3, fb: 'SMB enumeration targets system metadata and shares, not database internals.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: Modern Windows systems enable null sessions by default.', opts: ['True', 'False'], correct: 1, fb: 'Null sessions are largely disabled by default in modern Windows versions for security.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the native Windows command to view shares on a remote computer?', opts: ['net share', 'net view \\\\target', 'show shares', 'dir \\\\target'], correct: 1, fb: 'net view \\\\target lists the shares available on a remote host.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which NetBIOS service operates on UDP port 137?', opts: ['Name Service', 'Datagram Service', 'Session Service', 'File Service'], correct: 0, fb: 'UDP 137 is the NetBIOS Name Service.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does nbtstat -A [IP] do?', opts: ['Scans for open ports', 'Displays the NetBIOS name table of the remote host', 'Attempts a null session', 'Lists SMB shares'], correct: 1, fb: 'nbtstat -A displays the NetBIOS name table for a given IP address.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why is enumerating password policies useful to an attacker?', opts: ['It reveals the passwords.', 'It helps tailor brute-force or password guessing attacks.', 'It automatically grants admin access.', 'It bypasses firewalls.'], correct: 1, fb: 'Knowing the password policy (e.g., minimum length, complexity) makes password attacks more efficient.' }
  ],
  flashcards: [
    { f: 'SMB', b: 'Server Message Block, a network file sharing protocol.' },
    { f: 'enum4linux', b: 'A Linux tool used to extract information from Windows and Samba hosts.' }
  ],
  summary: ['NetBIOS and SMB are prime targets for enumeration in Windows networks.', 'Null sessions (anonymous connections to IPC$) can reveal sensitive domain data.', 'Tools like enum4linux and smbclient are essential for this process.', 'Enumeration can reveal users, groups, policies, and shares.', 'Securing SMB involves disabling null sessions and restricting share permissions.'],
  outcomes: ['Enumerate SMB shares and users.', 'Understand the significance of null sessions.', 'Utilize enum4linux and smbclient effectively.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['snmp-ldap'] = {
  eyebrow: 'Module 04 · Topic 3',
  title: 'SNMP and LDAP Enumeration',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Extracting data from network management and directory services.',
  objectives: ['Perform SNMP Walks', 'Analyze MIBs', 'Enumerate LDAP Structures'],
  learn: {
    simple: 'Simple Network Management Protocol (SNMP) manages devices on an IP network, while Lightweight Directory Access Protocol (LDAP) queries directory services like Active Directory. Both are rich sources of information if misconfigured.',
    analogy: 'Querying SNMP is like asking a building\\'s facility manager for the blueprints, while querying LDAP is like asking the HR department for the complete employee org chart.',
    architecture: 'SNMP uses "community strings" (essentially passwords) to authenticate requests. The default read-only string is often "public". Data is organized in a hierarchical Management Information Base (MIB). LDAP structures data hierarchically (trees, branches, leaves) and is often queryable anonymously if not properly secured, revealing extensive domain and user information.',
    why: 'In an enterprise, network devices (routers, switches) often run SNMP with default community strings. LDAP (Active Directory) is the backbone of Windows networks; anonymous LDAP queries can map the entire organization structure and identity hierarchy.'
  },
  enterprise: {
    gfs: 'At GFS, an SNMP walk of a core router might reveal routing tables and internal subnets, while an anonymous LDAP query could dump the entire employee directory.',
    windows: 'LDAP is the primary protocol for interacting with Active Directory in Windows environments.',
    linux: 'Linux network devices and servers frequently utilize SNMP for monitoring via tools like Nagios or Zabbix.'
  },
  workflow: ['Step 1: Identify devices running SNMP (UDP 161) or LDAP (TCP 389/636).', 'Step 2: Attempt to guess SNMP community strings (e.g., public, private).', 'Step 3: Use snmpwalk to extract the MIB tree.', 'Step 4: Attempt anonymous binding to the LDAP server.', 'Step 5: If successful, query LDAP for user objects, groups, and organizational units.', 'Step 6: Parse the output for sensitive data.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f8f9fa"/><text x="50%" y="50%" font-family="Arial" font-size="24" text-anchor="middle" fill="#333">SNMP & LDAP Enumeration</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'snmpwalk -c public -v1 10.0.0.5', purpose: 'Enumerate SNMP', out: 'Full MIB tree', note: 'Requires valid community string', mistake: 'Using wrong SNMP version (v1 vs v2c)' },
      { cmd: 'ldapsearch -x -h 10.0.0.5 -s base namingcontexts', purpose: 'Find LDAP base DN', out: 'Base DN string', note: 'Anonymous bind attempt', mistake: 'Not specifying the correct search base later' }
    ],
    win: [
      { cmd: 'Get-ADUser -Filter *', purpose: 'Enumerate AD users', out: 'List of AD users', note: 'Requires RSAT and credentials', mistake: 'Running without domain context' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['snmpwalk', 'ldapsearch'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS network operations suspects a misconfigured router is exposing management data. You must verify this using SNMP enumeration.',
    objectives: ['Query SNMP data using default community strings.', 'Perform anonymous LDAP queries.'],
    steps: ['Step 1: Use snmpwalk with the "public" string.', 'Step 2: Use ldapsearch to attempt an anonymous bind.'],
    evidence: ['Terminal output showing SNMP data and LDAP naming contexts.'],
    validation: ['You should see: MIB data or LDAP base DN'],
    troubleshooting: ['Ensure UDP port 161 is reachable for SNMP.'],
    mitre: [{ id: 'T1087', name: 'Account Discovery', tactic: 'Discovery' }],
    cleanup: ['Remove any temporary files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the default read-only community string for SNMP?', opts: ['admin', 'password', 'public', 'private'], correct: 2, fb: 'The default read-only community string is widely set to "public".' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which port does SNMP typically use?', opts: ['TCP 161', 'UDP 161', 'TCP 389', 'UDP 389'], correct: 1, fb: 'SNMP primarily uses UDP port 161.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does MIB stand for in the context of SNMP?', opts: ['Management Information Base', 'Multiple Interface Bridge', 'Managed Internal Broadband', 'Management Interface Board'], correct: 0, fb: 'MIB stands for Management Information Base, the hierarchical structure of SNMP data.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is used to query an entire SNMP MIB tree?', opts: ['snmpget', 'snmpset', 'snmpwalk', 'nmap'], correct: 2, fb: 'snmpwalk requests a subtree of management values using SNMP GETNEXT requests.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What port does LDAP typically run on?', opts: ['TCP 139', 'UDP 161', 'TCP 389', 'TCP 445'], correct: 2, fb: 'LDAP uses TCP port 389 (or 636 for LDAP over SSL).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary risk of an improperly secured LDAP server?', opts: ['Denial of Service', 'Anonymous extraction of the directory structure and users', 'Direct remote code execution', 'SQL injection'], correct: 1, fb: 'Misconfigured LDAP servers often allow anonymous binds, exposing the entire directory.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In ldapsearch, what does the -x flag indicate?', opts: ['Use simple authentication', 'Use SSL', 'Extract all data', 'Delete the entry'], correct: 0, fb: '-x tells ldapsearch to use simple authentication (instead of SASL).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: SNMPv3 sends data in cleartext.', opts: ['True', 'False'], correct: 1, fb: 'SNMPv3 introduces encryption and strong authentication, unlike v1 and v2c which use cleartext community strings.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol is most closely associated with querying Active Directory?', opts: ['SNMP', 'SMB', 'LDAP', 'SMTP'], correct: 2, fb: 'LDAP is the core protocol for querying and modifying Active Directory.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does the "private" SNMP community string usually allow?', opts: ['Read-only access', 'Read-write access', 'No access', 'Encrypted access'], correct: 1, fb: '"private" is commonly the default read-write community string.' }
  ],
  flashcards: [
    { f: 'SNMP', b: 'Simple Network Management Protocol, used for monitoring network devices.' },
    { f: 'LDAP', b: 'Lightweight Directory Access Protocol, used to query directory services like Active Directory.' }
  ],
  summary: ['SNMP and LDAP are critical protocols for network and identity management.', 'Default SNMP community strings ("public") are a major security risk.', 'LDAP can expose the entire organizational structure if anonymous binds are permitted.', 'Tools like snmpwalk and ldapsearch are used to extract this data.', 'Securing these services involves using SNMPv3 and disabling anonymous LDAP access.'],
  outcomes: ['Enumerate SNMP using community strings.', 'Understand MIB structures.', 'Perform basic LDAP queries.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['smtp-dns-enum'] = {
  eyebrow: 'Module 04 · Topic 4',
  title: 'SMTP and DNS Enumeration',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Validating users and extracting zone data.',
  objectives: ['Validate Users via SMTP', 'Perform DNS Zone Transfers', 'Enumerate rpcbind'],
  learn: {
    simple: 'SMTP (Simple Mail Transfer Protocol) can be abused to verify if specific email addresses or system accounts exist. DNS (Domain Name System) enumeration involves extracting records to map out the target\\'s external and internal infrastructure.',
    analogy: 'SMTP enumeration is like calling a company switchboard to confirm if a specific person works there. DNS enumeration is like looking up the company in a detailed phone book to find all their branch offices and direct lines.',
    architecture: 'SMTP includes commands like VRFY (Verify) and EXPN (Expand) which attackers use to confirm valid usernames. If not disabled, these provide a reliable way to build a list of valid accounts for brute-force attacks. DNS enumeration seeks to perform a Zone Transfer (AXFR), which, if permitted to untrusted IPs, dumps the entire DNS database for a domain, revealing all configured hostnames and IP addresses.',
    why: 'In enterprise security, preventing username enumeration via SMTP limits the effectiveness of password spraying. Preventing DNS zone transfers hides the internal structure and staging environments from external attackers.'
  },
  enterprise: {
    gfs: 'At GFS, a successful DNS zone transfer could reveal the IP addresses of hidden staging servers or internal gateways that are not meant to be publicly known.',
    windows: 'Windows DNS servers must be configured to only allow zone transfers to specific secondary servers.',
    linux: 'Linux mail servers (like Postfix or Sendmail) should be configured to disable VRFY and EXPN commands.'
  },
  workflow: ['Step 1: Identify SMTP (TCP 25) and DNS (TCP/UDP 53) services.', 'Step 2: Connect to the SMTP service via telnet or netcat.', 'Step 3: Issue VRFY or EXPN commands with guessed usernames.', 'Step 4: Use dig or host commands to attempt a DNS zone transfer (AXFR).', 'Step 5: Query specific DNS record types (MX, TXT, SRV).', 'Step 6: Document discovered valid users and subdomains.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f8f9fa"/><text x="50%" y="50%" font-family="Arial" font-size="24" text-anchor="middle" fill="#333">SMTP & DNS Enumeration</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'telnet 10.0.0.5 25\\nVRFY root', purpose: 'Verify SMTP user', out: '250 OK or 550 User unknown', note: 'Manual SMTP interaction', mistake: 'Syntax errors in manual SMTP commands' },
      { cmd: 'dig axfr @10.0.0.5 target.com', purpose: 'DNS Zone Transfer', out: 'Full DNS zone data', note: 'Requires TCP port 53', mistake: 'Attempting zone transfer on a server that explicitly denies it' }
    ],
    win: [
      { cmd: 'nslookup\\n> server 10.0.0.5\\n> ls -d target.com', purpose: 'DNS Zone Transfer', out: 'Full DNS zone data', note: 'Interactive nslookup', mistake: 'Not setting the server first' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['telnet', 'dig', 'enum4linux'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS needs to ensure their external DNS servers are not leaking infrastructure details via zone transfers and that their mail gateway does not permit user enumeration.',
    objectives: ['Attempt a DNS zone transfer.', 'Use SMTP commands to verify users.'],
    steps: ['Step 1: Use dig to request an AXFR record.', 'Step 2: Connect to the SMTP server and use the VRFY command.'],
    evidence: ['Terminal output of the DNS query and SMTP interaction.'],
    validation: ['You should see: DNS records or SMTP response codes'],
    troubleshooting: ['If DNS fails, ensure the correct target DNS server is specified using @.'],
    mitre: [{ id: 'T1087', name: 'Account Discovery', tactic: 'Discovery' }, { id: 'T1590', name: 'Gather Victim Network Information', tactic: 'Reconnaissance' }],
    cleanup: ['Remove any temporary files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which SMTP command is used to confirm if a specific username exists?', opts: ['EHLO', 'MAIL FROM', 'VRFY', 'RCPT TO'], correct: 2, fb: 'VRFY (Verify) is used to check if a user exists on the mail server.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does a successful DNS Zone Transfer (AXFR) provide to an attacker?', opts: ['A shell on the DNS server', 'A complete copy of the zone file, revealing all records', 'The administrator password', 'A list of active network connections'], correct: 1, fb: 'AXFR transfers the entire zone file, exposing all configured DNS records for that domain.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol and port are required for a DNS Zone Transfer?', opts: ['UDP 53', 'TCP 53', 'UDP 69', 'TCP 25'], correct: 1, fb: 'While regular DNS queries use UDP, zone transfers require the reliability of TCP port 53.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which command expands a mailing list to show its members via SMTP?', opts: ['VRFY', 'EXPN', 'LIST', 'SHOW'], correct: 1, fb: 'EXPN (Expand) is used to show the members of a mailing list.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What tool is commonly used on Linux to perform DNS enumeration and zone transfers?', opts: ['nslookup', 'dig', 'ping', 'netstat'], correct: 1, fb: 'dig is a flexible tool for interrogating DNS name servers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How should a secure SMTP server respond to a VRFY request to prevent enumeration?', opts: ['250 User exists', '550 User unknown', '252 Cannot VRFY user', 'Drop the connection immediately'], correct: 2, fb: 'Returning 252 (Cannot VRFY user) or disabling the command entirely prevents enumeration.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does rpcbind (port 111) do?', opts: ['Maps RPC services to their listening ports', 'Transfers files', 'Resolves DNS names', 'Sends email'], correct: 0, fb: 'rpcbind (or portmapper) maps RPC program numbers to the TCP/UDP ports they are listening on.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which command queries rpcbind to see available RPC services?', opts: ['rpcclient', 'rpcinfo -p', 'showmount', 'enum4linux'], correct: 1, fb: 'rpcinfo -p queries the portmapper to list registered RPC services.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: DNS zone transfers are required for normal users to resolve website names.', opts: ['True', 'False'], correct: 1, fb: 'Normal resolution uses standard queries; zone transfers are meant for syncing DNS servers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why is SMTP user enumeration dangerous?', opts: ['It allows direct code execution.', 'It helps attackers build a list of valid targets for password guessing attacks.', 'It crashes the mail server.', 'It decrypts network traffic.'], correct: 1, fb: 'Knowing valid usernames significantly improves the success rate of brute-force and phishing attacks.' }
  ],
  flashcards: [
    { f: 'VRFY', b: 'An SMTP command used to verify if a user exists.' },
    { f: 'Zone Transfer (AXFR)', b: 'A DNS transaction that replicates the entire DNS database for a domain.' }
  ],
  summary: ['SMTP can be abused to enumerate valid user accounts using VRFY and EXPN.', 'DNS zone transfers expose the entire infrastructure map of a domain.', 'TCP port 53 is required for zone transfers.', 'rpcbind (port 111) enumerates available RPC services.', 'Securing these involves disabling unused SMTP commands and restricting DNS zone transfers.'],
  outcomes: ['Enumerate users via SMTP.', 'Perform and understand DNS zone transfers.', 'Identify available RPC services using rpcinfo.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};
"""

new_content = content.replace('// ── TAB WIRING ──', payload + '\\n// ── TAB WIRING ──')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated frontend/index.html with M04 content.")
