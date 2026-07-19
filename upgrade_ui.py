import re
import sys

def upgrade_ui(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add CSS for floating terminal and LMS Dashboard
    css_addition = """
/* ── FLOATING TERMINALS ── */
.term-drawer { position:fixed; bottom:0; left:var(--sidebar-w); right:0; height:320px; background:#000; border-top:1px solid var(--border-bright); display:flex; transform:translateY(100%); transition:transform 0.3s cubic-bezier(0.4, 0, 0.2, 1); z-index:1000; box-shadow:0 -10px 40px rgba(0,0,0,0.5); font-family:var(--mono); }
.term-drawer.open { transform:translateY(0); }
@media(max-width:900px){ .term-drawer { left:0; flex-direction:column; height:50vh; } }
.term-panel { flex:1; display:flex; flex-direction:column; border-right:1px solid var(--border); overflow:hidden; }
.term-panel:last-child { border-right:none; }
.term-header { background:rgba(255,255,255,0.05); padding:8px 14px; font-size:0.75rem; color:var(--text-muted); display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); }
.term-body { flex:1; padding:12px; overflow-y:auto; font-size:0.82rem; line-height:1.6; }
.term-body::-webkit-scrollbar { width:4px; }
.term-body::-webkit-scrollbar-thumb { background:rgba(255,255,255,0.2); }
.term-input-line { display:flex; padding:8px 12px; background:rgba(0,0,0,0.5); border-top:1px solid rgba(255,255,255,0.1); }
.term-input { flex:1; background:transparent; border:none; outline:none; color:#fff; font-family:var(--mono); font-size:0.82rem; margin-left:8px; }
.term-win { color:#00BFFF; } /* Windows PowerShell Blue tint */
.term-lin { color:var(--green); } /* Kali Green */
.term-toggle-btn { position:fixed; bottom:20px; right:20px; background:var(--panel); border:1px solid var(--green); border-radius:30px; padding:10px 20px; color:var(--green); font-family:var(--mono); font-size:0.8rem; cursor:pointer; z-index:1001; box-shadow:var(--green-glow); display:flex; align-items:center; gap:8px; transition:all 0.2s; }
.term-toggle-btn:hover { background:var(--green-dim); transform:translateY(-2px); }

/* ── LMS DASHBOARD ── */
.lms-dash { padding:20px; width:100%; max-width:1200px; margin:0 auto; }
.lms-hero { display:flex; justify-content:space-between; align-items:flex-end; background:linear-gradient(135deg, rgba(0,255,136,0.1), rgba(0,0,0,0)); border:1px solid var(--border); border-radius:var(--radius); padding:30px; margin-bottom:30px; }
.lms-hero-left h1 { font-size:2.2rem; color:var(--green); margin-bottom:8px; }
.lms-hero-left p { color:var(--text-dim); font-size:0.95rem; max-width:500px; line-height:1.6; }
.lms-stats { display:flex; gap:30px; }
.lms-stat { text-align:right; }
.lms-stat-val { font-size:1.8rem; font-weight:700; color:#fff; }
.lms-stat-lbl { font-size:0.75rem; color:var(--text-muted); font-family:var(--mono); text-transform:uppercase; }
.lms-modules-grid { display:grid; grid-template-columns:repeat(auto-fill, minmax(300px, 1fr)); gap:20px; }
.lms-mod-card { background:var(--panel); border:1px solid var(--border); border-radius:var(--radius); padding:20px; cursor:pointer; transition:all 0.2s; }
.lms-mod-card:hover { border-color:var(--green); transform:translateY(-3px); box-shadow:var(--green-glow); }
.lms-mod-num { font-family:var(--mono); font-size:0.7rem; color:var(--green); margin-bottom:8px; }
.lms-mod-title { font-size:1.1rem; font-weight:600; margin-bottom:12px; }
.lms-mod-progress { height:4px; background:rgba(255,255,255,0.1); border-radius:2px; overflow:hidden; }
.lms-mod-fill { height:100%; background:var(--green); width:0%; transition:width 0.5s; }

/* ── AI TOOLS SECTION ── */
.tool-grid { display:grid; grid-template-columns:1fr; gap:16px; margin-bottom:24px; }
.tool-card { display:flex; flex-direction:column; background:rgba(0,0,0,0.4); border:1px solid var(--border); border-radius:var(--radius); overflow:hidden; }
.tool-header { background:rgba(0,255,136,0.08); padding:12px 16px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border); }
.tool-name { font-weight:700; color:var(--green); font-size:1.1rem; }
.tool-cmd { font-family:var(--mono); font-size:0.8rem; color:#fff; background:rgba(0,0,0,0.5); padding:4px 8px; border-radius:4px; }
.tool-body { display:grid; grid-template-columns:1fr 1fr; }
@media(max-width:700px){ .tool-body { grid-template-columns:1fr; } }
.tool-col { padding:16px; }
.tool-col.trad { border-right:1px solid rgba(255,255,255,0.05); }
.tool-lbl { font-family:var(--mono); font-size:0.65rem; color:var(--text-muted); margin-bottom:8px; letter-spacing:1px; }
.tool-desc { font-size:0.85rem; color:var(--text-dim); line-height:1.6; }
.clickable-cmd { cursor:pointer; padding:2px 4px; border-radius:4px; transition:background 0.2s; display:inline-block; }
.clickable-cmd:hover { background:rgba(0,255,136,0.15); }
"""
    # Insert CSS before </style>
    html = html.replace('</style>', css_addition + '\n</style>')

    # 2. Add Floating Terminal HTML just before closing #ceh-app
    terminal_html = """
  <!-- FLOATING TERMINALS -->
  <div class="term-drawer" id="term-drawer">
    <div class="term-panel">
      <div class="term-header">
        <span><span style="color:#00BFFF">❖</span> Windows PowerShell</span>
        <span style="cursor:pointer" onclick="document.getElementById('term-body-win').innerHTML=''">🗑️</span>
      </div>
      <div class="term-body term-win" id="term-body-win">
        <div>Windows PowerShell</div><div>Copyright (C) Microsoft Corporation. All rights reserved.</div><br/>
      </div>
      <div class="term-input-line">
        <span style="color:#64748B">PS C:\\Users\\Operator&gt;</span>
        <input class="term-input term-win" id="term-input-win" autocomplete="off" spellcheck="false"/>
      </div>
    </div>
    <div class="term-panel">
      <div class="term-header">
        <span><span style="color:var(--green)">🐧</span> Kali Linux Shell</span>
        <span style="cursor:pointer" onclick="document.getElementById('term-body-lin').innerHTML=''">🗑️</span>
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
"""
    html = html.replace('<!-- TOPBAR -->', terminal_html + '\n  <!-- TOPBAR -->')

    # 3. Replace welcome-screen with LMS Dashboard
    lms_html = """
      <div class="lms-dash" id="welcome-screen">
        <div class="lms-hero">
          <div class="lms-hero-left">
            <h1>SHADOWXLAB CEHv13 AI</h1>
            <p>Welcome to your centralized learning management system. Track your progress, execute hands-on labs, and master both traditional and AI-powered offensive security tools.</p>
          </div>
          <div class="lms-stats">
            <div class="lms-stat"><div class="lms-stat-val" id="dash-xp">0</div><div class="lms-stat-lbl">Total XP</div></div>
            <div class="lms-stat"><div class="lms-stat-val" id="dash-rank">Script Kiddie</div><div class="lms-stat-lbl">Rank</div></div>
          </div>
        </div>
        <div class="lms-modules-grid" id="lms-modules-grid"></div>
      </div>
"""
    # Replace existing welcome screen
    html = re.sub(r'<div class="welcome-screen".*?</div>\s*</div>', lms_html, html, flags=re.DOTALL)

    # 4. Modify buildCommandsHTML
    # Need to remove old terminal and change how tools/cmds are rendered
    new_build_commands = """
function buildCommandsHTML(d){
  const tools=d.tools||[];
  const cmds=d.commands||{win:[],lin:[]};
  
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

  return `
  ${toolsHtml}
  <div class="cmd-grid">
    <div class="cmd-block">
      <div class="cmd-os">▶ WINDOWS COMMANDS (Click to execute)</div>
      ${cmds.win&&cmds.win.length?cmds.win.map(c=>`<div class="cmd-line clickable-cmd" onclick="runCommand('win', '${c.replace(/'/g,"\\'").replace(/"/g,'&quot;')}')">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Windows commands.</div>'}
    </div>
    <div class="cmd-block">
      <div class="cmd-os">▶ LINUX / KALI COMMANDS (Click to execute)</div>
      ${cmds.lin&&cmds.lin.length?cmds.lin.map(c=>`<div class="cmd-line clickable-cmd" onclick="runCommand('lin', '${c.replace(/'/g,"\\'").replace(/"/g,'&quot;')}')">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Linux commands.</div>'}
    </div>
  </div>`;
}
"""
    # Replace the old buildCommandsHTML
    html = re.sub(r'function buildCommandsHTML\(d\)\{.*?(?=\n// -- TAB 5)', new_build_commands.strip(), html, flags=re.DOTALL)

    # 5. Modify buildLabHTML to make commands clickable
    # In `d.lab.steps.map`, we can replace inline code `...` with clickable spans, or just add a generic "run" button.
    # Currently steps are just text. We'll use regex to make anything looking like a command clickable if it's wrapped in backticks or quotes, or we'll just add a "Send to Terminal" icon.
    # A simpler way is to let the user type, but we can do a quick replace for backticks.
    new_build_lab = """
// -- TAB 6: LAB --
function buildLabHTML(d){
  if(!d.lab) return buildComingSoonHTML('🔬','Hands-On Lab is being designed');
  const dc={'Beginner':'var(--green)','Intermediate':'var(--blue)','Advanced':'var(--red)'};
  const color=dc[d.lab.difficulty]||'var(--text-dim)';
  
  const stepsHtml = d.lab.steps.map((s,i)=>{
    // Make text in backticks clickable to terminal
    let formattedText = s.replace(/`([^`]+)`/g, '<span class="clickable-cmd" style="color:var(--blue);background:rgba(0,170,255,0.1);padding:2px 6px;border-radius:4px;font-family:var(--mono);" onclick="runCommand(\\\'lin\\\', \\\'$1\\\')">$1</span>');
    return `<div class="lab-step" style="cursor:pointer;" onclick="toggleLabStep(this)"><div class="lab-step-num">${i+1}</div><div class="lab-step-text">${formattedText}</div><span class="lab-check" style="opacity:0;">✓</span></div>`;
  }).join('');

  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;flex-wrap:wrap;gap:10px;">
      <div>
        <div style="font-size:1.1rem;font-weight:700;color:var(--green);">🔬 ${d.lab.title}</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;align-items:flex-end;">
        <span style="font-family:var(--mono);font-size:0.7rem;background:rgba(0,0,0,0.4);border:1px solid var(--border);padding:4px 10px;border-radius:20px;color:${color};">${d.lab.difficulty||'Beginner'}</span>
      </div>
    </div>
    ${stepsHtml}
  </div>`;
}
"""
    html = re.sub(r'// -- TAB 6: LAB --.*?function buildLabHTML\(d\)\{.*?(?=\n// -- TAB 7)', new_build_lab.strip(), html, flags=re.DOTALL)

    # Remove the old terminal from buildTopicHTML
    html = re.sub(r'<div class="terminal-wrap" style="margin-top:20px;">.*?</div>\s*</div>\s*</div>\s*<!-- PITFALLS -->', '</div>\n\n  <!-- PITFALLS -->', html, flags=re.DOTALL)

    # 6. Replace initTerminal with new terminal logic
    new_terminal_logic = """
// ── FLOATING TERMINALS ──
let termOpen = false;
function toggleTerminal(){
  termOpen = !termOpen;
  const drawer = document.getElementById('term-drawer');
  const btn = document.getElementById('term-toggle-btn');
  if(termOpen){
    drawer.classList.add('open');
    btn.innerHTML = '🔽 <span>Close Terminals</span>';
  } else {
    drawer.classList.remove('open');
    btn.innerHTML = '⌨️ <span>Open Terminals</span>';
  }
}

function runCommand(os, cmd){
  if(!termOpen) toggleTerminal();
  const inputId = os === 'win' ? 'term-input-win' : 'term-input-lin';
  const input = document.getElementById(inputId);
  if(input){
    input.value = cmd;
    // trigger enter key event
    input.dispatchEvent(new KeyboardEvent('keydown', {key: 'Enter'}));
  }
}

function initFloatingTerminals(){
  const winInput = document.getElementById('term-input-win');
  const linInput = document.getElementById('term-input-lin');
  
  if(winInput) winInput.addEventListener('keydown', e => handleTerminalInput(e, 'win', winInput));
  if(linInput) linInput.addEventListener('keydown', e => handleTerminalInput(e, 'lin', linInput));
}

function handleTerminalInput(e, os, inputEl){
  if(e.key === 'Enter'){
    const cmd = inputEl.value.trim();
    inputEl.value = '';
    if(!cmd) return;
    
    const bodyId = os === 'win' ? 'term-body-win' : 'term-body-lin';
    const body = document.getElementById(bodyId);
    if(!body) return;
    
    const prompt = os === 'win' ? 'PS C:\\\\Users\\\\Operator> ' : 'root@shadowxlab:~# ';
    const cls = os === 'win' ? 'term-win' : 'term-lin';
    
    body.innerHTML += `<div><span style="color:#64748B">${prompt}</span><span style="color:#fff">${escapeHtml(cmd)}</span></div>`;
    
    // Mock Execution
    setTimeout(() => {
      let output = "Command executed successfully in mock environment.";
      if(cmd.toLowerCase() === 'clear' || cmd.toLowerCase() === 'cls'){
        body.innerHTML = ''; return;
      } else if(TERMINAL_CMDS[cmd.toLowerCase()]){
        output = TERMINAL_CMDS[cmd.toLowerCase()];
      } else if(cmd.includes('nmap')) {
        output = "Starting Nmap 7.94...\\nHost is up (0.00013s latency).\\nNot shown: 998 closed ports\\nPORT    STATE SERVICE\\n22/tcp  open  ssh\\n80/tcp  open  http\\nNmap done: 1 IP address (1 host up) scanned in 0.52 seconds";
      } else if(cmd.includes('ping')) {
        output = "Pinging 8.8.8.8 with 32 bytes of data:\\nReply from 8.8.8.8: bytes=32 time=14ms TTL=117\\nReply from 8.8.8.8: bytes=32 time=15ms TTL=117";
      }
      
      output.split('\\n').forEach(line => {
        body.innerHTML += `<div class="${cls}">${escapeHtml(line)}</div>`;
      });
      body.scrollTop = body.scrollHeight;
    }, 300);
  }
}
"""
    # Replace the old initTerminal and appendTermLine
    html = re.sub(r'function initTerminal\(topicId\)\{.*?(?=\n// ── CTF ──)', new_terminal_logic.strip() + '\n', html, flags=re.DOTALL)

    # Change initTerminal call in buildTopicHTML to initFloatingTerminals
    html = html.replace('initTerminal(id);', 'initFloatingTerminals();')

    # Add LMS Modules Grid rendering to bootApp/checkAuth
    lms_render = """
function renderLMSDashboard(){
  const grid = document.getElementById('lms-modules-grid');
  if(!grid) return;
  
  let html = '';
  MODULES.forEach((m, i) => {
    let completedCount = 0;
    m.topics.forEach(t => { if(completed[t.id]) completedCount++; });
    const pct = Math.round((completedCount / m.topics.length) * 100);
    
    html += `
      <div class="lms-mod-card" onclick="toggleModule('${m.id}', document.getElementById('mod-hdr-${m.id}'))">
        <div class="lms-mod-num">MODULE ${String(i+1).padStart(2,'0')}</div>
        <div class="lms-mod-title">${m.name}</div>
        <div style="display:flex;justify-content:space-between;font-size:0.75rem;color:var(--text-muted);margin-bottom:6px;font-family:var(--mono);">
          <span>${completedCount} / ${m.topics.length} Topics</span>
          <span>${pct}%</span>
        </div>
        <div class="lms-mod-progress"><div class="lms-mod-fill" style="width:${pct}%"></div></div>
      </div>
    `;
  });
  grid.innerHTML = html;
  
  document.getElementById('dash-xp').textContent = xp;
  document.getElementById('dash-rank').textContent = getRank(xp).name;
}
"""
    # Inject it before bootApp
    html = html.replace('function bootApp(email){', lms_render + '\nfunction bootApp(email){')
    
    # Call renderLMSDashboard inside updateProgress (so it stays synced)
    html = html.replace('document.getElementById(\'topics-total\').textContent=total;', 'document.getElementById(\'topics-total\').textContent=total;\n  if(typeof renderLMSDashboard === "function") renderLMSDashboard();')


    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("UI successfully upgraded to Dual Terminal + AI Tools + LMS Dashboard.")

upgrade_ui('frontend/index.html')
