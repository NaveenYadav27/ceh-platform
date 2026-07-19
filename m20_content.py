import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, 'frontend', 'index.html')

content_payload = r"""
CONTENT['crypto-concepts'] = {
  eyebrow: 'Module 20 · Topic 1',
  title: 'Cryptography Concepts',
  module: 'Phase 20: Cryptography Expert',
  sub: 'Fundamental principles of securing digital information through cryptography.',
  objectives: ['Understand CIA triad', 'Differentiate symmetric and asymmetric encryption', 'Explain hashing and digital signatures'],
  learn: {
    simple: 'Cryptography is the practice and study of techniques for secure communication in the presence of adversarial behavior. It involves constructing and analyzing protocols that prevent third parties or the public from reading private messages. Modern cryptography intersects the disciplines of mathematics, computer science, electrical engineering, communication science, and physics.',
    analogy: 'Think of cryptography like a lockbox with a special key. Only the person with the right key can open the box to see what is inside, keeping the contents safe from everyone else.',
    architecture: 'Cryptographic systems consist of algorithms and keys. Symmetric-key cryptography uses the same key for both encryption and decryption, requiring a secure method to exchange the key. Asymmetric-key (public-key) cryptography uses a pair of keys: a public key for encryption and a private key for decryption. This solves the key exchange problem but is computationally more expensive.\n\nHashing algorithms provide data integrity by generating a fixed-size string (hash value) from variable-size input data. Any change to the input drastically changes the hash. Digital signatures combine asymmetric encryption and hashing to provide authentication, non-repudiation, and integrity.',
    why: 'In an enterprise environment, cryptography is foundational for securing communications, protecting sensitive data at rest and in transit, and ensuring the authenticity of transactions and identities.'
  },
  enterprise: {
    gfs: 'Global Financial Services uses strong cryptography to secure customer financial transactions and comply with regulatory requirements like PCI DSS.',
    windows: 'Windows uses cryptography for BitLocker drive encryption, EFS (Encrypting File System), and TLS/SSL for secure network communications.',
    linux: 'Linux environments rely on cryptography for SSH access, LUKS (Linux Unified Key Setup) disk encryption, and GPG for file and email encryption.'
  },
  workflow: ['Step 1: Identify the data to be protected.', 'Step 2: Determine the appropriate cryptographic method (encryption, hashing, digital signature).', 'Step 3: Select a strong, industry-standard algorithm (e.g., AES, RSA, SHA-256).', 'Step 4: Manage cryptographic keys securely.', 'Step 5: Implement the cryptographic solution.', 'Step 6: Regularly review and update cryptographic practices.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f0f0f0"/><text x="300" y="200" font-family="Arial" font-size="24" text-anchor="middle">Cryptography Concepts Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'openssl enc -aes-256-cbc -in file.txt -out file.enc', purpose: 'Encrypt a file', out: 'Encrypted file', note: 'Prompts for password', mistake: 'Using weak algorithms like DES' }
    ],
    win: [
      { cmd: 'Protect-CmsMessage -To "recipient@gfs.com" -Content "Secret"', purpose: 'Encrypt message', out: 'CMS message object', note: 'Requires recipient certificate', mistake: 'Missing certificate' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['OpenSSL', 'GnuPG'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS needs to securely transmit a confidential financial report to a partner organization.',
    objectives: ['Encrypt and decrypt a file using OpenSSL'],
    steps: ['Step 1: Create a test file with `echo "Confidential Data" > report.txt`.', 'Step 2: Encrypt the file with `openssl enc -aes-256-cbc -in report.txt -out report.enc`.', 'Step 3: Decrypt the file to verify.'],
    evidence: ['Terminal output showing successful encryption and decryption.'],
    validation: ['You should see: the original plaintext after decryption'],
    troubleshooting: ['If openssl fails, ensure it is installed.'],
    mitre: [{ id: 'T1555', name: 'Credentials from Password Stores', tactic: 'Credential Access' }],
    cleanup: ['Remove the test files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following provides data integrity?', opts: ['Encryption', 'Hashing', 'Steganography', 'Obfuscation'], correct: 1, fb: 'Hashing generates a unique digest that changes if the data is altered, ensuring integrity.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Symmetric encryption uses:', opts: ['One shared key', 'A public and private key pair', 'No keys', 'Only a public key'], correct: 0, fb: 'Symmetric encryption uses a single shared key for both encryption and decryption.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which is a goal of cryptography?', opts: ['Confidentiality', 'Integrity', 'Non-repudiation', 'All of the above'], correct: 3, fb: 'Cryptography aims to provide confidentiality, integrity, authentication, and non-repudiation.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Asymmetric encryption is faster than symmetric encryption.', opts: ['True', 'False'], correct: 1, fb: 'Symmetric encryption is generally much faster than asymmetric encryption.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Digital signatures provide:', opts: ['Confidentiality', 'Non-repudiation', 'Availability', 'Redundancy'], correct: 1, fb: 'Digital signatures verify the sender identity and ensure they cannot deny sending the message.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which algorithm is asymmetric?', opts: ['AES', 'DES', 'RSA', 'RC4'], correct: 2, fb: 'RSA is a widely used asymmetric encryption algorithm.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does CIA stand for in security?', opts: ['Central Intelligence Agency', 'Confidentiality, Integrity, Availability', 'Control, Identity, Access', 'Cryptography, Information, Assurance'], correct: 1, fb: 'The CIA triad is the foundation of information security.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Hashing is reversible.', opts: ['True', 'False'], correct: 1, fb: 'Hashing is a one-way function and cannot be reversed to obtain the original data.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which is a common hashing algorithm?', opts: ['AES', 'RSA', 'SHA-256', 'Blowfish'], correct: 2, fb: 'SHA-256 is a standard cryptographic hash function.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Steganography is a form of cryptography.', opts: ['True', 'False'], correct: 1, fb: 'Steganography hides the existence of a message, whereas cryptography hides the meaning.' }
  ],
  flashcards: [
    { f: 'Cryptography', b: 'The practice of securing communication from adversaries.' },
    { f: 'Symmetric Encryption', b: 'Uses the same key to encrypt and decrypt data.' }
  ],
  summary: ['Cryptography secures digital information.', 'Symmetric encryption uses one key.', 'Asymmetric encryption uses two keys.', 'Hashing ensures data integrity.', 'Digital signatures provide authentication and non-repudiation.'],
  outcomes: ['Explain fundamental cryptographic concepts.', 'Identify appropriate cryptographic techniques for different scenarios.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['encryption-algorithms'] = {
  eyebrow: 'Module 20 · Topic 2',
  title: 'Encryption Algorithms',
  module: 'Phase 20: Cryptography Expert',
  sub: 'In-depth look at standard symmetric and asymmetric encryption algorithms.',
  objectives: ['Analyze block and stream ciphers', 'Understand AES and RSA', 'Evaluate algorithm strengths and weaknesses'],
  learn: {
    simple: 'Encryption algorithms are mathematical procedures used to convert plaintext into ciphertext. They are categorized mainly into symmetric and asymmetric algorithms. Symmetric algorithms can be further divided into block ciphers, which encrypt data in fixed-size blocks, and stream ciphers, which encrypt data one bit or byte at a time.',
    analogy: 'An encryption algorithm is like a complex recipe for scrambling a message. Only someone with the recipe and the secret ingredient (the key) can unscramble it.',
    architecture: 'Advanced Encryption Standard (AES) is the current standard for symmetric encryption, operating on 128-bit blocks with key sizes of 128, 192, or 256 bits. It replaced the Data Encryption Standard (DES) which is now considered insecure due to its small 56-bit key size.\n\nRSA (Rivest-Shamir-Adleman) is a widely used asymmetric algorithm based on the mathematical difficulty of factoring large prime numbers. It is commonly used for key exchange and digital signatures rather than bulk data encryption due to its performance overhead.',
    why: 'Choosing the right encryption algorithm is critical for enterprise security. Using outdated algorithms like DES or weak configurations can lead to data breaches.'
  },
  enterprise: {
    gfs: 'GFS mandates the use of AES-256 for encrypting all sensitive customer data at rest in their databases.',
    windows: 'Windows IPsec implementations utilize AES for securing network traffic between servers.',
    linux: 'Linux systems use strong algorithms like ChaCha20-Poly1305 for high-performance secure network tunnels (e.g., WireGuard).'
  },
  workflow: ['Step 1: Assess the data security requirements.', 'Step 2: Choose between symmetric (bulk data) or asymmetric (key exchange/signatures).', 'Step 3: Select a standard algorithm (e.g., AES for symmetric, RSA/ECC for asymmetric).', 'Step 4: Determine the appropriate key size (e.g., AES-256, RSA-2048+).', 'Step 5: Implement using established cryptographic libraries (e.g., OpenSSL, Bouncy Castle).', 'Step 6: Avoid custom cryptography implementations.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#e0f7fa"/><text x="300" y="200" font-family="Arial" font-size="24" text-anchor="middle">Encryption Algorithms Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'openssl speed aes-256-cbc rsa2048', purpose: 'Benchmark algorithms', out: 'Performance metrics', note: 'Compare speeds', mistake: 'Ignoring hardware acceleration' }
    ],
    win: [
      { cmd: 'Get-TlsCipherSuite', purpose: 'List supported cipher suites', out: 'List of ciphers', note: 'Useful for auditing', mistake: 'Leaving weak ciphers enabled' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['OpenSSL'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS needs to benchmark different encryption algorithms to select the optimal one for a new high-speed VPN.',
    objectives: ['Compare the performance of AES and RSA'],
    steps: ['Step 1: Open a terminal.', 'Step 2: Run `openssl speed aes-256-cbc rsa2048`.', 'Step 3: Analyze the output to see the difference in processing speed.'],
    evidence: ['Terminal output showing the benchmark results.'],
    validation: ['You should see: AES is significantly faster than RSA for bulk data'],
    troubleshooting: ['If the command is not found, install openssl.'],
    mitre: [{ id: 'T1555', name: 'Credentials from Password Stores', tactic: 'Credential Access' }],
    cleanup: ['No cleanup required.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is a symmetric block cipher?', opts: ['RSA', 'RC4', 'AES', 'Diffie-Hellman'], correct: 2, fb: 'AES is a standard symmetric block cipher.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the block size of AES?', opts: ['64 bits', '128 bits', '256 bits', 'Variable'], correct: 1, fb: 'AES always has a block size of 128 bits.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'RSA is based on the difficulty of:', opts: ['Calculating discrete logarithms', 'Factoring large prime numbers', 'Elliptic curve mathematics', 'Symmetric key exchange'], correct: 1, fb: 'RSA security relies on the difficulty of prime factorization.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which algorithm is considered obsolete and insecure?', opts: ['AES', 'DES', '3DES', 'Both B and C'], correct: 3, fb: 'DES and 3DES are no longer considered secure for modern applications.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'ECC (Elliptic Curve Cryptography) provides similar security to RSA with smaller key sizes.', opts: ['True', 'False'], correct: 0, fb: 'ECC is highly efficient and offers strong security with smaller keys compared to RSA.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Stream ciphers encrypt data:', opts: ['In fixed blocks', 'One bit or byte at a time', 'Using public keys only', 'Using hashing algorithms'], correct: 1, fb: 'Stream ciphers encrypt data continuously.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'RC4 is a widely recommended stream cipher for new applications.', opts: ['True', 'False'], correct: 1, fb: 'RC4 has known vulnerabilities and is deprecated in modern protocols like TLS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which mode of operation for block ciphers is generally discouraged due to pattern leakage?', opts: ['CBC', 'GCM', 'ECB', 'CTR'], correct: 2, fb: 'Electronic Codebook (ECB) mode encrypts identical plaintext blocks into identical ciphertext blocks.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which algorithm is commonly used for key exchange over an insecure channel?', opts: ['AES', 'Diffie-Hellman', 'SHA-1', 'MD5'], correct: 1, fb: 'Diffie-Hellman allows two parties to establish a shared secret over an insecure channel.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'A 256-bit key provides twice the security of a 128-bit key in symmetric encryption.', opts: ['True', 'False'], correct: 1, fb: 'A 256-bit key provides 2^128 times more security (in terms of brute-force combinations), not just twice as much.' }
  ],
  flashcards: [
    { f: 'AES', b: 'Advanced Encryption Standard, a symmetric block cipher.' },
    { f: 'RSA', b: 'An asymmetric algorithm based on prime factorization.' }
  ],
  summary: ['AES is the standard symmetric cipher.', 'RSA is a common asymmetric cipher.', 'Block ciphers process data in blocks.', 'Stream ciphers process data continuously.', 'Algorithm choice impacts both security and performance.'],
  outcomes: ['Compare symmetric and asymmetric algorithms.', 'Select appropriate encryption algorithms for specific use cases.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['pki-concepts'] = {
  eyebrow: 'Module 20 · Topic 3',
  title: 'Public Key Infrastructure (PKI)',
  module: 'Phase 20: Cryptography Expert',
  sub: 'Framework for managing digital certificates and public-key encryption.',
  objectives: ['Understand the role of a CA', 'Analyze digital certificates', 'Explain certificate revocation'],
  learn: {
    simple: 'Public Key Infrastructure (PKI) is a set of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption.',
    analogy: 'PKI is like the passport system. A passport agency (Certificate Authority) verifies your identity and issues a passport (Digital Certificate). Others trust the passport because they trust the agency that issued it.',
    architecture: 'At the heart of a PKI is the Certificate Authority (CA), which issues digital certificates binding a public key to an entity (person, organization, server). Registration Authorities (RAs) verify the identity of entities requesting certificates. \n\nCertificates follow the X.509 standard. When a certificate is compromised or no longer needed, it must be revoked. This is handled via Certificate Revocation Lists (CRLs) or the Online Certificate Status Protocol (OCSP), which allow clients to verify a certificate\'s validity in real-time.',
    why: 'PKI is essential for establishing trust in large networks, enabling secure web browsing (HTTPS), secure email (S/MIME), and strong authentication.'
  },
  enterprise: {
    gfs: 'GFS operates an internal two-tier PKI hierarchy to issue certificates for employee smart cards and internal web servers.',
    windows: 'Active Directory Certificate Services (AD CS) is the primary PKI solution for Windows enterprise environments.',
    linux: 'Linux environments often use OpenSSL or tools like Dogtag to manage internal CAs and issue certificates for services like Apache and Nginx.'
  },
  workflow: ['Step 1: Entity generates a key pair and a Certificate Signing Request (CSR).', 'Step 2: Entity submits the CSR to the RA/CA.', 'Step 3: RA verifies the entity\'s identity.', 'Step 4: CA signs the public key and issues the certificate.', 'Step 5: Entity installs the certificate.', 'Step 6: Relying parties verify the certificate against the CA\'s public key and check revocation status.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f9fbe7"/><text x="300" y="200" font-family="Arial" font-size="24" text-anchor="middle">PKI Architecture Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'openssl x509 -in cert.pem -text -noout', purpose: 'View certificate details', out: 'Decoded cert info', note: 'Check expiration date', mistake: 'Ignoring the issuer' }
    ],
    win: [
      { cmd: 'certutil -dump cert.cer', purpose: 'Dump certificate info', out: 'Detailed cert properties', note: 'Built-in Windows tool', mistake: 'Using incorrect format' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['OpenSSL'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires a new internal web server. You must generate a CSR to obtain an SSL certificate from the internal CA.',
    objectives: ['Generate a private key and a CSR'],
    steps: ['Step 1: Generate a key and CSR with `openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr`.', 'Step 2: Fill in the required details (Common Name is critical).', 'Step 3: View the CSR details with `openssl req -in server.csr -noout -text`.'],
    evidence: ['Terminal output showing the generated CSR details.'],
    validation: ['You should see: the Subject information you entered'],
    troubleshooting: ['If openssl prompts for a password, you omitted the -nodes flag.'],
    mitre: [{ id: 'T1555', name: 'Credentials from Password Stores', tactic: 'Credential Access' }],
    cleanup: ['Delete the key and CSR files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary function of a Certificate Authority (CA)?', opts: ['To encrypt data', 'To issue and manage digital certificates', 'To generate hash values', 'To route network traffic securely'], correct: 1, fb: 'The CA is the trusted entity that issues digital certificates.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which standard defines the format for public key certificates?', opts: ['IEEE 802.1X', 'X.509', 'PKCS#11', 'RFC 1918'], correct: 1, fb: 'X.509 is the standard format for digital certificates in PKI.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is used to check if a certificate has been revoked in real-time?', opts: ['CRL', 'OCSP', 'CSR', 'RA'], correct: 1, fb: 'Online Certificate Status Protocol (OCSP) provides real-time revocation checking.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'A Digital Certificate binds a public key to an entity\'s identity.', opts: ['True', 'False'], correct: 0, fb: 'Certificates verify that a specific public key belongs to a specific entity.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does an entity submit to a CA to request a certificate?', opts: ['A private key', 'A CSR (Certificate Signing Request)', 'A CRL', 'A digital signature'], correct: 1, fb: 'A CSR contains the entity\'s public key and identity information.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'If a CA\'s private key is compromised, what happens?', opts: ['Only new certificates are affected', 'All certificates issued by that CA must be revoked', 'Nothing, the public key is still safe', 'The RA takes over'], correct: 1, fb: 'Compromise of the CA\'s private key breaks the entire chain of trust.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Self-signed certificates are generally trusted by default web browsers.', opts: ['True', 'False'], correct: 1, fb: 'Browsers typically do not trust self-signed certificates and will show a warning.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Root CA?', opts: ['A CA that issues certificates to end-users only', 'The top-most CA in a PKI hierarchy', 'A CA that only revokes certificates', 'A temporary CA'], correct: 1, fb: 'The Root CA is the ultimate anchor of trust in a hierarchical PKI.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which component verifies the identity of the user before a certificate is issued?', opts: ['CA', 'RA', 'VA', 'CRL'], correct: 1, fb: 'The Registration Authority (RA) handles identity verification.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Certificate pinning helps prevent man-in-the-middle attacks by associating a host with its expected certificate or public key.', opts: ['True', 'False'], correct: 0, fb: 'Pinning restricts which certificates are considered valid for a particular website.' }
  ],
  flashcards: [
    { f: 'CA', b: 'Certificate Authority, the entity that issues certificates.' },
    { f: 'CSR', b: 'Certificate Signing Request, submitted to a CA to obtain a certificate.' }
  ],
  summary: ['PKI manages digital certificates and public keys.', 'CAs are the trusted root of the PKI.', 'Certificates follow the X.509 standard.', 'Revocation is handled via CRLs or OCSP.', 'PKI is crucial for HTTPS and secure email.'],
  outcomes: ['Explain the components of a PKI.', 'Analyze the lifecycle of a digital certificate.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['crypto-attacks'] = {
  eyebrow: 'Module 20 · Topic 4',
  title: 'Cryptographic Attacks',
  module: 'Phase 20: Cryptography Expert',
  sub: 'Techniques used by adversaries to break cryptographic systems.',
  objectives: ['Identify common cryptographic attacks', 'Understand brute-force and dictionary attacks', 'Implement countermeasures against crypto attacks'],
  learn: {
    simple: 'Cryptographic attacks attempt to bypass or break the security provided by cryptographic algorithms and protocols. Attackers may target the algorithm itself, the key management processes, or the implementation of the cryptography.',
    analogy: 'Attacking cryptography is like trying to open a safe. You can try every possible combination (brute force), use a list of common combinations (dictionary), or look for a flaw in the safe\'s lock mechanism itself.',
    architecture: 'Common attacks include Ciphertext-only (attacker only has the encrypted text), Known-plaintext (attacker has pairs of plaintext and ciphertext), and Chosen-plaintext (attacker can encrypt chosen messages). \n\nImplementation flaws are often exploited, such as side-channel attacks (monitoring power consumption or timing), padding oracle attacks, or exploiting weak random number generators. Downgrade attacks force a system to use a weaker, vulnerable cryptographic protocol (e.g., forcing SSLv3 instead of TLS 1.2).',
    why: 'Understanding cryptographic attacks is vital for defenders to configure systems securely, patch vulnerabilities, and avoid implementing custom, untested cryptography.'
  },
  enterprise: {
    gfs: 'GFS constantly monitors for TLS downgrade attacks on their public-facing web servers to prevent interception of customer data.',
    windows: 'Windows environments must secure NTLM and Kerberos authentication against offline cracking and pass-the-hash attacks.',
    linux: 'Linux administrators use strong password hashing algorithms like Yescrypt or Argon2 to protect /etc/shadow from brute-force attacks.'
  },
  workflow: ['Step 1: Threat model the cryptographic implementation.', 'Step 2: Ensure strong, modern algorithms are used (avoid DES, MD5, SHA1).', 'Step 3: Implement perfect forward secrecy (PFS) where possible.', 'Step 4: Protect cryptographic keys in hardware (HSM/TPM) if available.', 'Step 5: Apply patches to cryptographic libraries (e.g., OpenSSL updates).', 'Step 6: Monitor for anomalous cryptographic failures or downgrade attempts.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#ffebee"/><text x="300" y="200" font-family="Arial" font-size="24" text-anchor="middle">Cryptographic Attacks Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'hashcat -m 0 -a 0 hashes.txt wordlist.txt', purpose: 'Crack MD5 hashes', out: 'Recovered passwords', note: 'Dictionary attack', mistake: 'Not specifying correct hash type' }
    ],
    win: [
      { cmd: 'john.exe --format=NT hashes.txt', purpose: 'Crack NTLM hashes', out: 'Recovered passwords', note: 'Uses John the Ripper', mistake: 'Incorrect format specified' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Hashcat'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'As part of a penetration test for GFS, you have recovered a database dump containing MD5 password hashes and need to demonstrate the risk of using weak hashing.',
    objectives: ['Crack MD5 hashes using a dictionary attack'],
    steps: ['Step 1: Create a file `hashes.txt` with an MD5 hash (e.g., the hash for "password123").', 'Step 2: Use `hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt`.', 'Step 3: Review the output for cracked passwords.'],
    evidence: ['Terminal output showing the cracked hash.'],
    validation: ['You should see: the plaintext password alongside the hash'],
    troubleshooting: ['If hashcat fails, ensure the rockyou wordlist is extracted.'],
    mitre: [{ id: 'T1110.002', name: 'Password Cracking', tactic: 'Credential Access' }],
    cleanup: ['Remove the hashes.txt file.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which attack involves trying all possible keys?', opts: ['Dictionary attack', 'Rainbow table attack', 'Brute-force attack', 'Birthday attack'], correct: 2, fb: 'Brute-force tries every possible combination until the correct key is found.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Birthday attack primarily used against?', opts: ['Symmetric encryption', 'Asymmetric encryption', 'Hashing algorithms', 'Digital signatures'], correct: 2, fb: 'Birthday attacks exploit the mathematics of probability to find hash collisions.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In a Known-Plaintext attack, the attacker has access to:', opts: ['Only the ciphertext', 'Pairs of plaintext and its corresponding ciphertext', 'The private key', 'The hashing algorithm only'], correct: 1, fb: 'The attacker uses known plaintext-ciphertext pairs to deduce the key or algorithm.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Rainbow tables are used for:', opts: ['Encrypting large files', 'Speeding up the cracking of password hashes', 'Generating random numbers', 'Securing key exchanges'], correct: 1, fb: 'Rainbow tables contain precomputed hashes to quickly crack passwords.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which technique mitigates rainbow table attacks?', opts: ['Using a smaller key', 'Adding a random salt to the password before hashing', 'Using MD5', 'Encrypting the hash'], correct: 1, fb: 'Salting ensures that identical passwords have different hashes, rendering rainbow tables ineffective.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'A downgrade attack forces a system to use a weaker, older protocol.', opts: ['True', 'False'], correct: 0, fb: 'Attackers manipulate the negotiation phase to force the use of vulnerable protocols like SSLv3.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which attack exploits physical characteristics of an implementation, such as timing or power consumption?', opts: ['Brute-force', 'Side-channel attack', 'Chosen-ciphertext attack', 'Man-in-the-middle'], correct: 1, fb: 'Side-channel attacks look at physical leaks rather than mathematical weaknesses.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'POODLE is an example of an attack against which protocol?', opts: ['IPsec', 'SSLv3', 'SSH', 'WPA2'], correct: 1, fb: 'POODLE exploited a vulnerability in the fallback to SSLv3.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Collision resistance means it should be hard to find two different inputs that produce the same hash output.', opts: ['True', 'False'], correct: 0, fb: 'Strong cryptographic hash functions must be collision-resistant.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Man-in-the-Middle (MitM) attack in cryptography?', opts: ['An attacker intercepts and relays communications between two parties', 'An attacker steals the physical server', 'An attacker uses a supercomputer to guess keys', 'An attacker exploits a buffer overflow'], correct: 0, fb: 'In a MitM attack, the attacker secretly intercepts and possibly alters the communication.' }
  ],
  flashcards: [
    { f: 'Brute-force', b: 'An attack that tries every possible key combination.' },
    { f: 'Salt', b: 'Random data added to a password before hashing to prevent rainbow table attacks.' }
  ],
  summary: ['Cryptographic attacks target algorithms, keys, or implementations.', 'Brute-force tries all keys; dictionary tries common words.', 'Salting prevents rainbow table attacks.', 'Side-channel attacks exploit physical implementation leaks.', 'Downgrade attacks force the use of weak protocols.'],
  outcomes: ['Identify various cryptographic attacks.', 'Apply countermeasures like salting and using strong algorithms.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};
"""

def update_html():
    if not os.path.exists(html_path):
        print(f"Error: {html_path} does not exist.")
        # Ensure directory exists for a potential test
        os.makedirs(os.path.dirname(html_path), exist_ok=True)
        # Create a dummy index.html if testing locally
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write("<html><body>\n// ── TAB WIRING ──\n</body></html>")

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = "// ── TAB WIRING ──"
    if marker in content:
        # Check if already injected to avoid double injection
        if "CONTENT['crypto-concepts']" in content:
            print("Content already injected.")
            return

        new_content = content.replace(marker, content_payload + "\n" + marker)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected Module 20 Cryptography content into index.html")
    else:
        print("Marker not found in index.html. Could not inject.")

if __name__ == "__main__":
    update_html()
