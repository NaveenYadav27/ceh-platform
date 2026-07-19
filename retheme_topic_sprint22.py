import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_topic_html = """function buildTopicHTML(id, d){
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
}"""

new_topic_html = """function buildStandardizedCommands(cmds) {
  if (!cmds) return '';
  let html = '<div style="display:flex; flex-direction:column; gap:16px;">';
  
  const processPlatform = (arr, platformBadge) => {
    if(!arr || !Array.isArray(arr)) return;
    arr.forEach(cmd => {
      let cmdStr = typeof cmd === 'string' ? cmd : cmd.cmd || cmd.c || "Command pending";
      let purpose = cmd.purpose || cmd.p || "Purpose pending content completion.";
      let out = cmd.out || cmd.o || "Output pending.";
      let note = cmd.note || cmd.n || "Enterprise note pending.";
      let mistake = cmd.mistake || cmd.m || "Common mistake pending.";

      html += `
      <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1); border-radius:var(--gfs-radius); overflow:hidden;">
        <div style="background:rgba(255,255,255,0.05); padding:8px 16px; border-bottom:1px solid rgba(255,255,255,0.1); display:flex; justify-content:space-between; align-items:center;">
          <span style="font-family:var(--gfs-font-mono); font-size:0.75rem; color:var(--gfs-info);">${platformBadge}</span>
          <span style="font-family:var(--gfs-font-body); font-size:0.75rem; color:var(--gfs-text-muted);">${purpose}</span>
        </div>
        <div style="padding:16px;">
          <div style="font-family:var(--gfs-font-mono); color:#fff; font-size:0.9rem; margin-bottom:12px; background:#000; padding:12px; border-radius:4px; border-left:3px solid var(--gfs-primary);">$ ${cmdStr}</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
            <div style="background:var(--gfs-bg-secondary); padding:12px; border-radius:4px; border-left:2px solid var(--gfs-success);">
              <div style="font-family:var(--gfs-font-mono); font-size:0.65rem; color:var(--gfs-text-muted); text-transform:uppercase; margin-bottom:6px;">Expected Output</div>
              <div style="font-family:var(--gfs-font-mono); font-size:0.75rem; color:var(--gfs-text-secondary); white-space:pre-wrap;">${out}</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div style="background:var(--gfs-bg-secondary); padding:12px; border-radius:4px; border-left:2px solid var(--gfs-info);">
                <div style="font-family:var(--gfs-font-mono); font-size:0.65rem; color:var(--gfs-text-muted); text-transform:uppercase; margin-bottom:6px;">Enterprise Note</div>
                <div style="font-family:var(--gfs-font-body); font-size:0.8rem; color:var(--gfs-text-secondary);">${note}</div>
              </div>
              <div style="background:var(--gfs-bg-secondary); padding:12px; border-radius:4px; border-left:2px solid var(--gfs-danger);">
                <div style="font-family:var(--gfs-font-mono); font-size:0.65rem; color:var(--gfs-text-muted); text-transform:uppercase; margin-bottom:6px;">Common Mistake</div>
                <div style="font-family:var(--gfs-font-body); font-size:0.8rem; color:var(--gfs-text-secondary);">${mistake}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      `;
    });
  };

  processPlatform(cmds.lin || [], "LINUX");
  processPlatform(cmds.win || [], "WINDOWS");

  if(html === '<div style="display:flex; flex-direction:column; gap:16px;">') {
    return `<div style="font-family:var(--gfs-font-mono); font-size:0.8rem; color:var(--gfs-text-muted); background:var(--gfs-bg-panel); border:1px solid var(--gfs-border); padding:16px; border-radius:var(--gfs-radius);">Commands pending content completion sprint.</div>`;
  }

  html += '</div>';
  return html;
}

function buildTopicHTML(id, d){
  const hasContent = !!CONTENT[id] || !!TOPIC_STUBS[id];
  
  const dur = (d.duration || '15') + ' min';
  let diffColor = 'var(--gfs-info)';
  let diffBadge = 'Foundation';
  if(d.difficulty === 'Intermediate') { diffColor = 'var(--gfs-warning)'; diffBadge = 'Intermediate'; }
  if(d.difficulty === 'Advanced') { diffColor = 'var(--gfs-danger)'; diffBadge = 'Advanced'; }

  return `
  <div style="padding: 0 0 60px 0; max-width:960px; margin:0 auto;">
  
  <!-- 1. ENTERPRISE HEADER -->
  <div class="topic-header" style="background:var(--gfs-bg-panel); border:1px solid var(--gfs-border); border-radius:var(--gfs-radius); padding:32px; margin-bottom:40px; box-shadow:var(--gfs-shadow);">
    <div class="topic-eyebrow" style="font-family:var(--gfs-font-mono); color:var(--gfs-text-muted); font-size:0.75rem; text-transform:uppercase; margin-bottom:12px; letter-spacing:1px;">${d.module||'TRAINING MODULE'}</div>
    <div class="topic-title" style="font-family:var(--gfs-font-display); font-size:2.2rem; font-weight:700; color:var(--gfs-text-primary); margin-bottom:12px; line-height:1.2;">${d.title || id}</div>
    <div class="topic-sub" style="font-family:var(--gfs-font-body); font-size:1.05rem; color:var(--gfs-text-secondary); margin-bottom:24px;">${d.sub || 'Topic content pending.'}</div>
    
    <div class="topic-meta-ribbon" style="display:flex; gap:24px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
      <div style="font-family:var(--gfs-font-mono); font-size:0.8rem;"><span style="color:var(--gfs-text-muted);">EST:</span> ~${dur}</div>
      <div style="font-family:var(--gfs-font-mono); font-size:0.8rem; color:${diffColor};"><span style="color:var(--gfs-text-muted);">LVL:</span> ${diffBadge}</div>
      <div style="font-family:var(--gfs-font-mono); font-size:0.8rem; color:${completed[id] ? 'var(--gfs-success)' : 'var(--gfs-primary)'};"><span style="color:var(--gfs-text-muted);">STATUS:</span> ${completed[id] ? 'Completed' : 'In Progress'}</div>
    </div>
  </div>

  <div class="topic-body" style="display:flex; flex-direction:column; gap:48px;">
    
    <!-- 2. LEARNING OBJECTIVES -->
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Learning Objectives</h3>
      ${(d.objectives && d.objectives.length > 0) ? `<ul style="font-family:var(--gfs-font-body); color:var(--gfs-text-secondary); padding-left:24px; line-height:1.7; display:flex; flex-direction:column; gap:10px; font-size:0.95rem;">${d.objectives.map(o=>`<li>${o}</li>`).join('')}</ul>` : `<div style="font-family:var(--gfs-font-mono); font-size:0.8rem; color:var(--gfs-text-muted); background:var(--gfs-bg-panel); border:1px solid var(--gfs-border); padding:16px; border-radius:var(--gfs-radius);">Objectives pending content completion sprint.</div>`}
    </div>

    <!-- 3. BUSINESS CONTEXT (WHY) -->
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Business Context (WHY)</h3>
      ${d.enterprise ? `
        <div class="scenario-card" style="background:var(--gfs-bg-panel); border-left:4px solid var(--gfs-primary); border-radius:4px; padding:24px; box-shadow:var(--gfs-shadow);">
          <div style="font-family:var(--gfs-font-mono); font-size:0.75rem; color:var(--gfs-primary); margin-bottom:12px; letter-spacing:1px; text-transform:uppercase;">SOC Incident Report</div>
          <div style="font-family:var(--gfs-font-body); color:var(--gfs-text-primary); line-height:1.7; font-size:0.95rem;">
            ${d.enterprise.gfs || d.enterprise.text || d.enterprise.windows || d.enterprise.linux || d.enterprise}
          </div>
        </div>
      ` : `
        <div class="scenario-card" style="background:var(--gfs-bg-panel); border-left:4px solid var(--gfs-text-muted); border-radius:4px; padding:24px; box-shadow:var(--gfs-shadow);">
          <div style="font-family:var(--gfs-font-mono); font-size:0.75rem; color:var(--gfs-text-muted); margin-bottom:12px; letter-spacing:1px; text-transform:uppercase;">Enterprise Context</div>
          <div style="font-family:var(--gfs-font-body); color:var(--gfs-text-secondary); line-height:1.7; font-size:0.95rem;">
            This lesson has been technically implemented.<br>Enterprise business context will be added during the Content Completion Sprint.
            <br><br><strong style="color:var(--gfs-text-primary);">Learning Focus:</strong> Continue with the technical concepts below.
          </div>
        </div>
      `}
    </div>

    <!-- 4. CORE CONCEPT (WHAT) -->
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Core Concept (WHAT)</h3>
      <div style="font-family:var(--gfs-font-body); color:var(--gfs-text-primary); line-height:1.8; font-size:1rem;">
        ${d.learn?.simple || d.sub || `<div style="font-family:var(--gfs-font-mono); font-size:0.8rem; color:var(--gfs-text-muted); background:var(--gfs-bg-panel); border:1px solid var(--gfs-border); padding:16px; border-radius:var(--gfs-radius);">Core concept pending content completion sprint.</div>`}
      </div>
      ${d.diagram ? `
        <div style="margin-top:32px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.1); border-radius:var(--gfs-radius); padding:32px; text-align:center;">
           ${d.diagram.svg || '<div style="font-family:var(--gfs-font-mono); color:var(--gfs-text-muted);">Diagram Pending</div>'}
        </div>
      ` : ''}
    </div>
    
    <!-- 5. ENTERPRISE WORKFLOW -->
    ${d.workflow ? `
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Enterprise Workflow</h3>
      <div style="background:var(--gfs-bg-panel); border:1px solid var(--gfs-border); border-radius:var(--gfs-radius); padding:24px;">
        <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:16px;">
          ${d.workflow.map((step, i) => `
            <li style="display:flex; gap:16px;">
              <div style="font-family:var(--gfs-font-mono); color:var(--gfs-primary); width:24px; flex-shrink:0;">${i+1}.</div>
              <div style="font-family:var(--gfs-font-body); color:var(--gfs-text-secondary); line-height:1.6; font-size:0.95rem;">${step}</div>
            </li>
          `).join('')}
        </ul>
      </div>
    </div>` : ''}

    <!-- 6. TECHNICAL DEEP DIVE (HOW) -->
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Technical Deep Dive (HOW)</h3>
      <div style="font-family:var(--gfs-font-body); color:var(--gfs-text-primary); line-height:1.8; font-size:0.95rem;">
        ${d.learn?.architecture || `<div style="font-family:var(--gfs-font-mono); font-size:0.8rem; color:var(--gfs-text-muted); background:var(--gfs-bg-panel); border:1px solid var(--gfs-border); padding:16px; border-radius:var(--gfs-radius);">Technical deep dive pending content completion sprint.</div>`}
      </div>
    </div>
    
    <!-- 7. COMMAND REFERENCE -->
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Command Reference</h3>
      ${buildStandardizedCommands(d.commands)}
    </div>

    <!-- 8. KNOWLEDGE CHECK -->
    ${(d.quiz && d.quiz.length > 0) ? `
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Knowledge Check</h3>
      ${buildAssessmentHTML(d)}
    </div>` : ''}

    <!-- 9. KEY TAKEAWAYS -->
    <div class="topic-section">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-text-primary); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; margin-bottom:20px; font-size:1.4rem;">Key Takeaways</h3>
      ${d.summary ? `
      <ul style="font-family:var(--gfs-font-body); color:var(--gfs-text-secondary); padding-left:24px; line-height:1.7; display:flex; flex-direction:column; gap:10px; font-size:0.95rem;">
        ${d.summary.map(s => `<li>${s}</li>`).join('')}
      </ul>` : `<div style="font-family:var(--gfs-font-mono); font-size:0.8rem; color:var(--gfs-text-muted); background:var(--gfs-bg-panel); border:1px solid var(--gfs-border); padding:16px; border-radius:var(--gfs-radius);">Takeaways pending.</div>`}
    </div>
    
    <!-- 10. ESTIMATED OUTCOMES -->
    <div class="topic-section" style="background:var(--gfs-bg-secondary); border-radius:var(--gfs-radius); padding:32px; margin-top:16px;">
      <h3 style="font-family:var(--gfs-font-display); color:var(--gfs-success); margin-bottom:16px; font-size:1.2rem;">After completing this lesson you can:</h3>
      <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:12px;">
        ${(d.outcomes || ["Explain the core concepts of this topic.", "Identify security risks associated with this domain.", "Apply basic defensive measures."]).map(o => `
          <li style="display:flex; align-items:center; gap:12px; font-family:var(--gfs-font-body); color:var(--gfs-text-primary); font-size:0.95rem;">
            <span style="color:var(--gfs-success); font-weight:700;">✓</span> ${o}
          </li>
        `).join('')}
      </ul>
    </div>

    <!-- ACTION FOOTER -->
    <div class="topic-footer" style="margin-top:24px; padding-top:40px; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:flex-end;">
      <button class="btn-complete" onclick="completeTopic('${id}')" style="background:var(--gfs-success); color:#000; border:none; padding:16px 32px; border-radius:var(--gfs-radius); font-family:var(--gfs-font-display); font-weight:700; font-size:1.1rem; cursor:pointer; box-shadow:0 0 20px rgba(0,255,136,0.3); transition:all 0.2s;">
        ${completed[id] ? '✓ Topic Completed' : 'Mark Complete & Continue ➔'}
      </button>
    </div>

  </div>
  </div>
  `;
}"""

# Remove the wireTopicTabs call from openTopic as tabs no longer exist
old_open_topic = """  view.innerHTML = buildTopicHTML(id, data);
  wireTopicTabs(id, data);
  initFloatingTerminals();"""

new_open_topic = """  view.innerHTML = buildTopicHTML(id, data);
  // wireTopicTabs removed - using single scroll enterprise view
  initFloatingTerminals();"""

if old_topic_html in content:
    content = content.replace(old_topic_html, new_topic_html)
    content = content.replace(old_open_topic, new_open_topic)
    with open('frontend/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced buildTopicHTML and applied Sprint 2.2 Corporate architecture.")
else:
    print("ERROR: old_topic_html did not match content in index.html.")
