import os
import json

HTML_PATH = 'frontend/index.html'

m17_topics = {
    'mobile-concepts': {
        'eyebrow': 'Module 17 · Topic 1',
        'title': 'Mobile Platform Concepts',
        'module': 'Phase 17: Mobile Security Expert',
        'sub': 'Understand the fundamental architecture and security models of modern mobile operating systems.',
        'objectives': [
            'Analyze mobile device architectures.',
            'Understand mobile security models.',
            'Identify mobile attack vectors.'
        ],
        'learn': {
            'simple': 'Mobile platforms like Android and iOS are full-fledged operating systems designed for portability, touch interfaces, and constant connectivity. They employ sandboxing, permission models, and code signing to isolate applications and protect user data.',
            'analogy': 'Think of a mobile OS as an apartment building where each app has its own locked apartment. They can only use shared facilities (like the camera or GPS) if the building manager (the OS) grants them a specific key.',
            'architecture': 'Mobile architectures are built on a layered model. At the bottom is the kernel (Linux for Android, XNU for iOS), which handles hardware abstraction and core services. Above this sit system libraries and runtime environments (like ART in Android). The application framework provides APIs for developers, and the topmost layer contains the apps themselves. Security mechanisms like hardware-backed keystores and secure enclaves are tightly integrated into this stack to protect sensitive operations.',
            'why': 'With the shift to remote work and BYOD policies, mobile devices are a primary gateway into enterprise networks. Understanding their underlying concepts is crucial for securing corporate data.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, employees access trading dashboards and client data via mobile devices, making endpoint security a top priority.',
            'windows': 'Integration with Microsoft Intune for MDM allows enforcing policies on mobile devices accessing the corporate Windows environment.',
            'linux': 'Linux servers often host the backend APIs that mobile applications consume, requiring robust authentication and secure transport.'
        },
        'workflow': [
            'Step 1: Review mobile device policies.',
            'Step 2: Identify deployed mobile platforms (iOS, Android).',
            'Step 3: Analyze application permissions.',
            'Step 4: Assess device encryption status.',
            'Step 5: Verify MDM enrollment.',
            'Step 6: Monitor for unauthorized jailbroken or rooted devices.'
        ],
        'diagram': {
            'caption': 'Mobile Platform Architecture',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f0f0f0"/><text x="300" y="200" text-anchor="middle" font-size="24">Mobile Architecture Layers</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'dmesg | grep -i usb', 'purpose': 'Check connected USB devices', 'out': 'USB connection logs', 'note': 'Useful when attaching a mobile device', 'mistake': 'Ignoring permission errors' }
            ],
            'win': [
                { 'cmd': 'Get-PnpDevice -Class USB', 'purpose': 'List connected USB devices', 'out': 'List of USB devices including phones', 'note': 'Verify device recognition', 'mistake': 'Missing driver installation' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '45',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['ADB', 'Emulator'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'GFS requires an assessment of how corporate data is handled on employee mobile devices.',
            'objectives': ['Understand mobile device enumeration.'],
            'steps': ['Step 1: Connect the mobile device or start the emulator.', 'Step 2: Use ADB to list the device.'],
            'evidence': ['Output of connected devices.'],
            'validation': ['You should see the device listed with a specific ID.'],
            'troubleshooting': ['If no devices are found, ensure USB debugging is enabled.'],
            'mitre': [{ 'id': 'T1634', 'name': 'Native API', 'tactic': 'Execution' }],
            'cleanup': ['Disconnect the device.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which concept is central to isolating applications in a mobile OS?',
                'opts': ['Sandboxing', 'Virtualization', 'Containerization', 'Microsegmentation'],
                'correct': 0,
                'fb': 'Sandboxing restricts an application to its own environment and resources.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary role of code signing in mobile platforms?',
                'opts': ['To verify the author and ensure code integrity', 'To encrypt the application data', 'To optimize code performance', 'To compress the application size'],
                'correct': 0,
                'fb': 'Code signing ensures the app is from a known source and hasn\'t been tampered with.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'Mobile operating systems typically grant all applications root access by default.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Mobile OSes operate on a principle of least privilege; root access is highly restricted.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which component manages cryptographic keys on modern mobile devices?',
                'opts': ['Secure Enclave / Keystore', 'Baseband Processor', 'Application Sandbox', 'System Partition'],
                'correct': 0,
                'fb': 'Hardware-backed keystores or secure enclaves securely generate and store cryptographic keys.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What is the purpose of MDM in an enterprise?',
                'opts': ['Mobile Device Management to secure and monitor devices', 'Mobile Data Mining', 'Master Data Management', 'Mobile Display Mirroring'],
                'correct': 0,
                'fb': 'MDM software helps IT departments manage and secure mobile devices deployed across the enterprise.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'In mobile security, what does BYOD stand for?',
                'opts': ['Bring Your Own Device', 'Buy Your Own Data', 'Build Your Own Defense', 'Bring Your Own Dongle'],
                'correct': 0,
                'fb': 'BYOD policies allow employees to use their personal devices for work purposes.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'Both iOS and Android use the Linux kernel.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Android uses the Linux kernel, but iOS uses the XNU kernel based on Darwin.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which threat is specifically associated with third-party app stores?',
                'opts': ['Malicious apps bypassing official review processes', 'Physical theft of the device', 'Bluetooth sniffing', 'Baseband exploitation'],
                'correct': 0,
                'fb': 'Third-party stores often have less rigorous security checks, making it easier to distribute malware.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What is the function of the baseband processor in a smartphone?',
                'opts': ['Managing radio functions and cellular communication', 'Rendering graphics', 'Handling application execution', 'Storing user data'],
                'correct': 0,
                'fb': 'The baseband processor runs its own RTOS and manages all radio communications.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which mechanism prevents a malicious app from reading another app\'s data?',
                'opts': ['Sandboxing', 'Biometric authentication', 'Full disk encryption', 'ASLR'],
                'correct': 0,
                'fb': 'Sandboxing ensures apps are isolated from one another at the OS level.'
            }
        ],
        'flashcards': [
            { 'f': 'Sandboxing', 'b': 'A security mechanism that isolates running programs to prevent them from interacting with each other.' },
            { 'f': 'MDM', 'b': 'Mobile Device Management, software used by IT to control, secure, and enforce policies on smartphones and tablets.' }
        ],
        'summary': [
            'Mobile platforms use sandboxing and permissions to protect users.',
            'Code signing is critical for verifying app integrity.',
            'Hardware-backed keystores enhance cryptographic security.',
            'BYOD policies require robust MDM solutions.',
            'Understanding the OS architecture is key to securing it.'
        ],
        'outcomes': [
            'Explain the concept of mobile application sandboxing.',
            'Identify the key architectural components of mobile operating systems.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 45,
            'difficulty': 'Advanced',
            'prerequisites': [],
            'lastReviewed': '2026-07-18'
        }
    },
    'android-hacking': {
        'eyebrow': 'Module 17 · Topic 2',
        'title': 'Android Hacking',
        'module': 'Phase 17: Mobile Security Expert',
        'sub': 'Explore vulnerabilities, rooting techniques, and application security in the Android ecosystem.',
        'objectives': [
            'Understand Android application structure (APK).',
            'Perform static and dynamic analysis of Android apps.',
            'Understand the implications and methods of rooting.'
        ],
        'learn': {
            'simple': 'Android is an open-source platform based on the Linux kernel. Hacking Android involves understanding how its applications (APKs) are built, how they interact through Intents, and how to bypass security controls by gaining root access.',
            'analogy': 'Hacking an Android app is like disassembling a complex puzzle (the APK) to see how the pieces fit together, and rooting is like finding the master key to the building so you can access any room you want.',
            'architecture': 'Android apps are distributed as APK files, which contain Dalvik bytecode (classes.dex), resources, and the AndroidManifest.xml. The OS uses Intents for inter-process communication (IPC). Vulnerabilities often arise from improperly secured exported components (Activities, Services, Broadcast Receivers, Content Providers). Rooting involves exploiting a vulnerability in the kernel or recovery process to install the su binary, granting full administrative privileges.',
            'why': 'Android holds a massive market share globally. Insecure Android apps can leak sensitive corporate data or serve as a pivot point into the enterprise network.'
        },
        'enterprise': {
            'gfs': 'GFS develops custom Android applications for remote workforce management; ensuring these apps are secure from reverse engineering is critical.',
            'windows': 'Developers use Windows workstations with Android Studio and ADB to analyze and debug corporate apps.',
            'linux': 'Linux CI/CD pipelines automate the security scanning of APKs using tools like MobSF before deployment.'
        },
        'workflow': [
            'Step 1: Obtain the target APK.',
            'Step 2: Decompile the APK using Apktool or Jadx.',
            'Step 3: Analyze the AndroidManifest.xml for exported components.',
            'Step 4: Perform static code analysis on the decompiled Java code.',
            'Step 5: Install the app on a rooted device or emulator.',
            'Step 6: Hook into the app using Frida to perform dynamic analysis.'
        ],
        'diagram': {
            'caption': 'Android Application Assessment Workflow',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#e8f4f8"/><text x="300" y="200" text-anchor="middle" font-size="24">APK Static &amp; Dynamic Analysis</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'adb install app.apk', 'purpose': 'Install an APK on a device', 'out': 'Success message', 'note': 'Requires USB debugging', 'mistake': 'INSTALL_FAILED_ALREADY_EXISTS' },
                { 'cmd': 'apktool d app.apk', 'purpose': 'Decompile an APK', 'out': 'Decompiled folder', 'note': 'Reverses resources and smali code', 'mistake': 'Missing Java runtime' }
            ],
            'win': [
                { 'cmd': 'adb shell pm list packages', 'purpose': 'List installed packages', 'out': 'List of package names', 'note': 'Find target package name', 'mistake': 'Device not attached' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Advanced',
            'duration': '60',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['Apktool', 'Jadx', 'Frida'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment on provided vulnerable apps.'],
            'scenario': 'GFS has acquired a new mobile banking app and requires a security assessment before launch.',
            'objectives': ['Decompile the APK and find hardcoded credentials.'],
            'steps': ['Step 1: Run `apktool d target.apk`.', 'Step 2: Search for API keys in the `res/values/strings.xml` file.', 'Step 3: Open the APK in Jadx to review the Java source code.'],
            'evidence': ['Screenshot of the hardcoded credentials found.'],
            'validation': ['You should find the secret key `GFS_SECRET_API_2026`.'],
            'troubleshooting': ['If Apktool fails, ensure it is updated to the latest version.'],
            'mitre': [{ 'id': 'T1636', 'name': 'Protected User Data', 'tactic': 'Collection' }],
            'cleanup': ['Remove the decompiled files and uninstall the app.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which file contains the permissions and component declarations for an Android app?',
                'opts': ['AndroidManifest.xml', 'classes.dex', 'resources.arsc', 'build.gradle'],
                'correct': 0,
                'fb': 'The AndroidManifest.xml file describes fundamental characteristics of the app.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What tool is commonly used to reverse engineer an APK into Smali code and resources?',
                'opts': ['Apktool', 'Nmap', 'Burp Suite', 'Metasploit'],
                'correct': 0,
                'fb': 'Apktool is the standard tool for reverse engineering third-party, closed, binary Android apps.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'Rooting an Android device increases its overall security.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Rooting bypasses built-in security mechanisms like the app sandbox, generally decreasing security.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'Which Android component is typically targeted via intent spoofing if it is improperly exported?',
                'opts': ['Activity or Broadcast Receiver', 'SharedPreferences', 'SQLite Database', 'Keystore'],
                'correct': 0,
                'fb': 'Exported components can be invoked by other apps using Intents, leading to potential exploits.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What does ADB stand for?',
                'opts': ['Android Debug Bridge', 'Application Data Base', 'Advanced Device Bootloader', 'Android Deployment Binary'],
                'correct': 0,
                'fb': 'ADB is a versatile command-line tool that lets you communicate with a device.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'In Android, what is Dalvik/ART bytecode stored as?',
                'opts': ['.dex files', '.class files', '.java files', '.so files'],
                'correct': 0,
                'fb': 'Java code is compiled into Dalvik Executable (.dex) format.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'Frida is an dynamic instrumentation toolkit used for Android application analysis.',
                'opts': ['True', 'False'],
                'correct': 0,
                'fb': 'Frida allows you to inject snippets of JavaScript or your own library into native apps on Android.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'Which attack involves repackaging a legitimate app with malicious code?',
                'opts': ['Trojanizing', 'Phishing', 'Man-in-the-Middle', 'SQL Injection'],
                'correct': 0,
                'fb': 'Attackers often decompile popular apps, add malware, recompile, and distribute them.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What command retrieves files from an Android device?',
                'opts': ['adb pull', 'adb push', 'adb get', 'adb fetch'],
                'correct': 0,
                'fb': 'adb pull copies files or directories from the device to your computer.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which component allows apps to share data securely?',
                'opts': ['Content Providers', 'Services', 'Activities', 'Intents'],
                'correct': 0,
                'fb': 'Content Providers manage access to a central repository of data.'
            }
        ],
        'flashcards': [
            { 'f': 'APK', 'b': 'Android Package Kit, the file format used by Android for distribution and installation of mobile apps.' },
            { 'f': 'Smali', 'b': 'An assembler/disassembler for the dex format used by Dalvik/ART.' }
        ],
        'summary': [
            'Android apps are distributed as APKs and run on the Dalvik/ART virtual machine.',
            'AndroidManifest.xml defines app components and permissions.',
            'Apktool and Jadx are essential for static analysis.',
            'Rooting bypasses OS security to grant administrative access.',
            'Dynamic analysis often relies on instrumentation tools like Frida.'
        ],
        'outcomes': [
            'Explain the structure of an Android application package.',
            'Identify vulnerabilities in exported Android components.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 60,
            'difficulty': 'Advanced',
            'prerequisites': [],
            'lastReviewed': '2026-07-18'
        }
    },
    'ios-hacking': {
        'eyebrow': 'Module 17 · Topic 3',
        'title': 'iOS Hacking',
        'module': 'Phase 17: Mobile Security Expert',
        'sub': 'Understand iOS security mechanisms, jailbreaking, and application assessment.',
        'objectives': [
            'Understand iOS security architecture (Secure Boot, Enclave).',
            'Learn about jailbreaking techniques and risks.',
            'Perform basic iOS application analysis.'
        ],
        'learn': {
            'simple': 'iOS is a closed, proprietary operating system known for its robust security model. Hacking iOS typically involves bypassing its strict code signing and sandboxing restrictions through a process called jailbreaking, which allows root access and the installation of unauthorized software.',
            'analogy': 'iOS is like a high-security vault with guards at every door (code signing and sandboxing). Jailbreaking is like finding a hidden tunnel that bypasses the guards and gets you straight into the vault.',
            'architecture': 'iOS security is layered, starting with the hardware (Secure Enclave, hardware root of trust). The boot process verifies the signature of the bootloader, kernel, and OS (Secure Boot). Applications run in a strict sandbox and must be signed by an Apple-issued certificate. Jailbreaking exploits vulnerabilities in the kernel or bootrom to patch security checks dynamically, allowing unsigned code execution and root access.',
            'why': 'Executives and high-value targets frequently use iOS devices. Understanding how iOS security can be bypassed is critical for incident response and securing corporate assets on these devices.'
        },
        'enterprise': {
            'gfs': 'GFS executives primarily use iOS devices; ensuring these devices remain non-jailbroken and compliant via MDM is critical.',
            'windows': 'Administrators use Windows tools like 3uTools for managing device states and backups.',
            'linux': 'Security analysts use Kali Linux with tools like checkra1n to perform physical assessments of confiscated iOS devices.'
        },
        'workflow': [
            'Step 1: Check the iOS version and device model.',
            'Step 2: Identify a compatible jailbreak exploit.',
            'Step 3: Execute the jailbreak process to gain root access.',
            'Step 4: Install SSH or other access tools (e.g., via Cydia/Sileo).',
            'Step 5: Decrypt the target application (IPA).',
            'Step 6: Analyze the application binaries using class-dump and Hopper.'
        ],
        'diagram': {
            'caption': 'iOS Secure Boot Chain',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#fdfae8"/><text x="300" y="200" text-anchor="middle" font-size="24">Bootrom -> LLB -> iBoot -> Kernel</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'ssh root@<ios-ip>', 'purpose': 'Connect to a jailbroken device', 'out': 'Root shell', 'note': 'Default password is usually "alpine"', 'mistake': 'Not changing the default password' }
            ],
            'win': [
                { 'cmd': 'ping <ios-ip>', 'purpose': 'Verify connectivity', 'out': 'Ping replies', 'note': 'Ensure device is on the same network', 'mistake': 'Firewall blocking connections' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Advanced',
            'duration': '60',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['checkra1n', 'Objection', 'Frida'],
            'dependencies': [],
            'safety': ['Jailbreaking can void warranties and cause instability. Use only on dedicated lab devices.'],
            'scenario': 'GFS requires an assessment of an internally developed iOS application for sensitive data leaks.',
            'objectives': ['Bypass jailbreak detection and analyze app data storage.'],
            'steps': ['Step 1: SSH into the jailbroken device.', 'Step 2: Use Frida or Objection to hook the application.', 'Step 3: Search for SQLite databases containing sensitive data.'],
            'evidence': ['Extracted sensitive data from the local database.'],
            'validation': ['You should locate unencrypted PII in the app\'s sandbox directory.'],
            'troubleshooting': ['If SSH fails, ensure the OpenSSH package is installed via the package manager.'],
            'mitre': [{ 'id': 'T1636', 'name': 'Protected User Data', 'tactic': 'Collection' }],
            'cleanup': ['Reboot the device (if tethered jailbreak) or remove the app.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary purpose of the iOS Secure Boot process?',
                'opts': ['To ensure that only trusted, Apple-signed software loads at startup', 'To encrypt user data on the device', 'To prevent battery drain during startup', 'To isolate applications in sandboxes'],
                'correct': 0,
                'fb': 'Secure Boot creates a chain of trust verifying signatures at each step of the boot process.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What hardware component manages cryptographic keys on an iOS device?',
                'opts': ['Secure Enclave', 'Baseband', 'NFC Controller', 'A-Series CPU Cache'],
                'correct': 0,
                'fb': 'The Secure Enclave is a dedicated coprocessor that securely handles keys and biometric data.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'Jailbreaking an iOS device is required to install applications from the official App Store.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Jailbreaking is used to bypass restrictions, allowing installation of apps from outside the official App Store.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the default SSH password for a jailbroken iOS device?',
                'opts': ['alpine', 'root', 'admin', 'apple'],
                'correct': 0,
                'fb': '"alpine" is the widely known default password, which should be changed immediately after jailbreaking.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which file format is used for distributing iOS applications?',
                'opts': ['.ipa', '.apk', '.exe', '.deb'],
                'correct': 0,
                'fb': 'iOS App Store packages use the .ipa extension.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What type of jailbreak requires a computer connection every time the device reboots?',
                'opts': ['Tethered', 'Untethered', 'Semi-untethered', 'Semi-tethered'],
                'correct': 0,
                'fb': 'A tethered jailbreak requires re-exploiting the device via a computer on every boot.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'iOS applications can freely read data from other applications\' sandboxes by default.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'iOS enforces strict sandboxing, preventing apps from accessing each other\'s data without explicit permission.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which tool is commonly used to dynamically instrument iOS apps on a jailbroken device?',
                'opts': ['Frida', 'Apktool', 'Jadx', 'OllyDbg'],
                'correct': 0,
                'fb': 'Frida is highly effective for dynamically hooking and analyzing iOS apps.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What is ASLR, and how does it relate to iOS security?',
                'opts': ['Address Space Layout Randomization, which randomizes memory locations to prevent buffer overflow attacks', 'Apple Secure Login Routine, for biometric auth', 'Application Security Layer Restrictions, the sandbox implementation', 'Advanced System Logging Resource, for auditing'],
                'correct': 0,
                'fb': 'ASLR makes exploitation harder by randomizing where code and data are loaded in memory.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What vulnerability does checkm8 exploit?',
                'opts': ['Bootrom vulnerability', 'Safari WebKit vulnerability', 'Kernel use-after-free', 'Baseband overflow'],
                'correct': 0,
                'fb': 'checkm8 is an unpatchable bootrom exploit for older Apple devices.'
            }
        ],
        'flashcards': [
            { 'f': 'Jailbreaking', 'b': 'The process of removing software restrictions imposed by Apple on iOS devices.' },
            { 'f': 'Secure Enclave', 'b': 'A hardware-based security feature that isolates cryptographic functions and biometric data.' }
        ],
        'summary': [
            'iOS features a strong security model based on the Secure Enclave and Secure Boot.',
            'Jailbreaking bypasses code signing and sandboxing restrictions.',
            'iOS applications are distributed as .ipa files.',
            'Dynamic analysis requires a jailbroken device and tools like Frida.',
            'Default credentials (like "alpine") are a common risk on jailbroken devices.'
        ],
        'outcomes': [
            'Explain the iOS secure boot chain.',
            'Identify the risks associated with jailbroken devices.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 60,
            'difficulty': 'Advanced',
            'prerequisites': [],
            'lastReviewed': '2026-07-18'
        }
    },
    'mobile-security-tools': {
        'eyebrow': 'Module 17 · Topic 4',
        'title': 'Mobile Security Tools',
        'module': 'Phase 17: Mobile Security Expert',
        'sub': 'Leverage automated and manual tools for comprehensive mobile security assessments.',
        'objectives': [
            'Utilize MobSF for automated static analysis.',
            'Understand dynamic analysis frameworks like Frida and Objection.',
            'Intercept mobile application traffic.'
        ],
        'learn': {
            'simple': 'Analyzing mobile applications manually is time-consuming. Mobile security tools automate the extraction of code, scanning for known vulnerabilities, and intercepting network traffic to identify flaws rapidly.',
            'analogy': 'If manually analyzing an app is like reading a book word by word to find spelling errors, using these tools is like using an advanced spellchecker and grammar engine.',
            'architecture': 'Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis, and security assessment framework. For dynamic analysis, tools like Frida allow injecting JavaScript into native apps to hook functions, while Objection builds on Frida to provide a command-line interface for exploring the app\'s runtime environment. Interception proxies like Burp Suite are used to capture API traffic, requiring the installation of custom CA certificates on the device to bypass SSL pinning.',
            'why': 'Speed and efficiency are critical in enterprise security. Automated tools help security teams keep pace with agile development cycles by quickly identifying critical vulnerabilities before release.'
        },
        'enterprise': {
            'gfs': 'GFS integrates MobSF into its CI/CD pipeline to automatically scan all mobile releases for hardcoded secrets and insecure configurations.',
            'windows': 'Security engineers run Burp Suite on Windows workstations to intercept and analyze API traffic from test devices.',
            'linux': 'MobSF is typically hosted on dedicated Linux servers to provide centralized scanning capabilities for the development team.'
        },
        'workflow': [
            'Step 1: Upload the app package (APK/IPA) to MobSF for static analysis.',
            'Step 2: Review the generated report for high-risk vulnerabilities.',
            'Step 3: Configure a proxy (e.g., Burp Suite) and install its CA certificate on the mobile device.',
            'Step 4: Use Objection to bypass SSL pinning if implemented by the app.',
            'Step 5: Monitor network traffic while interacting with the app.',
            'Step 6: Use Frida to manipulate application behavior dynamically.'
        ],
        'diagram': {
            'caption': 'Mobile Application Traffic Interception',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#e8f8e8"/><text x="300" y="200" text-anchor="middle" font-size="24">App -> Proxy (Burp) -> Backend Server</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'docker run -it -p 8000:8000 opensecurity/mobsf', 'purpose': 'Start MobSF using Docker', 'out': 'MobSF listening on port 8000', 'note': 'Requires Docker installed', 'mistake': 'Port 8000 already in use' }
            ],
            'win': [
                { 'cmd': 'objection -g com.target.app explore', 'purpose': 'Launch Objection', 'out': 'Objection CLI', 'note': 'Requires device connected via ADB and Frida running', 'mistake': 'Frida server not running on device' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '45',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['MobSF', 'Burp Suite'],
            'dependencies': ['Docker'],
            'safety': ['Analyze only applications you have permission to test.'],
            'scenario': 'GFS needs a rapid security check on a third-party vendor application.',
            'objectives': ['Run an automated static analysis using MobSF.'],
            'steps': ['Step 1: Start the MobSF Docker container.', 'Step 2: Access the web interface at `localhost:8000`.', 'Step 3: Upload the target APK and wait for the analysis to complete.'],
            'evidence': ['PDF report generated by MobSF.'],
            'validation': ['Identify at least two high-severity findings in the report.'],
            'troubleshooting': ['If MobSF fails to start, verify Docker service is running.'],
            'mitre': [{ 'id': 'T1437', 'name': 'Application Data', 'tactic': 'Collection' }],
            'cleanup': ['Stop the Docker container.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary function of MobSF?',
                'opts': ['Automated static and dynamic analysis of mobile applications', 'Managing mobile devices in an enterprise', 'Providing physical security for mobile hardware', 'Developing iOS applications'],
                'correct': 0,
                'fb': 'Mobile Security Framework (MobSF) automates the assessment process for Android, iOS, and Windows apps.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Why is installing a custom CA certificate necessary for intercepting mobile app traffic?',
                'opts': ['To decrypt HTTPS traffic for inspection', 'To speed up network requests', 'To compress data payloads', 'To bypass firewall restrictions'],
                'correct': 0,
                'fb': 'An interception proxy needs its certificate trusted by the device to perform a Man-in-the-Middle attack and decrypt TLS traffic.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Advanced',
                'q': 'SSL Pinning makes intercepting traffic easier because the app trusts all certificates.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'SSL Pinning hardcodes the expected certificate, making interception much harder and requiring tools to bypass it.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'Which tool is commonly used to quickly bypass SSL pinning dynamically?',
                'opts': ['Objection', 'Apktool', 'Nmap', 'Wireshark'],
                'correct': 0,
                'fb': 'Objection (built on Frida) has built-in commands (like `android sslpinning disable`) to hook and bypass pinning checks.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What does Burp Suite primarily act as during mobile testing?',
                'opts': ['An interception proxy', 'A static analysis scanner', 'A reverse engineering toolkit', 'A mobile emulator'],
                'correct': 0,
                'fb': 'Burp Suite intercepts HTTP/HTTPS traffic between the mobile app and the backend API.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the advantage of using Docker to run MobSF?',
                'opts': ['It simplifies installation and dependency management', 'It makes the analysis faster', 'It provides a graphical interface for Android', 'It automatically roots the connected device'],
                'correct': 0,
                'fb': 'Docker provides a pre-configured environment, avoiding complex setup processes.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'Frida can only be used on Android devices.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Frida is cross-platform and heavily used on both Android and iOS.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'In the context of Frida, what is a "hook"?',
                'opts': ['Intercepting a function call to monitor or alter its behavior', 'A physical connection to the device', 'A type of malware', 'The process of installing the app'],
                'correct': 0,
                'fb': 'Hooking allows analysts to execute custom code when a specific function is called.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What must be running on the mobile device for remote Frida scripts to work?',
                'opts': ['frida-server', 'adb daemon', 'ssh daemon', 'mobsf agent'],
                'correct': 0,
                'fb': 'The frida-server binary must be executing on the device to communicate with the host computer.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is static analysis?',
                'opts': ['Analyzing the application\'s code or binary without running it', 'Running the application to observe its behavior', 'Intercepting network traffic', 'Fuzzing the application inputs'],
                'correct': 0,
                'fb': 'Static analysis involves examining the app\'s structure, code, and resources while it is at rest.'
            }
        ],
        'flashcards': [
            { 'f': 'SSL Pinning', 'b': 'A technique where an application is hardcoded to only trust specific SSL certificates, preventing MITM proxies.' },
            { 'f': 'Objection', 'b': 'A runtime mobile exploration toolkit powered by Frida, built to help assess the security posture of mobile apps.' }
        ],
        'summary': [
            'MobSF is a powerful tool for automated static analysis of mobile apps.',
            'Burp Suite is essential for intercepting and analyzing API traffic.',
            'SSL Pinning is a defensive mechanism that must often be bypassed during testing.',
            'Frida and Objection provide dynamic instrumentation capabilities.',
            'Automated tools streamline the assessment process but should be combined with manual testing.'
        ],
        'outcomes': [
            'Deploy MobSF for automated application scanning.',
            'Configure a mobile device to route traffic through an interception proxy.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 45,
            'difficulty': 'Intermediate',
            'prerequisites': [],
            'lastReviewed': '2026-07-18'
        }
    }
}

payload = ""
for topic_id, content in m17_topics.items():
    json_str = json.dumps(content, indent=4)
    payload += f"CONTENT['{topic_id}'] = {json_str};\n\n"

try:
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()

    if '// ── TAB WIRING ──' in html_content:
        html_content = html_content.replace('// ── TAB WIRING ──', payload + '// ── TAB WIRING ──')
        with open(HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("Successfully injected m17 content!")
    else:
        print("Could not find '// ── TAB WIRING ──' in index.html")
except Exception as e:
    print(f"Error: {e}")
