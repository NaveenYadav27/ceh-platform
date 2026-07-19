"""
CEH Platform — Content Injection Script
Fills in all tab content for:
- Module 06 Full (4 topics, all 8 tabs)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

INJECT_BEFORE = '// ==========================================================\n// AUTO-STUB GENERATOR'

ok = []
fail = []

MODULE06_CONTENT = """
// =================================================================
// MODULE 06 — System Hacking
// =================================================================

CONTENT['password-cracking'] = {
  module:'Module 06 \u00b7 System Hacking',
  title:'Password Cracking',
  sub:'Breaking the primary mechanism of authentication.',
  killchain:{phase:'Gaining Access',mitre:'T1110 \u2014 Brute Force',desc:'Once a vulnerability or misconfiguration is found, password cracking is often required to escalate privileges or access encrypted data.'},
  learn:{
    simple:'Password cracking is the process of recovering plaintext passwords from their hashed or encrypted formats. Since systems do not store passwords in plaintext (they store hashes), attackers steal the hash database and crack them offline.',
    analogy:'A password hash is like a fingerprint. You can\'t look at a fingerprint and know what the person looks like (irreversible). Password cracking is having a fingerprint, then fingerprinting a million different people (guessing passwords), and seeing if one matches.',
    why:'Many exploits only provide limited access. To gain full control of a domain, an attacker must compromise an administrative account. Since admins don\'t usually leave plaintext passwords around, cracking their extracted password hashes is mandatory.',
    architecture:'Cracking methods include: Dictionary (trying words from a list), Brute-Force (trying every possible character combination), Rule-based (trying words from a list but appending numbers/symbols like "Password123!"), and Rainbow Tables (pre-computed hashes).'
  },
  diagram:{
    title:'Offline Password Cracking Workflow',
    steps:[
      {icon:'\U0001f513',label:'1. Gain Initial Access',desc:'Exploit a vulnerability to gain low-level access to the system.'},
      {icon:'\U0001f5c4\ufe0f',label:'2. Extract Hashes',desc:'Extract the SAM database (Windows) or /etc/shadow (Linux) containing the password hashes.'},
      {icon:'\U0001f4bb',label:'3. Offline Cracking',desc:'Move the hashes to an attacker-controlled cracking rig (high-end GPUs).'},
      {icon:'\U0001f4da',label:'4. Dictionary Attack',desc:'Run Hashcat or John the Ripper using rockyou.txt (known breached passwords).'},
      {icon:'\U0001f9e9',label:'5. Rule-Based Attack',desc:'Apply mutation rules (e.g., capitalize first letter, append year) to the dictionary.'},
      {icon:'\U0001f511',label:'6. Plaintext Recovery',desc:'The cracked plaintext password is used to escalate privileges or move laterally.'}
    ]
  },
  enterprise:{
    role:'You are an internal red team operator at GlobalFinSec Corp.',
    situation:'You exploited a minor web vulnerability and gained a low-privilege shell on a Windows web server. You dumped the local SAM database and extracted the local Administrator NTLM hash.',
    challenge:'Crack the NTLM hash as quickly as possible to escalate privileges on the server.',
    steps:[
      'Extract Hash: Admin:500:aad3b435b51404eeaad3b435b51404ee:32ed87bdb5fdc5e9cba88547376818d4:::',
      'Identify Format: NTLM hashes are 32 hexadecimal characters. (Hashcat mode 1000).',
      'Dictionary Attack: hashcat -m 1000 -a 0 hash.txt rockyou.txt',
      'Rule Attack (if dictionary fails): hashcat -m 1000 -a 0 hash.txt rockyou.txt -r rules/best64.rule'
    ],
    outcome:'The dictionary attack with the best64 rule cracked the hash in 14 seconds. The password was "GlobalFinSec2023!". You used this password to log in via RDP and achieved full administrative control of the server.',
    lesson:'Weak password policies defeat strong cryptography. Even if NTLM or Kerberos encryption is mathematically secure, if users choose "CompanyYear!" passwords, attackers will crack them instantly using rules.'
  },
  tools:[
    {name:'Hashcat',cmd:'hashcat -m 1000 hash.txt wordlist.txt',desc:'The world\'s fastest password cracker (GPU accelerated)'},
    {name:'John the Ripper',cmd:'john --wordlist=rockyou.txt hash.txt',desc:'Classic, versatile CPU-based password cracker'},
    {name:'Hydra',cmd:'hydra -l admin -P pass.txt ssh://target',desc:'Online password brute-forcer (attacks login portals directly, unlike Hashcat)'},
    {name:'Mimikatz',cmd:'mimikatz "lsadump::sam"',desc:'Tool for extracting plaintext passwords and hashes from Windows memory'}
  ],
  commands:{
    win:['Rem - Use Mimikatz to dump hashes from memory','hashcat64.exe -m 1000 hash.txt rockyou.txt'],
    lin:['john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt','hashcat -m 1000 -a 0 hash.txt rockyou.txt','hydra -l admin -P rockyou.txt ssh://192.168.1.10']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Online Brute-Forcing Instead of Offline Cracking',desc:'Students often try to use Hydra (Online) to guess passwords against an SSH or SMB service. This is incredibly slow and triggers account lockouts after 3-5 attempts.',fix:'Whenever possible, extract the hash database (SAM/shadow) and crack it offline using Hashcat. Offline cracking causes no lockouts, generates zero network traffic, and can guess billions of passwords per second using GPUs.'},
    {icon:'\U0001f534',title:'Using Brute-Force Before Dictionary Attacks',desc:'Starting a pure brute-force attack (guessing a, b, c... aaaaaaa) for an 8-character password will take centuries.',fix:'Always run a Dictionary attack (rockyou.txt) first, followed by a Rule-based attack. 95% of passwords will crack within minutes. Pure brute-force is a last resort.'},
    {icon:'\u26d4',title:'Not Knowing the Hash Format',desc:'If you tell Hashcat to crack an MD5 hash (-m 0) but the hash is actually NTLM (-m 1000), it will fail instantly or produce garbage.',fix:'Use tools like "hashid" or "name-that-hash" to identify the hash type before attempting to crack it.'}
  ],
  lab:{
    title:'Lab: Crack an NTLM Hash with John the Ripper',
    difficulty:'Beginner',
    duration:'15 min',
    objectives:['Identify a hash type','Use a wordlist','Crack the hash using John the Ripper'],
    steps:[
      'Create a file named hash.txt containing this NTLM hash: 8846f7eaee8fb117ad06bdd830b7586c',
      'Identify it: Run hashid hash.txt (It should suggest MD4/NTLM).',
      'Crack it: run john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt hash.txt',
      'View the result: run john --show hash.txt',
      'The plaintext password should be revealed.'
    ],
    validation:'You should successfully recover the plaintext password ("password123") from the provided NTLM hash using the rockyou.txt dictionary.'
  },
  quiz:[
    {q:'What is the primary difference between an Online password attack and an Offline password attack?',opts:['Online uses the internet; Offline does not','Online attacks interact with a live login portal (like SSH or a website); Offline attacks crack extracted hashes locally on the attacker\'s hardware','Online attacks are legal; Offline attacks are illegal','There is no difference'],correct:1,fb:'Online attacks (Hydra) must communicate over the network and are subject to lockouts and rate limiting. Offline attacks (Hashcat) crack a stolen database at maximum hardware speed with no risk of lockout.'},
    {q:'Which password cracking technique uses a predefined list of common words and passwords?',opts:['Brute-Force Attack','Dictionary Attack','Rainbow Table Attack','Keylogging'],correct:1,fb:'A Dictionary attack reads through a text file (like rockyou.txt) and hashes each word, comparing it to the stolen hash. It is the fastest method.'},
    {q:'What is a "Rainbow Table"?',opts:['A list of colorful passwords','A pre-computed table of hash values for every possible password combination, allowing for nearly instant hash reversal','A tool for extracting passwords from memory','A type of encryption algorithm'],correct:1,fb:'Rainbow tables trade massive storage space (terabytes of pre-computed hashes) for extreme cracking speed. They are defeated by "salting" passwords.'},
    {q:'What defensive technique defeats Rainbow Tables?',opts:['Encryption','Salting (adding random data to the password before hashing)','Using a firewall','Changing the password every 90 days'],correct:1,fb:'A salt is a random string added to the password before it is hashed. Because the salt is unique for every user, an attacker cannot use pre-computed Rainbow Tables; they must compute the hashes from scratch.'},
    {q:'Which tool is widely considered the fastest, GPU-accelerated offline password cracker?',opts:['Hydra','John the Ripper','Hashcat','Medusa'],correct:2,fb:'While John the Ripper is excellent (primarily CPU), Hashcat is optimized to use modern Graphics Processing Units (GPUs), allowing it to crack billions of hashes per second.'},
    {q:'In Windows, where are local user password hashes stored?',opts:['In the C:\\Windows\\Passwords.txt file','In the Active Directory database','In the SAM (Security Account Manager) database','In the /etc/shadow file'],correct:2,fb:'Local Windows passwords are stored as NTLM hashes in the SAM database (located at C:\\Windows\\System32\\config\\SAM).'},
    {q:'What type of attack involves trying a few common passwords (e.g., "Welcome1!", "Fall2024!") against hundreds or thousands of user accounts?',opts:['Brute-force attack','Dictionary attack','Password Spraying','Phishing'],correct:2,fb:'Password Spraying aims to defeat account lockout policies. Instead of trying 100 passwords against 1 user (which locks them out), the attacker tries 1 password against 100 users.'},
    {q:'Which Linux file contains the password hashes for local users?',opts:['/etc/passwd','/etc/shadow','/etc/group','/var/log/auth.log'],correct:1,fb:'Historically, hashes were in /etc/passwd (readable by anyone). Modern Linux systems moved the hashes to /etc/shadow, which is only readable by the root user.'},
    {q:'What is a "Rule-Based" or "Hybrid" dictionary attack?',opts:['Combining online and offline tools','Applying mutation rules (like capitalizing the first letter or appending numbers) to the words in a dictionary list before hashing them','Using two different dictionaries at once','Cracking both Windows and Linux hashes simultaneously'],correct:1,fb:'Since users often use variations of common words (e.g., "Password123!"), a rule-based attack applies these common mutations to a dictionary list, drastically increasing the success rate.'},
    {q:'What is the primary function of the tool Mimikatz?',opts:['To brute-force SSH logins','To extract plaintext passwords, hashes, and Kerberos tickets from Windows memory (LSASS)','To perform SQL injection','To map network topologies'],correct:1,fb:'Mimikatz is a post-exploitation tool that interacts with the Local Security Authority Subsystem Service (LSASS) in Windows to extract credentials from memory.'}
  ],
  flashcards:[
    {f:'Offline Cracking',b:'Cracking stolen hashes locally on the attacker\'s hardware (Hashcat/John). No risk of account lockout.'},
    {f:'Online Cracking',b:'Brute-forcing a live login service (Hydra/Medusa). High risk of account lockout and detection.'},
    {f:'Dictionary Attack',b:'Using a wordlist of known passwords (like rockyou.txt) to crack hashes. The fastest and most common method.'},
    {f:'Rainbow Table',b:'Massive, pre-computed tables of hashes. Allows for near-instant cracking, but defeated by salting.'},
    {f:'Salting',b:'Adding random data to a password before hashing it. Defeats Rainbow Tables.'},
    {f:'SAM Database',b:'Security Account Manager. The file where local Windows password hashes are stored.'},
    {f:'/etc/shadow',b:'The file where local Linux password hashes are stored.'},
    {f:'Hashcat',b:'The industry-standard, extremely fast, GPU-accelerated offline password cracker.'}
  ],
  ctf:{
    scenario:'You dumped the /etc/shadow file from a Linux server. The root hash starts with "$6$". What hashing algorithm does "$6$" represent in Linux shadow files?',
    hint:'It is part of the Secure Hash Algorithm 2 family.',
    flag:'CEH{p4ssw0rd_cr4ck1ng_2026}',
    points:150
  },
  summary:[
    'Password cracking converts stolen hashes back into plaintext passwords.',
    'Offline cracking (Hashcat/John) is vastly superior to Online cracking (Hydra) because it avoids lockouts and is millions of times faster.',
    'Always start with a Dictionary Attack (rockyou.txt), followed by a Rule-based attack.',
    'Windows stores local hashes in the SAM database; Linux stores them in /etc/shadow.',
    'Salting defeats Rainbow Tables by ensuring identical passwords have different hashes.',
    'Mimikatz is the premier tool for extracting credentials from Windows memory.',
    'Password Spraying is used to bypass account lockout policies by testing one password across many users.'
  ]
};

CONTENT['privilege-escalation'] = {
  module:'Module 06 \u00b7 System Hacking',
  title:'Privilege Escalation',
  sub:'Going from standard user to absolute root control.',
  killchain:{phase:'Gaining Access',mitre:'TA0004 \u2014 Privilege Escalation',desc:'Initial exploits rarely grant Administrator/Root access. Privilege escalation is the mandatory step to take full control of the compromised asset.'},
  learn:{
    simple:'Privilege Escalation is the process of exploiting a bug, design flaw, or misconfiguration in an operating system or software application to gain elevated access to resources that are normally protected from standard users.',
    analogy:'Imagine sneaking into an office building as a janitor (low privilege). You can empty the trash, but you can\'t open the vault. Privilege escalation is finding a master key left on a desk, or tricking the security guard into opening the vault for you, turning you into the Bank Manager (high privilege).',
    why:'An attacker with a standard user shell is severely limited. They cannot dump password hashes, install rootkits, disable antivirus, or modify system files. To secure persistence and pivot through the network, gaining "SYSTEM" (Windows) or "root" (Linux) is absolutely required.',
    architecture:'Escalation is either Vertical (User -> Administrator/Root) or Horizontal (User A -> User B). Methods include exploiting kernel vulnerabilities, abusing misconfigured services (weak file permissions, unquoted service paths), or finding plaintext credentials in configuration files.'
  },
  diagram:{
    title:'Common Privilege Escalation Vectors',
    steps:[
      {icon:'\U0001f4bb',label:'Kernel Exploits',desc:'Exploiting vulnerabilities in the OS core (e.g., Dirty COW on Linux, PrintNightmare on Windows). Immediate root/SYSTEM access.'},
      {icon:'\U0001f527',label:'Misconfigured Services',desc:'Windows services running as SYSTEM that have weak permissions, allowing a low-level user to replace the service executable.'},
      {icon:'\U0001f4c4',label:'Cleartext Passwords',desc:'Finding admin passwords saved in text files, scripts, unattended installation files (sysprep.xml), or registry keys.'},
      {icon:'\U0001f511',label:'SUID / SUDO Rights (Linux)',desc:'Abusing Linux binaries that are configured to run as root (SUID bit set), or exploiting overly broad SUDO permissions.'},
      {icon:'\U0001f5a5\ufe0f',label:'Scheduled Tasks / Cron Jobs',desc:'Modifying scripts that are scheduled to run automatically as an administrator.'}
    ]
  },
  enterprise:{
    role:'You are an internal penetration tester at GlobalFinSec Corp.',
    situation:'You gained initial access via a phishing email, landing a standard user shell on a Windows 10 workstation.',
    challenge:'Escalate privileges from standard user to SYSTEM to disable the EDR software and dump local credentials.',
    steps:[
      'Enumeration: Run WinPEAS (Windows Privilege Escalation Awesome Scripts) to automate finding misconfigurations.',
      'Analysis: WinPEAS highlights a service called "BackupAgent" running as SYSTEM. The path to the executable is unquoted and contains spaces: C:\\Program Files\\Backup Software\\agent.exe.',
      'Exploitation (Unquoted Service Path): Because it is unquoted, Windows attempts to execute C:\\Program.exe before C:\\Program Files\\... You create a malicious payload named "Program.exe".',
      'Execution: You drop Program.exe in the C:\\ drive. You restart the workstation (or wait for a reboot).',
      'Result: Upon reboot, Windows executes your Program.exe with SYSTEM privileges instead of the real agent.'
    ],
    outcome:'The reverse shell connected back to your Kali machine as NT AUTHORITY\\SYSTEM. You successfully disabled the EDR agent and dumped the SAM database.',
    lesson:'Automated patch management is not enough. Misconfigurations (like unquoted paths or weak folder permissions) are logic flaws, not missing patches. Regular configuration auditing is required to prevent privilege escalation.'
  },
  tools:[
    {name:'WinPEAS / LinPEAS',cmd:'linpeas.sh',desc:'Industry-standard scripts that automate the discovery of privilege escalation vectors'},
    {name:'BloodHound',cmd:'(GUI)',desc:'Maps Active Directory domain privilege escalation paths'},
    {name:'Metasploit',cmd:'meterpreter > getsystem',desc:'Contains automated local exploit modules to elevate privileges'}
  ],
  commands:{
    win:['whoami /priv','net user','tasklist /svc','sc qc [service_name]'],
    lin:['sudo -l','find / -perm -u=s -type f 2>/dev/null','cat /etc/crontab','uname -a']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Jumping to Kernel Exploits First',desc:'Kernel exploits (like Dirty COW) are unstable and frequently crash the target system (Blue Screen / Kernel Panic).',fix:'Kernel exploits are a last resort. Always look for misconfigurations (cleartext passwords, SUID binaries, unquoted service paths) first. They are silent and 100% reliable.'},
    {icon:'\U0001f534',title:'Failing to Enumerate Local Information',desc:'Students gain a shell and immediately try to run random exploits. If you don\'t know the exact OS version, installed software, and running services, you are blind.',fix:'The first step of Privilege Escalation is Local Enumeration. Run systeminfo, whoami /all, or LinPEAS to map the local landscape before taking action.'},
    {icon:'\u26d4',title:'Ignoring "Horizontal" Escalation',desc:'Testers focus entirely on getting root. Sometimes getting root directly is impossible.',fix:'Look for horizontal escalation. Can you access an IT Helpdesk user\'s account? They aren\'t admin, but they have access to password reset portals that can eventually lead to admin.'}
  ],
  lab:{
    title:'Lab: Linux Privilege Escalation (SUID)',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Enumerate Linux for misconfigurations','Identify an SUID binary','Exploit the binary to gain a root shell'],
    steps:[
      'Assume you have a low-privilege SSH connection to a Linux target.',
      'Find files with the SUID bit set (executes with owner privileges, often root): find / -perm -u=s -type f 2>/dev/null',
      'Review the output. You notice /usr/bin/nmap has the SUID bit set.',
      'Check GTFOBins (gtfobins.github.io) for "nmap".',
      'Follow the GTFOBins instructions for older Nmap versions: run nmap --interactive, then type !sh at the prompt.',
      'Type whoami. You should be root.'
    ],
    validation:'You should understand how a misconfigured file permission (SUID bit on a binary that allows command execution) immediately destroys the security model of the operating system.'
  },
  quiz:[
    {q:'What is the definition of Privilege Escalation?',opts:['Bypassing a firewall','Increasing network bandwidth','Exploiting a vulnerability or misconfiguration to gain elevated access to resources normally protected from standard users','Encrypting data to prevent unauthorized access'],correct:2,fb:'Privilege escalation moves an attacker from a restricted, low-level context (like a web application service account) to an unrestricted context (like root or SYSTEM).'},
    {q:'What is the difference between Vertical and Horizontal privilege escalation?',opts:['Vertical is gaining admin rights; Horizontal is accessing another user\'s account with the same privilege level','Vertical is over the network; Horizontal is on the local machine','Vertical targets Windows; Horizontal targets Linux','There is no difference'],correct:0,fb:'Vertical escalation moves up the hierarchy (User -> Admin). Horizontal escalation moves sideways (User A -> User B), often to access specific files or as a stepping stone to vertical escalation.'},
    {q:'Which of the following is considered a "Misconfiguration" privilege escalation vector, rather than a software vulnerability?',opts:['A Linux kernel buffer overflow','An Unquoted Service Path in Windows','A zero-day exploit in Apache','A use-after-free bug in a web browser'],correct:1,fb:'An Unquoted Service Path is a logical configuration error (failing to put quotes around a file path with spaces), not a flaw in the code itself. The OS is doing exactly what it was programmed to do.'},
    {q:'What is the purpose of the tools WinPEAS and LinPEAS?',opts:['To crack passwords','To automate the discovery of potential privilege escalation vectors on Windows and Linux systems','To launch denial-of-service attacks','To encrypt network traffic'],correct:1,fb:'PEAS (Privilege Escalation Awesome Scripts) are massive enumeration scripts that search a compromised host for hundreds of known misconfigurations, saving the attacker hours of manual searching.'},
    {q:'In Linux, what does the SUID (Set Owner User ID) bit do?',opts:['It encrypts the file','It hides the file from standard users','It allows a user to execute the file with the permissions of the file\'s owner (often root), rather than the user executing it','It prevents the file from being deleted'],correct:2,fb:'If a binary owned by root has the SUID bit set, any user who runs it temporarily gains root privileges while the program executes. If that program allows shell access (like vim or nmap), it leads to instant privilege escalation.'},
    {q:'Why are Kernel Exploits generally considered a last resort by professional penetration testers?',opts:['They are illegal','They are highly unstable and frequently crash the target system (Kernel Panic / Blue Screen of Death)','They take days to run','They cannot grant root access'],correct:1,fb:'Kernel exploits manipulate memory at the core of the operating system. If they fail, they crash the entire server, disrupting business operations. Misconfigurations are much safer to exploit.'},
    {q:'What website is the definitive resource for finding how to bypass local security restrictions using legitimate Unix binaries (like exploiting SUID bits)?',opts:['Exploit-DB','NVD','GTFOBins','Shodan'],correct:2,fb:'GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems (e.g., how to get a root shell if `tar` has the SUID bit set).'},
    {q:'In Windows, what command would you run to see all the privileges assigned to your current user account?',opts:['netstat','whoami /priv','ipconfig','tasklist'],correct:1,fb:'`whoami /priv` lists all the security privileges assigned to the current token. Certain privileges (like SeImpersonatePrivilege or SeDebugPrivilege) can be abused to gain SYSTEM access.'},
    {q:'What is a "Cron Job" in Linux, and how can it lead to privilege escalation?',opts:['A password cracking tool','A scheduled task. If a cron job runs as root, and a low-privilege user has write access to the script it executes, they can inject malicious commands to run as root','A firewall rule','A type of kernel exploit'],correct:1,fb:'Cron jobs execute scripts on a schedule. If an administrator creates a root cron job but accidentally leaves the target script writable by standard users, anyone can rewrite the script to grant themselves root.'},
    {q:'If you find a file named `sysprep.xml` or `unattend.xml` on a Windows system, what are you likely looking for?',opts:['Cleartext administrator passwords used during the automated installation of the OS','Network routing tables','Firewall configurations','Vulnerability scanner logs'],correct:0,fb:'Unattended installation files (used to deploy Windows images automatically) frequently contain the local Administrator password in cleartext or weak Base64 encoding. Finding these files is a classic privilege escalation path.'}
  ],
  flashcards:[
    {f:'Privilege Escalation',b:'Exploiting a vulnerability or misconfiguration to gain elevated access (root/SYSTEM).'},
    {f:'Vertical Escalation',b:'Moving from a low-privilege user to a high-privilege user (Admin/Root).'},
    {f:'Horizontal Escalation',b:'Moving to another user account with the same privilege level.'},
    {f:'LinPEAS / WinPEAS',b:'Automated enumeration scripts that search for privilege escalation vectors on a local system.'},
    {f:'SUID Bit',b:'Linux permission that allows a program to execute with the privileges of its owner (often root). A major escalation vector if misconfigured.'},
    {f:'Unquoted Service Path',b:'Windows misconfiguration where a service path contains spaces but lacks quotes, allowing an attacker to drop a malicious executable in the path.'},
    {f:'GTFOBins',b:'Website cataloging how to exploit legitimate Unix binaries (like nmap or vim) to bypass restrictions and escalate privileges.'},
    {f:'Kernel Exploit',b:'Exploiting the OS core. Powerful but highly unstable; can cause system crashes (BSOD).' }
  ],
  ctf:{
    scenario:'You run `find / -perm -u=s -type f 2>/dev/null` on a Linux target and discover that `/usr/bin/find` has the SUID bit set. You consult GTFOBins and execute `find . -exec /bin/sh -p \\; -quit`. What user are you now?',
    hint:'You escalated vertically to the highest user on Linux.',
    flag:'CEH{pr1v_3sc_r00t_2026}',
    points:150
  },
  summary:[
    'Privilege Escalation is mandatory; initial shells are rarely highly privileged.',
    'Vertical escalation = gaining Admin/Root. Horizontal = accessing other user accounts.',
    'Always prioritize Misconfigurations (cleartext passwords, SUID, scheduled tasks) over Kernel Exploits (unstable/crashes).',
    'LinPEAS and WinPEAS automate local enumeration to find these misconfigurations.',
    'SUID binaries and Cron jobs are the primary Linux misconfiguration targets.',
    'Unquoted Service Paths and unattended installation files (cleartext passwords) are primary Windows targets.',
    'GTFOBins is the standard reference for abusing legitimate Linux binaries.'
  ]
};

CONTENT['maintaining-access'] = {
  module:'Module 06 \u00b7 System Hacking',
  title:'Maintaining Access',
  sub:'Ensuring you never lose the shell.',
  killchain:{phase:'Maintaining Access',mitre:'TA0003 \u2014 Persistence',desc:'Vulnerabilities get patched and servers get rebooted. Persistence mechanisms ensure the attacker retains access regardless of defender actions.'},
  learn:{
    simple:'Maintaining Access (Persistence) is the process of installing backdoors, rootkits, or creating hidden accounts so the attacker can re-enter the compromised system at any time, even if the original vulnerability they exploited is patched or the server is rebooted.',
    analogy:'Gaining access is picking the lock on the front door. Maintaining access is leaving the door unlocked, cutting a copy of the key, and installing a hidden doggie door in the back so you can come and go as you please, even if they change the front lock.',
    why:'Exploiting systems is noisy and risky. Attackers do not want to re-exploit the target every time they need access. Furthermore, IT departments regularly reboot servers and apply patches. Persistence guarantees the attacker survives these routine operations.',
    architecture:'Persistence mechanisms range from simple (creating a new Administrator account) to complex (installing a Rootkit in the OS kernel that hides files and processes). Attackers use Scheduled Tasks, Registry Run Keys, malicious services, and Trojanized system binaries to ensure their backdoor starts automatically.'
  },
  diagram:{
    title:'Common Persistence Mechanisms',
    steps:[
      {icon:'\U0001f465',label:'Account Manipulation',desc:'Creating hidden admin accounts, resetting passwords, or adding SSH keys to authorized_keys.'},
      {icon:'\U0001f5a5\ufe0f',label:'Scheduled Tasks / Cron',desc:'Configuring the OS to execute a reverse shell payload every hour or upon system boot.'},
      {icon:'\U0001f511',label:'Registry Run Keys',desc:'Adding the malware to Windows Startup registry keys (HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run).'},
      {icon:'\U0001f4bb',label:'Backdoored Services',desc:'Creating a hidden Windows Service that launches a Remote Access Trojan (RAT) in the background.'},
      {icon:'\U0001f4df',label:'Web Shells',desc:'Uploading a PHP or ASPX script to the web server that executes commands sent via HTTP (bypasses firewalls).'},
      {icon:'\U0001f977',label:'Rootkits',desc:'Modifying the OS kernel to completely hide the attacker\'s files, processes, and network connections from the defenders.'}
    ]
  },
  enterprise:{
    role:'You are an APT (Advanced Persistent Threat) actor targeting GlobalFinSec Corp.',
    situation:'You successfully exploited a zero-day vulnerability in their VPN gateway, escalated privileges, and now have full domain control. You know the zero-day patch will be released tomorrow.',
    challenge:'Establish multiple layers of persistence across the network so that when the VPN is patched, you do not lose access.',
    steps:[
      'Layer 1 (Web Shell): Drop a heavily obfuscated ASPX web shell deep in the IIS web server directory (e.g., error_log_template.aspx).',
      'Layer 2 (Registry): Use Metasploit to install a persistent backdoor in the Windows Registry Run key of a critical database server.',
      'Layer 3 (Accounts): Create a new Active Directory user named "svc_backup_admin", grant it Domain Admin rights, and set the password to never expire.',
      'Layer 4 (Golden Ticket): Extract the KRBTGT hash from the Domain Controller. This allows you to forge valid Kerberos tickets for any user at any time (Golden Ticket).'
    ],
    outcome:'The next day, the IT team patched the VPN gateway. Your initial entry point was gone. However, you simply browsed to the hidden ASPX web shell to regain a command prompt, and used the Golden Ticket to immediately act as Domain Admin. The network remains fully compromised.',
    lesson:'Defenders often stop at patching the vulnerability that caused the breach. Incident Response must include hunting for and eradicating persistence mechanisms (threat hunting), otherwise the attacker never really leaves.'
  },
  tools:[
    {name:'Metasploit',cmd:'run persistence -X -i 5 -p 4444',desc:'Contains automated post-exploitation modules for installing persistence'},
    {name:'Netcat (nc)',cmd:'nc -l -p 4444 -e /bin/bash',desc:'Can be set up as a simple listening backdoor'},
    {name:'Weevely',cmd:'weevely generate pass shell.php',desc:'Stealth PHP web shell generator'},
    {name:'Empire / Covenant',cmd:'(C2 Frameworks)',desc:'Advanced Command and Control frameworks designed specifically for persistence and stealth post-exploitation'}
  ],
  commands:{
    win:['net user hacker password123 /add','net localgroup administrators hacker /add','schtasks /create /tn "Update" /tr "C:\\payload.exe" /sc onstart'],
    lin:['echo "ssh-rsa AAAAB3..." >> ~/.ssh/authorized_keys','echo "@reboot root /tmp/payload.sh" >> /etc/crontab']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Creating Obvious Accounts',desc:'Creating a user named "hacker" or "admin2" is an instant red flag to any basic security audit.',fix:'Attackers blend in. They create accounts that look like legitimate service accounts (e.g., "svc_sql_monitor") or re-enable disabled employee accounts.'},
    {icon:'\U0001f534',title:'Relying on a Single Persistence Method',desc:'If you only install a backdoor in the registry, a good Antivirus sweep might find it and delete it, locking you out.',fix:'Professional attackers use redundant persistence. A web shell, a scheduled task, and compromised SSH keys across multiple different servers ensure access survives remediation attempts.'},
    {icon:'\u26d4',title:'Using Noisy Backdoors',desc:'Installing a backdoor that constantly connects out every 5 seconds generates massive, anomalous network traffic that the SOC will detect.',fix:'Use "sleep" intervals. Configure the backdoor (Command and Control agent) to check in randomly every 4 to 12 hours. This blends in with normal network traffic.'}
  ],
  lab:{
    title:'Lab: Web Shell Persistence',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Understand how a web shell works','Upload a simple PHP web shell','Execute commands via a web browser'],
    steps:[
      'Assume you have already compromised a Linux web server (Metasploitable).',
      'Create a simple PHP web shell: echo "<?php system(\\$_GET[\'cmd\']); ?>" > /var/www/html/hidden.php',
      'This file is now a permanent backdoor. As long as the web server is running, the attacker has access.',
      'Open your web browser and navigate to: http://[target_ip]/hidden.php?cmd=whoami',
      'The browser will display the output of the command (e.g., www-data).',
      'Change the command in the URL: http://[target_ip]/hidden.php?cmd=cat /etc/passwd'
    ],
    validation:'You should understand that a web shell provides a persistent, firewall-bypassing method of command execution that survives reboots and patching.'
  },
  quiz:[
    {q:'What is the primary goal of the "Maintaining Access" phase?',opts:['To discover open ports','To extract plaintext passwords','To ensure the attacker can return to the compromised system even if it is rebooted or the original vulnerability is patched','To crash the target system'],correct:2,fb:'Maintaining access (persistence) decouples the attacker\'s access from the initial vulnerability. They install backdoors so they can re-enter at will.'},
    {q:'Which of the following is a common method for achieving persistence on a Windows system?',opts:['Modifying the /etc/shadow file','Adding a malicious payload to the HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run registry key','Running a ping sweep','Exploiting a buffer overflow'],correct:1,fb:'The "Run" registry keys are executed every time Windows boots. Placing a payload here ensures the backdoor starts automatically when the server is restarted.'},
    {q:'What is a Web Shell?',opts:['A secure browser extension','A malicious script (PHP, ASPX) uploaded to a web server that allows an attacker to execute system commands via HTTP requests','A tool for analyzing HTML source code','A type of firewall'],correct:1,fb:'Web shells are incredibly popular for persistence because they communicate over port 80/443 (HTTP/HTTPS), which is almost always allowed through firewalls, blending in with normal web traffic.'},
    {q:'What makes a Rootkit fundamentally different from a standard Trojan or Backdoor?',opts:['A rootkit is written in Python','A rootkit modifies the core Operating System (Kernel) to actively hide its files, processes, and network connections from the administrator and antivirus','A rootkit is a hardware device','A rootkit only works on Linux'],correct:1,fb:'Standard backdoors can be seen in the task manager. A rootkit hooks deep into the OS to intercept queries, making itself completely invisible to standard system tools.'},
    {q:'How can an attacker establish persistence on a Linux server without installing any new software?',opts:['By adding their public SSH key to the root user\'s ~/.ssh/authorized_keys file','By deleting the /var/log directory','By running Nmap locally','By exploiting the Windows registry'],correct:0,fb:'Adding an SSH key to `authorized_keys` allows the attacker to log in as that user (e.g., root) via SSH at any time, without needing a password. It is a built-in OS feature used maliciously.'},
    {q:'What is a "Golden Ticket" attack?',opts:['Winning a bug bounty program','Forging a Kerberos Ticket Granting Ticket (TGT) after extracting the KRBTGT hash, granting the attacker domain-wide access for years','A VIP pass to a cybersecurity conference','A ransomware payment method'],correct:1,fb:'The Golden Ticket is the ultimate persistence mechanism in Active Directory. By compromising the central KRBTGT account, the attacker can forge authentication tickets for any user, bypassing password checks entirely.'},
    {q:'Why do professional attackers configure their persistence backdoors to use long "sleep" or "beaconing" intervals (e.g., checking in every 12 hours)?',opts:['To save battery power','To reduce the load on their own servers','To blend in with normal network traffic and avoid detection by SOC analysts monitoring for constant, anomalous outbound connections','Because the tools are slow'],correct:2,fb:'Stealth requires blending in. A backdoor connecting out every 5 seconds is incredibly noisy. Checking in randomly every few hours looks like legitimate background internet traffic.'},
    {q:'If an attacker compromises a web server and creates a new user account named "Administrator2", what is the primary flaw in this persistence strategy?',opts:['It is too slow','It relies on a vulnerability','It is highly visible and obvious; a basic audit by a defender will spot it immediately','It requires a reboot'],correct:2,fb:'Good persistence is stealthy. Attackers prefer to hijack existing service accounts or use naming conventions that blend in (e.g., "svc_sql_backup") rather than creating obvious, highly visible admin accounts.'},
    {q:'Which Metasploit payload feature is explicitly designed to ensure the attacker retains access?',opts:['The Port Scanner module','The Persistence module (which creates registry keys or scheduled tasks for the payload)','The Encoding module','The Exploit module'],correct:1,fb:'Metasploit includes post-exploitation modules specifically designed to automate the installation of persistence mechanisms (like registry run keys) for the Meterpreter payload.'},
    {q:'What defensive activity is explicitly designed to find attackers who have bypassed prevention controls and established persistence?',opts:['Vulnerability Scanning','Patch Management','Threat Hunting','Firewall Configuration'],correct:2,fb:'Threat Hunting is the proactive search through networks and endpoints to find advanced threats that evaded automated security controls and established persistence.'}
  ],
  flashcards:[
    {f:'Persistence',b:'The ability of an attacker to retain access to a compromised system across reboots and patching.'},
    {f:'Web Shell',b:'A malicious script (e.g., PHP, ASP) uploaded to a web server that executes OS commands via web requests.'},
    {f:'Rootkit',b:'Malware that deeply hooks into the OS Kernel to hide files, processes, and network connections from defenders.'},
    {f:'Registry Run Keys',b:'Windows registry locations where attackers place payloads to ensure they execute automatically on system boot.'},
    {f:'authorized_keys',b:'Linux file used for SSH authentication. Attackers add their keys here for silent, password-less persistence.'},
    {f:'Golden Ticket',b:'Forging Kerberos tickets using the compromised KRBTGT hash. Grants ultimate, long-term persistence in Active Directory.'},
    {f:'Beaconing',b:'The intermittent outbound connection made by a backdoor to its Command and Control (C2) server.'},
    {f:'Threat Hunting',b:'The defensive practice of proactively searching for persistence mechanisms and hidden attackers.'}
  ],
  ctf:{
    scenario:'You have root access on a Linux server. You want to ensure that a malicious script (`/tmp/backdoor.sh`) runs automatically every time the server reboots. What file should you edit to add the line `@reboot root /tmp/backdoor.sh`?',
    hint:'It is the table that manages scheduled tasks in Linux.',
    flag:'CEH{m41nt41n_4cc3ss_r00tk1t}',
    points:150
  },
  summary:[
    'Maintaining Access (Persistence) ensures survival after reboots or patching.',
    'Windows persistence relies on Registry Run Keys, Scheduled Tasks, and hidden accounts.',
    'Linux persistence relies on Cron jobs and adding SSH keys to authorized_keys.',
    'Web Shells provide stealthy, firewall-bypassing persistence on web servers.',
    'Rootkits provide the ultimate stealth by modifying the OS kernel to hide the attacker\'s actions.',
    'Active Directory persistence often utilizes Golden Tickets (forged Kerberos authentication).',
    'Incident Response must include Threat Hunting to eradicate persistence, not just patch the initial flaw.'
  ]
};

CONTENT['steganography'] = {
  module:'Module 06 \u00b7 System Hacking',
  title:'Covering Tracks & Steganography',
  sub:'Hiding the evidence and exfiltrating data silently.',
  killchain:{phase:'Covering Tracks',mitre:'TA0005 \u2014 Defense Evasion',desc:'The final phase of the CEH methodology. Attackers wipe logs and hide stolen data inside legitimate files to evade detection and forensic investigation.'},
  learn:{
    simple:'Covering tracks involves deleting or modifying log files to erase evidence of the attack. Steganography is the art of hiding secret data inside a non-secret file (like a picture or audio file) so it can be exfiltrated without arousing suspicion.',
    analogy:'Covering tracks is a burglar wiping down the doorknobs for fingerprints and deleting the security camera footage. Steganography is the burglar walking out the front door hiding the stolen diamonds inside a hollowed-out loaf of bread.',
    why:'If an attacker leaves Nmap logs, web shell access logs, and Windows Event logs untouched, the SOC will quickly detect the breach and forensic analysts will map their exact actions. Furthermore, exfiltrating a file named "credit_cards.txt" will trigger Data Loss Prevention (DLP) alarms. Steganography bypasses DLP.',
    architecture:'Track covering targets central logging mechanisms (Windows Event Logs, Linux bash_history, Apache access logs). Steganography uses techniques like LSB (Least Significant Bit) insertion to replace the least important data in an image pixel with the secret data, changing the image so slightly the human eye cannot detect it.'
  },
  diagram:{
    title:'Defense Evasion & Exfiltration Techniques',
    steps:[
      {icon:'\U0001f5d1\ufe0f',label:'Log Deletion',desc:'Clearing the Windows Security, System, and Application event logs (e.g., using wevtutil or Meterpreter).'},
      {icon:'\u270f\ufe0f',label:'Log Alteration (Timestomping)',desc:'Changing the creation/modification timestamps of malicious files to match legitimate OS files, hiding them from forensic timelines.'},
      {icon:'\U0001f464',label:'Clearing Command History',desc:'Deleting or linking /dev/null to the Linux ~/.bash_history file so executed commands are not recorded.'},
      {icon:'\U0001f5bc\ufe0f',label:'Steganography (Hiding)',desc:'Embedding stolen data (passwords, source code) inside a JPEG or WAV file.'},
      {icon:'\U0001f4e4',label:'Covert Exfiltration',desc:'Emailing the seemingly harmless JPEG out of the network. DLP and firewalls see it as a normal picture and allow it.'}
    ]
  },
  enterprise:{
    role:'You are an APT actor exfiltrating intellectual property from GlobalFinSec Corp.',
    situation:'You have compromised a developer\'s workstation and found the source code for the company\'s proprietary trading algorithm. The network has strict Data Loss Prevention (DLP) that blocks any files containing code or the word "algorithm" from leaving the network.',
    challenge:'Exfiltrate the source code without triggering the DLP system, and erase evidence of your actions.',
    steps:[
      'Steganography: Use Steghide to embed the source_code.zip file inside a large, high-resolution JPEG image of the company logo: steghide embed -cf logo.jpg -ef source_code.zip -p secretpass',
      'Exfiltration: Upload the modified logo.jpg to an external server or attach it to an email. The DLP system scans it, sees a valid JPEG structure with no restricted keywords, and allows it to pass.',
      'Covering Tracks: Use the Meterpreter "timestomp" command on the web shell you used to gain access, matching its creation date to the original web server installation date in 2019.',
      'Log Clearing: Clear the Windows Event logs using "wevtutil cl Security" and "wevtutil cl System".'
    ],
    outcome:'The source code was successfully exfiltrated. Because the logs were cleared and the web shell was timestomped, the incident response team spent weeks trying to determine how the breach occurred and exactly what data was taken.',
    lesson:'Steganography defeats content-inspection (DLP). Log clearing blinds forensic investigators. Centralized, append-only logging (sending logs to an immutable SIEM server immediately) is the only defense against log clearing.'
  },
  tools:[
    {name:'Steghide',cmd:'steghide embed -cf cover.jpg -ef secret.txt',desc:'Command-line steganography tool that hides data in image and audio files'},
    {name:'OpenStego',cmd:'(GUI Tool)',desc:'Open-source graphical steganography application'},
    {name:'Meterpreter (clearev)',cmd:'meterpreter > clearev',desc:'Wipes the Application, System, and Security event logs on a Windows target'},
    {name:'wevtutil',cmd:'wevtutil cl Security',desc:'Native Windows command-line utility to clear event logs'}
  ],
  commands:{
    win:['wevtutil cl System','wevtutil cl Security','wevtutil cl Application'],
    lin:['export HISTSIZE=0','cat /dev/null > ~/.bash_history','rm -rf /var/log/apache2/access.log']
  },
  pitfalls:[
    {icon:'\u26a0\ufe0f',title:'Deleting the Entire Log File',desc:'An attacker deleting the entire Security log is a massive, glowing red flag to any SOC. It generates an Event ID (1102: The audit log was cleared) that triggers high-priority alerts.',fix:'Advanced attackers do not delete the entire log. They selectively edit the log to remove only their specific IP address or actions, leaving the rest intact. (This requires advanced tools).'},
    {icon:'\U0001f534',title:'Forgetting Centralized Logging (SIEM)',desc:'Clearing logs on the local compromised server is useless if that server automatically forwards all logs to a central Splunk/SIEM server every second.',fix:'If a target uses centralized logging, the attacker must either disrupt the forwarding service before acting, or compromise the SIEM itself.'},
    {icon:'\u26d4',title:'Confusing Steganography with Cryptography',desc:'Cryptography scrambles data making it unreadable (but obviously a secret). Steganography hides the existence of the data entirely.',fix:'Attackers usually combine them: encrypt the data first (Cryptography), then hide the encrypted blob inside an image (Steganography).'}
  ],
  lab:{
    title:'Lab: Hiding Data with Steghide',
    difficulty:'Beginner',
    duration:'15 min',
    objectives:['Embed a secret file inside an image','Extract the secret file','Understand LSB steganography'],
    steps:[
      'Create a secret file: echo "Confidential Passwords" > secret.txt',
      'Download a sample JPEG image (e.g., cover.jpg).',
      'Embed the secret: steghide embed -cf cover.jpg -ef secret.txt (Enter a passphrase when prompted).',
      'Look at cover.jpg. It opens normally in an image viewer and looks identical to the original.',
      'Extract the secret: steghide extract -sf cover.jpg (Enter the passphrase).',
      'Read the extracted file: cat secret.txt'
    ],
    validation:'You should successfully hide a text file inside an image, demonstrating how attackers bypass DLP systems that look for specific file types or keywords.'
  },
  quiz:[
    {q:'What is the definition of Steganography?',opts:['The process of encrypting data using complex mathematical algorithms','The art and science of hiding secret data within non-secret files (like images or audio) so its existence is concealed','The process of clearing system logs','A type of password cracking attack'],correct:1,fb:'While cryptography hides the meaning of a message, steganography hides the very existence of the message by burying it in normal-looking files.'},
    {q:'What is the primary reason an attacker uses Steganography during the Exfiltration phase?',opts:['To compress the data and save bandwidth','To bypass Data Loss Prevention (DLP) systems and firewalls that would flag or block files containing sensitive data or code','To execute the payload on the target machine','To crack the passwords faster'],correct:1,fb:'DLP systems inspect outbound traffic for credit cards, source code, or keywords. By embedding this data inside a seemingly harmless JPEG, the DLP system sees only a picture and lets it pass.'},
    {q:'What is LSB (Least Significant Bit) insertion?',opts:['A method of clearing the bash history','A cryptography algorithm','A common steganography technique where the right-most bit of a pixel\'s color value is replaced with a bit of the secret data','A type of buffer overflow'],correct:2,fb:'LSB insertion modifies the least significant bit of pixel data. Changing this bit alters the color so slightly (e.g., from a specific shade of red to a shade 1/256th different) that the human eye cannot detect the change.'},
    {q:'In Windows, what does the command `wevtutil cl Security` do?',opts:['Encrypts the Security log','Clears (deletes) all entries in the Windows Security Event Log','Copies the Security log to a remote server','Scans the Security log for vulnerabilities'],correct:1,fb:'wevtutil is the native Windows Event Log utility. `cl` stands for clear log. Clearing the Security log is a classic track-covering technique to hide unauthorized logins.'},
    {q:'If an attacker clears the Windows Security Event Log, what specific Event ID is generated and recorded?',opts:['Event ID 4624','Event ID 1102 (The audit log was cleared)','Event ID 445','No event ID is generated'],correct:1,fb:'Clearing the log ironically leaves a massive forensic artifact: Event ID 1102. Modern SOCs configure high-priority alerts for this specific Event ID.'},
    {q:'What is "Timestomping"?',opts:['A denial-of-service attack that targets the NTP (Time) server','The process of modifying the MAC (Modified, Accessed, Created) timestamps of a malicious file to match legitimate OS files, hiding them from forensic timelines','Clearing the bash history','Waiting for a specific time to launch an attack'],correct:1,fb:'Forensic analysts often build timelines of an attack (e.g., "Show me all files created on Tuesday"). Timestomping allows attackers to change a backdoor\'s creation date to years ago, hiding it from the timeline.'},
    {q:'Which Metasploit command automatically wipes the Application, System, and Security event logs on a compromised Windows target?',opts:['hashdump','timestomp','clearev','getsystem'],correct:2,fb:'The `clearev` (Clear Event Logs) command in a Meterpreter session automatically wipes the three primary Windows event logs.'},
    {q:'How can an attacker prevent their commands from being saved to the Linux bash history file (~/.bash_history)?',opts:['By running `export HISTSIZE=0` or unsetting the HISTFILE variable','By encrypting the terminal','By running the commands as root','By using the `sudo` command for everything'],correct:0,fb:'Setting HISTSIZE to 0 prevents the bash shell from recording any executed commands into the history file, hiding the attacker\'s actions.'},
    {q:'Which tool is a popular command-line utility for hiding text or files inside JPEG and BMP image files?',opts:['Nmap','Steghide','John the Ripper','Wireshark'],correct:1,fb:'Steghide is a classic steganography tool that allows for embedding and extracting secret data from image and audio files.'},
    {q:'What is the most effective defensive strategy against an attacker attempting to cover their tracks by clearing local log files?',opts:['Disabling logging entirely to save disk space','Using centralized, append-only logging (like a SIEM), where logs are instantly forwarded to a secure server the attacker cannot access','Changing the administrator password daily','Using steganography defensively'],correct:1,fb:'If logs are instantly forwarded to a central SIEM (Splunk, Elastic), it doesn\'t matter if the attacker clears the local logs. The SIEM already has the immutable record of the attack.'}
  ],
  flashcards:[
    {f:'Covering Tracks',b:'The final CEH phase. Deleting logs and altering artifacts to evade detection and hinder forensic investigation.'},
    {f:'Steganography',b:'The art of hiding secret data within non-secret files (images, audio) to conceal its existence.'},
    {f:'LSB Insertion',b:'Least Significant Bit. A steganography technique replacing the least important bit of pixel data with secret data.'},
    {f:'Timestomping',b:'Modifying the MAC (Modified, Accessed, Created) timestamps of a file to hide it from forensic timelines.'},
    {f:'clearev',b:'Meterpreter command that wipes the Windows Application, System, and Security event logs.'},
    {f:'Event ID 1102',b:'The Windows Event ID generated when the audit log is cleared. A critical SOC alert.'},
    {f:'HISTSIZE=0',b:'Linux command to disable the recording of commands in the bash history file.'},
    {f:'Centralized Logging (SIEM)',b:'The primary defense against log clearing. Logs are forwarded instantly to a secure, separate server.'}
  ],
  ctf:{
    scenario:'You use the Meterpreter shell to cover your tracks on a Windows system. You want to wipe the Application, System, and Security logs all at once using the built-in Meterpreter command. What is the command?',
    hint:'It stands for Clear Event logs.',
    flag:'CEH{st3g0_c0v3r_tr4cks}',
    points:150
  },
  summary:[
    'Covering Tracks hinders forensics and delays detection.',
    'Windows track covering involves clearing logs (wevtutil, clearev) and timestomping files.',
    'Linux track covering involves clearing or disabling ~/.bash_history.',
    'Clearing the Windows Security log generates Event ID 1102 (a massive red flag).',
    'Steganography (like Steghide) hides data inside images/audio to bypass DLP exfiltration filters.',
    'LSB insertion is the most common steganography technique.',
    'Centralized logging (SIEM) is the only reliable defense against local track covering.'
  ]
};
"""

if INJECT_BEFORE in html:
    pos = html.find(INJECT_BEFORE)
    html = html[:pos] + MODULE06_CONTENT + '\n\n' + html[pos:]
    ok.append('Module 06 (password-cracking, privilege-escalation, maintaining-access, steganography) injected')
else:
    fail.append('INJECT_BEFORE marker missing for Module 06')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('=' * 55)
print('MODULE 06 CONTENT INJECTION COMPLETE')
print('=' * 55)
for s in ok: print(f'  [OK]  {s}')
for s in fail: print(f'  [FAIL] {s}')
print()
print(f'New size: {len(html):,} bytes / {html.count(chr(10)):,} lines')
