import re

def apply_hotfix_2(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        html = f.read()

    # 1. Update toggleTerminal
    # We want to hide the button when terminal is open.
    old_toggle = r"function toggleTerminal\(\)\{\s*termOpen = !termOpen;\s*const drawer = document\.getElementById\('term-drawer'\);\s*const btn = document\.getElementById\('term-toggle-btn'\);\s*if\(termOpen\)\{\s*drawer\.classList\.add\('open'\);\s*btn\.innerHTML = '[^']+';\s*\} else \{\s*drawer\.classList\.remove\('open'\);\s*btn\.innerHTML = '[^']+';\s*\}\s*\}"
    
    new_toggle = """function toggleTerminal(){
  termOpen = !termOpen;
  const drawer = document.getElementById('term-drawer');
  const btn = document.getElementById('term-toggle-btn');
  if(termOpen){
    drawer.classList.add('open');
    if(btn) btn.style.display = 'none';
  } else {
    drawer.classList.remove('open');
    if(btn) {
      btn.style.display = 'flex';
      btn.innerHTML = '⌨️ <span>Open Terminals</span>';
    }
  }
}"""
    html = re.sub(old_toggle, lambda m: new_toggle, html, flags=re.DOTALL)
    
    # 2. Update buildCommandsHTML
    # We will search for function buildCommandsHTML(d){ ... return `...`; }
    old_build_cmds = r'function buildCommandsHTML\(d\)\{.*?return `.*?`;\s*\}'
    
    new_build_cmds = r"""function buildCommandsHTML(d){
  const tools = d.tools || [];
  const cmds = d.commands || { win: [], lin: [] };
  
  let toolsHtml = '';
  if(tools.length){
    toolsHtml = `<div style="margin-bottom:24px;"><div class="card-label" style="margin-bottom:12px;">KEY TOOLS</div><div class="tool-grid">` + 
      tools.map(t => {
        const aiDesc = t.desc.includes('AI') ? t.desc : `AI models can automate ${t.name} by parsing its raw output, correlating vulnerabilities with external threat feeds, and autonomously verifying exploit paths.`;
        return `
        <div class="tool-card">
          <div class="tool-header">
            <div class="tool-name">${t.name}</div>
            <div class="tool-cmd" onclick="runCommand('lin', '${t.cmd}')" style="cursor:pointer" title="Click to run in Linux Terminal">$ ${t.cmd}</div>
          </div>
          <div class="tool-body">
            <div class="tool-col trad">
              <div class="tool-lbl">TRADITIONAL USAGE</div>
              <div class="tool-desc">${t.desc}</div>
            </div>
            <div class="tool-col">
              <div class="tool-lbl" style="color:var(--purple)">✨ AI-POWERED EVOLUTION</div>
              <div class="tool-desc">${aiDesc}</div>
            </div>
          </div>
        </div>`;
      }).join('') + `</div></div>`;
  }

  // Generate Dual-pane enterprise command cards
  // We pair linux and windows commands by index
  let maxLen = Math.max(cmds.lin ? cmds.lin.length : 0, cmds.win ? cmds.win.length : 0);
  let cardsHtml = '';
  
  if (maxLen === 0) {
    cardsHtml = `<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No commands for this topic.</div>`;
  } else {
    for(let i = 0; i < maxLen; i++){
      let linCmdObj = (cmds.lin && cmds.lin[i]) || null;
      let winCmdObj = (cmds.win && cmds.win[i]) || null;
      
      const renderCard = (cmdObj, os) => {
        if (!cmdObj) return `<div class="ent-card" style="opacity:0.3; display:flex; align-items:center; justify-content:center; font-family:var(--mono); font-size:0.8rem; color:var(--text-muted)">N/A</div>`;
        
        let c = typeof cmdObj === 'string' ? { command: cmdObj } : cmdObj;
        let cname = c.command || c.cmd || '';
        let cclean = cname.replace(/'/g,"\\'").replace(/"/g,'&quot;');
        let purpose = c.purpose || 'Execute command in standard terminal.';
        let expected = c.expected || 'Command standard output.';
        let mitre = c.mitre || (os==='win'?'T1059.001':'T1059.004');
        let note = c.analystNote ? `<div style="background:rgba(255,183,77,0.1); border-left:3px solid var(--orange); padding:10px; margin-top:12px; font-size:0.8rem; color:var(--text-muted);"><strong style="color:var(--orange);">💡 Analyst Note:</strong><br/>${c.analystNote}</div>` : '';
        
        return `
          <div class="ent-card" style="display:flex; flex-direction:column; gap:8px;">
            <div style="display:flex; justify-content:space-between; align-items:flex-start;">
              <div style="font-family:var(--mono); font-size:0.95rem; font-weight:bold; color:${os==='win'?'#00BFFF':'var(--green)'}; background:rgba(0,0,0,0.4); padding:6px 12px; border-radius:4px; border:1px solid rgba(255,255,255,0.1); display:inline-block;">${cname}</div>
              <div style="font-family:var(--mono); font-size:0.65rem; color:var(--text-muted); border:1px solid var(--border); padding:2px 6px; border-radius:4px;">MITRE: ${mitre}</div>
            </div>
            
            <div style="font-size:0.85rem; color:var(--text); margin-top:8px;">
              <strong style="color:#fff;">Purpose:</strong> ${purpose}
            </div>
            <div style="font-size:0.85rem; color:var(--text); margin-bottom:8px;">
              <strong style="color:#fff;">Expected Output:</strong> ${expected}
            </div>
            
            ${note}
            
            <div style="display:flex; gap:10px; margin-top:auto; padding-top:12px;">
              <button onclick="runCommand('${os}', '${cclean}')" style="background:var(--green); color:#000; border:none; padding:6px 16px; border-radius:4px; font-weight:bold; cursor:pointer; font-size:0.75rem;">▶ Run</button>
              <button onclick="navigator.clipboard.writeText('${cclean}'); alert('Copied to clipboard')" style="background:rgba(255,255,255,0.1); color:#fff; border:1px solid var(--border); padding:6px 16px; border-radius:4px; cursor:pointer; font-size:0.75rem;">📋 Copy</button>
              <button onclick="alert('Explanation for: ${cclean}\\n\\nPurpose: ${purpose.replace(/'/g,"\\'").replace(/"/g,'&quot;')}')" style="background:rgba(255,255,255,0.1); color:#fff; border:1px solid var(--border); padding:6px 16px; border-radius:4px; cursor:pointer; font-size:0.75rem;">ℹ Explain</button>
            </div>
          </div>
        `;
      };

      cardsHtml += `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
          ${renderCard(winCmdObj, 'win')}
          ${renderCard(linCmdObj, 'lin')}
        </div>
      `;
    }
  }

  return `
  ${toolsHtml}
  <div style="margin-bottom:24px;">
    <div class="card-label" style="margin-bottom:12px;">ENTERPRISE TERMINAL COMMANDS</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:12px;">
      <div class="cmd-os" style="margin:0; padding:10px; text-align:center; background:rgba(0,191,255,0.1); border:1px solid rgba(0,191,255,0.3); color:#00BFFF;">❖ WINDOWS EQUIVALENT</div>
      <div class="cmd-os" style="margin:0; padding:10px; text-align:center; background:rgba(0,255,136,0.1); border:1px solid rgba(0,255,136,0.3); color:var(--green);">🐧 KALI LINUX</div>
    </div>
    ${cardsHtml}
  </div>`;
}"""
    html = re.sub(old_build_cmds, lambda m: new_build_cmds, html, flags=re.DOTALL)
    
    # 3. Update the term-drawer HTML headers
    old_drawer = r'<div class="term-drawer" id="term-drawer">.*?<!-- FLOATING TERMINALS END -->'
    new_drawer = r"""<div class="term-drawer" id="term-drawer">
    <div class="term-panel">
      <div class="term-header" style="flex-direction:column; align-items:stretch;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span><span style="color:#00BFFF">❖</span> <strong>Windows Operator</strong></span>
          <span style="cursor:pointer; color:var(--text-muted); font-size:1.1rem; padding:0 4px;" onclick="toggleTerminal()" title="Minimize Terminal">✕</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px; font-size:0.75rem; font-family:var(--mono); color:var(--text-dim); margin-bottom:12px;">
          <div>Host: WIN-CLIENT01</div><div>Windows 11</div>
          <div>User: Analyst</div><div>PowerShell 7.5</div>
          <div>Privilege: Standard User</div><div>Session: Interactive</div>
        </div>
        <div style="display:flex; justify-content:flex-start; gap:16px; font-size:0.75rem; border-top:1px solid rgba(255,255,255,0.05); padding-top:8px;">
          <span style="cursor:pointer; color:var(--text-muted); transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--text-muted)'" onclick="document.getElementById('term-body-win').innerHTML=''">🗑 Clear</span>
          <span style="cursor:pointer; color:var(--text-muted); transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--text-muted)'" onclick="alert('History exporting not available in mock environment.')">📜 History</span>
          <span style="cursor:pointer; color:var(--text-muted); transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--text-muted)'" onclick="alert('Export not available in mock environment.')">⬇ Export</span>
        </div>
      </div>
      <div class="term-body term-win" id="term-body-win">
        <div>Windows PowerShell</div><div>Copyright (C) Microsoft Corporation. All rights reserved.</div><br/>
      </div>
      <div class="term-input-line">
        <span style="color:#64748B">PS C:\Users\Operator&gt;</span>
        <input class="term-input term-win" id="term-input-win" autocomplete="off" spellcheck="false"/>
      </div>
    </div>
    
    <div class="term-panel">
      <div class="term-header" style="flex-direction:column; align-items:stretch;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span><span style="color:var(--green)">🐧</span> <strong>Kali Security Analyst</strong></span>
          <span style="cursor:pointer; color:var(--text-muted); font-size:1.1rem; padding:0 4px;" onclick="toggleTerminal()" title="Minimize Terminal">✕</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px; font-size:0.75rem; font-family:var(--mono); color:var(--text-dim); margin-bottom:12px;">
          <div>Host: KALI-SOC01</div><div>Kali Linux</div>
          <div>User: root</div><div>Bash</div>
          <div>Privilege: root</div><div>Network: Lab VLAN</div>
        </div>
        <div style="display:flex; justify-content:flex-start; gap:16px; font-size:0.75rem; border-top:1px solid rgba(255,255,255,0.05); padding-top:8px;">
          <span style="cursor:pointer; color:var(--text-muted); transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--text-muted)'" onclick="document.getElementById('term-body-lin').innerHTML=''">🗑 Clear</span>
          <span style="cursor:pointer; color:var(--text-muted); transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--text-muted)'" onclick="alert('History exporting not available in mock environment.')">📜 History</span>
          <span style="cursor:pointer; color:var(--text-muted); transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--text-muted)'" onclick="alert('Export not available in mock environment.')">⬇ Export</span>
        </div>
      </div>
      <div class="term-body term-lin" id="term-body-lin">
        <div>Linux shadowxlab 6.1.0-kali-amd64</div><div>Welcome to the ShadowXLab Offensive Security Shell.</div><br/>
      </div>
      <div class="term-input-line">
        <span style="color:#64748B">root@shadowxlab:~#</span>
        <input class="term-input term-lin" id="term-input-lin" autocomplete="off" spellcheck="false"/>
      </div>
    </div>
  </div>
  <button class="term-toggle-btn" id="term-toggle-btn" onclick="toggleTerminal()">
    ⌨️ <span>Open Terminals</span>
  </button>
  
  <!-- FLOATING TERMINALS END -->"""
  
    # Just grab everything before <!-- FLOATING TERMINALS END --> to ensure we don't accidentally swallow the topbar
    # Actually my regex above is correct but might be greedy if there are multiple.
    
    # Wait, the end of the term drawer might just be `</button>` if I don't have the comment. Let's just do a simpler search.
    old_drawer2 = r'<div class="term-drawer" id="term-drawer">.*?<button class="term-toggle-btn"[^>]*>.*?</button>'
    
    html = re.sub(old_drawer2, lambda m: new_drawer.replace('<!-- FLOATING TERMINALS END -->', ''), html, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf8') as f:
        f.write(html)
    print(f"Patched {file_path}")

apply_hotfix_2('frontend/index.html')
apply_hotfix_2('frontend/index.min.html')
