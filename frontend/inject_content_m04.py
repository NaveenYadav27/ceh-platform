"""
CEH Platform — Content Injection Script
Fills in all tab content for:
- Module 04 Full (4 topics, all 8 tabs)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

INJECT_BEFORE = '// ==========================================================\n// AUTO-STUB GENERATOR'

ok = []
fail = []

MODULE04_CONTENT = """
// =================================================================
// MODULE 04 — Enumeration
// =================================================================

CONTENT['enumeration-overview'] = {
  module:'Module 04 \u00b7 Enumeration',
  title:'Enumeration Concepts',
  sub:'Extracting usernames, machine names, network resources, and shares.',
  killchain:{phase:'Scanning & Enumeration',mitre:'TA0007 \u2014 Discovery',desc:'Enumeration is the final step before exploitation. It turns an open port into a list of valid users, shares, and configurations.'},
  learn:{
    simple:'Enumeration involves actively connecting to the target\'s open ports and querying them to extract lists of data: usernames, machine names, network shares, routing tables, and SNMP data. It requires an active connection to the target system.',
    analogy:'Footprinting is finding the building. Scanning is checking which doors are unlocked. Enumeration is walking through the unlocked doors, reading the staff directory on the wall, checking the labels on the filing cabinets, and figuring out who works where.',
    why:'You cannot crack a password if you don\'t have a valid username. You cannot access a file share if you don\'t know its name. Enumeration provides the specific data points (usernames, shares, domains) required to launch targeted attacks like brute-forcing or privilege escalation.',
    architecture:'Enumeration relies on specific protocols that are designed to share information. SMB (Server Message Block), NetBIOS, SNMP (Simple Network Management Protocol), LDAP (Lightweight Directory Access Protocol), and SMTP (Simple Mail Transfer Protocol) are the most commonly enumerated services.'
  },
  diagram:{
    title:'The Enumeration Phase Target Data',
    steps:[
      {icon:'\U0001f465',label:'Usernames & Groups',desc:'Extracting valid user accounts, administrator groups, and domain controllers (via SMB, SNMP, LDAP, SMTP).'},
      {icon:'\U0001f5a5\ufe0f',label:'Hostnames & Domains',desc:'Identifying machine names, Active Directory domains, and workgroups (via NetBIOS, SMB, DNS).'},
      {icon:'\U0001f4c2',label:'Network Shares',desc:'Discovering shared folders on the network, often containing sensitive documents or passwords (via SMB/CIFS).'},
      {icon:'\U0001f5a8\ufe0f',label:'Routing Tables & Devices',desc:'Mapping network topology, routers, printers, and switches (via SNMP).'},
      {icon:'\U0001f4df',label:'Services & Settings',desc:'Extracting detailed configurations, audit policies, and password policies (via LDAP, SMB).'}
    ]
  },
  enterprise:{
    role:'You are an Internal Penetration Tester at GlobalFinSec Corp.',
    situation:'You have bypassed the perimeter firewall and are sitting on an internal VLAN (10.0.50.0/24) with no credentials. You have discovered several Windows servers with port 445 (SMB) and port 161 (SNMP) open.',
    challenge:'Without any initial credentials (null session), enumerate the Windows servers to extract a list of valid usernames and identify any open file shares.',
    steps:[
      'Null Session SMB: Attempt to connect to the IPC$ share without a password using smbclient or enum4linux.',
      'Enumerate Users: Run enum4linux -U 10.0.50.100 to pull the list of local users and domain users from the domain controller.',
      'Enumerate Shares: Run enum4linux -S 10.0.50.100 to list all network shares on the file server.',
      'SNMP Walk: Run snmpwalk -v2c -c public 10.0.50.150 to pull the entire management tree from the router, including interface IPs and routing tables.'
    ],
    outcome:'The enum4linux scan successfully established a Null Session with a legacy Windows Server 2008 machine. It returned 450 valid Active Directory usernames and revealed a hidden share named "IT_Scripts$".',
    lesson:'Legacy protocols (like SMBv1 and SNMPv1/v2c) are enumeration goldmines. They are designed to share information freely. Hardening networks requires disabling Null Sessions, requiring SMB signing, and upgrading to SNMPv3.'
  },
  tools:[
    {name:'enum4linux',cmd:'enum4linux -a 192.168.1.100',desc:'The ultimate tool for enumerating Windows/Samba environments'},
    {name:'Nmap NSE',cmd:'nmap --script=smb-enum-users target',desc:'Nmap scripts for various enumeration tasks'},
    {name:'SNMPWalk',cmd:'snmpwalk -v 2c -c public target',desc:'Queries SNMP-enabled devices for their full MIB tree'}
  ],
  commands:{
    win:['net view \\\\target','net user /domain','net localgroup administrators'],
    lin:['enum4linux -U -S 192.168.1.100','nmap --script=enum target','smbclient -L //192.168.1.100 -N']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Stopping at Port Scanning',desc:'A common beginner mistake is finding port 445 open and immediately trying to run an exploit like EternalBlue. If the system is patched, the attack ends.',fix:'Always enumerate before exploiting. Even if port 445 is patched against RCE, you might be able to enumerate usernames or find an open share containing passwords.'},
    {icon:'\U0001f534',title:'Ignoring "Access Denied" as Useless',desc:'If you try to enumerate a username via SMTP (VRFY) and get an "Access Denied" or "User Unknown" response, you didn\'t fail.',fix:'"Access Denied" or specific error messages often confirm that the service is running and that your syntax is correct. Negative responses are still intelligence.'},
    {icon:'\u26d4',title:'Assuming Null Sessions Still Work Everywhere',desc:'Modern Windows (Server 2012+) disables Null Sessions (anonymous access to IPC$) by default.',fix:'If anonymous enumeration fails, try to capture or crack a low-privileged user account first. Enumeration as an authenticated (even low-privilege) user yields massively more data.'}
  ],
  lab:{
    title:'Lab: Null Session Enumeration',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Understand the concept of a Null Session','Use enum4linux to extract usernames','Discover network shares'],
    steps:[
      'Identify a target with port 139/445 open (e.g., a vulnerable Metasploitable or Windows VM).',
      'Run a full enum4linux scan: enum4linux -a [target_ip].',
      'Review the output section for "User Enumeration". Note the usernames (e.g., Administrator, Guest).',
      'Review the output section for "Share Enumeration". Note any non-default shares (e.g., /tmp, /opt).',
      'Attempt to connect to a discovered share anonymously using smbclient: smbclient \\\\[target_ip]\\[share_name] -N'
    ],
    validation:'You should successfully extract a list of usernames and shares from the target machine without providing a password, demonstrating the danger of Null Sessions.'
  },
  quiz:[
    {q:'What is the primary goal of the Enumeration phase?',opts:['To crash the target system','To discover live IP addresses','To extract lists of usernames, machine names, network resources, and shares','To hide the attacker\'s IP address'],correct:2,fb:'Enumeration involves actively connecting to services to extract detailed lists of data (users, shares, domains) required for subsequent attacks.'},
    {q:'How does Enumeration differ from Scanning?',opts:['Enumeration is passive; scanning is active','Enumeration requires an active connection and queries to specific services; scanning primarily checks if ports are open','Enumeration is only performed on Linux; scanning is for Windows','There is no difference'],correct:1,fb:'Scanning looks at the outside of the doors (ports). Enumeration involves walking through the open doors (connecting to the services) and asking for information.'},
    {q:'Which of the following protocols is NOT typically a primary target for enumeration?',opts:['SMB (Port 445)','SNMP (Port 161)','LDAP (Port 389)','ICMP (Ping)'],correct:3,fb:'ICMP is used for host discovery (scanning). SMB, SNMP, and LDAP are rich, directory-like protocols designed to share information, making them prime targets for enumeration.'},
    {q:'What is a "Null Session" in the context of Windows enumeration?',opts:['A session that has timed out','An unauthenticated connection to the IPC$ share that allows anonymous enumeration of users and shares','A session established by the SYSTEM account','A denial-of-service attack'],correct:1,fb:'A Null Session (connecting with a blank username and password) was historically allowed by Windows, permitting anonymous attackers to extract the entire user list and share list from the domain.'},
    {q:'Which tool is widely considered the standard for enumerating Windows and Samba systems from a Linux machine?',opts:['Wireshark','John the Ripper','enum4linux','Aircrack-ng'],correct:2,fb:'enum4linux is a wrapper around the Samba tools (smbclient, rpcclient, net) designed specifically to extract users, shares, password policies, and OS info from Windows/SMB targets.'},
    {q:'Why is enumerating a list of valid usernames a critical step before attempting a brute-force password attack?',opts:['It encrypts the attack traffic','It ensures you don\'t lock out the Administrator account','If you don\'t have a valid username, your brute-force attack will fail 100% of the time, regardless of the passwords tried','It makes the brute-force attack run faster'],correct:2,fb:'You cannot log in without a valid username. Enumerating the exact usernames used by the organization (e.g., jsmith vs john.smith) is a prerequisite for password attacks.'},
    {q:'If you find port 161 open during a scan, which enumeration tool should you immediately prepare to use?',opts:['smbclient','snmpwalk','sqlmap','dirb'],correct:1,fb:'Port 161 UDP is SNMP (Simple Network Management Protocol). snmpwalk is the tool used to query the SNMP tree to extract device configuration and routing info.'},
    {q:'What type of information does LDAP enumeration typically reveal?',opts:['Website source code','SQL database tables','Active Directory objects, users, organizational units (OUs), and group memberships','Wireless network passwords'],correct:2,fb:'LDAP (Lightweight Directory Access Protocol) on port 389 is the protocol used to query Active Directory. Enumerating it reveals the entire organizational structure.'},
    {q:'Which Nmap feature is heavily used during the Enumeration phase to extract data from services?',opts:['The -sn flag (Ping Sweep)','The -O flag (OS Fingerprinting)','The Nmap Scripting Engine (NSE) scripts (e.g., --script=smb-enum-users)','The -T4 flag (Timing)'],correct:2,fb:'Nmap\'s NSE scripts extend Nmap from a port scanner into a powerful enumeration tool, capable of querying SMB, LDAP, SNMP, and HTTP services for data.'},
    {q:'How can an administrator prevent Null Session enumeration on a Windows network?',opts:['Disable ICMP ping','Block port 80','Configure the RestrictAnonymous registry key to 1 or 2','Install an antivirus program'],correct:2,fb:'Changing the RestrictAnonymous registry key prevents anonymous (Null Session) users from enumerating SAM accounts and shares.'}
  ],
  flashcards:[
    {f:'Enumeration',b:'Actively connecting to target services to extract lists of usernames, machine names, network shares, and configurations.'},
    {f:'Null Session',b:'An unauthenticated (anonymous) connection to a Windows IPC$ share, historically allowing attackers to extract user lists.'},
    {f:'enum4linux',b:'The primary Linux command-line tool for enumerating users, shares, and policies from Windows/SMB systems.'},
    {f:'SMB (Server Message Block)',b:'Port 139/445. Windows file sharing protocol. Prime target for user and share enumeration.'},
    {f:'SNMP (Simple Network Management Protocol)',b:'Port 161 UDP. Used for network monitoring. Often misconfigured with default community strings, revealing routing and device info.'},
    {f:'LDAP',b:'Port 389. Protocol for querying directories (like Active Directory). Reveals users, groups, and OU structure.'},
    {f:'RestrictAnonymous',b:'Windows registry setting used to prevent Null Session enumeration.'},
    {f:'IPC$',b:'Inter-Process Communication share in Windows. The target of Null Session connections.'}
  ],
  ctf:{
    scenario:'You use enum4linux against a Windows Server. The tool successfully establishes a Null Session and enumerates the users. What is the Windows registry key that should have been configured to prevent this anonymous enumeration?',
    hint:'It restricts anonymous access.',
    flag:'CEH{3num3r4t10n_c0nc3pts}',
    points:150
  },
  summary:[
    'Enumeration extracts data (users, shares, networks) needed for exploitation.',
    'It requires an active connection to the specific service.',
    'Null Sessions allow anonymous attackers to extract entire user lists from legacy Windows systems.',
    'enum4linux is the standard tool for SMB/Windows enumeration.',
    'SNMP (port 161) and LDAP (port 389) are major enumeration targets.',
    'User enumeration is a mandatory prerequisite for password cracking or brute-forcing.',
    'Defend against enumeration by disabling anonymous access, using strong authentication, and upgrading legacy protocols.'
  ]
};

CONTENT['netbios-smb'] = {
  module:'Module 04 \u00b7 Enumeration',
  title:'NetBIOS & SMB Enumeration',
  sub:'Extracting the keys to the Windows kingdom.',
  killchain:{phase:'Scanning & Enumeration',mitre:'T1039 \u2014 Data from Network Shared Drive',desc:'SMB (Server Message Block) is the foundation of Windows networking. Enumerating it provides attackers with usernames, password policies, and access to shared files.'},
  learn:{
    simple:'NetBIOS (Network Basic Input/Output System) and SMB (Server Message Block) are the protocols Windows uses to share files and printers. Enumerating them allows attackers to list all users on the domain, view password policies, and find open shared folders containing sensitive data.',
    analogy:'Think of a corporate office. SMB is the file room where everyone stores their documents, and NetBIOS is the name tag on the door. Enumerating SMB is walking into the file room, reading the list of employees allowed inside, and checking which filing cabinets were accidentally left unlocked.',
    why:'Windows networks rely on SMB. If an attacker can enumerate the list of valid Active Directory usernames, they can launch targeted password spraying attacks. If they find an open SMB share containing a backup file or a script with hardcoded credentials, they achieve immediate compromise without needing a complex exploit.',
    architecture:'NetBIOS operates on UDP 137 (Name Service), UDP 138 (Datagram), and TCP 139 (Session). Modern SMB operates directly over TCP 445. Attackers connect to the hidden Inter-Process Communication share (IPC$) to request data from the remote procedure call (RPC) service.'
  },
  diagram:{
    title:'SMB Enumeration Targets',
    steps:[
      {icon:'\U0001f465',label:'User & Group Extraction',desc:'Querying the SAM (Security Account Manager) or AD database for all valid usernames and group memberships (e.g., Domain Admins).'},
      {icon:'\U0001f4c2',label:'Share Discovery',desc:'Listing all network shares (C$, ADMIN$, IPC$, UserData). Attackers look for misconfigured shares with read/write access.'},
      {icon:'\U0001f512',label:'Password Policy',desc:'Extracting the domain password policy (e.g., minimum length 8, lockout after 3 attempts). Critical for planning brute-force attacks.'},
      {icon:'\U0001f5a5\ufe0f',label:'OS & Architecture',desc:'Identifying the exact Windows version (e.g., Windows Server 2016 Standard) and architecture (x64).'},
      {icon:'\U0001f5a7\ufe0f',label:'Active Sessions',desc:'Seeing which users are currently logged into the machine (useful for Pass-the-Hash targeting).'}
    ]
  },
  enterprise:{
    role:'You are an internal penetration tester at GlobalFinSec Corp.',
    situation:'You are on the internal network. You have identified a file server at 10.0.50.20 with port 445 open. You do not have any valid credentials.',
    challenge:'Enumerate the SMB service to find valid usernames, identify the password policy to avoid locking out accounts, and search for exposed file shares.',
    steps:[
      'Check for Null Session: smbclient -L //10.0.50.20 -N (The -N means no password).',
      'Run enum4linux: enum4linux -a 10.0.50.20 to automate the extraction.',
      'Analyze Password Policy: The output shows "Lockout Threshold: 5". This means you can only guess 4 passwords per user before locking their account.',
      'Analyze Users: The output lists 500 valid usernames (e.g., j.doe, a.smith).',
      'Analyze Shares: The output lists a non-default share named "IT_Deployment_Scripts".',
      'Connect to Share: smbclient //10.0.50.20/IT_Deployment_Scripts -N. Download scripts and grep for passwords.'
    ],
    outcome:'The Null Session succeeded because it was a legacy Server 2003 machine. You downloaded a batch script from the open IT share that contained a plaintext Domain Admin password used for automated software installations. You achieved full domain compromise in 15 minutes without running a single exploit.',
    lesson:'Misconfigured SMB shares are the most common source of internal breaches. Disable SMBv1, disable Null Sessions (RestrictAnonymous=1), and audit share permissions regularly. Never store credentials in scripts on network shares.'
  },
  tools:[
    {name:'enum4linux',cmd:'enum4linux -a target_ip',desc:'Automated wrapper for SMB enumeration tools'},
    {name:'smbclient',cmd:'smbclient -L //target_ip -U username',desc:'FTP-like client to access SMB/CIFS resources on servers'},
    {name:'rpcclient',cmd:'rpcclient -U "" target_ip',desc:'Tool for executing client side MS-RPC functions'},
    {name:'nbtstat',cmd:'nbtstat -A target_ip',desc:'Windows native tool for NetBIOS enumeration'},
    {name:'CrackMapExec / NetExec',cmd:'nxc smb target_ip --shares',desc:'Modern, highly powerful post-exploitation and enumeration tool for AD environments'}
  ],
  commands:{
    win:['net view \\\\192.168.1.100','net share','nbtstat -A 192.168.1.100'],
    lin:['enum4linux -U -S -P 192.168.1.100','smbclient -L //192.168.1.100 -N','nmap --script=smb-os-discovery,smb-enum-shares -p 445 192.168.1.100','rpcclient -U "" -N 192.168.1.100']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Ignoring Modern Tools like NetExec (CrackMapExec)',desc:'While enum4linux is classic and taught in CEH, modern penetration testers use NetExec/CrackMapExec for SMB enumeration across entire subnets simultaneously.',fix:'Learn enum4linux for the exam, but learn NetExec (nxc smb 10.0.0.0/24 -u user -p pass --shares) for real-world enterprise assessments.'},
    {icon:'\U0001f534',title:'Brute-Forcing Without Checking the Policy',desc:'Starting a password brute-force attack via SMB without first enumerating the password policy will instantly lock out hundreds of users, causing a massive denial of service.',fix:'Always run enum4linux -P (Password Policy). If lockout is enabled at 3 attempts, you must use a "Password Spray" attack (trying 1 or 2 common passwords across all users) rather than brute-forcing one user.'},
    {icon:'\u26d4',title:'Assuming Port 139/445 Means "Vulnerable to Exploits"',desc:'Students see port 445 and immediately run MS17-010 (EternalBlue). If the server is patched, they give up.',fix:'An open port 445 is an enumeration opportunity, not just an exploit target. Focus on extracting users, shares, and data even if the system is fully patched.'}
  ],
  lab:{
    title:'Lab: SMB Enumeration & Share Access',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Enumerate shares using smbclient','Use enum4linux to extract users and password policies','Connect to an open share and download a file'],
    steps:[
      'List shares anonymously: smbclient -L //10.10.10.X -N (Replace with practice target IP).',
      'Look for shares without a "$" at the end (e.g., "Backups" instead of "IPC$").',
      'Connect to the open share: smbclient //10.10.10.X/Backups -N',
      'Use FTP-like commands: type "ls" to list files, and "get secret.txt" to download a file.',
      'Run enum4linux -U 10.10.10.X to extract the user list.',
      'Run enum4linux -P 10.10.10.X to view the password lockout policy.'
    ],
    validation:'You should successfully connect to the target\'s SMB share, list the contents, and download a file to your local machine using smbclient.'
  },
  quiz:[
    {q:'Which ports are primarily associated with NetBIOS and SMB enumeration?',opts:['TCP 21, 22, 23','UDP 161, TCP 389','UDP 137, UDP 138, TCP 139, TCP 445','TCP 80, TCP 443'],correct:2,fb:'NetBIOS uses UDP 137 (Name), UDP 138 (Datagram), and TCP 139 (Session). Modern SMB operates directly over TCP 445.'},
    {q:'What is the primary function of the tool enum4linux?',opts:['To emulate a Linux environment on Windows','To automate the extraction of users, shares, password policies, and OS info from Windows and Samba systems','To crack SMB password hashes','To scan for Linux vulnerabilities'],correct:1,fb:'enum4linux is a Perl script that wraps Samba tools (like smbclient and rpcclient) to automate the enumeration of data from Windows and SMB servers.'},
    {q:'What does the command smbclient -L //10.0.0.5 -N accomplish?',opts:['Logs into the server as Administrator','Lists the network shares on the server using a Null Session (no password)','Locks the user accounts on the server','Uploads a payload to the C$ share'],correct:1,fb:'The -L flag lists the shares available on the target. The -N flag tells smbclient to use a Null Session (no password).'},
    {q:'Why is enumerating the Password Policy via SMB critical before launching a password attack?',opts:['To ensure the passwords are encrypted','To find out if the server uses Kerberos','To discover the Account Lockout Threshold to avoid locking out user accounts and causing a Denial of Service','To find the Administrator\'s password'],correct:2,fb:'If the lockout threshold is 5 attempts, and you use Hydra to guess 10 passwords for every user, you will lock out every user in the organization. You must know the policy to stay under the limit.'},
    {q:'What is the IPC$ share?',opts:['Internet Protocol Configuration share','Inter-Process Communication share; a hidden network share used for remote administration and the target for Null Session enumeration','Internal Password Cache share','A share created by malware'],correct:1,fb:'IPC$ (Inter-Process Communication) is a hidden share used by Windows for communication between processes. Attackers connect to it anonymously (Null Session) to request data from the server via RPC.'},
    {q:'Which Windows native command-line tool can be used to view shared resources on a remote computer?',opts:['ipconfig','net view \\\\target_ip','tracert','ping'],correct:1,fb:'The "net view" command (e.g., net view \\\\192.168.1.10) lists the shared resources (folders, printers) available on a remote Windows computer.'},
    {q:'What is the difference between a brute-force attack and a password spray attack (often informed by SMB enumeration)?',opts:['Brute-force uses numbers; spraying uses letters','Brute-force tries many passwords against one user; spraying tries one common password against many users to avoid lockout','There is no difference','Spraying is only used for WiFi'],correct:1,fb:'SMB enumeration provides the list of all users. If the lockout policy is strict (e.g., 3 attempts), the attacker "sprays" one likely password (e.g., "Fall2024!") against all 500 enumerated users.'},
    {q:'Which Nmap scripting engine (NSE) script is used to enumerate SMB shares?',opts:['--script=smb-vuln-ms17-010','--script=http-enum','--script=smb-enum-shares','--script=ftp-anon'],correct:2,fb:'The smb-enum-shares script connects to the SMB service and attempts to list all available shares and determine their access permissions (read/write).'},
    {q:'What defensive configuration prevents Null Session enumeration on Windows systems?',opts:['Setting the RestrictAnonymous registry key to 1 or 2','Disabling the Windows Firewall','Enabling SMBv1','Changing the Administrator password'],correct:0,fb:'The RestrictAnonymous registry setting in Windows determines whether anonymous users can enumerate SAM accounts and shares. Setting it to 1 or 2 blocks Null Sessions.'},
    {q:'If you find an open SMB share and want to interact with it from a Linux attacking machine using an FTP-like interface, which tool should you use?',opts:['enum4linux','rpcclient','smbclient','nbtstat'],correct:2,fb:'smbclient provides an FTP-like interface (with commands like ls, cd, get, put) to connect to and interact with Windows/Samba file shares.'}
  ],
  flashcards:[
    {f:'SMB (TCP 445)',b:'Server Message Block. The standard Windows protocol for file and printer sharing.'},
    {f:'NetBIOS (TCP 139)',b:'Network Basic Input/Output System. Older API allowing applications on separate computers to communicate over a LAN.'},
    {f:'enum4linux',b:'The definitive Linux tool for automating SMB enumeration (users, shares, policies).'},
    {f:'smbclient',b:'Linux tool providing an FTP-like interface to connect to SMB shares (e.g., smbclient //ip/share).'},
    {f:'IPC$ Share',b:'Inter-Process Communication. A hidden administrative share. Connecting to it with a Null Session allows enumeration.'},
    {f:'Null Session',b:'Connecting to a Windows share (typically IPC$) with a blank username and blank password ("").'},
    {f:'RestrictAnonymous',b:'Windows Registry key used to disable Null Sessions and prevent anonymous enumeration.'},
    {f:'Password Spraying',b:'Trying 1 or 2 common passwords against a large list of enumerated users to avoid triggering the account lockout policy.'}
  ],
  ctf:{
    scenario:'You use enum4linux against a target and discover an open share containing a file named "passwords.txt". You need to download it to your Kali Linux machine. What command do you use inside the smbclient interactive prompt to download the file?',
    hint:'It is the same command used in FTP to download a file.',
    flag:'CEH{n3tb10s_smb_3num3r8}',
    points:150
  },
  summary:[
    'SMB (TCP 445) and NetBIOS (TCP 139) are the primary targets for Windows enumeration.',
    'Enumeration extracts Usernames, Network Shares, Password Policies, and OS details.',
    'A Null Session (anonymous connection to IPC$) is the historical method for extracting this data.',
    'enum4linux automates the extraction process; smbclient is used to interact with the discovered shares.',
    'Always enumerate the password policy (lockout threshold) before attempting any password attacks.',
    'Password Spraying relies entirely on the list of users extracted during SMB enumeration.',
    'Defend against it by disabling SMBv1, enforcing SMB signing, and setting RestrictAnonymous=1.'
  ]
};

CONTENT['snmp-ldap'] = {
  module:'Module 04 \u00b7 Enumeration',
  title:'SNMP & LDAP Enumeration',
  sub:'Mapping infrastructure and directory structures.',
  killchain:{phase:'Scanning & Enumeration',mitre:'T1087 \u2014 Account Discovery',desc:'SNMP reveals the physical and network topology (routers, switches). LDAP reveals the organizational structure (Active Directory users, groups, and hierarchy).'},
  learn:{
    simple:'SNMP (Simple Network Management Protocol) manages devices like routers, switches, and printers. LDAP (Lightweight Directory Access Protocol) manages directory services like Active Directory. Both protocols, if misconfigured, act as open books, giving attackers complete maps of the network and the organization.',
    analogy:'SNMP is like reading the building\'s plumbing and electrical blueprints; it tells you exactly how the infrastructure is connected. LDAP is like reading the company\'s official org chart and employee directory; it tells you who everyone is, what department they are in, and who has the keys to the vault (Domain Admins).',
    why:'SNMP enumeration provides attackers with routing tables, connected devices, and interface IPs, allowing them to map the network perfectly without noisy scanning. LDAP enumeration provides the entire Active Directory structure, allowing attackers to identify high-value targets (administrators) and their exact locations in the directory.',
    architecture:'SNMP (UDP 161) organizes data in a hierarchical tree called a MIB (Management Information Base). Access is controlled by "Community Strings" (passwords). Version 1 and 2c send strings in plaintext. LDAP (TCP 389) organizes data in a tree (Directory Information Tree) using Distinguished Names (DNs) like CN=John,OU=IT,DC=Company,DC=com.'
  },
  diagram:{
    title:'What SNMP & LDAP Reveal',
    steps:[
      {icon:'\U0001f5a8\ufe0f',label:'SNMP: Network Topology',desc:'Routing tables, ARP caches, and interface IP addresses on routers.'},
      {icon:'\U0001f5a5\ufe0f',label:'SNMP: Device Info',desc:'System name, location, uptime, running processes, and installed software.'},
      {icon:'\U0001f465',label:'LDAP: User Accounts',desc:'Every user in Active Directory, their email, phone number, and description fields (which sometimes contain passwords).'},
      {icon:'\U0001f511',label:'LDAP: Group Memberships',desc:'Identifying exactly who is in the "Domain Admins" or "Enterprise Admins" groups.'},
      {icon:'\U0001f3e2',label:'LDAP: Organizational Units (OUs)',desc:'Mapping the company structure (e.g., OU=Sales, OU=IT, OU=Servers).'}
    ]
  },
  enterprise:{
    role:'You are a Red Team operator at GlobalFinSec Corp.',
    situation:'You are on the internal network. You found a Cisco router on 10.0.1.1 (port 161 UDP open) and a Windows Domain Controller on 10.0.1.10 (port 389 TCP open).',
    challenge:'Extract the routing tables from the router to find other internal subnets, and extract the list of Domain Admins from the Domain Controller.',
    steps:[
      'SNMP Enumeration: Run onesixtyone to guess the community string of the router. It finds the default string "public" is still enabled.',
      'SNMP Walk: Run snmpwalk -v2c -c public 10.0.1.1. Parse the output for routing tables (ipRouteTable). Discover a hidden management subnet at 192.168.100.0/24.',
      'LDAP Enumeration: Run Nmap LDAP scripts against the DC: nmap -n -sV --script "ldap* and not brute" 10.0.1.10.',
      'LDAP Search: Use ldapsearch to query the directory using an anonymous bind (or a compromised low-priv user): ldapsearch -x -h 10.0.1.10 -b "DC=globalfinsec,DC=local" "(objectClass=User)"'
    ],
    outcome:'The SNMP enumeration revealed a hidden, highly secure management subnet that you were unaware of. The LDAP enumeration provided the exact usernames of the 5 Domain Admins. You are now targeting those 5 users specifically to gain access to the management subnet.',
    lesson:'Default configurations are fatal. SNMPv1/v2c with a "public" community string allows anyone to map the network. Anonymous LDAP binds allow anyone to download the corporate directory.'
  },
  tools:[
    {name:'snmpwalk',cmd:'snmpwalk -v 2c -c public target_ip',desc:'Walks the entire SNMP MIB tree, dumping all available data'},
    {name:'onesixtyone',cmd:'onesixtyone -c dict.txt target_ip',desc:'Extremely fast SNMP community string brute-forcer'},
    {name:'ldapsearch',cmd:'ldapsearch -x -h target_ip -b "dc=example,dc=com"',desc:'Linux command-line utility to query LDAP directories'},
    {name:'BloodHound',cmd:'(GUI Tool / Ingestors)',desc:'Uses LDAP queries to visually map Active Directory privilege relationships (Advanced)'}
  ],
  commands:{
    win:['Rem - Use PowerShell ActiveDirectory module for LDAP, or third-party tools for SNMP'],
    lin:['snmpwalk -v2c -c public 192.168.1.1','snmpcheck -t 192.168.1.1','onesixtyone 192.168.1.1 -c /usr/share/doc/onesixtyone/dict.txt','ldapsearch -x -h 10.0.0.5 -s base namingcontexts']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Forgetting SNMP is UDP',desc:'If you run a standard Nmap scan (which is TCP only by default), you will never see port 161 open, and you will miss SNMP enumeration entirely.',fix:'Always run a UDP scan (nmap -sU) on at least the top 100 ports. SNMP is one of the most valuable enumeration targets.'},
    {icon:'\U0001f534',title:'Ignoring SNMP "Write" Strings',desc:'SNMP usually has two community strings: "public" (read-only) and "private" (read-write). If you find the "private" string, you can actually reconfigure the router.',fix:'Always brute-force for both read and write community strings. A compromised "private" string allows you to change routing tables or disable interfaces.'},
    {icon:'\u26d4',title:'Not Reading the LDAP "Description" Fields',desc:'When dumping LDAP, students often just look at usernames. IT administrators frequently put passwords, locker combinations, or sensitive notes in the "Description" field of user or computer objects.',fix:'Grep the ldapsearch output specifically for the "description" attribute. It is a goldmine of poorly secured information.'}
  ],
  lab:{
    title:'Lab: SNMP Enumeration with snmpwalk',
    difficulty:'Intermediate',
    duration:'20 min',
    objectives:['Understand SNMP community strings','Use onesixtyone to brute-force the string','Use snmpwalk to extract system info'],
    steps:[
      'Identify a target with port 161/UDP open (e.g., Metasploitable).',
      'Brute-force the community string: onesixtyone -c /usr/share/wordlists/snmp.txt [target_ip]',
      'Note the string found (usually "public").',
      'Extract the system information tree: snmpwalk -v2c -c public [target_ip] system',
      'Extract the list of running processes: snmpwalk -v2c -c public [target_ip] hrSWRunName',
      'Observe how much detail SNMP provides without any exploitation.'
    ],
    validation:'You should successfully dump the running processes of the target system using snmpwalk, proving that misconfigured SNMP acts as a massive information leak.'
  },
  quiz:[
    {q:'Which port and protocol does SNMP (Simple Network Management Protocol) primarily use?',opts:['TCP 161','UDP 161','TCP 389','UDP 137'],correct:1,fb:'SNMP operates on UDP port 161. Because it is UDP, it is often missed by standard TCP-only port scans.'},
    {q:'What serves as the "password" for SNMP versions 1 and 2c?',opts:['The IPC$ share','The Distinguished Name (DN)','The Community String','The MIB tree'],correct:2,fb:'SNMPv1 and v2c use Community Strings (typically "public" for read-only and "private" for read/write) to authenticate requests. These are transmitted in plaintext.'},
    {q:'What is a MIB (Management Information Base) in the context of SNMP?',opts:['A tool for cracking passwords','The hierarchical database/tree structure that stores the variables and data SNMP can query on a device','A type of firewall','The master domain controller'],correct:1,fb:'The MIB is the tree-like structure on the device. Tools like snmpwalk "walk" this tree to dump all the data (routing tables, system info, processes) it contains.'},
    {q:'Which tool is specifically designed to quickly brute-force SNMP community strings?',opts:['Hydra','John the Ripper','onesixtyone','enum4linux'],correct:2,fb:'onesixtyone is an extremely fast, lightweight SNMP community string brute-forcer that sends multiple SNMP requests rapidly to identify valid strings.'},
    {q:'What port does LDAP (Lightweight Directory Access Protocol) use by default?',opts:['TCP 445','UDP 161','TCP 389','TCP 3389'],correct:2,fb:'LDAP operates on TCP port 389. Secure LDAP (LDAPS) operates on TCP port 636.'},
    {q:'What kind of information is an attacker primarily looking for when enumerating LDAP?',opts:['Network routing tables','Active Directory objects (users, groups, organizational units, and their attributes)','Website source code','Open firewall ports'],correct:1,fb:'LDAP is the protocol used to query directory services like Microsoft Active Directory. It reveals the entire organizational structure, user list, and group memberships.'},
    {q:'What is an "Anonymous Bind" in LDAP?',opts:['A denial-of-service attack','An encryption method','A misconfiguration that allows an unauthenticated user to query the LDAP directory and extract information','A secure way to authenticate administrators'],correct:2,fb:'If a Domain Controller allows Anonymous Binds, anyone on the network can query LDAP without providing a username or password, extracting the entire Active Directory structure.'},
    {q:'Which Linux command-line tool is used to query LDAP directories?',opts:['smbclient','ldapsearch','snmpwalk','netstat'],correct:1,fb:'ldapsearch is the standard utility for querying LDAP directories. An attacker uses it to execute complex searches against Active Directory to extract user and group data.'},
    {q:'Why is SNMPv3 significantly more secure than SNMPv1 and SNMPv2c?',opts:['It uses TCP instead of UDP','It replaces plaintext Community Strings with proper username/password authentication and encrypts the traffic','It blocks Nmap scans automatically','It can only be accessed from the local console'],correct:1,fb:'SNMPv1 and v2c send community strings and data in plaintext. SNMPv3 introduces cryptographic authentication and payload encryption, making it resistant to sniffing and enumeration.'},
    {q:'In an LDAP hierarchy, what does "OU" stand for?',opts:['Object User','Open Unit','Organizational Unit','Operating Utility'],correct:2,fb:'Organizational Units (OUs) are containers in Active Directory used to organize objects (users, computers) hierarchically (e.g., OU=Sales, OU=IT). Enumerating OUs reveals the company\'s departmental structure.'}
  ],
  flashcards:[
    {f:'SNMP (UDP 161)',b:'Simple Network Management Protocol. Used for monitoring devices. Major enumeration target.'},
    {f:'Community String',b:'The "password" for SNMPv1/v2c. Transmitted in plaintext. Defaults are often "public" (read) and "private" (write).'},
    {f:'MIB (Management Information Base)',b:'The hierarchical database/tree structure that SNMP queries to retrieve device information.'},
    {f:'snmpwalk',b:'Tool used to query an entire SNMP MIB tree, extracting all variables and data from a device.'},
    {f:'onesixtyone',b:'A very fast command-line tool for brute-forcing SNMP community strings.'},
    {f:'LDAP (TCP 389)',b:'Lightweight Directory Access Protocol. Protocol used to query directory services like Microsoft Active Directory.'},
    {f:'Anonymous Bind',b:'A misconfiguration allowing unauthenticated users to query an LDAP directory.'},
    {f:'ldapsearch',b:'Linux command-line utility to construct queries and extract data from LDAP servers.'}
  ],
  ctf:{
    scenario:'You discover port 161 UDP is open on a router. You want to extract its routing tables. You need to use a tool that will traverse the entire MIB tree using the community string "public". What is the name of the tool?',
    hint:'It "walks" the SNMP tree.',
    flag:'CEH{snmp_ld4p_3xp0s3d}',
    points:150
  },
  summary:[
    'SNMP operates on UDP 161. Always include UDP in your scanning phase.',
    'SNMPv1/v2c use plaintext "Community Strings". Defaults ("public") allow attackers to extract routing tables, processes, and device info.',
    'snmpwalk and onesixtyone are the primary SNMP enumeration tools.',
    'LDAP operates on TCP 389 and queries Active Directory.',
    'LDAP enumeration extracts users, groups (Domain Admins), OUs, and descriptions.',
    'Anonymous Binds allow unauthenticated users to dump the entire AD directory.',
    'Upgrade to SNMPv3 (encryption/auth) and disable LDAP Anonymous Binds to secure networks.'
  ]
};

CONTENT['smtp-dns-enum'] = {
  module:'Module 04 \u00b7 Enumeration',
  title:'SMTP & DNS Enumeration',
  sub:'Extracting valid emails and internal network topologies.',
  killchain:{phase:'Scanning & Enumeration',mitre:'T1590 \u2014 Gather Victim Network Information',desc:'SMTP enumeration verifies valid target emails for phishing or brute-forcing. DNS enumeration (like zone transfers) provides the roadmap to the entire network.'},
  learn:{
    simple:'SMTP (Simple Mail Transfer Protocol) is used to send email. Attackers can interact with mail servers to verify if specific email addresses actually exist. DNS enumeration goes beyond footprinting to actively extract bulk infrastructure data, primarily through misconfigured Zone Transfers.',
    analogy:'SMTP enumeration is like calling a company\'s front desk and asking "Does John Smith work here?" to build a directory. DNS Zone Transfer is like asking the front desk for a copy of the company\'s internal phone book and them accidentally handing it to you.',
    why:'Spear-phishing requires valid email addresses. If you send 100 emails to guessed addresses and 90 bounce back, the mail server flags you as spam. SMTP enumeration allows you to silently verify which addresses exist before sending the attack. DNS enumeration prevents you from missing hidden, unlinked servers (like staging or development databases).',
    architecture:'SMTP (TCP 25) supports commands like VRFY (Verify) and EXPN (Expand) which ask the server to confirm a user or expand a mailing list. DNS (TCP/UDP 53) uses AXFR (Zone Transfer) to replicate databases between DNS servers. If AXFR is allowed to any IP, attackers can download the whole database.'
  },
  diagram:{
    title:'SMTP & DNS Enumeration Vectors',
    steps:[
      {icon:'\U0001f4e7',label:'SMTP VRFY Command',desc:'Asks the mail server: "Does user [name] exist?" Server responds with 250 (Yes) or 550 (No).'},
      {icon:'\U0001f4e5',label:'SMTP EXPN Command',desc:'Asks the mail server to expand a mailing list (e.g., "all-staff@company.com"), returning all member email addresses.'},
      {icon:'\U0001f465',label:'SMTP RCPT TO',desc:'If VRFY is disabled, attackers start an email and use "RCPT TO:" to test if the server accepts the address.'},
      {icon:'\U0001f504',label:'DNS Zone Transfer (AXFR)',desc:'Requesting a full copy of the DNS zone file, revealing all A records, CNAMEs, and internal hostnames.'},
      {icon:'\U0001f5fa\ufe0f',label:'DNS Cache Snooping',desc:'Querying a DNS server to see if a specific record is cached, proving users on that network recently visited that site.'}
    ]
  },
  enterprise:{
    role:'You are preparing a Red Team phishing campaign against GlobalFinSec Corp.',
    situation:'You generated a list of 500 potential employee email addresses using a script (firstname.lastname@globalfinsec.com), but you don\'t know which ones are currently employed. You found their mail server on port 25.',
    challenge:'Enumerate the SMTP server to validate your list of 500 emails, ensuring your phishing campaign has a 100% delivery rate and avoids triggering spam filters with bounced emails.',
    steps:[
      'Connect to the SMTP server: nc globalfinsec-mail.com 25',
      'Test VRFY manually: VRFY jdoe. The server responds "250 2.1.5 jdoe@globalfinsec.com" (User exists).',
      'Automate the list: Use a tool like smtp-user-enum or Nmap (nmap --script=smtp-enum-users).',
      'Run the tool against your list of 500 guessed names: smtp-user-enum -M VRFY -U names.txt -t globalfinsec-mail.com'
    ],
    outcome:'The enumeration revealed that 142 of the 500 guessed emails were valid. You discarded the 358 invalid ones. The phishing campaign was sent to exactly 142 valid inboxes with zero bounced emails, completely bypassing the spam filter\'s anomaly detection.',
    lesson:'SMTP servers should be configured to disable VRFY and EXPN commands, and to provide generic responses to RCPT TO commands. Never give attackers a way to validate their target lists.'
  },
  tools:[
    {name:'smtp-user-enum',cmd:'smtp-user-enum -M VRFY -U users.txt -t 10.0.0.5',desc:'Automates the testing of VRFY, EXPN, and RCPT TO commands'},
    {name:'Nmap NSE',cmd:'nmap --script=smtp-enum-users target',desc:'Nmap script for SMTP enumeration'},
    {name:'dig',cmd:'dig axfr @ns1.target.com target.com',desc:'Command-line tool for DNS queries and Zone Transfers'}
  ],
  commands:{
    win:['nslookup','set type=any','ls -d target.com (attempt zone transfer in nslookup)'],
    lin:['nc -nv 192.168.1.25 25 (then type VRFY root)','dig axfr @ns1.target.com target.com','smtp-user-enum -M RCPT -U users.txt -t 192.168.1.25']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Assuming SMTP Enumeration is Dead',desc:'Many modern mail servers (like Exchange or Office 365) disable VRFY by default. Students assume SMTP enumeration no longer works.',fix:'If VRFY and EXPN are disabled, attackers use the "RCPT TO" method. They initiate a fake email (MAIL FROM) and test recipients (RCPT TO). If the server accepts it, the user exists.'},
    {icon:'\U0001f534',title:'Testing Zone Transfers on Only One Name Server',desc:'DNS footprints usually reveal 2-4 Name Servers (NS1, NS2, NS3). Organizations often lock down NS1 but forget to secure the secondary servers.',fix:'Always attempt an AXFR (Zone Transfer) against EVERY authoritative name server listed for the domain. It only takes one misconfigured server to reveal the whole network.'},
    {icon:'\u26d4',title:'Ignoring Internal DNS Servers',desc:'External DNS zone transfers are rare today. However, once you breach the perimeter, internal Active Directory DNS servers are frequently misconfigured to allow zone transfers to any internal IP.',fix:'DNS enumeration is just as important during the internal Post-Exploitation phase as it is during external Reconnaissance. Always try an AXFR on the internal Domain Controller.'}
  ],
  lab:{
    title:'Lab: Manual SMTP User Verification',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Connect to an SMTP server manually','Interact using raw SMTP commands','Verify if a user exists'],
    steps:[
      'Connect to a practice SMTP server (e.g., Metasploitable): nc -nv 10.10.10.X 25',
      'The server should respond with a 220 banner.',
      'Type: HELO attacker.com (and press Enter).',
      'Type: VRFY root (and press Enter). Note the 250 response (User exists).',
      'Type: VRFY fakeuser123 (and press Enter). Note the 550 response (User unknown).',
      'Type: QUIT to exit.'
    ],
    validation:'You should understand how to manually interact with an SMTP server to extract intelligence without sending an actual email.'
  },
  quiz:[
    {q:'Which port does SMTP (Simple Mail Transfer Protocol) operate on by default?',opts:['TCP 21','TCP 25','TCP 110','UDP 161'],correct:1,fb:'SMTP operates on TCP port 25 (unencrypted) or 587/465 (encrypted). Port 110 is POP3.'},
    {q:'Which SMTP command asks the server to confirm if a specific email address or username exists?',opts:['EXPN','HELO','VRFY','RCPT TO'],correct:2,fb:'VRFY (Verify) is explicitly designed to ask the mail server to confirm the existence of a user. It returns a 250 status code if the user exists.'},
    {q:'If VRFY is disabled on a mail server, what sequence of SMTP commands can an attacker use to achieve the same result?',opts:['HELO followed by QUIT','MAIL FROM followed by RCPT TO','EXPN followed by DATA','AUTH LOGIN followed by USER'],correct:1,fb:'If VRFY is disabled, an attacker can start an email transaction (MAIL FROM) and then specify a recipient (RCPT TO). The server will often reject the RCPT TO command if the user does not exist, confirming the validity of the address.'},
    {q:'What does the SMTP EXPN command do?',opts:['Exports the mail server configuration','Expands a mailing list alias, returning the email addresses of all members on that list','Expires an email in the queue','Exploits a buffer overflow in the SMTP daemon'],correct:1,fb:'EXPN (Expand) is used to expand mailing list aliases (e.g., "sales-team"). If allowed, it provides the attacker with a bulk list of valid employee emails.'},
    {q:'Which tool is specifically designed to automate the testing of usernames against an SMTP server?',opts:['enum4linux','smtp-user-enum','snmpwalk','Nmap'],correct:1,fb:'smtp-user-enum is a perl script that automates the process of testing lists of usernames against an SMTP server using VRFY, EXPN, or RCPT TO methods.'},
    {q:'What is the primary risk of a misconfigured DNS Zone Transfer (AXFR)?',opts:['It allows attackers to send spoofed emails','It reveals the entire DNS database, exposing all subdomains, internal IP addresses, and hostnames to the attacker in a single query','It crashes the DNS server','It decrypts SSL/TLS certificates'],correct:1,fb:'A zone transfer copies the entire zone file. If left open to the public, it provides the attacker with a complete map of the organization\'s network infrastructure without requiring brute-force subdomain guessing.'},
    {q:'Which command-line tool is commonly used on Linux to attempt a DNS Zone Transfer?',opts:['nslookup','ping','dig (e.g., dig axfr @server domain.com)','traceroute'],correct:2,fb:'While nslookup can be used, `dig` is the standard and most powerful command-line tool for querying DNS records and requesting zone transfers (axfr) on Linux.'},
    {q:'What is DNS Cache Snooping?',opts:['Stealing passwords from the DNS cache','Querying a DNS server to see if a specific record is in its cache, revealing whether users on that network have recently visited a specific site','Corrupting the DNS cache to redirect traffic (Cache Poisoning)','Encrypting DNS queries'],correct:1,fb:'Cache snooping involves asking a DNS server (without recursion) for a domain. If it answers immediately, the record is in the cache, proving someone on that network recently visited that domain. This is used to profile target organizations.'},
    {q:'How should a secure organization configure DNS Zone Transfers?',opts:['Allow AXFR to all internal IP addresses','Disable DNS entirely','Restrict AXFR only to authorized secondary/slave DNS servers using IP whitelisting or TSIG keys','Allow AXFR only on port 53 UDP'],correct:2,fb:'Zone transfers are necessary for DNS redundancy, but they should be strictly limited to the specific IP addresses of the authorized secondary DNS servers that need to replicate the database.'},
    {q:'During an internal penetration test, you gain access to the network and find the Active Directory Domain Controller. Why is DNS enumeration highly relevant here?',opts:['Internal Active Directory relies on DNS; a zone transfer against the internal DC will often succeed and map the entire internal corporate network','Internal DNS servers are immune to zone transfers','DNS enumeration will crack the Domain Admin password','It allows you to bypass the perimeter firewall'],correct:0,fb:'Active Directory is heavily dependent on DNS. Internal DNS servers (often the Domain Controllers themselves) are frequently misconfigured to allow zone transfers to any internal IP, providing an instant map of all servers, workstations, and services on the internal network.'}
  ],
  flashcards:[
    {f:'SMTP (TCP 25)',b:'Simple Mail Transfer Protocol. Target for enumerating valid email addresses.'},
    {f:'SMTP VRFY',b:'SMTP command used to verify if a specific user exists on the server.'},
    {f:'SMTP EXPN',b:'SMTP command used to expand a mailing list alias into individual email addresses.'},
    {f:'SMTP RCPT TO',b:'Used to specify an email recipient. Attackers use it to verify users if VRFY is disabled.'},
    {f:'smtp-user-enum',b:'Command-line tool to automate the discovery of valid email addresses via SMTP.'},
    {f:'DNS AXFR',b:'Zone Transfer. A query that requests a full copy of the DNS database. Exposes entire network topologies if misconfigured.'},
    {f:'dig',b:'Linux command-line tool used for complex DNS queries, including attempting zone transfers (dig axfr @server domain).'},
    {f:'DNS Cache Snooping',b:'Querying a DNS server to check its cache, revealing if target users recently visited specific websites.'}
  ],
  ctf:{
    scenario:'You connect to an SMTP server manually via Netcat. You want to check if the user "admin" exists on the server. What four-letter command do you type?',
    hint:'It stands for Verify.',
    flag:'CEH{smtp_dns_3num3r4t10n}',
    points:150
  },
  summary:[
    'SMTP enumeration validates email addresses for use in spear-phishing or brute-force attacks.',
    'VRFY, EXPN, and RCPT TO are the three methods to extract this information from SMTP servers.',
    'Disable VRFY and EXPN on mail servers to prevent enumeration.',
    'DNS Zone Transfers (AXFR) are the holy grail of enumeration, exposing the entire domain infrastructure in one query.',
    'Use `dig axfr @nameserver target.com` to attempt a zone transfer.',
    'Always test zone transfers against ALL authoritative name servers, as secondary servers are often forgotten and misconfigured.',
    'Internal DNS servers (Active Directory) are prime targets for zone transfers during post-exploitation.'
  ]
};
"""

if INJECT_BEFORE in html:
    pos = html.find(INJECT_BEFORE)
    html = html[:pos] + MODULE04_CONTENT + '\n\n' + html[pos:]
    ok.append('Module 04 (enumeration-overview, netbios-smb, snmp-ldap, smtp-dns-enum) injected')
else:
    fail.append('INJECT_BEFORE marker missing for Module 04')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('=' * 55)
print('MODULE 04 CONTENT INJECTION COMPLETE')
print('=' * 55)
for s in ok: print(f'  [OK]  {s}')
for s in fail: print(f'  [FAIL] {s}')
print()
print(f'New size: {len(html):,} bytes / {html.count(chr(10)):,} lines')
