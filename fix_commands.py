import re

def clean_build_commands(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        html = f.read()

    # The previous script broke the file by leaving orphaned code from the old buildCommandsHTML
    # Let's cleanly replace from function buildCommandsHTML(d){ to // -- TAB 5: PITFALLS --
    
    # First, let's just find where it starts and ends
    pattern = r'function buildCommandsHTML\(d\)\{.*?// -- TAB 5: PITFALLS --'
    
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
}
// -- TAB 5: PITFALLS --"""

    # We use lambda to avoid regex escape sequence issues
    html = re.sub(pattern, lambda m: new_build_cmds, html, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(html)
    print(f"Cleaned and patched {file_path}")

clean_build_commands('frontend/index.html')
clean_build_commands('frontend/index.min.html')
