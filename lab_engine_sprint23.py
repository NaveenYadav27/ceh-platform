with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. ADD NEW LAB ENGINE CSS ───────────────────────────────────────────────
old_lab_css = """.lab-step{display:flex;gap:14px;margin-bottom:16px;align-items:flex-start;}
.lab-step-num{width:32px;height:32px;border-radius:50%;background:var(--gfs-success-dim);border:1px solid var(--gfs-success);display:flex;align-items:center;justify-content:center;font-family:var(--gfs-font-mono);font-size:0.78rem;color:var(--gfs-success);flex-shrink:0;}
.lab-step-text{flex:1;font-size:0.86rem;color:var(--gfs-text-secondary);line-height:1.7;padding-top:6px;}"""

new_lab_css = """.lab-step{display:flex;gap:14px;margin-bottom:12px;align-items:flex-start;background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:16px;cursor:pointer;transition:var(--gfs-transition);}
.lab-step:hover{border-color:var(--gfs-border-highlight);}
.lab-step.done{border-color:var(--gfs-success);background:rgba(0,255,136,0.04);}
.lab-step-num{width:32px;height:32px;border-radius:50%;background:var(--gfs-success-dim);border:1px solid var(--gfs-success);display:flex;align-items:center;justify-content:center;font-family:var(--gfs-font-mono);font-size:0.78rem;color:var(--gfs-success);flex-shrink:0;}
.lab-step-text{flex:1;font-size:0.9rem;color:var(--gfs-text-secondary);line-height:1.7;}
.lab-check{font-size:1rem;color:var(--gfs-success);opacity:0;transition:opacity 0.2s;flex-shrink:0;margin-top:6px;}

/* Lab Engine Components */
.lab-env-card{background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:20px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
.lab-env-item{display:flex;flex-direction:column;gap:4px;}
.lab-env-label{font-family:var(--gfs-font-mono);font-size:0.65rem;color:var(--gfs-text-muted);text-transform:uppercase;letter-spacing:0.5px;}
.lab-env-val{font-family:var(--gfs-font-body);font-size:0.9rem;color:var(--gfs-text-primary);}

.lab-safety-card{background:rgba(255,214,0,0.05);border:1px solid var(--gfs-warning);border-radius:var(--gfs-radius);padding:16px 20px;display:flex;align-items:flex-start;gap:12px;}
.lab-safety-icon{font-size:1.2rem;flex-shrink:0;margin-top:2px;}
.lab-safety-text{font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-secondary);line-height:1.6;}

.lab-evidence-card{background:rgba(0,170,255,0.05);border:1px solid var(--gfs-info);border-radius:var(--gfs-radius);padding:16px 20px;}
.lab-evidence-header{font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-info);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:10px;}
.lab-evidence-item{font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-secondary);padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.04);}

.lab-validation-card{background:rgba(0,255,136,0.03);border:1px solid var(--gfs-success);border-radius:var(--gfs-radius);padding:16px 20px;}
.lab-validation-header{font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-success);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:10px;}
.lab-validation-item{display:flex;gap:10px;font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-secondary);padding:6px 0;}

.lab-mitre-card{background:var(--gfs-bg-panel);border:1px solid var(--gfs-danger);border-radius:var(--gfs-radius);padding:16px 20px;}
.lab-mitre-header{font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-danger);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:10px;}

.lab-reflection-card{background:var(--gfs-bg-panel);border:1px solid var(--gfs-primary);border-radius:var(--gfs-radius);padding:24px;}
.lab-reflection-q{font-family:var(--gfs-font-body);font-size:0.9rem;color:var(--gfs-text-primary);margin-bottom:8px;}
.lab-reflection-input{width:100%;background:rgba(0,0,0,0.3);border:1px solid var(--gfs-border);border-radius:4px;padding:12px;color:var(--gfs-text-primary);font-family:var(--gfs-font-body);font-size:0.88rem;min-height:80px;resize:vertical;outline:none;transition:var(--gfs-transition);}
.lab-reflection-input:focus{border-color:var(--gfs-primary);}

@media(max-width:767px){.lab-env-card{grid-template-columns:repeat(2,1fr);}}"""

content = content.replace(old_lab_css, new_lab_css)


# ─── 2. REPLACE buildLabHTML WITH FULL LAB ENGINE ────────────────────────────
old_lab_fn = """function buildLabHTML(d){
  if(!d.lab) return buildComingSoonHTML('🔬','Hands-On Lab is being designed');
  const dc={'Beginner':'var(--gfs-success)','Intermediate':'var(--gfs-info)','Advanced':'var(--gfs-danger)'};
  const color=dc[d.lab.difficulty]||'var(--gfs-text-secondary)';
  
  const stepsHtml = d.lab.steps.map((s,i)=>{
    // Make text in backticks clickable to terminal
    let formattedText = s.replace(/`([^`]+)`/g, '<span class="clickable-cmd" style="color:var(--gfs-info);background:rgba(0,170,255,0.1);padding:2px 6px;border-radius:4px;font-family:var(--gfs-font-mono);" onclick="runCommand(\\'lin\\', \\'$1\\')">$1</span>');
    return `<div class="lab-step" style="cursor:pointer;" onclick="toggleLabStep(this)"><div class="lab-step-num">${i+1}</div><div class="lab-step-text">${formattedText}</div><span class="lab-check" style="opacity:0;">✓</span></div>`;
  }).join('');

  return `
  <div style="background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:24px;">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;flex-wrap:wrap;gap:10px;">
      <div>
        <div style="font-size:1.1rem;font-weight:700;color:var(--gfs-success);">🔬 ${d.lab.title}</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;align-items:flex-end;">
        <span style="font-family:var(--gfs-font-mono);font-size:0.7rem;background:rgba(0,0,0,0.4);border:1px solid var(--gfs-border);padding:4px 10px;border-radius:20px;color:${color};">${d.lab.difficulty||'Beginner'}</span>
      </div>
    </div>
    ${stepsHtml}
  </div>`;
}"""

new_lab_fn = r"""/* ── ENTERPRISE LAB ENGINE ─────────────────────────────────────── */

function formatLabCommand(text) {
  return text.replace(/`([^`]+)`/g,
    '<span class="clickable-cmd" style="color:var(--gfs-info);background:rgba(0,170,255,0.1);padding:2px 6px;border-radius:4px;font-family:var(--gfs-font-mono);" onclick="runCommand(\'lin\', \'$1\')">$1</span>');
}

function buildLabSection(label, content) {
  if (!content) return '';
  return `
    <div class="lab-section" style="margin-bottom:40px;">
      <h4 style="font-family:var(--gfs-font-mono);font-size:0.75rem;color:var(--gfs-text-muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:16px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.06);">${label}</h4>
      ${content}
    </div>`;
}

function buildLabPendingBlock(label) {
  return `<div style="font-family:var(--gfs-font-mono);font-size:0.8rem;color:var(--gfs-text-muted);background:var(--gfs-bg-panel);border:1px dashed rgba(255,255,255,0.1);padding:16px;border-radius:var(--gfs-radius);">${label} pending content completion sprint.</div>`;
}

function buildLabTypeBadge(type) {
  const types = {
    guided:     { color:'var(--gfs-info)',    label:'Guided Lab' },
    challenge:  { color:'var(--gfs-warning)', label:'Challenge Lab' },
    incident:   { color:'var(--gfs-danger)',  label:'Incident Lab' },
    assessment: { color:'var(--gfs-danger)',  label:'Assessment Lab' },
    capstone:   { color:'var(--gfs-primary)', label:'Capstone Lab' }
  };
  const t = types[type] || types.guided;
  return `<span style="font-family:var(--gfs-font-mono);font-size:0.65rem;padding:4px 10px;border-radius:20px;border:1px solid ${t.color};color:${t.color};text-transform:uppercase;letter-spacing:0.5px;">${t.label}</span>`;
}

function buildLabDiffBadge(diff) {
  const diffMap = {
    Foundation:   'var(--gfs-info)',
    Beginner:     'var(--gfs-info)',
    Intermediate: 'var(--gfs-warning)',
    Advanced:     'var(--gfs-danger)'
  };
  const color = diffMap[diff] || 'var(--gfs-text-secondary)';
  return `<span style="font-family:var(--gfs-font-mono);font-size:0.65rem;padding:4px 10px;border-radius:20px;border:1px solid ${color};color:${color};">${diff || 'Foundation'}</span>`;
}

function buildLabHTML(d) {
  if (!d.lab) {
    return `
    <div style="background:var(--gfs-bg-panel);border:1px dashed rgba(255,255,255,0.12);border-radius:var(--gfs-radius);padding:40px;text-align:center;">
      <div style="font-size:2.5rem;margin-bottom:16px;">🔬</div>
      <div style="font-family:var(--gfs-font-display);font-size:1.1rem;color:var(--gfs-text-primary);margin-bottom:8px;">Lab Framework Ready</div>
      <div style="font-family:var(--gfs-font-body);font-size:0.9rem;color:var(--gfs-text-muted);line-height:1.6;max-width:420px;margin:0 auto;">
        This topic's lab exercise will be authored during the Content Completion Sprint (Sprint 3). The Lab Engine framework is fully operational.
      </div>
    </div>`;
  }

  const lab = d.lab;
  const labId = `lab-${(lab.title||'lab').replace(/\s+/g,'-').toLowerCase()}`;

  // ── Header ─────────────────────────────────────────────────────
  const headerHtml = `
  <div style="background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:32px;margin-bottom:40px;box-shadow:var(--gfs-shadow);">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:20px;">
      <div>
        <div style="font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-text-muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Enterprise Lab Exercise</div>
        <div style="font-family:var(--gfs-font-display);font-size:1.6rem;font-weight:700;color:var(--gfs-text-primary);">🔬 ${lab.title}</div>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;">
        ${buildLabTypeBadge(lab.type || 'guided')}
        ${buildLabDiffBadge(lab.difficulty || 'Foundation')}
      </div>
    </div>
    <div class="lab-env-card">
      <div class="lab-env-item"><span class="lab-env-label">Est. Duration</span><span class="lab-env-val">~${lab.duration || '30'} min</span></div>
      <div class="lab-env-item"><span class="lab-env-label">Platform</span><span class="lab-env-val">${lab.platform || 'Windows / Linux'}</span></div>
      <div class="lab-env-item"><span class="lab-env-label">Environment</span><span class="lab-env-val">${lab.environment || 'Local Lab'}</span></div>
      <div class="lab-env-item"><span class="lab-env-label">Required Tools</span><span class="lab-env-val">${(lab.tools || []).join(', ') || 'Pending'}</span></div>
      <div class="lab-env-item"><span class="lab-env-label">Dependencies</span><span class="lab-env-val">${(lab.dependencies || []).join(', ') || 'None'}</span></div>
      <div class="lab-env-item"><span class="lab-env-label">Lab Status</span><span class="lab-env-val" style="color:var(--gfs-primary);" id="${labId}-status">Not Started</span></div>
    </div>
  </div>`;

  // ── Business Scenario ───────────────────────────────────────────
  const scenarioHtml = lab.scenario ? `
    <div class="scenario-card" style="background:var(--gfs-bg-panel);border-left:4px solid var(--gfs-primary);border-radius:4px;padding:24px;box-shadow:var(--gfs-shadow);">
      <div style="font-family:var(--gfs-font-mono);font-size:0.75rem;color:var(--gfs-primary);margin-bottom:12px;letter-spacing:1px;text-transform:uppercase;">GFS Business Scenario</div>
      <div style="font-family:var(--gfs-font-body);color:var(--gfs-text-primary);line-height:1.7;font-size:0.95rem;">${lab.scenario}</div>
    </div>` : buildLabPendingBlock('Business scenario');

  // ── Objectives ─────────────────────────────────────────────────
  const objectivesHtml = (lab.objectives && lab.objectives.length) ? `
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px;">
      ${lab.objectives.map(o => `<li style="display:flex;gap:12px;align-items:flex-start;font-family:var(--gfs-font-body);font-size:0.9rem;color:var(--gfs-text-secondary);line-height:1.6;"><span style="color:var(--gfs-success);flex-shrink:0;font-weight:700;">▸</span>${o}</li>`).join('')}
    </ul>` : buildLabPendingBlock('Objectives');

  // ── Safety Notice ───────────────────────────────────────────────
  const safetyNotices = lab.safety || [
    'Perform this lab only in an authorized environment.',
    'Do not run these commands against production systems.',
    'Ensure you have written permission before testing any network or system.'
  ];
  const safetyHtml = `
    <div class="lab-safety-card">
      <div class="lab-safety-icon">⚠️</div>
      <div>
        <div style="font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-warning);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:8px;">Safety Notice</div>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
          ${safetyNotices.map(s => `<li class="lab-safety-text">${s}</li>`).join('')}
        </ul>
      </div>
    </div>`;

  // ── Tasks ───────────────────────────────────────────────────────
  const stepsHtml = (lab.steps && lab.steps.length) ? `
    <div id="${labId}-steps" style="display:flex;flex-direction:column;gap:8px;">
      ${lab.steps.map((s, i) => {
        const text = formatLabCommand(typeof s === 'string' ? s : s.text || s.step || String(s));
        return `<div class="lab-step" onclick="toggleLabStep(this)">
          <div class="lab-step-num">${i+1}</div>
          <div class="lab-step-text">${text}</div>
          <span class="lab-check">✓</span>
        </div>`;
      }).join('')}
    </div>` : buildLabPendingBlock('Lab tasks');

  // ── Evidence Collection ─────────────────────────────────────────
  const evidenceItems = lab.evidence || [
    'Terminal output from each command.',
    'Screenshot of final configuration.',
    'Any error messages encountered.'
  ];
  const evidenceHtml = `
    <div class="lab-evidence-card">
      <div class="lab-evidence-header">Evidence to Collect</div>
      ${evidenceItems.map(e => `<div class="lab-evidence-item">📎 ${e}</div>`).join('')}
    </div>`;

  // ── Validation ──────────────────────────────────────────────────
  const validationItems = lab.validation || ['Pending content completion sprint.'];
  const validationHtml = `
    <div class="lab-validation-card">
      <div class="lab-validation-header">How to Validate Success</div>
      ${validationItems.map(v => `<div class="lab-validation-item"><span style="color:var(--gfs-success);flex-shrink:0;">✓</span>${v}</div>`).join('')}
    </div>`;

  // ── Troubleshooting ─────────────────────────────────────────────
  const troubleshootingHtml = (lab.troubleshooting && lab.troubleshooting.length) ? `
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px;">
      ${lab.troubleshooting.map(t => `<li style="display:flex;gap:10px;font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-secondary);line-height:1.6;padding:12px;background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);"><span style="flex-shrink:0;color:var(--gfs-warning);">⚡</span>${t}</li>`).join('')}
    </ul>` : buildLabPendingBlock('Troubleshooting tips');

  // ── MITRE ATT&CK ────────────────────────────────────────────────
  const mitreSectionHtml = lab.mitre ? `
    <div class="lab-mitre-card">
      <div class="lab-mitre-header">MITRE ATT&CK Mapping</div>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;">
        ${(Array.isArray(lab.mitre) ? lab.mitre : [lab.mitre]).map(m => `
          <div style="background:var(--gfs-bg-primary);border:1px solid rgba(255,59,92,0.2);border-radius:4px;padding:12px;">
            <div style="font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-danger);margin-bottom:4px;">${m.id || 'ATT&CK-ID'}</div>
            <div style="font-family:var(--gfs-font-body);font-size:0.85rem;color:var(--gfs-text-primary);">${m.name || m}</div>
            ${m.tactic ? `<div style="font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-text-muted);margin-top:4px;">${m.tactic}</div>` : ''}
          </div>`).join('')}
      </div>
    </div>` : '';

  // ── Cleanup ─────────────────────────────────────────────────────
  const cleanupHtml = (lab.cleanup && lab.cleanup.length) ? `
    <div style="display:flex;flex-direction:column;gap:8px;">
      ${lab.cleanup.map((s,i) => `<div style="display:flex;gap:12px;font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-secondary);padding:10px 14px;background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);"><span style="color:var(--gfs-text-muted);font-family:var(--gfs-font-mono);flex-shrink:0;">${i+1}.</span>${s}</div>`).join('')}
    </div>` : buildLabPendingBlock('Cleanup steps');

  // ── Enterprise Reflection ───────────────────────────────────────
  const reflectionHtml = `
    <div class="lab-reflection-card">
      <div style="font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-primary);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:20px;">Enterprise Reflection</div>
      <div style="display:flex;flex-direction:column;gap:16px;">
        <div>
          <div class="lab-reflection-q">1. What happened during this exercise? Summarize the key findings.</div>
          <textarea class="lab-reflection-input" placeholder="Your response..."></textarea>
        </div>
        <div>
          <div class="lab-reflection-q">2. Why did this vulnerability or scenario occur? What was the root cause?</div>
          <textarea class="lab-reflection-input" placeholder="Your response..."></textarea>
        </div>
        <div>
          <div class="lab-reflection-q">3. How would this be handled in a production enterprise environment? What controls would you recommend?</div>
          <textarea class="lab-reflection-input" placeholder="Your response..."></textarea>
        </div>
      </div>
    </div>`;

  // ── Assemble ────────────────────────────────────────────────────
  return `<div style="padding:0 0 60px 0; max-width:960px; margin:0 auto;">
    ${headerHtml}
    <div style="display:flex;flex-direction:column;gap:40px;">
      ${buildLabSection('1. Business Scenario', scenarioHtml)}
      ${buildLabSection('2. Learning Objectives', objectivesHtml)}
      ${buildLabSection('3. Safety Notice', safetyHtml)}
      ${buildLabSection('4. Lab Tasks', stepsHtml)}
      ${buildLabSection('5. Evidence Collection', evidenceHtml)}
      ${buildLabSection('6. Validation', validationHtml)}
      ${buildLabSection('7. Troubleshooting', troubleshootingHtml)}
      ${mitreSectionHtml ? buildLabSection('8. MITRE ATT&CK Mapping', mitreSectionHtml) : ''}
      ${buildLabSection('9. Cleanup', cleanupHtml)}
      ${buildLabSection('10. Enterprise Reflection', reflectionHtml)}
    </div>
  </div>`;
}"""

if old_lab_fn in content:
    content = content.replace(old_lab_fn, new_lab_fn)
    print("Lab Engine: buildLabHTML replaced successfully.")
else:
    print("ERROR: old_lab_fn did not match — checking first 100 chars of expected vs file...")
    idx = content.find('function buildLabHTML(d){')
    if idx >= 0:
        print(f"Found buildLabHTML at char {idx}")
        print(repr(content[idx:idx+100]))
    else:
        print("buildLabHTML function NOT found in file.")

# ─── 3. UPDATE toggleLabStep to sync status badge ─────────────────────────────
old_toggle = """function toggleLabStep(el){
  const check=el.querySelector('.lab-check');
  if(!check) return;
  const done=check.style.opacity==='1';
  check.style.opacity=done?'0':'1';
  el.style.background=done?'':'rgba(0,200,83,0.06)';
}"""

new_toggle = """function toggleLabStep(el){
  el.classList.toggle('done');
  const check = el.querySelector('.lab-check');
  if(check) check.style.opacity = el.classList.contains('done') ? '1' : '0';

  // Update lab status badge based on step completion
  const container = el.closest('[id$="-steps"]');
  if(!container) return;
  const total = container.querySelectorAll('.lab-step').length;
  const done  = container.querySelectorAll('.lab-step.done').length;
  const labId = container.id.replace('-steps', '');
  const badge = document.getElementById(labId + '-status');
  if(!badge) return;
  if(done === 0)          { badge.textContent = 'Not Started'; badge.style.color = 'var(--gfs-text-muted)'; }
  else if(done < total)   { badge.textContent = 'In Progress';  badge.style.color = 'var(--gfs-warning)'; }
  else                    { badge.textContent = 'Completed';    badge.style.color = 'var(--gfs-success)'; }
}"""

if old_toggle in content:
    content = content.replace(old_toggle, new_toggle)
    print("Lab Engine: toggleLabStep updated successfully.")
else:
    print("WARNING: toggleLabStep not found — skipping.")

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Sprint 2.3 Lab Engine applied.")
