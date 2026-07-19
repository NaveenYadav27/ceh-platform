"""
CEH Platform Skeleton Rebuild Script - Clean Version
Run with: python rebuild_skeleton.py
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)
ok = []
fail = []

def mark(step, success):
    if success: ok.append(step)
    else: fail.append(step)

# =============================================================
# 1. NEW CSS - inject before </style>
# =============================================================
NEW_CSS = r"""
/* ── Diagram ── */
.diagram-flow{display:flex;flex-direction:column;gap:0;}
.diagram-step{display:flex;gap:16px;align-items:flex-start;padding:16px;background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:var(--radius);margin-bottom:4px;}
.diagram-step-icon{font-size:1.8rem;min-width:40px;text-align:center;}
.diagram-step-body{flex:1;}
.diagram-step-label{font-weight:700;color:var(--blue);font-size:0.9rem;margin-bottom:4px;}
.diagram-step-desc{font-size:0.84rem;color:var(--text-muted);}
.diagram-arrow{text-align:center;color:var(--green);font-size:1.2rem;padding:4px 0;}
/* ── Enterprise ── */
.enterprise-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
@media(max-width:640px){.enterprise-grid{grid-template-columns:1fr;}}
.ent-card{background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:var(--radius);padding:18px;}
.ent-label{font-family:var(--mono);font-size:0.7rem;color:var(--green);letter-spacing:0.1em;margin-bottom:8px;}
.ent-text{font-size:0.87rem;color:var(--text);line-height:1.6;}
.ent-situation{border-color:rgba(100,181,246,0.3);}
.ent-challenge{border-color:rgba(255,183,77,0.3);}
/* ── Lab ── */
.lab-check{margin-left:auto;font-size:1.1rem;color:var(--green);transition:opacity 0.2s;min-width:20px;text-align:center;}
/* ── Complete Button ── */
.btn-complete{background:linear-gradient(135deg,var(--green),#00b8a9);color:#000;font-family:var(--mono);font-size:0.75rem;font-weight:700;letter-spacing:0.08em;border:none;border-radius:var(--radius);padding:12px 24px;cursor:pointer;transition:all 0.2s;}
.btn-complete:hover{transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,255,136,0.3);}
"""

count_before = html.count('</style>')
html = html.replace('</style>', NEW_CSS + '</style>', 1)
mark('CSS', html.count('</style>') == count_before)

# =============================================================
# 2. REPLACE TAB BUTTONS
# =============================================================
OLD_TABS = ('  <div class="topic-tabs">\r\n'
            '    <button class="tab-btn active" data-tab="mission">\U0001f4cb MISSION</button>\r\n'
            '    <button class="tab-btn" data-tab="terminal">\U0001f4bb TERMINAL</button>\r\n'
            '    <button class="tab-btn" data-tab="ctf">\U0001f6a9 CTF</button>\r\n'
            '    <button class="tab-btn" data-tab="quiz">\u2753 QUIZ</button>\r\n'
            '    <button class="tab-btn" data-tab="flashcards">\U0001f0cf FLASHCARDS</button>\r\n'
            '    <button class="tab-btn" data-tab="lab">\U0001f52c LAB</button>\r\n'
            '  </div>')

NEW_TABS = ('  <div class="topic-tabs">\r\n'
            '    <button class="tab-btn active" data-tab="learn">\U0001f4da Learn</button>\r\n'
            '    <button class="tab-btn" data-tab="diagram">\U0001f504 Diagram &amp; Workflow</button>\r\n'
            '    <button class="tab-btn" data-tab="enterprise">\U0001f3e2 Enterprise (GFS)</button>\r\n'
            '    <button class="tab-btn" data-tab="commands">\U0001f4bb Commands</button>\r\n'
            '    <button class="tab-btn" data-tab="pitfalls">\u26a0\ufe0f Pitfalls &amp; Security</button>\r\n'
            '    <button class="tab-btn" data-tab="lab">\U0001f52c Hands-On Lab</button>\r\n'
            '    <button class="tab-btn" data-tab="assessment">\U0001f3af Assessment</button>\r\n'
            '    <button class="tab-btn" data-tab="summary">\U0001f4cb Summary</button>\r\n'
            '  </div>')

if OLD_TABS in html:
    html = html.replace(OLD_TABS, NEW_TABS, 1)
    mark('Tab buttons', True)
else:
    # Try without \r
    OLD_TABS2 = OLD_TABS.replace('\r\n', '\n')
    if OLD_TABS2 in html:
        html = html.replace(OLD_TABS2, NEW_TABS.replace('\r\n', '\n'), 1)
        mark('Tab buttons (LF)', True)
    else:
        mark('Tab buttons', False)

# =============================================================
# 3. REPLACE TAB PANES - find the section in buildTopicHTML
# =============================================================
PANES_START_MARKER = '  <!-- MISSION -->'
PANES_END_MARKER = "  `;\n}"

ps = html.find(PANES_START_MARKER)
if ps == -1:
    PANES_START_MARKER = '  <!-- MISSION -->\r\n'
    ps = html.find(PANES_START_MARKER)

if ps == -1:
    mark('Tab panes', False)
else:
    pe = html.find(PANES_END_MARKER, ps)
    if pe == -1:
        mark('Tab panes (end not found)', False)
    else:
        pe += len(PANES_END_MARKER)
        NEW_PANES = """  <!-- LEARN -->
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
    <div class="terminal-wrap" style="margin-top:20px;">
      <div class="terminal-titlebar">
        <div class="t-dot red"></div><div class="t-dot yellow"></div><div class="t-dot green"></div>
        <span class="terminal-title">root@shadowxlab \u2014 ${d.title||''} shell</span>
      </div>
      <div class="terminal-output" id="term-output">
        <div class="t-line"><span class="t-success">ShadowXLab CEH v13 \u2014 Operator Shell</span></div>
        <div class="t-line"><span class="t-out">Commands for this topic are listed above. Type 'help' for all commands.</span></div>
        <div class="t-line">&nbsp;</div>
      </div>
      <div class="terminal-input-row">
        <span class="t-prompt-prefix">root@shadowxlab:~# </span>
        <input class="terminal-input" id="term-input" autocomplete="off" spellcheck="false" placeholder=""/>
      </div>
    </div>
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
}"""
        html = html[:ps] + NEW_PANES + html[pe:]
        mark('Tab panes', True)

# =============================================================
# 4. REPLACE ALL BUILDER FUNCTIONS
# =============================================================
BS_MARKER = 'function buildClassifiedHTML(d){'
BE_MARKER = '// \u2500\u2500 TAB WIRING \u2500\u2500'

bs = html.find(BS_MARKER)
be = html.find(BE_MARKER, bs if bs != -1 else 0)

if bs == -1 or be == -1:
    mark('Builder functions', False)
else:
    NEW_BUILDERS = """// -- COMING SOON PLACEHOLDER --
function buildComingSoonHTML(icon,message){
  return `<div class="classified-card"><div class="classified-icon">${icon}</div><div class="classified-title">${message}</div><div class="classified-bar"></div><div class="classified-sub">ShadowXLab analysts are preparing this content. Check back soon.</div></div>`;
}

// -- TAB 1: LEARN --
function buildLearnHTML(d){
  if(!d.learn||!d.learn.simple) return buildComingSoonHTML('\\u{1F4DA}','Learn content is being prepared');
  return `
  <div class="mission-grid">
    <div class="info-card"><div class="card-label">SIMPLE EXPLANATION</div><div class="card-text">${d.learn.simple}</div></div>
    <div class="info-card"><div class="card-label">ANALOGY</div><div class="card-text">${d.learn.analogy}</div></div>
    <div class="info-card"><div class="card-label">WHY IT EXISTS</div><div class="card-text">${d.learn.why}</div></div>
    <div class="info-card"><div class="card-label">HOW IT WORKS</div><div class="card-text">${d.learn.architecture}</div></div>
  </div>`;
}

// -- TAB 2: DIAGRAM --
function buildDiagramHTML(d){
  if(!d.diagram||!d.diagram.steps||!d.diagram.steps.length) return buildComingSoonHTML('\\u{1F504}','Diagram & Workflow is being designed');
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="font-size:1rem;font-weight:700;color:var(--blue);margin-bottom:24px;font-family:var(--mono);">${d.diagram.title||'Process Flow'}</div>
    <div class="diagram-flow">
      ${d.diagram.steps.map((s,i)=>`
        <div class="diagram-step">
          <div class="diagram-step-icon">${s.icon||'\u25B6'}</div>
          <div class="diagram-step-body">
            <div class="diagram-step-label">Step ${i+1}: ${s.label}</div>
            <div class="diagram-step-desc">${s.desc}</div>
          </div>
        </div>
        ${i<d.diagram.steps.length-1?'<div class="diagram-arrow">\u2193</div>':''}
      `).join('')}
    </div>
  </div>`;
}

// -- TAB 3: ENTERPRISE --
function buildEnterpriseHTML(d){
  if(!d.enterprise) return buildComingSoonHTML('\\u{1F3E2}','Enterprise scenario is being written');
  const e=d.enterprise;
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:24px;">
      <div style="font-size:2.2rem;">\\u{1F3E2}</div>
      <div>
        <div style="font-size:0.7rem;font-family:var(--mono);color:var(--green);letter-spacing:0.12em;">ENTERPRISE SCENARIO \u2014 GLOBALFINSEC CORP</div>
        <div style="font-size:1rem;font-weight:700;color:var(--text);">${e.role||'Lead Penetration Tester'}</div>
      </div>
    </div>
    <div class="enterprise-grid">
      <div class="ent-card ent-situation"><div class="ent-label">\\u{1F4CB} SITUATION</div><div class="ent-text">${e.situation||''}</div></div>
      <div class="ent-card ent-challenge"><div class="ent-label">\\u{1F3AF} YOUR CHALLENGE</div><div class="ent-text">${e.challenge||''}</div></div>
    </div>
    ${e.steps&&e.steps.length?`<div style="margin-top:20px;">
      <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:12px;">// YOUR INVESTIGATION STEPS</div>
      ${e.steps.map((s,i)=>`<div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:10px;padding:12px;background:rgba(0,0,0,0.3);border-radius:8px;border-left:3px solid var(--green);"><span style="font-family:var(--mono);color:var(--green);font-size:0.75rem;min-width:20px;">${i+1}.</span><span style="font-size:0.88rem;color:var(--text);">${s}</span></div>`).join('')}
    </div>`:''}
    <div class="ent-card" style="margin-top:20px;background:rgba(0,200,83,0.08);border-color:rgba(0,200,83,0.3);">
      <div class="ent-label">\\u2705 OUTCOME &amp; LESSON</div>
      <div class="ent-text"><strong>Outcome:</strong> ${e.outcome||''}</div>
      <div class="ent-text" style="margin-top:8px;"><strong>Key Lesson:</strong> ${e.lesson||''}</div>
    </div>
  </div>`;
}

// -- TAB 4: COMMANDS --
function buildCommandsHTML(d){
  const tools=d.tools||[];
  const cmds=d.commands||{win:[],lin:[]};
  return `
  ${tools.length?`<div style="margin-bottom:20px;"><div class="card-label" style="margin-bottom:12px;">KEY TOOLS</div><div style="display:flex;gap:10px;flex-wrap:wrap;">${tools.map(t=>`<div style="background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:var(--radius);padding:12px 16px;min-width:180px;"><div style="font-weight:600;color:var(--blue);margin-bottom:4px;">${t.name}</div><div style="font-family:var(--mono);font-size:0.75rem;color:var(--green);margin-bottom:4px;">$ ${t.cmd}</div><div style="font-size:0.78rem;color:var(--text-muted);">${t.desc}</div></div>`).join('')}</div></div>`:''}
  <div class="cmd-grid">
    <div class="cmd-block">
      <div class="cmd-os">\\u25B6 WINDOWS</div>
      ${cmds.win&&cmds.win.length?cmds.win.map(c=>`<div class="cmd-line">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Windows commands for this topic.</div>'}
    </div>
    <div class="cmd-block">
      <div class="cmd-os">\\u25B6 LINUX / KALI</div>
      ${cmds.lin&&cmds.lin.length?cmds.lin.map(c=>`<div class="cmd-line">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Linux commands for this topic.</div>'}
    </div>
  </div>`;
}

// -- TAB 5: PITFALLS --
function buildPitfallsHTML(d){
  if(!d.pitfalls||!d.pitfalls.length) return buildComingSoonHTML('\\u26A0','Pitfalls & Security analysis is being prepared');
  return `<div style="display:flex;flex-direction:column;gap:16px;">${d.pitfalls.map((p,i)=>`
    <div style="background:rgba(255,59,92,0.07);border:1px solid rgba(255,59,92,0.25);border-radius:var(--radius);padding:20px;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
        <span style="font-size:1.3rem;">${p.icon||'\\u26A0'}</span>
        <span style="font-weight:700;color:var(--red);font-size:0.95rem;">${p.title}</span>
        <span style="margin-left:auto;font-family:var(--mono);font-size:0.65rem;background:rgba(255,59,92,0.15);color:var(--red);padding:3px 8px;border-radius:20px;">PITFALL #${i+1}</span>
      </div>
      <div style="font-size:0.87rem;color:var(--text);margin-bottom:10px;">${p.desc}</div>
      <div style="background:rgba(0,200,83,0.08);border:1px solid rgba(0,200,83,0.2);border-radius:8px;padding:10px;">
        <span style="font-family:var(--mono);font-size:0.7rem;color:var(--green);">\\u2713 FIX: </span>
        <span style="font-size:0.84rem;color:var(--text-muted);">${p.fix}</span>
      </div>
    </div>
  `).join('')}</div>`;
}

// -- TAB 6: LAB --
function buildLabHTML(d){
  if(!d.lab) return buildComingSoonHTML('\\u{1F52C}','Hands-On Lab is being designed');
  const dc={'Beginner':'var(--green)','Intermediate':'var(--blue)','Advanced':'var(--red)'};
  const color=dc[d.lab.difficulty]||'var(--text-dim)';
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;flex-wrap:wrap;gap:10px;">
      <div>
        <div style="font-size:1.1rem;font-weight:700;color:var(--green);">\\u{1F52C} ${d.lab.title}</div>
        ${d.lab.objectives&&d.lab.objectives.length?`<div style="margin-top:8px;">${d.lab.objectives.map(o=>`<div style="font-size:0.82rem;color:var(--text-muted);margin-top:4px;">\\u2746 ${o}</div>`).join('')}</div>`:''}
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;align-items:flex-end;">
        <span style="font-family:var(--mono);font-size:0.7rem;background:rgba(0,0,0,0.4);border:1px solid var(--border);padding:4px 10px;border-radius:20px;color:${color};">${d.lab.difficulty||'Beginner'}</span>
        <span style="font-family:var(--mono);font-size:0.7rem;color:var(--text-dim);">\\u23F1 ${d.lab.duration||'30 min'}</span>
      </div>
    </div>
    ${d.lab.steps.map((s,i)=>`<div class="lab-step" style="cursor:pointer;" onclick="toggleLabStep(this)"><div class="lab-step-num">${i+1}</div><div class="lab-step-text">${s}</div><span class="lab-check" style="opacity:0;">\\u2713</span></div>`).join('')}
    ${d.lab.validation?`<div style="margin-top:20px;padding:14px;background:rgba(0,200,83,0.08);border:1px solid rgba(0,200,83,0.25);border-radius:8px;"><div style="font-family:var(--mono);font-size:0.7rem;color:var(--green);margin-bottom:6px;">\\u2713 HOW TO CONFIRM SUCCESS</div><div style="font-size:0.86rem;color:var(--text-muted);">${d.lab.validation}</div></div>`:''}
  </div>`;
}

// -- TAB 7: ASSESSMENT --
function buildAssessmentHTML(d){
  return `
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 1 OF 3 \u2014 KNOWLEDGE CHECK</div>
    <div class="quiz-score" id="quiz-score" style="display:none;"></div>
    ${buildQuizHTML(d)}
  </div>
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 2 OF 3 \u2014 FLASHCARDS (hover to flip)</div>
    ${buildFlashcardsHTML(d)}
  </div>
  <div>
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 3 OF 3 \u2014 CAPTURE THE FLAG</div>
    ${buildCTFHTML(d)}
  </div>`;
}

// -- TAB 8: SUMMARY --
function buildSummaryHTML(id,d){
  const isDone=!!completed[id];
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="font-size:1rem;font-weight:700;color:var(--green);margin-bottom:20px;font-family:var(--mono);">// KEY TAKEAWAYS \u2014 EXAM READY</div>
    ${d.summary&&d.summary.length?`<ul class="summary-list">${d.summary.map(s=>`<li>${s}</li>`).join('')}</ul>`:'<div style="color:var(--text-dim);">Summary content coming soon.</div>'}
    <div style="margin-top:32px;padding-top:24px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
      <div id="complete-status-${id}" style="font-family:var(--mono);font-size:0.8rem;color:var(--text-dim);">
        ${isDone?'<span style="color:var(--green);">\\u2713 TOPIC COMPLETED \u2014 XP AWARDED</span>':'Complete all sections, then mark done to earn XP.'}
      </div>
      <button class="btn-complete" id="btn-complete-${id}" onclick="markComplete('${id}')"
        ${isDone?'disabled style="opacity:0.5;cursor:default;"':''}>
        ${isDone?'\\u2713 COMPLETED':'\\u2714 MARK COMPLETE \u2014 EARN 200 XP'}
      </button>
    </div>
  </div>`;
}

// -- QUIZ --
function buildQuizHTML(d){
  if(!d.quiz||!d.quiz.length) return buildComingSoonHTML('\\u2753','Quiz \u2014 10 questions coming soon');
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
  if(!d.flashcards||!d.flashcards.length) return buildComingSoonHTML('\\u{1F0CF}','Flashcards coming soon');
  return `
  <div style="margin-bottom:10px;font-family:var(--mono);font-size:0.75rem;color:var(--text-muted);">// Hover a card to flip and reveal the definition</div>
  <div class="flashcards-grid">${d.flashcards.map(f=>`<div class="flashcard"><div class="fc-front">${f.f}</div><div class="fc-back">${f.b}</div></div>`).join('')}</div>`;
}

// -- CTF --
function buildCTFHTML(d){
  const ctf=d.ctf||{scenario:'Complete all sections to unlock the CTF challenge.',hint:'Study the Learn and Commands tabs first.',flag:'',points:150};
  return `
  <div class="ctf-card">
    <div class="ctf-header"><div class="ctf-flag-icon">\\u{1F6A9}</div><div><div class="ctf-title">CAPTURE THE FLAG</div><div class="ctf-subtitle">// CLASSIFIED INTELLIGENCE CHALLENGE</div></div></div>
    <div class="ctf-points">\\u{1F48E} ${ctf.points||150} POINTS</div>
    <div class="ctf-scenario">${ctf.scenario}</div>
    <div class="ctf-hint" id="ctf-hint" onclick="revealHint(this)" data-hint="${ctf.hint||''}">\\u{1F4A1} HINT: Click to reveal (costs no points)</div>
    <div class="ctf-input-row">
      <input class="ctf-input" id="ctf-flag-input" placeholder="CEH{your_flag_here}" autocomplete="off" spellcheck="false"/>
      <button class="ctf-submit" onclick="submitCTF('${currentTopic}')">SUBMIT FLAG</button>
    </div>
    <div class="ctf-result" id="ctf-result"></div>
  </div>`;
}

"""
    html = html[:bs] + NEW_BUILDERS + html[be:]
    mark('Builder functions', True)

# =============================================================
# 5. ADD markComplete + toggleLabStep AFTER wireDragDrop
# =============================================================
DRAG_MARKER = 'function wireFlashcards(id, d){}\nfunction wireDragDrop(id, d){}'
NEW_HELPERS = """function wireFlashcards(id, d){}
function wireDragDrop(id, d){}

// -- MARK COMPLETE --
async function markComplete(topicId){
  const btn=document.getElementById('btn-complete-'+topicId);
  if(!btn||btn.disabled) return;
  const token=localStorage.getItem('ceh_token');
  if(!token) return;
  btn.textContent='SAVING...'; btn.disabled=true;
  try{
    const r=await fetch('/api/progress/topic',{method:'POST',
      headers:{'Content-Type':'application/json','Authorization':'Bearer '+token},
      body:JSON.stringify({topic_id:topicId,xp_earned:200,flag_captured:false})});
    const data=await r.json();
    if(r.ok){
      completed[topicId]=true; totalXP=data.total_xp||(totalXP+200);
      localStorage.setItem('ceh_completed',JSON.stringify(completed));
      updateProgressUI(); updateTopicButtons();
      btn.textContent='\u2713 COMPLETED'; btn.style.opacity='0.5'; btn.style.cursor='default';
      const st=document.getElementById('complete-status-'+topicId);
      if(st) st.innerHTML='<span style="color:var(--green);">\u2713 TOPIC COMPLETED \u2014 XP AWARDED</span>';
    } else { btn.textContent='\u2714 MARK COMPLETE \u2014 EARN 200 XP'; btn.disabled=false; }
  }catch(e){ btn.textContent='\u2714 MARK COMPLETE \u2014 EARN 200 XP'; btn.disabled=false; }
}

// -- LAB STEP TOGGLE --
function toggleLabStep(el){
  const check=el.querySelector('.lab-check');
  if(!check) return;
  const done=check.style.opacity==='1';
  check.style.opacity=done?'0':'1';
  el.style.background=done?'':'rgba(0,200,83,0.06)';
}"""

if DRAG_MARKER in html:
    html = html.replace(DRAG_MARKER, NEW_HELPERS, 1)
    mark('markComplete+toggleLabStep', True)
else:
    mark('markComplete+toggleLabStep', False)

# =============================================================
# 6. ADD AUTO-STUB GENERATOR before PARTICLES
# =============================================================
PARTICLES_MARKER = '// \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nfunction initParticles'

STUB_GEN = """// ==========================================================
// AUTO-STUB GENERATOR -- fills all topics without content
// ==========================================================
(function(){
  function makeStub(module,title,sub,flag){
    return {module,title,sub,
      killchain:{phase:'Coming Soon',mitre:'TBD',desc:'Content is being prepared.'},
      learn:null,diagram:null,enterprise:null,
      tools:[],commands:{win:[],lin:[]},pitfalls:[],lab:null,
      quiz:[],flashcards:[],
      ctf:{scenario:'Complete the topic learning to unlock this CTF.',hint:'Study the Learn and Commands tabs first.',flag:flag,points:150},
      summary:[]
    };
  }
  MODULES.forEach(m=>{
    const mNum=m.id.replace('m','').padStart(2,'0');
    m.topics.forEach(t=>{
      if(!CONTENT[t.id]){
        CONTENT[t.id]=makeStub(
          'Module '+mNum+' \u00b7 '+m.name, t.name,
          'Content for this topic is being prepared by ShadowXLab analysts.',
          'CEH{'+t.id.replace(/-/g,'_')+'_2026}'
        );
      }
    });
  });
})();

// ==========================================================
function initParticles"""

if PARTICLES_MARKER in html:
    html = html.replace(PARTICLES_MARKER, STUB_GEN, 1)
    mark('Auto-stub generator', True)
else:
    # Try to find initParticles directly
    IP = 'function initParticles(){'
    ip_pos = html.rfind(IP)
    if ip_pos != -1:
        html = html[:ip_pos] + STUB_GEN.replace('function initParticles', 'function initParticles') + html[ip_pos + len(IP):]
        mark('Auto-stub generator (alt)', True)
    else:
        mark('Auto-stub generator', False)

# =============================================================
# 7. ADD diagram+enterprise+pitfalls to Module 01 topics
# =============================================================

# Topic 1: info-security-overview
ANCHOR_T1 = "    lab:{\n      title:'Lab: Map the CIA Triad to Real-World Scenarios',"
PREFIX_T1 = """    diagram:{
      title:'Information Security Threat Lifecycle',
      steps:[
        {icon:'\U0001f464',label:'Threat Actor Emerges',desc:'An adversary identifies your organization as a target with valuable data or systems.'},
        {icon:'\U0001f50d',label:'Reconnaissance',desc:'The attacker researches: open ports, employee names, software versions, IP ranges via OSINT.'},
        {icon:'\U0001f4a5',label:'Exploit Vulnerability',desc:'A weakness is exploited — unpatched software, weak password, phishing, or misconfiguration.'},
        {icon:'\U0001f513',label:'CIA Triad Violated',desc:'Data is stolen (Confidentiality), altered (Integrity), or systems go offline (Availability).'},
        {icon:'\U0001f6e1\ufe0f',label:'Detection & Response',desc:'SIEM, IDS, or analysts detect anomaly and trigger the incident response process.'},
        {icon:'\U0001f4cb',label:'Remediation & Lessons',desc:'Root cause fixed, controls updated, post-incident report filed to prevent recurrence.'}
      ]
    },
    enterprise:{
      role:'You are the Security Architect at GlobalFinSec Corp.',
      situation:'An external audit flagged three critical gaps: no asset inventory, no data classification policy, and no formal incident response plan — ahead of a PCI-DSS compliance deadline.',
      challenge:'Map the CIA Triad to the top three assets (trading platform, customer database, internal email) and identify which controls are missing for each.',
      steps:[
        'List the three assets and classify them by CIA priority (customer DB = highest Confidentiality need).',
        'Run: nmap -sV 192.168.1.0/24 to discover what services are exposed on each asset.',
        'Check for missing patches on Windows hosts: systeminfo | findstr "OS Version".',
        'Identify existing controls (firewall? MFA? encryption?) and document gaps.',
        'Write a one-page risk register: Asset, Threat, Vulnerability, CIA Impact, Recommended Control.'
      ],
      outcome:'You identified 12 missing controls. The trading platform lacked MFA (Confidentiality), the database had no encryption at rest (Confidentiality + Integrity), and email had no DLP (Confidentiality).',
      lesson:'Every security investment must map to a CIA pillar. Without this framing, security spending cannot be justified to the board.'
    },
    pitfalls:[
      {icon:'\u26a0\ufe0f',title:'Mistaking Compliance for Security',desc:'Passing a PCI-DSS or ISO audit does not mean you are secure. Compliance is a minimum bar, not a security guarantee.',fix:'Treat compliance as the floor. Layer additional threat-model-driven controls beyond regulatory minimums.'},
      {icon:'\U0001f534',title:'Neglecting Availability in Security Planning',desc:'Security teams over-focus on Confidentiality (encryption, access control) and neglect Availability until a DDoS hits.',fix:'Include RTO/RPO metrics in all security plans. Regularly test failover and backup restoration.'},
      {icon:'\u26d4',title:'Treating Risk as a One-Time Assessment',desc:'A yearly risk assessment misses new vulnerabilities introduced by software updates, new vendors, and infrastructure changes.',fix:'Implement continuous risk monitoring. Reassess whenever major changes occur.'},
      {icon:'\U0001f3ad',title:'Over-Relying on Perimeter Security',desc:'The castle-and-moat model assumes threats come from outside. Modern threats (insiders, cloud misconfigs) originate inside.',fix:'Adopt Zero Trust: verify every request as untrusted regardless of source location.'}
    ],
    lab:{\n      title:'Lab: Map the CIA Triad to Real-World Scenarios',"""

if ANCHOR_T1 in html:
    html = html.replace(ANCHOR_T1, PREFIX_T1, 1)
    mark('M01T1 diagram+enterprise+pitfalls', True)
else:
    mark('M01T1 diagram+enterprise+pitfalls', False)

# Topic 2: hacker-classes
ANCHOR_T2 = "    lab:{title:'Lab: Threat Actor Profiling',"
PREFIX_T2 = """    diagram:{
      title:'Hacker Classification Decision Tree',
      steps:[
        {icon:'\u2696\ufe0f',label:'Assess Intent',desc:'Is the actor motivated by financial gain, ideology, espionage, curiosity, or authorized testing?'},
        {icon:'\U0001f511',label:'Check Authorization',desc:'Does the actor have explicit written permission from the target? White hat = yes. Everyone else = no.'},
        {icon:'\U0001f3af',label:'Identify Target Type',desc:'Opportunistic (random victims) vs. targeted (specific org, person, or system)?'},
        {icon:'\U0001f6e0\ufe0f',label:'Evaluate Skill',desc:'Script kiddie (pre-built tools, zero understanding) vs. sophisticated (custom exploits, zero-days, persistence).'},
        {icon:'\U0001f3f7\ufe0f',label:'Apply Classification',desc:'White Hat, Grey Hat, Black Hat, Hacktivist, APT/Nation-State, Malicious Insider, or Script Kiddie.'},
        {icon:'\U0001f6e1\ufe0f',label:'Tailor Defenses',desc:'Match your defense investment to the most likely threat actors for your industry and data profile.'}
      ]
    },
    enterprise:{
      role:'You are the Threat Intelligence Analyst at GlobalFinSec Corp.',
      situation:'A SOC alert fires at 2 AM: a privileged database administrator is transferring 50GB of customer records to a personal Dropbox account.',
      challenge:'Classify this threat actor, determine their likely motivation, and recommend immediate containment actions.',
      steps:[
        'Pull the employee access logs for the past 30 days — is this the first anomalous transfer?',
        'Check HR records — any recent performance reviews, disciplinary actions, or resignation notices?',
        'Verify if the destination IP is on threat intelligence blocklists (VirusTotal, AbuseIPDB).',
        'Classify: this is a Malicious Insider — authorized access, clearly malicious intent.',
        'Trigger the Insider Threat IR playbook: disable account, preserve forensic evidence, notify Legal and HR.'
      ],
      outcome:'The employee was a departing staff member harvesting customer PII for a competitor. Early DLP and UEBA detection prevented full exfiltration. The employee was prosecuted under the CFAA.',
      lesson:'Insiders are the hardest threat to detect because their traffic looks legitimate. The solution is behavioral analytics (UEBA), not just perimeter firewalls.'
    },
    pitfalls:[
      {icon:'\u26a0\ufe0f',title:'Underestimating Script Kiddies',desc:'Organizations dismiss script kiddies as low-skill noise. But automated tools (Metasploit, SQLmap) require zero expertise and can cause real damage at scale.',fix:'Patch all publicly-known CVEs promptly. Most script kiddie attacks exploit unpatched, well-documented vulnerabilities.'},
      {icon:'\U0001f534',title:'Focusing All Defenses on External Threats',desc:'Most security budgets go to perimeter controls. But Verizon DBIR shows insiders cause 20-30% of all breaches.',fix:'Implement insider threat programs: UEBA, DLP, Privileged Access Management (PAM), and quarterly access reviews.'},
      {icon:'\u26d4',title:'Treating Grey Hat Reports as Goodwill',desc:'Grey hats who report vulnerabilities after unauthorized testing are still committing a crime under CFAA/Computer Misuse Act.',fix:'Establish a formal Bug Bounty or Responsible Disclosure program. Never encourage unsolicited testing.'}
    ],
    lab:{title:'Lab: Threat Actor Profiling',"""

if ANCHOR_T2 in html:
    html = html.replace(ANCHOR_T2, PREFIX_T2, 1)
    mark('M01T2 diagram+enterprise+pitfalls', True)
else:
    mark('M01T2 diagram+enterprise+pitfalls', False)

# Topic 3: ethical-hacking-concepts
ANCHOR_T3 = "    lab:{title:'Lab: Draft a Rules of Engagement Document',"
PREFIX_T3 = """    diagram:{
      title:'Ethical Hacking Engagement Lifecycle',
      steps:[
        {icon:'\U0001f4dd',label:'Pre-Engagement',desc:'Define scope, sign NDA and SOW, establish Rules of Engagement. Get written authorization — without this you are a criminal.'},
        {icon:'\U0001f50d',label:'Reconnaissance',desc:'Gather intelligence: OSINT, WHOIS, DNS enumeration, employee profiling, IP range mapping.'},
        {icon:'\U0001f4e1',label:'Scanning & Enumeration',desc:'Actively probe target: port scanning (Nmap), service versioning, OS fingerprinting, vulnerability scanning.'},
        {icon:'\U0001f4a5',label:'Exploitation',desc:'Attempt to exploit discovered vulnerabilities within the agreed scope to gain unauthorized access.'},
        {icon:'\U0001f4ca',label:'Post-Exploitation & Reporting',desc:'Document findings: proof-of-concept, CVSS scores, business impact assessment, remediation steps.'},
        {icon:'\U0001f91d',label:'Remediation & Retest',desc:'Client fixes vulnerabilities. You verify fixes were correctly implemented. Cycle repeats until clean.'}
      ]
    },
    enterprise:{
      role:'You are the Lead Penetration Tester contracted by GlobalFinSec Corp.',
      situation:'The CISO verbally tells you to "test everything" before a PCI-DSS audit next month. No paperwork has been signed.',
      challenge:'Identify every legal and ethical action you must take BEFORE beginning any testing activity.',
      steps:[
        'Decline to start testing. Verbal authorization is legally insufficient under CFAA (USA) and Computer Misuse Act (UK).',
        'Draft a Statement of Work (SOW): scope (IP ranges, domains, apps), excluded systems, testing windows, emergency contacts.',
        'Draft a Rules of Engagement (RoE): allowed techniques, prohibited actions (no production DoS), escalation procedures.',
        'Get both documents signed by an authorized executive (CISO, CTO, or CEO).',
        'Only then begin passive OSINT reconnaissance — no active probing until paperwork is signed.'
      ],
      outcome:'Proper documentation protects both tester (legal immunity) and client (defined liability). Testing began 3 days later after paperwork was signed. 47 vulnerabilities found, including 3 critical RCEs.',
      lesson:'The most important tool in an ethical hacker\\'s kit is not Nmap or Metasploit. It is the signed authorization document.'
    },
    pitfalls:[
      {icon:'\u26a0\ufe0f',title:'Testing Without Written Authorization',desc:'A verbal "go ahead" from the IT manager is not legal authorization. If anything goes wrong, you face criminal prosecution.',fix:'Always obtain a signed Statement of Work AND Rules of Engagement before generating a single packet.'},
      {icon:'\U0001f534',title:'Testing Systems Outside Defined Scope',desc:'Following an attack chain to an out-of-scope system is unauthorized access — a criminal offense regardless of employment status.',fix:'Define scope boundaries explicitly in the RoE. If you discover a path to out-of-scope systems, stop and notify the client immediately.'},
      {icon:'\u26d4',title:'Saving Critical Findings for the Final Report',desc:'Discovering a critical RCE on Day 1 and waiting 3 weeks to report it leaves the client exposed throughout the engagement.',fix:'Establish an escalation procedure for critical findings. Call the emergency contact the moment a critical vulnerability is confirmed.'},
      {icon:'\U0001f3ad',title:'Confusing a Vuln Scan with a Penetration Test',desc:'Running Nessus and handing over a scan report is not a penetration test. It is a vulnerability scan.',fix:'A real penetration test involves manual exploitation, chained attack paths, business impact assessment, and proof-of-concept evidence.'}
    ],
    lab:{title:'Lab: Draft a Rules of Engagement Document',"""

if ANCHOR_T3 in html:
    html = html.replace(ANCHOR_T3, PREFIX_T3, 1)
    mark('M01T3 diagram+enterprise+pitfalls', True)
else:
    mark('M01T3 diagram+enterprise+pitfalls', False)

# =============================================================
# WRITE OUTPUT
# =============================================================
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print("=" * 50)
print("REBUILD SKELETON COMPLETE")
print("=" * 50)
for s in ok:
    print(f"  [OK]  {s}")
for s in fail:
    print(f"  [FAIL] {s}")
print()
print(f"Original: {original_len:,} bytes")
print(f"New:      {len(html):,} bytes")
print(f"Lines:    {html.count(chr(10)):,}")
