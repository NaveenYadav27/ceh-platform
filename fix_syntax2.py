import re

def fix_terminal(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        html = f.read()

    # The corrupted block starts with window.escapeHtml and ends at the end of handleTerminalInput
    pattern = r'window\.escapeHtml = function.*?function handleTerminalInput\(e, os, inputEl\).*?\n\}'
    
    # We want to replace it with the clean version
    replacement = r"""window.escapeHtml = function(unsafe) {
  return (unsafe || '').replace(/&/g, "&amp;")
       .replace(/</g, "&lt;")
       .replace(/>/g, "&gt;")
       .replace(/"/g, "&quot;")
       .replace(/'/g, "&#039;");
};

function appendTerminal(os, cmd, output) {
  const bodyId = os === 'win' ? 'term-body-win' : 'term-body-lin';
  const body = document.getElementById(bodyId);
  if(!body) return;
  const cls = os === 'win' ? 'term-win' : 'term-lin';
  
  if(output === null) {
    const prompt = os === 'win' ? 'PS C:\\Users\\Operator> ' : 'root@shadowxlab:~# ';
    body.innerHTML += `<div><span style="color:#64748B">${prompt}</span><span style="color:#fff">${window.escapeHtml(cmd)}</span></div>`;
  } else {
    if(cmd.toLowerCase() === 'clear' || cmd.toLowerCase() === 'cls'){
      body.innerHTML = ''; 
      return;
    }
    output.split('\n').forEach(line => {
      body.innerHTML += `<div class="${cls}">${window.escapeHtml(line)}</div>`;
    });
    body.scrollTop = body.scrollHeight;
  }
}

function handleTerminalInput(e, os, inputEl){
  if(e.key === 'Enter'){
    const cmd = inputEl.value.trim();
    inputEl.value = '';
    if(!cmd) return;
    
    appendTerminal(os, cmd, null);
    
    setTimeout(() => {
      let output = "[+] Command executed successfully in mock environment.";
      const lowerCmd = cmd.toLowerCase();
      
      if(lowerCmd === 'clear' || lowerCmd === 'cls'){
        output = ""; 
      } else if(typeof TERMINAL_CMDS !== 'undefined' && TERMINAL_CMDS[lowerCmd]){
        output = TERMINAL_CMDS[lowerCmd];
      } else if(cmd.includes('nmap -sV') || cmd.includes('nmap')) {
        output = "Starting Nmap 7.94...\nHost is up (0.00013s latency).\nNot shown: 998 closed ports\nPORT    STATE SERVICE VERSION\n22/tcp  open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1\n80/tcp  open  http    nginx 1.18.0\nNmap done: 1 IP address (1 host up) scanned in 0.52 seconds";
      } else if(cmd.includes('ping')) {
        output = "Pinging 8.8.8.8 with 32 bytes of data:\nReply from 8.8.8.8: bytes=32 time=14ms TTL=117\nReply from 8.8.8.8: bytes=32 time=15ms TTL=117";
      } else if(lowerCmd.includes('systeminfo')) {
        output = "Host Name: GFS-WKSTN-01\nOS Name: Microsoft Windows 10 Enterprise\nOS Version: 10.0.19044 N/A Build 19044";
      } else if(lowerCmd.includes('ipconfig')) {
        output = "Windows IP Configuration\n\nEthernet adapter Ethernet0:\n   Connection-specific DNS Suffix  . : localdomain\n   IPv4 Address. . . . . . . . . . . : 192.168.1.105\n   Subnet Mask . . . . . . . . . . . : 255.255.255.0\n   Default Gateway . . . . . . . . . : 192.168.1.1";
      } else if(lowerCmd.includes('whoami')) {
        output = os === 'win' ? "gfs-domain\\operator" : "root (authenticated CEH operator)";
      } else if(lowerCmd.includes('net user')) {
        output = "User accounts for \\\\GFS-WKSTN-01\n-------------------------------------------------------------------------------\nAdministrator            Guest                    jdoe\nThe command completed successfully.";
      }
      
      if(output !== "") appendTerminal(os, lowerCmd === 'clear' ? 'clear' : cmd, output);
    }, 300);
  }
}"""
    
    # We replace using string replacement to avoid any regex escape processing
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        print(f"Failed to find corrupted block in {file_path}")
        return
        
    old_block = match.group(0)
    
    # We write the raw replacement string so newlines and backslashes are preserved
    # but wait, the replacement string is a python raw string (r"") so \n is a backslash and n!
    # Wait, in JS I actually WANT the backslash and n in output.split('\n')!
    # And I want literal newlines for the code structure!
    # A python raw string r"""...""" leaves \n as backslash n. But it also leaves actual newlines as actual newlines.
    
    new_html = html.replace(old_block, replacement)
    
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(new_html)
    print(f"Patched {file_path}")

fix_terminal('frontend/index.html')
fix_terminal('frontend/index.min.html')
