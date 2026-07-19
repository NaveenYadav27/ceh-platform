import re

def inject_m16_m20(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # PHASE 16: Wireless Security Specialist (Wireless Hacking)
    m16_content = """
    topics: [
      {
        id: "t16_01",
        title: "Wireless Security Auditing",
        scenario: "GFS is opening a new branch. As a Wireless Security Specialist, audit the new branch's Wi-Fi network (GFS-Branch-Guest) to ensure it uses WPA3 and is not susceptible to deauthentication or KRACK attacks.",
        commands: [
          { os: "Linux", cmd: "airmon-ng start wlan0" },
          { os: "Linux", cmd: "airodump-ng wlan0mon" }
        ],
        summary: [
          "WEP: Deprecated, easily cracked using IV collisions.",
          "WPA/WPA2: Uses PSK or Enterprise (802.1x). Vulnerable to dictionary attacks on the 4-way handshake.",
          "WPA3: Uses SAE (Simultaneous Authentication of Equals) to prevent dictionary attacks."
        ],
        flashcards: [
          { q: "What tool puts a wireless adapter into monitor mode?", a: "airmon-ng" },
          { q: "What vulnerability affects WPA2's 4-way handshake?", a: "KRACK (Key Reinstallation Attack)." }
        ],
        ctf: {
          scenario: "You captured a WPA2 handshake. What command extracts the handshake for cracking?",
          flag: "aircrack-ng -w wordlist.txt capture.cap",
          points: 50,
          hint: "Provide the basic aircrack-ng syntax with a wordlist (-w) and the capture file."
        }
      }
    ]
"""

    # PHASE 17: Mobile Security Engineer (Hacking Mobile Platforms)
    m17_content = """
    topics: [
      {
        id: "t17_01",
        title: "Mobile OS Vulnerabilities",
        scenario: "A GFS employee's corporate Android phone was compromised after installing an unverified trading app. Analyze the APK to find hardcoded AWS credentials.",
        commands: [
          { os: "Linux", cmd: "apktool d trading_app.apk" },
          { os: "Linux", cmd: "grep -r 'AKIA' trading_app/" }
        ],
        summary: [
          "Rooting (Android) / Jailbreaking (iOS): Removing OS restrictions, increasing attack surface.",
          "Reverse Engineering: Using tools like apktool to decompile apps.",
          "Mobile threats: Malicious apps, insecure data storage, weak cryptography."
        ],
        flashcards: [
          { q: "What does MDM stand for?", a: "Mobile Device Management." },
          { q: "What tool decompiles Android APKs?", a: "apktool" }
        ],
        ctf: {
          scenario: "You extracted the AndroidManifest.xml. What permission indicates the app can read SMS messages?",
          flag: "android.permission.READ_SMS",
          points: 50,
          hint: "Standard Android permission syntax for reading SMS."
        }
      }
    ]
"""

    # PHASE 18: OT/IoT Security Researcher (IoT & OT Hacking)
    m18_content = """
    topics: [
      {
        id: "t18_01",
        title: "IoT & OT Security",
        scenario: "The HVAC system in the GFS datacenter is managed by legacy IoT controllers. Test the MQTT protocol used by these devices for authentication bypass.",
        commands: [
          { os: "Linux", cmd: "nmap -p 1883 --script mqtt-subscribe 10.10.80.5" },
          { os: "Linux", cmd: "mosquitto_sub -h 10.10.80.5 -t '#'" }
        ],
        summary: [
          "IoT (Internet of Things): Smart devices, often lacking basic security.",
          "OT (Operational Technology): ICS, SCADA systems controlling physical processes.",
          "Common protocols: MQTT, CoAP, Modbus."
        ],
        flashcards: [
          { q: "What does SCADA stand for?", a: "Supervisory Control and Data Acquisition." },
          { q: "What port does MQTT commonly use?", a: "1883 (or 8883 over TLS)." }
        ],
        ctf: {
          scenario: "You subscribed to all MQTT topics. What is the payload of the message published to 'gfs/datacenter/hvac/temp'?",
          flag: "72F",
          points: 50,
          hint: "The flag is the temperature value transmitted."
        }
      }
    ]
"""

    # PHASE 19: Cloud Security Architect (Cloud Computing Threats)
    m19_content = """
    topics: [
      {
        id: "t19_01",
        title: "Cloud Infrastructure Attacks",
        scenario: "GFS is migrating to AWS. As a Cloud Security Architect, identify misconfigured S3 buckets that might leak sensitive customer financial data.",
        commands: [
          { os: "Linux", cmd: "aws s3 ls s3://gfs-customer-backups --no-sign-request" },
          { os: "Linux", cmd: "pacu" }
        ],
        summary: [
          "Shared Responsibility Model: Provider secures the cloud, customer secures data IN the cloud.",
          "Serverless architectures (Lambda) have their own attack vectors (Event Injection).",
          "IAM (Identity and Access Management) misconfigurations are a leading cause of breaches."
        ],
        flashcards: [
          { q: "What is an SSRF attack in the cloud?", a: "Server-Side Request Forgery, often used to access the instance metadata service (IMDS)." },
          { q: "What AWS service holds instance metadata?", a: "IMDS (Instance Metadata Service) at 169.254.169.254." }
        ],
        ctf: {
          scenario: "Extract the AWS access key ID from the metadata service response provided.",
          flag: "AKIAIOSFODNN7EXAMPLE",
          points: 50,
          hint: "Look for the string starting with AKIA."
        }
      }
    ]
"""

    # PHASE 20: Cryptographic Specialist (Cryptography)
    m20_content = """
    topics: [
      {
        id: "t20_01",
        title: "Applied Cryptography",
        scenario: "You have reached the final stage of your GFS career. A ransomware gang has encrypted a critical GFS database. Analyze the encryption implementation to find flaws or extract the key from memory.",
        commands: [
          { os: "Linux", cmd: "hashcat -m 1000 hashes.txt rockyou.txt" },
          { os: "Linux", cmd: "openssl rsa -in private.key -text -noout" }
        ],
        summary: [
          "Symmetric Encryption: Same key for encryption and decryption (AES, DES).",
          "Asymmetric Encryption: Public and Private key pairs (RSA, ECC).",
          "Hashing: One-way function (SHA-256, MD5)."
        ],
        flashcards: [
          { q: "What does PKI stand for?", a: "Public Key Infrastructure." },
          { q: "Which cryptographic attack exploits the fact that two different inputs produce the same hash?", a: "Collision Attack." }
        ],
        ctf: {
          scenario: "You found a hashed password: '5d41402abc4b2a76b9719d911017c592'. This is a very common MD5 hash. What is the plaintext?",
          flag: "hello",
          points: 50,
          hint: "Use an online hash cracker or recognize the classic MD5 for 'hello'."
        }
      }
    ]
"""

    html = re.sub(r'id:\s*"m16".*?topics:\s*\[.*?\]', f'id: "m16",\n    name: "Phase 16: Wireless Security Specialist (Wireless Hacking)",\n{m16_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m17".*?topics:\s*\[.*?\]', f'id: "m17",\n    name: "Phase 17: Mobile Security Engineer (Hacking Mobile Platforms)",\n{m17_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m18".*?topics:\s*\[.*?\]', f'id: "m18",\n    name: "Phase 18: OT/IoT Security Researcher (IoT & OT Hacking)",\n{m18_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m19".*?topics:\s*\[.*?\]', f'id: "m19",\n    name: "Phase 19: Cloud Security Architect (Cloud Computing Threats)",\n{m19_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m20".*?topics:\s*\[.*?\]', f'id: "m20",\n    name: "Phase 20: Cryptographic Specialist (Cryptography)",\n{m20_content}', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Content for Phases 16-20 injected successfully.")

inject_m16_m20('frontend/index.html')
