import os
import json

HTML_FILE = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"

# If frontend/index.html is a relative path to the script:
script_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(script_dir, "frontend", "index.html")

# Fallback if the specific path doesn't exist but the script is run in the root
if not os.path.exists(html_path):
    html_path = HTML_FILE

payload = """
CONTENT['iot-concepts'] = {
  eyebrow: 'Module 18 · Topic 1',
  title: 'IoT Concepts',
  module: 'Phase 18: OT/IoT Security Specialist',
  sub: 'Understanding the fundamentals of Internet of Things architecture and communication.',
  objectives: ['Understand IoT architecture models', 'Identify common IoT communication protocols', 'Recognize components of IoT devices'],
  learn: {
    simple: 'The Internet of Things (IoT) refers to the rapidly growing network of connected objects that are able to collect and exchange data using embedded sensors. These devices span from everyday household items like smart thermostats to sophisticated industrial tools. The primary goal of IoT is to create a seamless integration between the physical and digital worlds, allowing for real-time monitoring and control.',
    analogy: 'Think of IoT like the nervous system of a house. The sensors are the sensory organs (eyes, ears, skin) collecting information like temperature, light, and sound. The network is the spinal cord transmitting this data, and the central hub or cloud is the brain processing the information and deciding on an action (e.g., turning on the AC).',
    architecture: 'A typical IoT architecture consists of three core layers: the Perception layer (sensors and actuators), the Network layer (gateways and communication protocols like MQTT, CoAP, Zigbee), and the Application layer (cloud platforms and analytics). Devices often have limited computational power, making security implementations challenging.\\n\\nEdge computing is increasingly used to process data closer to the source, reducing latency and bandwidth usage. This shifts some processing burden from the central cloud to the edge devices or gateways.\\n\\nSecurity must be integrated at every layer, from hardware-based trusted execution environments on the devices to secure TLS/SSL communication over the network and robust IAM in the application layer.',
    why: 'As enterprises deploy millions of IoT devices to optimize operations, each device represents a potential entry point for attackers. Understanding IoT concepts is critical for securing these expanded attack surfaces.'
  },
  enterprise: {
    gfs: 'Global Financial Services (GFS) has deployed smart HVAC and lighting systems across its global branches to reduce energy costs. These IoT devices must be segregated from the corporate financial network to prevent a compromise of a smart thermostat from leading to a breach of customer data.',
    windows: 'In a Windows environment, IoT devices might integrate with Azure IoT Hub, requiring secure provisioning, certificate management, and role-based access controls within Active Directory for administrative access.',
    linux: 'Linux is the dominant OS for IoT gateways and devices. Securing these involves hardening the Linux kernel, minimizing installed packages, and using technologies like SELinux or AppArmor to restrict device capabilities.'
  },
  workflow: [
    'Step 1: Identify the IoT device and its purpose.',
    'Step 2: Map the network topology to see where the device connects.',
    'Step 3: Analyze the communication protocols in use (e.g., MQTT, HTTP).',
    'Step 4: Inspect the device for open ports and running services.',
    'Step 5: Review the authentication and authorization mechanisms.',
    'Step 6: Assess the physical security of the device.'
  ],
  diagram: {
    caption: 'Click to interact with the IoT Architecture diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f0f0f0"/><text x="300" y="200" text-anchor="middle" font-size="24">IoT Architecture Model</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -sV -p 1883,8883 <target>', purpose: 'Scan for MQTT services', out: 'Port status and service version', note: 'Port 1883 is unencrypted MQTT; 8883 is MQTT over TLS.', mistake: 'Assuming all MQTT is on standard ports' }
    ],
    win: [
      { cmd: 'Test-NetConnection -ComputerName <target> -Port 1883', purpose: 'Check basic TCP connectivity to MQTT', out: 'TcpTestSucceeded: True', note: 'Useful for quick checks from a Windows admin box.', mistake: 'Failing to verify TLS on port 8883' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nmap', 'Mosquitto-clients'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment. Do not scan production IoT devices.'],
    scenario: 'GFS has tasked you with auditing the new smart building management system. You need to identify running services on the IoT gateway.',
    objectives: ['Identify open ports on an IoT gateway', 'Interact with an unauthenticated MQTT broker'],
    steps: [
      'Step 1: Run an Nmap scan against the gateway IP: `nmap -sV -p- <gateway_ip>`.',
      'Step 2: Note the open port 1883 (MQTT).',
      'Step 3: Use mosquitto_sub to subscribe to all topics: `mosquitto_sub -h <gateway_ip> -t "#"`.',
      'Step 4: Observe the data being published by sensors.'
    ],
    evidence: ['Nmap scan results showing port 1883 open.', 'Terminal output showing MQTT messages.'],
    validation: ['You should see real-time sensor data printed in the terminal.'],
    troubleshooting: ['If mosquitto_sub times out, ensure the gateway IP is correct and port 1883 is reachable.'],
    mitre: [{ id: 'T1046', name: 'Network Service Discovery', tactic: 'Discovery' }],
    cleanup: ['Stop the mosquitto_sub process with Ctrl+C.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which IoT architecture layer is responsible for data collection?',
      opts: ['Network Layer', 'Perception Layer', 'Application Layer', 'Transport Layer'],
      correct: 1,
      fb: 'The Perception layer includes sensors and actuators that collect data from the environment.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which protocol is commonly used for lightweight messaging in IoT?',
      opts: ['HTTP', 'FTP', 'MQTT', 'SSH'],
      correct: 2,
      fb: 'MQTT (Message Queuing Telemetry Transport) is a lightweight publish-subscribe network protocol common in IoT.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a significant challenge in securing IoT devices?',
      opts: ['Excessive computational power', 'Limited processing and memory resources', 'Lack of wireless connectivity', 'Overreliance on wired networks'],
      correct: 1,
      fb: 'IoT devices often have limited resources, making it hard to implement strong encryption and complex security agents.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What port does MQTT typically use when unencrypted?',
      opts: ['443', '80', '1883', '8883'],
      correct: 2,
      fb: 'Port 1883 is the standard port for unencrypted MQTT traffic.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which architecture model brings computation closer to the IoT sensors?',
      opts: ['Cloud Computing', 'Grid Computing', 'Edge Computing', 'Quantum Computing'],
      correct: 2,
      fb: 'Edge computing processes data near the edge of the network, closer to where the data is generated.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'IoT devices should always be placed on the main corporate network for easy management.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. IoT devices should be segregated into their own VLANs to limit the impact of a potential compromise.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which component acts as an intermediary between IoT devices and the cloud?',
      opts: ['Sensor', 'Actuator', 'IoT Gateway', 'Switch'],
      correct: 2,
      fb: 'An IoT Gateway aggregates data from sensors and translates protocols before sending it to the cloud.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does an actuator do in an IoT system?',
      opts: ['Collects data', 'Translates protocols', 'Performs a physical action based on commands', 'Stores data in a database'],
      correct: 2,
      fb: 'Actuators receive commands and perform physical actions, such as closing a valve or turning on a motor.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Physical security is not a concern for IoT devices since they are usually connected to the cloud.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Physical security is a major concern, as attackers can extract firmware or keys if they have physical access.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is an example of an IoT operating system?',
      opts: ['Windows Server 2022', 'macOS Sonoma', 'FreeRTOS', 'Kali Linux'],
      correct: 2,
      fb: 'FreeRTOS is a popular real-time operating system designed specifically for microcontrollers in IoT devices.'
    }
  ],
  flashcards: [
    { f: 'MQTT', b: 'Message Queuing Telemetry Transport, a lightweight pub-sub protocol for IoT.' },
    { f: 'Edge Computing', b: 'Processing data closer to the source to reduce latency and bandwidth.' }
  ],
  summary: [
    'IoT connects physical objects to the internet.',
    'The architecture consists of Perception, Network, and Application layers.',
    'MQTT and CoAP are common lightweight protocols.',
    'Resource constraints make IoT security challenging.',
    'Network segmentation is crucial for defending enterprise IoT deployments.'
  ],
  outcomes: [
    'Explain the layers of the IoT architecture.',
    'Identify common IoT protocols and their default ports.',
    'Describe the security challenges inherent to IoT devices.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Networking Concepts'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['ot-concepts'] = {
  eyebrow: 'Module 18 · Topic 2',
  title: 'OT Concepts',
  module: 'Phase 18: OT/IoT Security Specialist',
  sub: 'Understanding Operational Technology and Industrial Control Systems.',
  objectives: ['Define OT and ICS architectures', 'Understand the Purdue Model', 'Differentiate between IT and OT priorities'],
  learn: {
    simple: 'Operational Technology (OT) encompasses hardware and software that detects or causes a change through the direct monitoring and/or control of industrial equipment, assets, processes, and events. Unlike Information Technology (IT), which deals with data (information), OT deals with the physical world. This includes Industrial Control Systems (ICS) like SCADA and DCS used in manufacturing, energy, and water treatment.',
    analogy: 'If IT is the brain and nervous system handling thoughts and memories (data), OT is the muscles and autonomous reflexes of the body (machinery). If IT fails, you might lose a document; if OT fails, a factory might explode or a city might lose power.',
    architecture: 'OT environments are traditionally modeled using the Purdue Enterprise Reference Architecture (PERA), which divides the network into hierarchical zones. Level 0 is the physical process (sensors, pumps). Level 1 is basic control (PLCs, RTUs). Level 2 is area supervisory control (HMI, SCADA nodes). Level 3 is site operations (historians). Levels 4 and 5 represent the enterprise IT network.\\n\\nHistorically, OT networks were air-gapped from IT networks, providing security through isolation. However, Industry 4.0 and digital transformation are driving IT/OT convergence, breaking down the air gap to allow for data analytics and remote management, thereby exposing OT systems to IT-based cyber threats.\\n\\nOT protocols (e.g., Modbus, DNP3, Profinet) were designed for reliability and speed, not security. They often lack authentication or encryption by default.',
    why: 'Compromising OT environments can lead to physical damage, environmental disasters, or loss of life. As IT and OT converge, security professionals must understand how to protect critical infrastructure.'
  },
  enterprise: {
    gfs: 'Global Financial Services (GFS) relies on immense data centers to process transactions. The OT systems (cooling, backup generators, physical access controls) in these data centers are mission-critical. An attack on the data center OT could cause thermal shutdowns, halting GFS trading platforms.',
    windows: 'Windows is heavily used in OT environments at Level 2 and Level 3 (HMIs, SCADA servers, Historians). These systems are often legacy (e.g., Windows 7 or even XP) because patching them requires downtime that industrial processes cannot tolerate.',
    linux: 'Linux is increasingly found in modern OT gateways and some modern PLCs, though proprietary real-time operating systems (RTOS) are more common at Level 1.'
  },
  workflow: [
    'Step 1: Identify the critical industrial processes.',
    'Step 2: Map the network according to the Purdue Model.',
    'Step 3: Identify the boundary between IT and OT (the Industrial Demilitarized Zone - IDMZ).',
    'Step 4: Inventory PLCs, RTUs, and SCADA servers.',
    'Step 5: Analyze the industrial protocols in use (e.g., Modbus TCP).',
    'Step 6: Evaluate the patching status and backup procedures for HMIs.'
  ],
  diagram: {
    caption: 'Click to interact with the Purdue Model diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f0f0f0"/><text x="300" y="200" text-anchor="middle" font-size="24">Purdue Model for ICS Security</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -Pn -sT -p 502 <target>', purpose: 'Scan for Modbus TCP', out: 'Port 502 status', note: 'Use extreme caution scanning OT networks; aggressive scans can crash legacy PLCs.', mistake: 'Running heavy vulnerability scans on PLCs' }
    ],
    win: [
      { cmd: 'Get-NetTCPConnection -LocalPort 502', purpose: 'Check if a Windows HMI is listening on Modbus port', out: 'Connection details', note: 'Useful for auditing local services on an HMI workstation.', mistake: 'Ignoring alternative or proprietary ports' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nmap', 'modbus-cli'],
    dependencies: [],
    safety: ['Perform this lab only against simulated PLCs in an isolated environment. NEVER scan production OT equipment.'],
    scenario: 'GFS wants to assess the security of the cooling system controllers in their primary data center. You will interact with a simulated Modbus PLC.',
    objectives: ['Identify a Modbus service', 'Read holding registers from a PLC'],
    steps: [
      'Step 1: Discover the PLC IP: `nmap -Pn -p 502 <subnet>`.',
      'Step 2: Verify Modbus service is running.',
      'Step 3: Use modbus-cli to read holding registers: `modbus read <plc_ip> %MW0 10`.',
      'Step 4: Analyze the returned data values representing cooling temperatures.'
    ],
    evidence: ['Nmap output showing port 502 open.', 'modbus-cli output showing register values.'],
    validation: ['You should see decimal or hex values corresponding to the simulated temperature data.'],
    troubleshooting: ['If modbus-cli fails to connect, check firewall rules allowing port 502.'],
    mitre: [{ id: 'T0861', name: 'Point & Tag Identification', tactic: 'Discovery' }],
    cleanup: ['Close connections to the simulated PLC.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary focus of OT compared to IT?',
      opts: ['Data Confidentiality', 'Data Integrity', 'Availability and Safety', 'Non-repudiation'],
      correct: 2,
      fb: 'In OT environments, Safety and Availability are paramount, often overriding confidentiality.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which architecture model is commonly used to segment OT networks?',
      opts: ['OSI Model', 'TCP/IP Model', 'Purdue Model', 'Zero Trust Model'],
      correct: 2,
      fb: 'The Purdue Model (PERA) defines hierarchical levels of an ICS network for segmentation.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What device directly controls the physical process in an ICS environment?',
      opts: ['HMI', 'Historian', 'PLC', 'Firewall'],
      correct: 2,
      fb: 'A Programmable Logic Controller (PLC) is a ruggedized computer used for industrial automation.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which port is traditionally used by Modbus TCP?',
      opts: ['443', '502', '1883', '3389'],
      correct: 1,
      fb: 'Port 502 is the well-known port for Modbus TCP communications.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does HMI stand for in an OT environment?',
      opts: ['Human-Machine Interface', 'Hardware Management Infrastructure', 'Host Monitoring Indicator', 'High-level Machine Instruction'],
      correct: 0,
      fb: 'HMI stands for Human-Machine Interface, a dashboard or UI that allows operators to interact with the control system.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'OT protocols were originally designed with strong encryption and authentication.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Most legacy OT protocols were designed for serial links and lack built-in security features.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a significant risk of IT/OT convergence?',
      opts: ['Decreased network speed', 'Exposing air-gapped OT systems to IT-based threats', 'Inability to use cloud services', 'Hardware obsolescence'],
      correct: 1,
      fb: 'Convergence connects previously isolated OT networks to corporate IT networks and the internet, increasing the attack surface.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which component is responsible for storing long-term process data?',
      opts: ['PLC', 'RTU', 'Data Historian', 'Actuator'],
      correct: 2,
      fb: 'A Data Historian logs and stores time-series data from the control system for analysis.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Active vulnerability scanning is highly recommended for all legacy PLCs.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Active scanning can cause legacy PLCs to crash or malfunction. Passive monitoring is preferred.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'At which level of the Purdue Model would you typically find a PLC?',
      opts: ['Level 0', 'Level 1', 'Level 3', 'Level 4'],
      correct: 1,
      fb: 'Level 1 contains basic control devices like PLCs and RTUs.'
    }
  ],
  flashcards: [
    { f: 'PLC', b: 'Programmable Logic Controller; a specialized computer used to control industrial processes.' },
    { f: 'Purdue Model', b: 'A reference architecture that segments ICS networks into hierarchical levels.' }
  ],
  summary: [
    'OT controls physical processes; safety and availability are the top priorities.',
    'The Purdue Model is the standard architecture for OT network segmentation.',
    'IT/OT convergence increases efficiency but exposes OT to cyber threats.',
    'Legacy OT protocols lack built-in security features.',
    'Active scanning must be done with extreme caution in OT environments.'
  ],
  outcomes: [
    'Differentiate between IT and OT priorities.',
    'Explain the levels of the Purdue Model.',
    'Identify common OT components like PLCs, HMIs, and Historians.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Networking Concepts'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['iot-ot-threats'] = {
  eyebrow: 'Module 18 · Topic 3',
  title: 'IoT & OT Threats',
  module: 'Phase 18: OT/IoT Security Specialist',
  sub: 'Analyzing the threat landscape and attack vectors targeting IoT and OT environments.',
  objectives: ['Identify common attack vectors against IoT devices', 'Understand OT-specific malware (e.g., Stuxnet, Industroyer)', 'Analyze the impact of botnets on IoT'],
  learn: {
    simple: 'IoT and OT environments face unique threats. IoT devices are often mass-produced with weak default passwords, unpatchable firmware, and insecure communication protocols, making them prime targets for botnets like Mirai. OT environments, on the other hand, face sophisticated, often nation-state-sponsored attacks aimed at disrupting physical processes, such as power grids or manufacturing plants.',
    analogy: 'Attacking IoT is like a burglar finding a million identical houses that all use the same key (default passwords) to steal small items or use the houses as hideouts. Attacking OT is like a highly planned heist targeting a city\'s water supply to cause maximum disruption and chaos.',
    architecture: 'IoT threats typically involve exploiting weak authentication or web interfaces to gain control of a device, incorporating it into a botnet to launch DDoS attacks. Vulnerabilities in UPnP or insecure APIs are common entry points.\\n\\nOT threats are more complex. Attackers often pivot from the IT network into the OT network through poorly configured IDMZs. Once inside, they may use "living off the land" techniques or specialized malware that understands industrial protocols to manipulate PLCs, causing physical damage while spoofing HMI readouts to hide the attack from operators.\\n\\nRansomware is a significant threat to both. While traditionally an IT problem, ransomware affecting OT HMIs or Historians can blind operators, forcing a complete shutdown of industrial processes (as seen in the Colonial Pipeline incident).',
    why: 'The sheer volume of IoT devices and the critical nature of OT systems mean that threats in this space can cause massive internet outages, financial ruin, or catastrophic physical damage.'
  },
  enterprise: {
    gfs: 'GFS experienced a near-miss when a vendor installed wireless IoT cameras with default credentials on the same network segment as the physical security badge system. A threat actor could have used the cameras to pivot and unlock doors.',
    windows: 'Windows-based OT systems (HMIs) are prime targets for ransomware. Attackers exploit missing patches or weak RDP credentials to encrypt the HMI, blinding operators to the physical process.',
    linux: 'Linux-based IoT devices (like routers and IP cameras) are constantly scanned for default SSH/Telnet credentials to be recruited into botnets like Mirai or Mozi.'
  },
  workflow: [
    'Step 1: Identify the threat actor profile (e.g., script kiddie for IoT, APT for OT).',
    'Step 2: Map the attack surface (e.g., exposed web interfaces, IT/OT boundaries).',
    'Step 3: Analyze potential attack vectors (e.g., default credentials, zero-days in OT protocols).',
    'Step 4: Assess the potential impact (e.g., DDoS participation vs. physical destruction).',
    'Step 5: Review historical case studies (e.g., Triton, BlackEnergy) for TTPs.',
    'Step 6: Develop threat models specific to the deployed architecture.'
  ],
  diagram: {
    caption: 'Click to interact with the IoT/OT Attack Vectors diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f0f0f0"/><text x="300" y="200" text-anchor="middle" font-size="24">IoT/OT Attack Vectors</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'hydra -L users.txt -P passwords.txt telnet://<target>', purpose: 'Test for default/weak Telnet credentials on IoT', out: 'Valid credentials if found', note: 'Demonstrates how Mirai propagates.', mistake: 'Running against unauthorized targets' }
    ],
    win: [
      { cmd: 'Get-EventLog -LogName Security | Where-Object {$_.EventID -eq 4625}', purpose: 'Check for failed RDP login attempts on an HMI', out: 'List of failed logons', note: 'Helps identify brute-force attacks against OT systems.', mistake: 'Not configuring audit policies' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Hydra', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment against provided vulnerable VMs.'],
    scenario: 'GFS has tasked you with demonstrating how quickly an insecure IoT camera can be compromised using automated tools.',
    objectives: ['Brute-force SSH/Telnet credentials on an IoT device', 'Analyze network traffic for plaintext credentials'],
    steps: [
      'Step 1: Use Nmap to confirm Telnet is open on the simulated IoT camera.',
      'Step 2: Run Hydra with a list of default IoT credentials (e.g., admin/admin, root/12345): `hydra -l root -P default_passes.txt telnet://<camera_ip>`.',
      'Step 3: Use the discovered credentials to log in.',
      'Step 4: Use Wireshark to capture the Telnet traffic and observe the plaintext password.'
    ],
    evidence: ['Hydra output showing successful login.', 'Wireshark packet capture showing plaintext credentials.'],
    validation: ['You should successfully authenticate to the camera and view the traffic in Wireshark.'],
    troubleshooting: ['If Hydra fails, ensure the target IP is correct and the password list contains the right defaults.'],
    mitre: [{ id: 'T1110.001', name: 'Password Guessing', tactic: 'Credential Access' }],
    cleanup: ['Exit the Telnet session.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which malware famously targeted Iranian nuclear centrifuges by manipulating Siemens PLCs?',
      opts: ['Mirai', 'Stuxnet', 'WannaCry', 'BlackEnergy'],
      correct: 1,
      fb: 'Stuxnet is the first known cyber weapon designed specifically to cause physical destruction in an OT environment.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary goal of the Mirai botnet?',
      opts: ['Encrypting hard drives for ransom', 'Launching massive Distributed Denial of Service (DDoS) attacks', 'Stealing credit card information', 'Manipulating industrial processes'],
      correct: 1,
      fb: 'Mirai infects vulnerable IoT devices to harness their combined bandwidth for devastating DDoS attacks.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'How do attackers most commonly gain initial access to consumer IoT devices?',
      opts: ['Zero-day exploits', 'Spear-phishing', 'Exploiting default or hardcoded credentials', 'Physical tampering'],
      correct: 2,
      fb: 'Many IoT devices are shipped with default credentials that are never changed by the user, making them easy targets.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which OT attack vector involves an attacker sending false normal operating data to the HMI while the physical process is failing?',
      opts: ['Man-in-the-Middle (MitM)', 'Replay Attack', 'Blinding/Spoofing', 'SQL Injection'],
      correct: 2,
      fb: 'Spoofing HMI data "blinds" operators to the reality of the physical process, a technique used in attacks like Stuxnet.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why is ransomware particularly dangerous in an OT environment?',
      opts: ['It steals intellectual property', 'It can encrypt the HMI, removing visibility and control of physical processes', 'It uses up all network bandwidth', 'It changes default passwords'],
      correct: 1,
      fb: 'If operators cannot see or control the physical process because the HMI is encrypted, they often have to shut down operations for safety.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'IoT devices are generally easy to patch and update automatically.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Many IoT devices lack a mechanism for seamless updates, leading to long-lived vulnerabilities.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which malware framework was specifically designed to attack electric grids and uses protocols like IEC 60870-5-104?',
      opts: ['Industroyer (CrashOverride)', 'Triton (Trisis)', 'NotPetya', 'Slammer'],
      correct: 0,
      fb: 'Industroyer is a sophisticated malware framework that caused power outages in Ukraine by directly speaking industrial protocols.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What type of OT system did the Triton (Trisis) malware specifically target?',
      opts: ['Data Historians', 'Safety Instrumented Systems (SIS)', 'SCADA Servers', 'IoT Gateways'],
      correct: 1,
      fb: 'Triton targeted the SIS, which is the last line of automated defense against physical disasters.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'A compromised IoT device on a corporate network can be used as a pivot point to attack internal IT assets.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'True. Insecure IoT devices often serve as a beachhead for attackers to move laterally into more secure areas.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which feature of UPnP (Universal Plug and Play) makes it a security risk for IoT?',
      opts: ['It uses strong encryption', 'It automatically opens firewall ports for inbound connections', 'It requires complex passwords', 'It limits network speed'],
      correct: 1,
      fb: 'UPnP allows devices to seamlessly discover each other and can automatically configure firewalls to allow inbound traffic, exposing devices to the internet.'
    }
  ],
  flashcards: [
    { f: 'Mirai', b: 'A botnet that infects poorly secured IoT devices to launch DDoS attacks.' },
    { f: 'Stuxnet', b: 'A sophisticated computer worm that targeted Iranian nuclear centrifuges.' }
  ],
  summary: [
    'IoT devices are plagued by weak default credentials and lack of updates.',
    'IoT botnets like Mirai use compromised devices for massive DDoS attacks.',
    'OT threats are often highly targeted and aimed at physical disruption.',
    'Malware like Stuxnet and Industroyer speak industrial protocols natively.',
    'Ransomware in OT can blind operators, forcing physical shutdowns.'
  ],
  outcomes: [
    'Describe the impact of botnets on IoT ecosystems.',
    'Analyze historical OT attacks and their methodologies.',
    'Identify the risks of IT/OT convergence.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Advanced',
    prerequisites: ['IoT and OT Concepts'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['iot-ot-hacking-tools'] = {
  eyebrow: 'Module 18 · Topic 4',
  title: 'IoT & OT Hacking Tools',
  module: 'Phase 18: OT/IoT Security Specialist',
  sub: 'Practical tools and techniques for assessing and exploiting IoT and OT environments.',
  objectives: ['Utilize Shodan for finding exposed devices', 'Use specialized tools for sniffing IoT/OT traffic', 'Understand firmware analysis tools'],
  learn: {
    simple: 'Securing IoT and OT requires specialized tools. Because traditional IT vulnerability scanners can crash fragile OT equipment, security professionals rely on passive network monitoring and specialized search engines. For IoT, analyzing hardware and firmware is often necessary to uncover hardcoded credentials or hidden backdoors.',
    analogy: 'Using a traditional IT scanner in an OT environment is like using a megaphone to check if someone is sleeping—you might find out, but you\'ll cause a lot of disruption. OT hacking tools are more like a stethoscope, listening passively without causing harm.',
    architecture: 'Reconnaissance often starts outside the network using OSINT and search engines like Shodan or Censys, which index exposed IoT and OT devices globally. Once on the network, passive sniffing with Wireshark (which has dissectors for protocols like Modbus and DNP3) is critical.\\n\\nFor IoT devices, hardware hacking involves tools like a Bus Pirate to interface with JTAG or UART pins on the circuit board, allowing extraction of the firmware. Firmware is then analyzed using tools like Binwalk to extract the file system and reverse-engineer the binaries using Ghidra or IDA Pro.\\n\\nIn OT environments, specialized frameworks like the Industrial Control Systems Exploitation Framework (ISF) provide modules specifically designed to interact with PLCs safely for assessment purposes.',
    why: 'Security professionals need hands-on experience with these specialized tools to properly audit and defend environments where standard IT tools are ineffective or dangerous.'
  },
  enterprise: {
    gfs: 'GFS\'s red team uses Shodan to ensure no enterprise building management systems are accidentally exposed to the internet. They also use Binwalk to analyze the firmware of new physical security badge readers before deployment.',
    windows: 'Windows machines can run Wireshark and specialized tools like the Modbus Poll application to simulate and test HMI-to-PLC communication during security assessments.',
    linux: 'Kali Linux includes many built-in tools for this domain, such as Binwalk for firmware extraction, RouterSploit for testing embedded devices, and various Python scripts for OT protocol interaction.'
  },
  workflow: [
    'Step 1: Perform external reconnaissance using Shodan or Censys.',
    'Step 2: If physical access is available, locate debugging ports (UART, JTAG) on the IoT device.',
    'Step 3: Extract firmware using a hardware interface tool or by downloading it from the vendor.',
    'Step 4: Use Binwalk to extract the filesystem from the firmware image.',
    'Step 5: Analyze the filesystem for hardcoded secrets, certificates, or vulnerable binaries.',
    'Step 6: For OT, use passive sniffing to capture traffic and analyze protocol exchanges in Wireshark.'
  ],
  diagram: {
    caption: 'Click to interact with the Firmware Extraction Workflow',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f0f0f0"/><text x="300" y="200" text-anchor="middle" font-size="24">Firmware Analysis Workflow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'binwalk -e firmware.bin', purpose: 'Extract files from a firmware image', out: 'Extracted filesystem directory', note: 'Crucial for finding hardcoded credentials in IoT devices.', mistake: 'Running binwalk without the extraction (-e) flag' }
    ],
    win: [
      { cmd: 'tshark -r capture.pcap -Y "mbtcp"', purpose: 'Filter PCAP for Modbus TCP traffic', out: 'Filtered packet list', note: 'Useful for passively analyzing OT communications.', mistake: 'Filtering for the wrong protocol port' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Binwalk', 'Firmware-Mod-Kit'],
    dependencies: [],
    safety: ['Perform firmware analysis on provided images only. Ensure you have the right to reverse-engineer the firmware.'],
    scenario: 'GFS has procured new smart locks for the server room. You need to analyze the vendor-provided firmware to check for backdoor accounts before deployment.',
    objectives: ['Extract a filesystem from an IoT firmware image', 'Locate sensitive files within the extracted filesystem'],
    steps: [
      'Step 1: Use binwalk to analyze the firmware image: `binwalk smartlock_fw.bin`.',
      'Step 2: Extract the filesystem: `binwalk -e smartlock_fw.bin`.',
      'Step 3: Navigate into the extracted `squashfs-root` directory.',
      'Step 4: Inspect `etc/shadow` or `etc/passwd` for hardcoded user hashes.',
      'Step 5: Look for web server configuration files that might reveal hidden API endpoints.'
    ],
    evidence: ['Binwalk extraction output.', 'Contents of the discovered shadow file.'],
    validation: ['You should find a hardcoded root password hash in the extracted filesystem.'],
    troubleshooting: ['If binwalk fails to extract, ensure `sasquatch` (for squashfs) is properly installed.'],
    mitre: [{ id: 'T1012', name: 'Query Registry/Filesystem', tactic: 'Discovery' }],
    cleanup: ['Delete the extracted filesystem directory to save space.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which search engine is specifically designed to find internet-connected devices like webcams, routers, and ICS systems?',
      opts: ['Google', 'DuckDuckGo', 'Shodan', 'Baidu'],
      correct: 2,
      fb: 'Shodan indexes banners and metadata from devices connected to the internet, making it invaluable for IoT/OT recon.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary purpose of the tool `binwalk`?',
      opts: ['Scanning for open ports', 'Extracting embedded files and executable code from firmware images', 'Sniffing wireless traffic', 'Brute-forcing passwords'],
      correct: 1,
      fb: 'Binwalk is the standard tool for analyzing, reverse engineering, and extracting firmware images.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which hardware interface is commonly used to debug and extract firmware directly from a circuit board?',
      opts: ['HDMI', 'JTAG', 'PCIe', 'SATA'],
      correct: 1,
      fb: 'JTAG (Joint Test Action Group) and UART are common hardware debugging interfaces exploited by hardware hackers.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why is passive network monitoring preferred over active scanning in OT environments?',
      opts: ['It is faster', 'Active scanning can crash legacy PLCs and disrupt physical processes', 'Passive monitoring finds more vulnerabilities', 'Passive monitoring uses less disk space'],
      correct: 1,
      fb: 'Legacy OT devices often have fragile TCP/IP stacks that crash when hit with unexpected packets from active scanners like Nmap.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which tool is an exploitation framework similar to Metasploit but focused on embedded devices and routers?',
      opts: ['RouterSploit', 'Burp Suite', 'Wireshark', 'Hashcat'],
      correct: 0,
      fb: 'RouterSploit contains modules for exploiting known vulnerabilities in routers, cameras, and other IoT devices.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Wireshark cannot decode industrial protocols like Modbus or DNP3.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Wireshark includes built-in dissectors for many common industrial protocols.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a "Bus Pirate"?',
      opts: ['A software tool for stealing data from a CAN bus', 'A hardware tool used to interface with electronic chips and protocols like I2C, SPI, and UART', 'A type of malware targeting industrial networks', 'A network switch used in OT'],
      correct: 1,
      fb: 'A Bus Pirate is a versatile hardware hacking tool used to communicate with various chips on an IoT device.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'When extracting a Linux-based IoT firmware, which filesystem format is most commonly found?',
      opts: ['NTFS', 'FAT32', 'SquashFS', 'EXT4'],
      correct: 2,
      fb: 'SquashFS is a highly compressed, read-only filesystem commonly used in embedded Linux devices to save space.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Finding a hardcoded private key in IoT firmware is a minor issue since it only affects that specific device.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Hardcoded keys are often shared across all devices of that model, meaning extracting it once compromises them all.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which tool is best suited for passively identifying ICS assets by analyzing a PCAP file?',
      opts: ['Nmap', 'Nessus', 'Zeek (Bro) / Wireshark', 'Metasploit'],
      correct: 2,
      fb: 'Zeek or Wireshark can passively analyze packet captures to identify assets and protocols without sending any traffic.'
    }
  ],
  flashcards: [
    { f: 'Shodan', b: 'A search engine for internet-connected devices, useful for finding exposed IoT/OT systems.' },
    { f: 'Binwalk', b: 'A tool for analyzing and extracting files from firmware images.' }
  ],
  summary: [
    'Shodan is essential for external IoT/OT reconnaissance.',
    'Passive sniffing is safer than active scanning in OT networks.',
    'Hardware hacking involves interfacing via UART or JTAG.',
    'Binwalk is used to extract and analyze IoT firmware.',
    'Hardcoded credentials and keys are common findings in firmware analysis.'
  ],
  outcomes: [
    'Explain the importance of passive reconnaissance in OT.',
    'Describe the firmware extraction process using Binwalk.',
    'Identify specialized tools used for hardware hacking.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Advanced',
    prerequisites: ['Linux Basics', 'Networking'],
    lastReviewed: '2026-07-18'
  }
};
"""

try:
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "// ── TAB WIRING ──" in content:
        # Check if already injected
        if "CONTENT['iot-concepts'] = {" not in content:
            new_content = content.replace("// ── TAB WIRING ──", payload + "\n// ── TAB WIRING ──")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Successfully injected Module 18 content into " + html_path)
        else:
            print("Content already seems to be injected in " + html_path)
    else:
        print("Could not find '// ── TAB WIRING ──' in " + html_path)
        print("Appending to the end of file as fallback.")
        with open(html_path, "a", encoding="utf-8") as f:
            f.write("\n" + payload)
except Exception as e:
    print("Error processing HTML file: " + str(e))
