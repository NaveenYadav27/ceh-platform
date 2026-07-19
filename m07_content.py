import json
import os
import re

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'

def get_content():
    return [
        {
            "id": "malware-concepts",
            "content": {
                "eyebrow": "Module 07 · Topic 1",
                "title": "Malware Concepts",
                "module": "Phase 07: Malware Analyst",
                "sub": "Static vs Dynamic, APTs, and Droppers",
                "objectives": ["Understand static vs dynamic analysis", "Identify APT characteristics", "Explain malware droppers"],
                "learn": {
                    "simple": "Malware concepts encompass the fundamental theories of malicious software, including how it is created, propagated, and analyzed. Understanding the difference between static (examining code without running it) and dynamic (running it in a sandbox) analysis is key. Advanced Persistent Threats (APTs) represent sophisticated, long-term attacks, often state-sponsored, while droppers are specialized malware designed to install other malware.",
                    "analogy": "Think of a dropper as a trojan horse that smuggles an army (the actual malware payload) into a fortress (your computer). Static analysis is like reading the blueprints of the horse, while dynamic analysis is watching the horse operate in a safe, contained environment.",
                    "architecture": "A typical malware dropper is a lightweight executable, often polymorphic or packed to evade detection. Once executed, it reaches out to a Command and Control (C2) server to download the primary payload, decrypts it in memory, and executes it, typically employing process hollowing or DLL injection. APTs leverage these droppers as part of a multi-stage kill chain, establishing persistence through registry keys, WMI subscriptions, or scheduled tasks.",
                    "why": "Understanding these concepts is critical for enterprise defense because modern malware frequently evades traditional antivirus through obfuscation and multi-stage delivery mechanisms. Defense-in-depth requires analyzing both the delivery mechanism (dropper) and the payload."
                },
                "enterprise": {
                    "gfs": "At Global Financial Services, we observed an incident where a phishing email delivered a dropper disguised as a PDF. It attempted to download a banking trojan, but our EDR flagged the anomalous network connection.",
                    "windows": "In Windows, malware droppers often abuse legitimate binaries (Living off the Land) like bitsadmin.exe or powershell.exe to download payloads.",
                    "linux": "On Linux, attackers may use curl or wget in bash scripts, establishing persistence via cron jobs or systemd services."
                },
                "workflow": ["Step 1: Identify suspicious file.", "Step 2: Isolate the system.", "Step 3: Perform static analysis.", "Step 4: Perform dynamic analysis.", "Step 5: Extract IOCs.", "Step 6: Update defenses."],
                "diagram": {
                    "caption": "Click to interact with the diagram",
                    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"50\" y=\"50\" width=\"100\" height=\"50\" fill=\"#f00\"/><text x=\"75\" y=\"80\">Dropper</text></svg>"
                },
                "commands": {
                    "lin": [
                        { "cmd": "strings suspicious_file | grep http", "purpose": "Extract URLs from dropper", "out": "http://c2.example.com", "note": "Basic static analysis", "mistake": "Running the executable instead of strings" }
                    ],
                    "win": [
                        { "cmd": "Get-FileHash suspicious_file.exe", "purpose": "Calculate hash for OSINT lookup", "out": "SHA256 hash", "note": "Check VirusTotal", "mistake": "Relying only on MD5" }
                    ]
                },
                "lab": {
                    "type": "guided",
                    "difficulty": "Advanced",
                    "duration": "45",
                    "platform": "Kali Linux",
                    "environment": "Local Lab",
                    "tools": ["YARA", "Cuckoo"],
                    "dependencies": [],
                    "safety": ["Perform this lab only in an isolated sandbox environment."],
                    "scenario": "GFS incident response team needs to analyze a suspected dropper found on a trading terminal.",
                    "objectives": ["Identify the C2 domain using static analysis."],
                    "steps": ["Step 1: Run strings against the malware sample with `strings sample.exe`."],
                    "evidence": ["Terminal output showing the extracted domain."],
                    "validation": ["You should see: evil-c2.com"],
                    "troubleshooting": ["If no output, try using a deobfuscator."],
                    "mitre": [{ "id": "T1106", "name": "Native API", "tactic": "Execution" }],
                    "cleanup": ["Revert the sandbox VM."]
                },
                "quiz": [
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the primary function of a malware dropper?",
                        "opts": ["To encrypt files", "To download and install other malware", "To steal passwords", "To launch DDoS attacks"],
                        "correct": 1,
                        "fb": "A dropper's main purpose is to 'drop' or install the primary malware payload onto the system."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Which analysis method involves executing the malware?",
                        "opts": ["Static analysis", "Dynamic analysis", "Heuristic analysis", "Signature analysis"],
                        "correct": 1,
                        "fb": "Dynamic analysis involves running the malware in a controlled environment to observe its behavior."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What does APT stand for?",
                        "opts": ["Advanced Persistent Threat", "Automated Phishing Tool", "Active Process Tracker", "Advanced Payload Trojan"],
                        "correct": 0,
                        "fb": "APT stands for Advanced Persistent Threat, typically state-sponsored actors."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Static analysis requires running the malware in a sandbox.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. Static analysis examines the code without executing it."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "Which technique is commonly used by droppers to evade static analysis?",
                        "opts": ["Code signing", "Packing", "Network encryption", "Privilege escalation"],
                        "correct": 1,
                        "fb": "Packing compresses and obfuscates the executable, making static analysis difficult."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is a C2 server?",
                        "opts": ["Command and Control server", "Cryptographic Calculation server", "Client-to-Client server", "Core Configuration server"],
                        "correct": 0,
                        "fb": "C2 stands for Command and Control, used by attackers to manage malware."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Droppers always contain the full malware payload within themselves.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. They often download the payload from a C2 server."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Which of the following is a characteristic of an APT?",
                        "opts": ["Short-term attack", "Random targets", "Long-term persistence", "Loud, disruptive attacks"],
                        "correct": 2,
                        "fb": "APTs aim to maintain long-term, undetected access to the target network."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "What is process hollowing?",
                        "opts": ["A denial of service attack", "Injecting malicious code into a legitimate process", "Deleting system files", "Extracting passwords from memory"],
                        "correct": 1,
                        "fb": "Process hollowing involves replacing the code of a legitimate process with malicious code."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Dynamic analysis is safer than static analysis because the malware is contained.",
                        "opts": ["True", "False"],
                        "correct": 0,
                        "fb": "True, but both have their uses. Static analysis is inherently safe because the code isn't executed."
                    }
                ],
                "flashcards": [
                    { "f": "Dropper", "b": "Malware designed to install other malware payloads." },
                    { "f": "APT", "b": "Advanced Persistent Threat; a sophisticated, long-term cyberattack." }
                ],
                "summary": ["Malware concepts include droppers, APTs, and analysis techniques.", "Static analysis examines code without running it.", "Dynamic analysis observes malware behavior in a sandbox.", "Droppers deliver primary payloads.", "APTs are stealthy, long-term threats."],
                "outcomes": ["Explain static vs dynamic analysis.", "Identify characteristics of APTs and droppers."],
                "meta": {
                    "contentVersion": "1.0.0",
                    "estimatedTime": 45,
                    "difficulty": "Advanced",
                    "prerequisites": [],
                    "lastReviewed": "2026-07-18"
                }
            }
        },
        {
            "id": "trojans-backdoors",
            "content": {
                "eyebrow": "Module 07 · Topic 2",
                "title": "Trojans and Backdoors",
                "module": "Phase 07: Malware Analyst",
                "sub": "RATs, Banking Trojans, Wrappers, and Crypters",
                "objectives": ["Understand RAT capabilities", "Identify banking trojans", "Explain wrappers and crypters"],
                "learn": {
                    "simple": "Trojans disguise themselves as legitimate software to trick users into executing them. Once running, they can establish backdoors, allowing attackers unauthorized access. Remote Access Trojans (RATs) provide full control over the compromised system. Banking trojans specifically target financial information, while wrappers and crypters are tools used by attackers to hide malware from antivirus software.",
                    "analogy": "A trojan is like a Greek wooden horse. It looks like a gift (a legitimate app), but inside are soldiers (malicious code). A crypter is like a cloaking device that hides the horse from guards (antivirus) until it's inside the city walls.",
                    "architecture": "Banking trojans like TrickBot or Emotet use web injects to modify banking pages in the victim's browser, capturing credentials. RATs establish a reverse TCP shell back to the C2 server, bypassing inbound firewall rules. Attackers use crypters to encrypt the malware payload; the executable includes a small stub that decrypts the payload in memory at runtime, a technique known as 'RunPE'.",
                    "why": "Trojans are a primary vector for initial access in enterprise breaches. The use of crypters makes detection based on traditional signatures ineffective, necessitating behavioral analysis."
                },
                "enterprise": {
                    "gfs": "GFS thwarted an attack where a fake software update wrapper delivered a banking trojan designed to intercept wire transfer approvals.",
                    "windows": "Trojans often exploit Windows user privileges, tricking users into accepting UAC prompts to gain SYSTEM access.",
                    "linux": "Linux backdoors may modify SSH binaries or install rootkits to maintain access."
                },
                "workflow": ["Step 1: Monitor network traffic for unusual connections.", "Step 2: Investigate unknown processes.", "Step 3: Analyze startup items and registry keys.", "Step 4: Contain the infected host.", "Step 5: Reverse engineer the payload.", "Step 6: Deploy IoCs to security appliances."],
                "diagram": {
                    "caption": "Click to interact with the diagram",
                    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><circle cx=\"300\" cy=\"200\" r=\"50\" fill=\"#00f\"/><text x=\"280\" y=\"205\" fill=\"#fff\">Trojan</text></svg>"
                },
                "commands": {
                    "lin": [
                        { "cmd": "netstat -anp | grep ESTABLISHED", "purpose": "Find active connections", "out": "IP addresses and PIDs", "note": "Look for unusual ports", "mistake": "Ignoring short-lived connections" }
                    ],
                    "win": [
                        { "cmd": "netstat -ano | findstr ESTABLISHED", "purpose": "Find active connections", "out": "IP addresses and PIDs", "note": "Correlate PID with task manager", "mistake": "Not running as administrator" }
                    ]
                },
                "lab": {
                    "type": "guided",
                    "difficulty": "Advanced",
                    "duration": "45",
                    "platform": "Windows 10",
                    "environment": "Local Lab",
                    "tools": ["Process Hacker", "Wireshark"],
                    "dependencies": [],
                    "safety": ["Perform this lab only in an isolated sandbox environment."],
                    "scenario": "Investigate a workstation suspected of hosting a RAT connecting to an external C2.",
                    "objectives": ["Identify the malicious process and its C2 IP."],
                    "steps": ["Step 1: Run netstat to find established connections with `netstat -ano`."],
                    "evidence": ["Screenshot of the malicious connection."],
                    "validation": ["You should see: connection to 10.10.10.55 on port 4444"],
                    "troubleshooting": ["If process terminates, check persistence mechanisms."],
                    "mitre": [{ "id": "T1071", "name": "Application Layer Protocol", "tactic": "Command and Control" }],
                    "cleanup": ["Revert the sandbox VM."]
                },
                "quiz": [
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the main purpose of a RAT?",
                        "opts": ["To steal passwords locally", "To provide remote administrative control to the attacker", "To encrypt files for ransom", "To spread to other computers"],
                        "correct": 1,
                        "fb": "RAT stands for Remote Access Trojan, giving the attacker control over the infected system."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What tool do attackers use to combine a legitimate executable with a malicious one?",
                        "opts": ["Crypter", "Wrapper", "Packer", "Obfuscator"],
                        "correct": 1,
                        "fb": "A wrapper combines two executables into one."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Banking trojans only steal data; they do not alter web pages.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. They often use web injects to alter what the user sees on banking sites."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "How does a crypter evade antivirus detection?",
                        "opts": ["By changing the file extension", "By encrypting the malicious payload and decrypting it in memory", "By deleting the antivirus software", "By hiding in the recycle bin"],
                        "correct": 1,
                        "fb": "Crypters encrypt the payload on disk, only decrypting it when run in memory."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Which of the following is a common persistence mechanism for Windows trojans?",
                        "opts": ["/etc/shadow", "Registry Run keys", "cron jobs", "DNS cache"],
                        "correct": 1,
                        "fb": "Registry Run keys are a very common way for malware to start on Windows boot."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Trojans typically self-replicate to spread across a network.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. Trojans require user interaction (like clicking a link or running a file) to spread. Viruses and worms self-replicate."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is 'RunPE'?",
                        "opts": ["A process enumeration tool", "A technique to run executables from memory, often used by crypters", "A Windows built-in security feature", "A type of ransomware"],
                        "correct": 1,
                        "fb": "RunPE (Run Portable Executable) is a technique for loading an executable directly into memory, bypassing disk scanning."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the primary difference between a backdoor and a trojan?",
                        "opts": ["A trojan is the delivery mechanism; a backdoor is the access provided", "A backdoor is hardware; a trojan is software", "They are the exact same thing", "A backdoor requires physical access"],
                        "correct": 0,
                        "fb": "A trojan is how the malware gets in (disguised), while the backdoor is the unauthorized access channel it creates."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "Which technique do banking trojans use to intercept credentials before they are encrypted by TLS?",
                        "opts": ["DNS spoofing", "ARP poisoning", "Form grabbing / Web injects", "MAC flooding"],
                        "correct": 2,
                        "fb": "Form grabbing and web injects capture the data within the browser before it hits the network stack."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Using a wrapper guarantees the malware will bypass antivirus.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. Modern AV can unpack or dynamically analyze wrapped files."
                    }
                ],
                "flashcards": [
                    { "f": "RAT", "b": "Remote Access Trojan, giving an attacker control." },
                    { "f": "Crypter", "b": "Software used to encrypt malware to evade AV detection." }
                ],
                "summary": ["Trojans disguise themselves as legitimate software.", "RATs provide remote control to attackers.", "Banking trojans target financial data using web injects.", "Wrappers bundle malware with legitimate files.", "Crypters encrypt malware to evade signature-based detection."],
                "outcomes": ["Explain RATs and backdoors.", "Identify the purpose of wrappers and crypters."],
                "meta": {
                    "contentVersion": "1.0.0",
                    "estimatedTime": 45,
                    "difficulty": "Advanced",
                    "prerequisites": [],
                    "lastReviewed": "2026-07-18"
                }
            }
        },
        {
            "id": "viruses-worms",
            "content": {
                "eyebrow": "Module 07 · Topic 3",
                "title": "Viruses and Worms",
                "module": "Phase 07: Malware Analyst",
                "sub": "Ransomware, File Infection, and Propagation",
                "objectives": ["Differentiate viruses and worms", "Understand ransomware mechanics", "Identify propagation techniques"],
                "learn": {
                    "simple": "Viruses and worms are self-replicating malware. A virus requires a host file and user interaction to spread, while a worm is standalone and exploits network vulnerabilities to propagate automatically. Ransomware, which can be delivered via viruses, worms, or trojans, encrypts the victim's files and demands payment for the decryption key.",
                    "analogy": "A virus is like a biological virus; it needs a host (a file) to infect. A worm is like a mold spore; it drifts on the wind (the network) and grows wherever it lands, without needing a specific host.",
                    "architecture": "A file infector virus modifies an executable, inserting its malicious payload and modifying the entry point (OEP). When the file runs, the virus executes first, then passes control to the original program. Worms, like WannaCry, use exploits (e.g., EternalBlue/SMBv1) to scan the network, find vulnerable hosts, and execute arbitrary code to copy themselves over. Ransomware utilizes asymmetric cryptography (RSA) to encrypt a symmetric key (AES) which encrypts the actual files.",
                    "why": "Worms can cause rapid, catastrophic failure across an enterprise network. Ransomware attacks pose significant financial and reputational risks."
                },
                "enterprise": {
                    "gfs": "To protect against worms, GFS segments its network and strictly manages patch deployments to close vulnerabilities before they can be exploited.",
                    "windows": "Ransomware on Windows typically targets documents and database files, often disabling Volume Shadow Copies (vssadmin) to prevent recovery.",
                    "linux": "Linux worms often target vulnerable web applications or weak SSH credentials for lateral movement."
                },
                "workflow": ["Step 1: Disconnect infected systems from the network immediately.", "Step 2: Identify the propagation vector.", "Step 3: Block the exploit or port.", "Step 4: Locate patient zero.", "Step 5: Restore from offline backups.", "Step 6: Patch vulnerabilities."],
                "diagram": {
                    "caption": "Click to interact with the diagram",
                    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><polygon points=\"300,100 400,300 200,300\" fill=\"#0f0\"/><text x=\"270\" y=\"220\">Worm</text></svg>"
                },
                "commands": {
                    "lin": [
                        { "cmd": "iptables -A INPUT -p tcp --dport 445 -j DROP", "purpose": "Block SMB traffic to stop worm propagation", "out": "No output", "note": "Temporary mitigation", "mistake": "Blocking all traffic unnecessarily" }
                    ],
                    "win": [
                        { "cmd": "vssadmin list shadows", "purpose": "Check if ransomware deleted shadow copies", "out": "List of shadow copies or error", "note": "Ransomware often deletes these", "mistake": "Relying solely on shadow copies for backup" }
                    ]
                },
                "lab": {
                    "type": "guided",
                    "difficulty": "Advanced",
                    "duration": "45",
                    "platform": "Windows 10",
                    "environment": "Local Lab",
                    "tools": ["Sysinternals", "Wireshark"],
                    "dependencies": [],
                    "safety": ["Perform this lab only in an isolated sandbox environment."],
                    "scenario": "Analyze the network traffic of a simulated worm attempting lateral movement via SMB.",
                    "objectives": ["Identify the scanning behavior and targeted ports."],
                    "steps": ["Step 1: Capture traffic in Wireshark and filter by `tcp.port == 445`."],
                    "evidence": ["PCAP showing excessive ARP requests and SYN packets to port 445."],
                    "validation": ["You should see: port scans originating from the infected IP."],
                    "troubleshooting": ["Ensure the vulnerable VM is online in the sandbox."],
                    "mitre": [{ "id": "T1210", "name": "Exploitation of Remote Services", "tactic": "Lateral Movement" }],
                    "cleanup": ["Revert the sandbox VM."]
                },
                "quiz": [
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the primary difference between a virus and a worm?",
                        "opts": ["Viruses are more dangerous", "Worms do not require a host file or user interaction to spread", "Viruses spread via network exploits", "Worms only infect Linux systems"],
                        "correct": 1,
                        "fb": "Worms are self-propagating and exploit network vulnerabilities, while viruses attach to host files."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What action does ransomware typically take to prevent recovery?",
                        "opts": ["Deletes the OS", "Encrypts files and deletes Volume Shadow Copies", "Changes the user password", "Formats the hard drive"],
                        "correct": 1,
                        "fb": "Ransomware deletes shadow copies (backups) and encrypts files."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "A worm requires a user to click an executable to spread across the network.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. Worms spread automatically by exploiting vulnerabilities."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "Which cryptography scheme is commonly used by modern ransomware to secure the decryption key?",
                        "opts": ["Symmetric only (e.g., AES)", "Asymmetric (e.g., RSA) to encrypt a Symmetric key", "Hashing (e.g., SHA-256)", "Base64 encoding"],
                        "correct": 1,
                        "fb": "Ransomware uses a symmetric key for fast file encryption, and encrypts that key with an asymmetric public key."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Which of the following is a famous example of a worm that exploited SMBv1?",
                        "opts": ["Zeus", "WannaCry", "Emotet", "Stuxnet"],
                        "correct": 1,
                        "fb": "WannaCry was a massive ransomware worm that exploited the EternalBlue vulnerability in SMBv1."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "File infector viruses modify the original executable file.",
                        "opts": ["True", "False"],
                        "correct": 0,
                        "fb": "True. They insert malicious code and change the execution flow."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the 'OEP' in the context of file infectors?",
                        "opts": ["Original Execution Priority", "Original Entry Point", "Obfuscated Encryption Payload", "Open Enterprise Protocol"],
                        "correct": 1,
                        "fb": "OEP (Original Entry Point) is where the legitimate program starts, which viruses often modify."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "How can network segmentation mitigate worm propagation?",
                        "opts": ["By encrypting all traffic", "By updating antivirus signatures", "By restricting traffic flow between different network zones", "By disabling the firewall"],
                        "correct": 2,
                        "fb": "Segmentation prevents a worm on one subnet from easily reaching and infecting systems on another subnet."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Paying the ransom guarantees that your files will be decrypted.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. You are dealing with criminals; there is no guarantee they will provide the key."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Which command is often used by ransomware on Windows to delete shadow copies?",
                        "opts": ["del *.*", "vssadmin delete shadows /all /quiet", "format c:", "rmdir /s /q"],
                        "correct": 1,
                        "fb": "vssadmin is the legitimate tool abused to delete Volume Shadow Copies."
                    }
                ],
                "flashcards": [
                    { "f": "Worm", "b": "Standalone malware that propagates automatically over networks." },
                    { "f": "Ransomware", "b": "Malware that encrypts files and demands payment." }
                ],
                "summary": ["Viruses require a host file and user interaction.", "Worms propagate automatically by exploiting network vulnerabilities.", "Ransomware encrypts files and deletes backups.", "WannaCry is a classic example of a ransomware worm.", "Network segmentation and patching are key defenses against worms."],
                "outcomes": ["Differentiate viruses and worms.", "Understand ransomware encryption mechanisms."],
                "meta": {
                    "contentVersion": "1.0.0",
                    "estimatedTime": 45,
                    "difficulty": "Advanced",
                    "prerequisites": [],
                    "lastReviewed": "2026-07-18"
                }
            }
        },
        {
            "id": "fileless-malware",
            "content": {
                "eyebrow": "Module 07 · Topic 4",
                "title": "Fileless Malware",
                "module": "Phase 07: Malware Analyst",
                "sub": "Living off the Land, PowerShell, WMI, and Memory Injection",
                "objectives": ["Understand fileless malware concepts", "Identify LoTL techniques", "Analyze malicious PowerShell"],
                "learn": {
                    "simple": "Fileless malware is a type of malicious activity that uses native, legitimate tools built into the operating system (like PowerShell or WMI) to execute attacks. Instead of dropping a traditional executable file (.exe) onto the hard drive, it operates entirely in memory or hides within registry keys. This approach, known as 'Living off the Land' (LoTL), makes detection by traditional signature-based antivirus extremely difficult.",
                    "analogy": "Imagine a burglar who breaks into a house not by bringing their own tools, but by finding the homeowner's tools in the garage and using them to open the safe. Because they use the owner's tools, it's harder to prove they brought anything suspicious.",
                    "architecture": "A fileless attack often begins with a malicious macro in a Word document or a drive-by download. This triggers a script (e.g., PowerShell) that downloads a payload directly into RAM (Reflective DLL Injection) without writing it to disk. Persistence is achieved by creating WMI event subscriptions or adding scripts to the Windows Registry. Attackers abuse dual-use tools like certutil or mshta to download and execute code.",
                    "why": "Fileless malware is pervasive in advanced attacks because it evades traditional file scanning. Defending against it requires behavior monitoring, script logging, and endpoint detection and response (EDR) solutions."
                },
                "enterprise": {
                    "gfs": "GFS mitigates fileless threats by enforcing PowerShell Constrained Language Mode and enabling Script Block Logging, ensuring all commands are audited.",
                    "windows": "Windows is the primary target for fileless malware due to the power of PowerShell, WMI, and the Registry.",
                    "linux": "Linux fileless attacks might involve executing scripts directly from memory using bash features (e.g., `curl | bash`) or abusing tools like Python."
                },
                "workflow": ["Step 1: Enable PowerShell Script Block Logging.", "Step 2: Monitor process execution (Sysmon Event ID 1).", "Step 3: Analyze command-line arguments for obfuscation.", "Step 4: Hunt for unusual WMI activity.", "Step 5: Check registry run keys.", "Step 6: Implement application whitelisting."],
                "diagram": {
                    "caption": "Click to interact with the diagram",
                    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><text x=\"200\" y=\"200\" font-size=\"24\">RAM (No Disk Write)</text></svg>"
                },
                "commands": {
                    "lin": [
                        { "cmd": "history | grep curl", "purpose": "Find potentially malicious downloads", "out": "Command history", "note": "Attackers may clear history", "mistake": "Only checking history, not memory" }
                    ],
                    "win": [
                        { "cmd": "Get-WmiObject -Namespace root\\subscription -Class __EventFilter", "purpose": "Hunt for WMI persistence", "out": "WMI event filters", "note": "Look for unknown filters", "mistake": "Ignoring WMI as a persistence mechanism" }
                    ]
                },
                "lab": {
                    "type": "guided",
                    "difficulty": "Advanced",
                    "duration": "45",
                    "platform": "Windows 10",
                    "environment": "Local Lab",
                    "tools": ["Sysmon", "Event Viewer"],
                    "dependencies": [],
                    "safety": ["Perform this lab only in an isolated sandbox environment."],
                    "scenario": "Investigate an alert indicating suspicious PowerShell activity utilizing Base64 encoding.",
                    "objectives": ["Decode the malicious PowerShell command and identify its intent."],
                    "steps": ["Step 1: Check Windows Event Logs for PowerShell Event ID 4104 (Script Block Logging).", "Step 2: Decode the Base64 string found in the log."],
                    "evidence": ["Decoded payload showing an attempted download."],
                    "validation": ["You should see: IEX (New-Object Net.WebClient).DownloadString(...)"],
                    "troubleshooting": ["Ensure Script Block Logging is enabled via GPO in the lab."],
                    "mitre": [{ "id": "T1059.001", "name": "PowerShell", "tactic": "Execution" }],
                    "cleanup": ["Revert the sandbox VM."]
                },
                "quiz": [
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the defining characteristic of fileless malware?",
                        "opts": ["It only infects Linux", "It operates primarily in memory using native OS tools", "It does not use the network", "It requires physical access"],
                        "correct": 1,
                        "fb": "Fileless malware avoids writing executables to disk, running in memory via tools like PowerShell."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What does LoTL stand for in cybersecurity?",
                        "opts": ["Living on the LAN", "Living off the Land", "Local Threat Logging", "Loss of Trust Level"],
                        "correct": 1,
                        "fb": "Living off the Land refers to using legitimate, pre-installed tools for malicious purposes."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Traditional signature-based antivirus is highly effective against fileless malware.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. Since there is no traditional executable file to scan, signature-based AV often misses fileless attacks."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "Which Windows feature is frequently abused for fileless persistence?",
                        "opts": ["Windows Defender", "WMI (Windows Management Instrumentation)", "BitLocker", "Hyper-V"],
                        "correct": 1,
                        "fb": "Attackers create WMI event subscriptions to execute scripts persistently without traditional run keys."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Why do attackers encode PowerShell commands in Base64?",
                        "opts": ["To make them execute faster", "To evade command-line inspection and logging", "To compress the payload", "Because PowerShell only understands Base64"],
                        "correct": 1,
                        "fb": "Base64 encoding obfuscates the command, bypassing simple string-matching detection rules."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Fileless malware never writes any data to the hard drive.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. While it avoids executables, it may write scripts or configurations to the registry."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Which Sysinternals tool is highly recommended for logging process creations with command-line arguments?",
                        "opts": ["Process Explorer", "Sysmon (System Monitor)", "Autoruns", "TCPView"],
                        "correct": 1,
                        "fb": "Sysmon logs detailed process creation events (Event ID 1), crucial for spotting malicious command lines."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "What is Reflective DLL Injection?",
                        "opts": ["Writing a DLL to disk and loading it via the registry", "Loading a DLL directly from memory without saving it to disk", "Replacing a legitimate Windows DLL", "Using a DLL to bypass UAC"],
                        "correct": 1,
                        "fb": "Reflective DLL injection allows an attacker to load a DLL entirely from memory, leaving no artifact on disk."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the best defense against malicious PowerShell scripts in an enterprise environment?",
                        "opts": ["Uninstalling PowerShell", "Using Constrained Language Mode and Script Block Logging", "Disabling the command prompt", "Installing a third-party firewall"],
                        "correct": 1,
                        "fb": "Constrained Language Mode limits capabilities, and logging provides visibility into executed scripts."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Fileless attacks can begin with a malicious macro in a Microsoft Word document.",
                        "opts": ["True", "False"],
                        "correct": 0,
                        "fb": "True. The macro executes a script (like PowerShell) that downloads and runs the payload in memory."
                    }
                ],
                "flashcards": [
                    { "f": "Fileless Malware", "b": "Malware that operates in memory using native OS tools." },
                    { "f": "LoTL", "b": "Living off the Land; using built-in tools for attacks." }
                ],
                "summary": ["Fileless malware evades traditional AV by operating in memory.", "LoTL uses native tools like PowerShell and WMI.", "Persistence is often achieved via Registry or WMI.", "Base64 encoding is commonly used to obfuscate commands.", "Defenses include Script Block Logging and EDR."],
                "outcomes": ["Understand Living off the Land techniques.", "Identify methods for detecting fileless malware."],
                "meta": {
                    "contentVersion": "1.0.0",
                    "estimatedTime": 45,
                    "difficulty": "Advanced",
                    "prerequisites": [],
                    "lastReviewed": "2026-07-18"
                }
            }
        },
        {
            "id": "malware-analysis",
            "content": {
                "eyebrow": "Module 07 · Topic 5",
                "title": "Malware Analysis",
                "module": "Phase 07: Malware Analyst",
                "sub": "YARA rules, Cuckoo sandbox, and Reversing basics",
                "objectives": ["Write YARA rules", "Understand sandbox analysis", "Explain basic reverse engineering"],
                "learn": {
                    "simple": "Malware analysis is the process of understanding the behavior and purpose of a suspicious file. It is divided into static analysis (examining code without running it) and dynamic analysis (running it in a secure environment like a Cuckoo sandbox). YARA is a powerful tool used to identify and classify malware based on textual or binary patterns. Reverse engineering involves taking the compiled malware and decompiling or disassembling it to understand its core logic.",
                    "analogy": "Malware analysis is like investigating a suspected bomb. Static analysis is x-raying it to see the wires and components. Dynamic analysis is detonating it in a reinforced bunker to see the blast radius. Reverse engineering is carefully taking it apart piece by piece.",
                    "architecture": "A malware analyst uses tools like IDA Pro or Ghidra for reverse engineering, reading assembly language (x86/x64) to trace the execution flow. They look for API calls (e.g., CreateRemoteThread, VirtualAllocEx) indicative of malicious activity. YARA rules use boolean expressions to match strings, hex byte sequences, or regular expressions within files. A Cuckoo Sandbox automates dynamic analysis, running the malware in a VM and generating a report on network activity, file system changes, and API hooking.",
                    "why": "In-house malware analysis allows enterprises to extract Indicators of Compromise (IoCs) specific to targeted attacks, enabling proactive defense and threat hunting."
                },
                "enterprise": {
                    "gfs": "GFS uses a combination of automated sandbox analysis for initial triage and manual reverse engineering for complex, targeted APT payloads.",
                    "windows": "Analyzing Windows malware requires deep understanding of the PE (Portable Executable) file format and the Windows API.",
                    "linux": "Linux malware analysis involves analyzing ELF binaries and understanding Linux system calls."
                },
                "workflow": ["Step 1: Set up an isolated analysis environment.", "Step 2: Obtain the malware hash and check OSINT.", "Step 3: Perform basic static analysis (strings, PE headers).", "Step 4: Perform dynamic analysis in a sandbox.", "Step 5: Write YARA rules based on findings.", "Step 6: Perform advanced reverse engineering if needed."],
                "diagram": {
                    "caption": "Click to interact with the diagram",
                    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"200\" y=\"150\" width=\"200\" height=\"100\" fill=\"#aaa\"/><text x=\"250\" y=\"200\">Cuckoo Sandbox</text></svg>"
                },
                "commands": {
                    "lin": [
                        { "cmd": "yara -m rules.yar suspicious_file", "purpose": "Scan for malware signatures", "out": "Matched rule names", "note": "Requires updated signatures", "mistake": "Scanning without updating rules" }
                    ],
                    "win": [
                        { "cmd": "strings.exe -a malware.exe > output.txt", "purpose": "Extract human-readable strings from binary", "out": "Text strings", "note": "Useful for finding URLs and IPs", "mistake": "Ignoring Unicode strings" }
                    ]
                },
                "lab": {
                    "type": "guided",
                    "difficulty": "Advanced",
                    "duration": "45",
                    "platform": "Kali Linux",
                    "environment": "Local Lab",
                    "tools": ["YARA", "Strings"],
                    "dependencies": [],
                    "safety": ["Perform this lab only in an isolated sandbox environment."],
                    "scenario": "Create a custom YARA rule to detect a specific variant of ransomware found on a GFS server.",
                    "objectives": ["Extract strings and write a functional YARA rule."],
                    "steps": ["Step 1: Extract strings from the sample.", "Step 2: Create a YARA rule matching the unique ransom note string."],
                    "evidence": ["Successful execution of the YARA rule against the sample."],
                    "validation": ["You should see: Ransomware_Rule_Matched"],
                    "troubleshooting": ["Check YARA syntax if the rule fails to compile."],
                    "mitre": [{ "id": "T1059", "name": "Command and Scripting Interpreter", "tactic": "Execution" }],
                    "cleanup": ["Revert the sandbox VM."]
                },
                "quiz": [
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is the primary purpose of a Cuckoo sandbox?",
                        "opts": ["To write YARA rules", "To safely perform dynamic malware analysis", "To decompile malware", "To scan for vulnerabilities"],
                        "correct": 1,
                        "fb": "Cuckoo is an automated dynamic malware analysis system."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What does a YARA rule primarily do?",
                        "opts": ["Blocks network traffic", "Identifies malware based on textual or binary patterns", "Encrypts sensitive files", "Reverses compiled code"],
                        "correct": 1,
                        "fb": "YARA helps classify malware by looking for specific strings or byte sequences."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Static analysis requires executing the malware.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. Static analysis involves examining the file without running it."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "Which tool is commonly used for disassembling and decompiling malware?",
                        "opts": ["Wireshark", "Nmap", "Ghidra", "Metasploit"],
                        "correct": 2,
                        "fb": "Ghidra (and IDA Pro) are the standard tools for reverse engineering binaries."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "When analyzing Windows malware, what is the PE file format?",
                        "opts": ["Private Execution", "Portable Executable", "Pre-Compiled Environment", "Primary Extractor"],
                        "correct": 1,
                        "fb": "The Portable Executable (PE) format is used for executables, object code, and DLLs in Windows."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "Extracting 'strings' from a binary is a form of dynamic analysis.",
                        "opts": ["True", "False"],
                        "correct": 1,
                        "fb": "False. It is a form of basic static analysis because the file is not executed."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "What is a major limitation of basic static analysis?",
                        "opts": ["It is too dangerous", "It requires an internet connection", "It can be defeated by packers and obfuscators", "It only works on Linux"],
                        "correct": 2,
                        "fb": "Packers encrypt or compress the code, hiding the true strings and imports from static analysis tools."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Advanced",
                        "q": "In reverse engineering, what does x86 Assembly language represent?",
                        "opts": ["High-level source code", "Human-readable representation of machine code", "Encrypted network traffic", "YARA rule syntax"],
                        "correct": 1,
                        "fb": "Assembly language is the lowest human-readable level of programming, translating directly to machine instructions."
                    },
                    {
                        "type": "multiple-choice",
                        "difficulty": "Intermediate",
                        "q": "Why is a sandbox environment critical for malware analysis?",
                        "opts": ["It prevents the malware from infecting the host system or network", "It makes the malware run faster", "It automatically writes the malware report", "It provides a legal shield"],
                        "correct": 0,
                        "fb": "A sandbox isolates the malware to prevent accidental infection and damage."
                    },
                    {
                        "type": "true-false",
                        "difficulty": "Easy",
                        "q": "YARA rules can match both text strings and hexadecimal byte sequences.",
                        "opts": ["True", "False"],
                        "correct": 0,
                        "fb": "True. YARA is highly versatile and can match various patterns."
                    }
                ],
                "flashcards": [
                    { "f": "YARA", "b": "Tool used to identify malware based on patterns." },
                    { "f": "Sandbox", "b": "Isolated environment for safely running dynamic analysis." }
                ],
                "summary": ["Malware analysis involves static and dynamic techniques.", "YARA uses rules to classify malware based on patterns.", "Cuckoo automates dynamic analysis in a sandbox.", "Reverse engineering uses tools like Ghidra to analyze code.", "Analysis provides IoCs for enterprise defense."],
                "outcomes": ["Write basic YARA rules.", "Explain the purpose of a malware sandbox."],
                "meta": {
                    "contentVersion": "1.0.0",
                    "estimatedTime": 45,
                    "difficulty": "Advanced",
                    "prerequisites": [],
                    "lastReviewed": "2026-07-18"
                }
            }
        }
    ]

def inject():
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print("Failed to read html:", e)
        return
        
    marker = "// ── TAB WIRING ──"
    if marker not in content:
        print("Marker not found.")
        return
        
    injection = ""
    for topic in get_content():
        # format as javascript assignment
        injection += f"CONTENT['{topic['id']}'] = {json.dumps(topic['content'], indent=2)};\n\n"
        
    new_content = content.replace(marker, injection + marker)
    
    try:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected content for Module 07.")
    except Exception as e:
        print("Failed to write html:", e)

if __name__ == "__main__":
    inject()
