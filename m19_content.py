import os

payload = """
CONTENT['cloud-concepts'] = {
  eyebrow: 'Module 19 · Topic 1',
  title: 'Cloud Computing Concepts',
  module: 'Phase 19: Cloud Security Architect',
  sub: 'Understanding the foundational models, services, and concepts of modern cloud computing.',
  objectives: ['Define essential cloud characteristics', 'Differentiate IaaS, PaaS, and SaaS', 'Understand cloud deployment models'],
  learn: {
    simple: 'Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider.',
    analogy: 'Think of cloud computing like using a public utility such as electricity. You do not need to build your own power plant; you just plug in your appliances and pay for the electricity you consume.',
    architecture: 'Cloud environments abstract physical resources using hypervisors and orchestration platforms. These abstracted resources form a massive, shared pool that can be dynamically provisioned. Users interact with these resources via web portals, command-line interfaces, or APIs. The control plane handles scheduling, authentication, and management of these resources, fundamentally shifting administration from hardware to software.',
    why: 'Enterprise cybersecurity professionals must understand cloud concepts because the traditional perimeter no longer exists. Security must be integrated into the control plane, identity systems, and the application layer itself.'
  },
  enterprise: {
    gfs: 'Global Financial Services is migrating its consumer-facing applications to the cloud to handle variable user loads during peak trading hours.',
    windows: 'In a Microsoft enterprise, this means integrating on-premises Active Directory with Azure Entra ID to establish a hybrid identity model for cloud resources.',
    linux: 'For Linux-based workloads, this involves adopting Amazon EKS (Elastic Kubernetes Service) to orchestrate containerized microservices dynamically.'
  },
  workflow: ['Step 1: Analyze business requirements.', 'Step 2: Choose service model (IaaS/PaaS/SaaS).', 'Step 3: Select deployment model (Public/Hybrid).', 'Step 4: Review shared responsibility model.', 'Step 5: Design initial architecture.', 'Step 6: Plan security and IAM controls.'],
  diagram: {
    caption: 'Cloud Service Models Comparison',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#2d3748"/><text x="300" y="200" fill="#fff" font-family="Arial" font-size="20" text-anchor="middle">Cloud Service Models (IaaS, PaaS, SaaS)</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'aws ec2 describe-instances', purpose: 'List EC2 instances', out: 'JSON object describing instances', note: 'Requires AWS CLI and credentials', mistake: 'Failing to specify region' }
    ],
    win: [
      { cmd: 'Get-AzVM', purpose: 'List Azure Virtual Machines', out: 'VM details', note: 'Requires Az module', mistake: 'Not logged in' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Beginner',
    duration: '30',
    platform: 'Web Console',
    environment: 'Cloud Lab',
    tools: ['AWS CLI', 'Azure CLI'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires a baseline audit of available cloud resources in a newly acquired tenant.',
    objectives: ['Enumerate cloud resources using CLI tools'],
    steps: ['Step 1: Authenticate with `aws configure`.', 'Step 2: List instances with `aws ec2 describe-instances`.', 'Step 3: Check S3 buckets with `aws s3 ls`.'],
    evidence: ['Output of listed resources.'],
    validation: ['You should see the provisioned lab resources.'],
    troubleshooting: ['Verify IAM permissions if Access Denied occurs.'],
    mitre: [{ id: 'T1526', name: 'Cloud Service Discovery', tactic: 'Discovery' }],
    cleanup: ['Remove local credentials.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Which cloud model provides software fully managed by the provider?', opts: ['IaaS', 'PaaS', 'SaaS', 'DaaS'], correct: 2, fb: 'SaaS abstracts everything away from the user except the software interface.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What describes the ability to rapidly scale resources up or down?', opts: ['Elasticity', 'High Availability', 'Fault Tolerance', 'Broad Network Access'], correct: 0, fb: 'Elasticity allows rapid provisioning and deprovisioning of resources.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Who is responsible for physical datacenter security in IaaS?', opts: ['Customer', 'Cloud Provider', 'Shared', 'Third Party'], correct: 1, fb: 'The cloud provider handles security OF the cloud, including physical data centers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which describes a hybrid cloud?', opts: ['Multiple public clouds', 'Public and private cloud combination', 'On-premises only', 'Community shared cloud'], correct: 1, fb: 'Hybrid cloud mixes public cloud services with private or on-premises infrastructure.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In PaaS, what is the customer primarily responsible for?', opts: ['Hypervisor security', 'Physical security', 'Data and application logic', 'Network cabling'], correct: 2, fb: 'In PaaS, the provider handles the platform, while you manage your apps and data.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which NIST cloud characteristic enables pay-as-you-go?', opts: ['Resource Pooling', 'Measured Service', 'Broad Network Access', 'On-demand Self Service'], correct: 1, fb: 'Measured service automatically controls and optimizes resource use by leveraging a metering capability.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is a key benefit of resource pooling?', opts: ['Higher cost', 'Multi-tenancy optimization', 'Physical isolation', 'Reduced bandwidth'], correct: 1, fb: 'Resource pooling serves multiple consumers using a multi-tenant model.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'In IaaS, the customer manages the hypervisor.', opts: ['True', 'False'], correct: 1, fb: 'The cloud provider manages the hypervisor in IaaS.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Multi-cloud and hybrid cloud mean the exact same thing.', opts: ['True', 'False'], correct: 1, fb: 'Multi-cloud uses multiple public providers, while hybrid combines public and private environments.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Serverless computing eliminates the need for physical servers entirely.', opts: ['True', 'False'], correct: 1, fb: 'Physical servers still exist, but their management is entirely abstracted away from the user.' }
  ],
  flashcards: [
    { f: 'IaaS', b: 'Infrastructure as a Service. Provider manages hardware, you manage OS and apps.' },
    { f: 'SaaS', b: 'Software as a Service. Provider manages everything, you just use the software.' }
  ],
  summary: ['Cloud computing delivers resources over the internet.', 'Service models define responsibilities.', 'Deployment models define infrastructure location.', 'Elasticity is a key cloud trait.', 'Security responsibilities are shared.'],
  outcomes: ['Identify cloud service models.', 'Understand cloud deployment models.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Beginner", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['cloud-threats'] = {
  eyebrow: 'Module 19 · Topic 2',
  title: 'Cloud Threats and Vulnerabilities',
  module: 'Phase 19: Cloud Security Architect',
  sub: 'Analyzing the modern threat landscape specific to cloud infrastructure and applications.',
  objectives: ['Identify common cloud vulnerabilities', 'Understand API security risks', 'Analyze misconfiguration impacts'],
  learn: {
    simple: 'As organizations move to the cloud, the threat landscape evolves. Traditional network attacks are less common, while identity-based attacks, API exploitation, and misconfigurations have become the primary vectors. Attackers target the control plane to gain pervasive access across the environment.',
    analogy: 'If a traditional network is a medieval castle with a moat, a cloud environment is a modern corporate high-rise. Attackers do not try to scale the walls; they try to steal an employee badge (identity) or exploit an unlocked side door (misconfiguration).',
    architecture: 'Cloud threats often exploit the management plane APIs. A compromised IAM credential can allow an attacker to bypass all network controls. Server-Side Request Forgery (SSRF) is particularly dangerous in the cloud, as it can be used to query the Instance Metadata Service (IMDS) and steal temporary compute credentials. Storage misconfigurations, such as publicly readable S3 buckets, remain a leading cause of massive data breaches.',
    why: 'Understanding these threats is vital because a single misconfiguration in the cloud can instantly expose terabytes of sensitive data to the public internet, completely bypassing traditional firewalls.'
  },
  enterprise: {
    gfs: 'GFS experienced an incident where an overly permissive IAM role assigned to a developer instance was compromised, leading to unauthorized data access.',
    windows: 'In Azure, attackers often target Global Administrator accounts using credential stuffing, attempting to bypass Conditional Access policies.',
    linux: 'In AWS, attackers look for SSRF vulnerabilities in web applications to extract EC2 IAM role credentials from the IMDS endpoint at 169.254.169.254.'
  },
  workflow: ['Step 1: Identify exposed APIs and endpoints.', 'Step 2: Review IAM policies for excessive permissions.', 'Step 3: Audit public storage containers.', 'Step 4: Implement MFA on all administrative accounts.', 'Step 5: Monitor for anomalous API calls (e.g., CloudTrail).', 'Step 6: Enforce IMDSv2 to mitigate SSRF.'],
  diagram: {
    caption: 'Cloud Threat Vectors',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#2d3748"/><text x="300" y="200" fill="#fff" font-family="Arial" font-size="20" text-anchor="middle">Cloud Threat Vectors</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'curl http://169.254.169.254/latest/meta-data/iam/security-credentials/', purpose: 'Query IMDS for IAM roles', out: 'Role names', note: 'Demonstrates SSRF risk', mistake: 'Running on non-EC2 instances' }
    ],
    win: [
      { cmd: 'Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri "http://169.254.169.254/metadata/instance?api-version=2021-02-01"', purpose: 'Query Azure IMDS', out: 'Instance metadata JSON', note: 'Requires Azure VM', mistake: 'Forgetting the Metadata header' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Cloud Lab',
    tools: ['Pacu', 'curl'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS wants to demonstrate the impact of SSRF and IMDS exploitation to its development team.',
    objectives: ['Exploit a simulated SSRF vulnerability', 'Extract cloud credentials from IMDS'],
    steps: ['Step 1: Identify the vulnerable web endpoint.', 'Step 2: Use `curl` to pass the IMDS URL payload to the SSRF parameter.', 'Step 3: Extract the temporary STS credentials.', 'Step 4: Configure AWS CLI with stolen credentials.'],
    evidence: ['Terminal output showing successful retrieval of STS credentials.'],
    validation: ['You should see the AccessKeyId, SecretAccessKey, and Token.'],
    troubleshooting: ['Ensure the SSRF payload is properly URL-encoded.'],
    mitre: [{ id: 'T1528', name: 'Steal Application Access Token', tactic: 'Credential Access' }],
    cleanup: ['Patch the SSRF vulnerability in the lab application.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is a common cause of cloud data breaches?', opts: ['Strong encryption', 'Misconfigured storage buckets', 'Proper IAM roles', 'Hardware failure'], correct: 1, fb: 'Misconfigured storage (like public S3 buckets) is a leading cause of cloud data leaks.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Which IP address is commonly used to access Instance Metadata Services (IMDS)?', opts: ['192.168.1.1', '10.0.0.1', '169.254.169.254', '127.0.0.1'], correct: 2, fb: '169.254.169.254 is the link-local address used for IMDS across most major cloud providers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What vulnerability allows attackers to query IMDS from outside the instance?', opts: ['XSS', 'SQLi', 'SSRF', 'CSRF'], correct: 2, fb: 'Server-Side Request Forgery (SSRF) allows attackers to force the server to make requests on their behalf, often targeting IMDS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does "Shadow IT" refer to in a cloud context?', opts: ['Hidden dark web services', 'Unsanctioned cloud resources deployed by employees', 'Encrypted network traffic', 'Cloud provider background tasks'], correct: 1, fb: 'Shadow IT occurs when employees deploy cloud resources without approval or oversight from IT.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which attack involves trying many compromised passwords against a cloud identity provider?', opts: ['Credential Stuffing', 'Phishing', 'DDoS', 'Ransomware'], correct: 0, fb: 'Credential stuffing uses known breached passwords to attempt logins on other services.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'How does IMDSv2 mitigate SSRF attacks in AWS?', opts: ['By blocking port 80', 'By requiring session tokens via PUT requests', 'By encrypting all metadata', 'By requiring MFA'], correct: 1, fb: 'IMDSv2 requires a session token fetched via a PUT request with specific headers, which most SSRF vulnerabilities cannot generate.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is "Cloud Jacking"?', opts: ['Stealing physical servers', 'Taking over a cloud account/subscription', 'Encrypting local data', 'Bypassing firewalls'], correct: 1, fb: 'Cloud jacking refers to an attacker gaining control of a victim’s cloud account, often for cryptomining or data theft.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'Cloud providers are responsible for configuring your S3 bucket permissions.', opts: ['True', 'False'], correct: 1, fb: 'Under the shared responsibility model, configuring access controls (like bucket policies) is the customer’s responsibility.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'API keys should be embedded directly into client-side code for easy access.', opts: ['True', 'False'], correct: 1, fb: 'Embedding API keys in code (hardcoding) is a severe security risk, as they can be easily extracted.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'A compromised IAM user with administrator privileges can delete entire cloud environments.', opts: ['True', 'False'], correct: 0, fb: 'An administrator account has full control over the environment and can cause catastrophic damage, including resource deletion.' }
  ],
  flashcards: [
    { f: 'SSRF', b: 'Server-Side Request Forgery, often used to attack cloud IMDS.' },
    { f: 'IMDS', b: 'Instance Metadata Service, accessible at 169.254.169.254.' }
  ],
  summary: ['Misconfigurations are the top cloud threat.', 'SSRF is heavily used to steal cloud credentials.', 'Identity is the new security perimeter.', 'IMDS exploitation provides attackers with lateral movement capabilities.', 'Shadow IT increases the attack surface.'],
  outcomes: ['Understand IMDS exploitation.', 'Identify risks of misconfigured storage.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 50, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['cloud-architecture'] = {
  eyebrow: 'Module 19 · Topic 3',
  title: 'Cloud Security Architecture',
  module: 'Phase 19: Cloud Security Architect',
  sub: 'Designing resilient, secure, and compliant cloud architectures.',
  objectives: ['Design secure VPCs', 'Implement Zero Trust principles', 'Understand microsegmentation'],
  learn: {
    simple: 'Cloud security architecture involves designing your cloud environment to be inherently secure. This includes properly isolating networks using Virtual Private Clouds (VPCs), implementing strict identity controls, and ensuring data is encrypted at rest and in transit.',
    analogy: 'Designing cloud architecture is like urban planning. You zone residential areas away from industrial ones (segmentation), ensure police and fire services can reach everywhere securely (monitoring), and check IDs at key checkpoints (Zero Trust).',
    architecture: 'A secure cloud architecture typically employs a multi-account strategy (like AWS Organizations or Azure Management Groups) to provide blast radius isolation. Network architecture relies on VPCs with public and private subnets, utilizing NAT Gateways for outbound access. Zero Trust architectures mandate that no entity is trusted by default, regardless of its network location, requiring continuous verification of identity, device health, and context before granting access.',
    why: 'Without a solid security architecture, tactical security tools will fail. Architecture provides the foundation that prevents lateral movement and contains breaches to a limited scope.'
  },
  enterprise: {
    gfs: 'GFS uses a hub-and-spoke network architecture in the cloud, routing all egress traffic through a centralized inspection VPC to enforce security policies.',
    windows: 'In Azure, this is implemented using Azure Virtual WAN and Azure Firewall to inspect traffic between spoke VNets and on-premises networks.',
    linux: 'In AWS, Transit Gateway is used to connect multiple VPCs, routing traffic through a centralized security VPC containing Next-Generation Firewalls.'
  },
  workflow: ['Step 1: Define account and subscription boundaries.', 'Step 2: Design the network layout (VPCs, Subnets).', 'Step 3: Implement routing and security groups/NSGs.', 'Step 4: Establish centralized logging and monitoring.', 'Step 5: Apply Zero Trust Identity controls.', 'Step 6: Automate infrastructure deployment via IaC.'],
  diagram: {
    caption: 'Secure Hub-and-Spoke Architecture',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#2d3748"/><text x="300" y="200" fill="#fff" font-family="Arial" font-size="20" text-anchor="middle">Cloud Architecture Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'terraform plan', purpose: 'Preview Infrastructure as Code changes', out: 'Execution plan detailing changes', note: 'Requires Terraform and cloud provider plugins', mistake: 'Running apply without reviewing plan' }
    ],
    win: [
      { cmd: 'Test-AzTemplate', purpose: 'Validate ARM template syntax', out: 'Validation result', note: 'Requires Azure PowerShell', mistake: 'Ignoring validation warnings' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Cloud Lab',
    tools: ['Terraform', 'Checkov'],
    dependencies: [],
    safety: ['Review Terraform plans carefully before applying.'],
    scenario: 'GFS is adopting Infrastructure as Code (IaC) and needs to ensure Terraform templates are free of security misconfigurations before deployment.',
    objectives: ['Scan IaC for vulnerabilities', 'Deploy a secure VPC architecture'],
    steps: ['Step 1: Run `checkov -d .` to scan the Terraform directory.', 'Step 2: Remediate identified issues (e.g., enabling encryption).', 'Step 3: Run `terraform init` and `terraform plan`.', 'Step 4: Execute `terraform apply` to deploy.'],
    evidence: ['Checkov scan output and successful Terraform deployment logs.'],
    validation: ['Resources should deploy without high-severity Checkov warnings.'],
    troubleshooting: ['If Checkov fails, review the specific rule ID and adjust the Terraform code.'],
    mitre: [{ id: 'T1562', name: 'Impair Defenses', tactic: 'Defense Evasion' }],
    cleanup: ['Run `terraform destroy` to tear down the environment.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is the primary purpose of a Virtual Private Cloud (VPC)?', opts: ['To increase compute speed', 'To provide a logically isolated network environment', 'To host public websites', 'To manage user passwords'], correct: 1, fb: 'VPCs provide logical network isolation for your cloud resources.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In a Zero Trust architecture, what is the core principle?', opts: ['Trust internal networks, distrust external', 'Trust but verify', 'Never trust, always verify', 'Rely solely on firewalls'], correct: 2, fb: 'Zero trust assumes breach and verifies every request regardless of origin.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is microsegmentation?', opts: ['Dividing a large hard drive into smaller partitions', 'Applying security policies to individual workloads or applications', 'Using small physical servers', 'Reducing the size of network packets'], correct: 1, fb: 'Microsegmentation isolates workloads from one another to prevent lateral movement.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is a benefit of a Hub-and-Spoke network topology in the cloud?', opts: ['It is the cheapest option', 'It centralizes network inspection and routing', 'It removes the need for IAM', 'It only works with one VPC'], correct: 1, fb: 'Hub-and-Spoke allows centralized security inspection, logging, and routing for multiple environments.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Why use a multi-account strategy (e.g., AWS Organizations)?', opts: ['To reduce the blast radius of a security incident', 'To increase the number of passwords needed', 'To bypass billing limits', 'To avoid using IAM'], correct: 0, fb: 'Multi-account architectures isolate environments (e.g., dev vs prod), limiting the impact if one account is compromised.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What does IaC stand for?', opts: ['Identity and Control', 'Infrastructure as Code', 'Internet Access Center', 'Internal Application Core'], correct: 1, fb: 'IaC allows provisioning infrastructure through machine-readable definition files.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which subnet type has a route to an Internet Gateway?', opts: ['Private Subnet', 'Public Subnet', 'Isolated Subnet', 'Management Subnet'], correct: 1, fb: 'A public subnet has a route to the internet, allowing resources within it to be directly accessible.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'A private subnet allows direct inbound connections from the internet.', opts: ['True', 'False'], correct: 1, fb: 'Private subnets do not have a direct route to the internet and are used for backend resources like databases.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Security Groups are stateful firewalls operating at the instance level.', opts: ['True', 'False'], correct: 0, fb: 'Security groups are stateful (return traffic is automatically allowed) and evaluate traffic at the ENI (instance) level.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'Network ACLs (NACLs) are stateless and operate at the subnet level.', opts: ['True', 'False'], correct: 0, fb: 'NACLs are stateless (requiring explicit inbound and outbound rules) and apply to entire subnets.' }
  ],
  flashcards: [
    { f: 'Zero Trust', b: 'Never trust, always verify. No implicit trust granted based on network location.' },
    { f: 'VPC', b: 'Virtual Private Cloud. A logically isolated network space in the cloud.' }
  ],
  summary: ['Architecture is the foundation of cloud security.', 'VPCs and subnets provide network isolation.', 'Zero Trust eliminates implicit trust.', 'Multi-account strategies limit blast radius.', 'IaC allows for repeatable, auditable deployments.'],
  outcomes: ['Design secure network topologies.', 'Understand the principles of Zero Trust.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 55, difficulty: "Advanced", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['cloud-security-tools'] = {
  eyebrow: 'Module 19 · Topic 4',
  title: 'Cloud Security Posture and Tooling',
  module: 'Phase 19: Cloud Security Architect',
  sub: 'Utilizing specialized tools to manage posture, detect threats, and ensure compliance.',
  objectives: ['Understand CSPM and CWPP', 'Configure cloud-native logging', 'Implement CASB solutions'],
  learn: {
    simple: 'Securing the cloud requires specialized tools. Cloud Security Posture Management (CSPM) tools continuously check your environment for misconfigurations. Cloud Workload Protection Platforms (CWPP) secure the actual servers and containers. Cloud Access Security Brokers (CASB) monitor and control user interactions with cloud services.',
    analogy: 'If the cloud is an office building, CSPM is the building inspector checking for code violations. CWPP is the security guard protecting specific rooms. CASB is the receptionist monitoring who enters and what they carry in or out.',
    architecture: 'Modern cloud security heavily relies on native tooling. Centralized logging (e.g., AWS CloudTrail, Azure Monitor) captures all API activity. These logs are ingested into a SIEM or a Cloud-Native Application Protection Platform (CNAPP), which combines CSPM, CWPP, and CIEM (Cloud Infrastructure Entitlement Management) into a single cohesive system for holistic visibility and automated remediation.',
    why: 'The scale and speed of cloud environments make manual auditing impossible. Automated tools are essential to maintain continuous compliance, detect anomalous API activity, and rapidly remediate misconfigurations before they are exploited.'
  },
  enterprise: {
    gfs: 'GFS deployed a CNAPP solution to gain unified visibility across their AWS and Azure environments, automatically remediating open S3 buckets and overly permissive Azure NSGs.',
    windows: 'Microsoft Defender for Cloud provides built-in CSPM and CWPP capabilities, offering secure score recommendations and threat protection for Azure resources.',
    linux: 'In AWS environments, Amazon GuardDuty acts as a threat detection service, continuously monitoring CloudTrail, VPC Flow Logs, and DNS logs for malicious behavior.'
  },
  workflow: ['Step 1: Enable comprehensive API logging (CloudTrail/Azure Activity Logs).', 'Step 2: Deploy a CSPM tool to establish a security baseline.', 'Step 3: Implement CWPP agents on compute workloads (if required).', 'Step 4: Integrate alerts with a SIEM or ticketing system.', 'Step 5: Setup automated remediation for high-risk misconfigurations.', 'Step 6: Regularly review posture and secure scores.'],
  diagram: {
    caption: 'Cloud Security Tooling Ecosystem',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#2d3748"/><text x="300" y="200" fill="#fff" font-family="Arial" font-size="20" text-anchor="middle">CSPM, CWPP, CASB Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'aws guardduty get-findings --detector-id <id> --finding-ids <id>', purpose: 'Retrieve GuardDuty threat findings', out: 'JSON detailed finding', note: 'Requires GuardDuty enabled', mistake: 'Using wrong detector ID' }
    ],
    win: [
      { cmd: 'Get-AzSecurityPricing', purpose: 'Check Defender for Cloud pricing tiers', out: 'List of plans and statuses', note: 'Requires Security module', mistake: 'Lacking subscription reader permissions' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Web Console',
    environment: 'Cloud Lab',
    tools: ['AWS Security Hub', 'ScoutSuite'],
    dependencies: [],
    safety: ['Run auditing tools with read-only credentials.'],
    scenario: 'GFS requires an immediate compliance report of their cloud infrastructure against the CIS Foundations Benchmark.',
    objectives: ['Run an open-source CSPM tool', 'Analyze the generated compliance report'],
    steps: ['Step 1: Configure AWS CLI with read-only credentials.', 'Step 2: Run `scout aws` to initiate the ScoutSuite audit.', 'Step 3: Open the generated HTML report in a browser.', 'Step 4: Identify the top 3 high-severity misconfigurations.'],
    evidence: ['Generated ScoutSuite HTML report.'],
    validation: ['The report should highlight specific IAM and S3 misconfigurations intentionally placed in the lab.'],
    troubleshooting: ['If ScoutSuite fails, verify python dependencies and AWS credential validity.'],
    mitre: [{ id: 'T1526', name: 'Cloud Service Discovery', tactic: 'Discovery' }],
    cleanup: ['Delete the generated report files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Which tool type focuses on identifying misconfigurations in cloud infrastructure?', opts: ['CWPP', 'CASB', 'CSPM', 'WAF'], correct: 2, fb: 'Cloud Security Posture Management (CSPM) evaluates cloud configurations against security best practices and compliance frameworks.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What does CASB stand for?', opts: ['Cloud Application Security Broker', 'Cloud Access Security Broker', 'Centralized Authentication System Base', 'Cloud Assessment and Security Board'], correct: 1, fb: 'A Cloud Access Security Broker sits between users and cloud applications to monitor activity and enforce security policies.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which service provides threat detection by monitoring AWS logs for malicious activity?', opts: ['AWS Shield', 'AWS WAF', 'Amazon Macie', 'Amazon GuardDuty'], correct: 3, fb: 'GuardDuty continuously monitors CloudTrail, VPC Flow Logs, and DNS logs for threats.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary function of a CWPP?', opts: ['Monitoring network traffic', 'Securing workloads like VMs and containers', 'Managing IAM policies', 'Generating compliance reports'], correct: 1, fb: 'Cloud Workload Protection Platforms (CWPP) focus on securing the internal components of workloads (servers, containers, serverless).' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What does CNAPP aim to achieve?', opts: ['Providing free cloud storage', 'Combining CSPM, CWPP, and CIEM into a single platform', 'Replacing all local firewalls', 'Managing physical datacenter access'], correct: 1, fb: 'Cloud-Native Application Protection Platforms (CNAPP) unify various cloud security tools for comprehensive visibility.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In Azure, what is the primary service for centralizing security alerts and posture management?', opts: ['Azure Active Directory', 'Azure Firewall', 'Microsoft Defender for Cloud', 'Azure Key Vault'], correct: 2, fb: 'Defender for Cloud is Microsoft’s unified CSPM and CWPP solution.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is CIEM?', opts: ['Cloud Infrastructure Entitlement Management', 'Cloud Incident Execution Matrix', 'Centralized Identity and Encryption Mechanism', 'Compute Infrastructure Elastic Management'], correct: 0, fb: 'CIEM focuses on managing identities and privileges, ensuring least privilege access across cloud environments.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'CSPM tools can often automatically remediate misconfigurations.', opts: ['True', 'False'], correct: 0, fb: 'Many modern CSPM tools support auto-remediation, such as automatically turning off public access to an S3 bucket.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'AWS CloudTrail only logs API calls made via the web console.', opts: ['True', 'False'], correct: 1, fb: 'CloudTrail logs API calls made from the console, CLI, SDKs, and other AWS services.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'ScoutSuite is an open-source CWPP tool.', opts: ['True', 'False'], correct: 1, fb: 'ScoutSuite is an open-source multi-cloud security auditing tool, which functions more like a CSPM than a CWPP.' }
  ],
  flashcards: [
    { f: 'CSPM', b: 'Cloud Security Posture Management. Checks for misconfigurations.' },
    { f: 'CASB', b: 'Cloud Access Security Broker. Monitors user interactions with SaaS.' }
  ],
  summary: ['CSPM manages infrastructure posture.', 'CWPP protects compute workloads.', 'CASB secures user access to SaaS applications.', 'CNAPP unifies cloud security tools.', 'Automated remediation is critical for cloud security.'],
  outcomes: ['Understand the difference between CSPM and CWPP.', 'Identify appropriate tools for cloud auditing.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 40, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};
"""

html_path = 'C:/Users/navee/OneDrive/Desktop/Greatcoder/CEHv13/ceh-platform/frontend/index.html'

try:
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    marker = '// ── TAB WIRING ──'
    if marker in content:
        new_content = content.replace(marker, payload + '\\n' + marker)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected payload into index.html")
    else:
        print("Marker not found in index.html!")
except Exception as e:
    print(f"Error modifying index.html: {e}")
