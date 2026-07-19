import re

def fix_ui(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix the newlines inside the JS string
    html = html.replace('output = "Starting Nmap 7.94...\nHost is up (0.00013s latency).\nNot shown: 998 closed ports\nPORT    STATE SERVICE\n22/tcp  open  ssh\n80/tcp  open  http\nNmap done: 1 IP address (1 host up) scanned in 0.52 seconds";', 'output = "Starting Nmap 7.94...\\nHost is up (0.00013s latency).\\nNot shown: 998 closed ports\\nPORT    STATE SERVICE\\n22/tcp  open  ssh\\n80/tcp  open  http\\nNmap done: 1 IP address (1 host up) scanned in 0.52 seconds";')
    html = html.replace('output = "Pinging 8.8.8.8 with 32 bytes of data:\nReply from 8.8.8.8: bytes=32 time=14ms TTL=117\nReply from 8.8.8.8: bytes=32 time=15ms TTL=117";', 'output = "Pinging 8.8.8.8 with 32 bytes of data:\\nReply from 8.8.8.8: bytes=32 time=14ms TTL=117\\nReply from 8.8.8.8: bytes=32 time=15ms TTL=117";')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed JS newlines.")

fix_ui('frontend/index.html')
