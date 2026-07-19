import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the CSS :root block
old_root = """:root{
  --bg:#0A0F1E;
  --bg2:#0D1526;
  --panel:rgba(13,21,38,0.85);
  --border:rgba(0,255,136,0.15);
  --border-bright:rgba(0,255,136,0.5);
  --green:#00FF88;
  --green-dim:rgba(0,255,136,0.15);
  --green-glow:0 0 20px rgba(0,255,136,0.35);
  --red:#FF3B5C;
  --red-dim:rgba(255,59,92,0.15);
  --blue:#00AAFF;
  --blue-dim:rgba(0,170,255,0.15);
  --purple:#7B2FBE;
  --purple-dim:rgba(123,47,190,0.15);
  --yellow:#FFD600;
  --text:#E2E8F0;
  --text-muted:#64748B;
  --text-dim:#94A3B8;
  --sidebar-w:270px;
  --topbar-h:56px;
  --radius:8px;
  --font:'Space Grotesk',sans-serif;
  --mono:'IBM Plex Mono',monospace;
}"""

new_root = """:root {
  /* GFS Color Palette - Semantic */
  --gfs-primary: #0EA5B7;
  --gfs-primary-dim: rgba(14, 165, 183, 0.15);
  --gfs-success: #00FF88;
  --gfs-success-dim: rgba(0, 255, 136, 0.15);
  --gfs-success-glow: 0 0 20px rgba(0, 255, 136, 0.35);
  --gfs-warning: #FFD600;
  --gfs-warning-dim: rgba(255, 214, 0, 0.15);
  --gfs-danger: #FF3B5C;
  --gfs-danger-dim: rgba(255, 59, 92, 0.15);
  --gfs-info: #00AAFF;
  --gfs-info-dim: rgba(0, 170, 255, 0.15);

  /* Backgrounds & Panels */
  --gfs-bg-primary: #0A1128;
  --gfs-bg-secondary: #0D1630;
  --gfs-bg-panel: rgba(13, 22, 48, 0.85);
  
  /* Borders & Shadows */
  --gfs-border: rgba(14, 165, 183, 0.2);
  --gfs-border-highlight: rgba(14, 165, 183, 0.5);
  --gfs-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  
  /* Typography Colors */
  --gfs-text-primary: #E2E8F0;
  --gfs-text-secondary: #94A3B8;
  --gfs-text-muted: #64748B;
  
  /* Structural Tokens */
  --gfs-sidebar-w: 270px;
  --gfs-topbar-h: 56px;
  --gfs-radius: 8px;
  --gfs-spacing: 20px;
  --gfs-transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  
  /* Fonts */
  --gfs-font-display: 'Space Grotesk', sans-serif;
  --gfs-font-body: 'Inter', sans-serif;
  --gfs-font-mono: 'IBM Plex Mono', monospace;
}"""

content = content.replace(old_root, new_root)

# 2. Search and replace all var(--old) with var(--new) across the entire file
var_mapping = {
    '--bg': '--gfs-bg-primary',
    '--bg2': '--gfs-bg-secondary',
    '--panel': '--gfs-bg-panel',
    '--border': '--gfs-border',
    '--border-bright': '--gfs-border-highlight',
    '--green': '--gfs-success',
    '--green-dim': '--gfs-success-dim',
    '--green-glow': '--gfs-success-glow',
    '--red': '--gfs-danger',
    '--red-dim': '--gfs-danger-dim',
    '--blue': '--gfs-info',
    '--blue-dim': '--gfs-info-dim',
    '--purple': '--gfs-primary',
    '--purple-dim': '--gfs-primary-dim',
    '--yellow': '--gfs-warning',
    '--text': '--gfs-text-primary',
    '--text-muted': '--gfs-text-muted',
    '--text-dim': '--gfs-text-secondary',
    '--sidebar-w': '--gfs-sidebar-w',
    '--topbar-h': '--gfs-topbar-h',
    '--radius': '--gfs-radius',
    '--font': '--gfs-font-body',
    '--mono': '--gfs-font-mono'
}

for old, new in var_mapping.items():
    content = content.replace(f'var({old})', f'var({new})')

# We need to manually fix headers to use gfs-font-display
content = content.replace("font-family:var(--gfs-font-body);", "font-family:var(--gfs-font-body);")

# 3. Replace Dashboard CSS
old_dash_css = """/* ── LMS DASHBOARD ── */
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
.lms-mod-fill { height:100%; background:var(--green); width:0%; transition:width 0.5s; }"""

new_dash_css = """/* ── ENTERPRISE DASHBOARD ── */
.lms-dash { padding: var(--gfs-spacing); width:100%; max-width:1280px; margin:0 auto; display:flex; flex-direction:column; gap:32px; }

/* KPI Ribbon */
.kpi-ribbon { display:grid; grid-template-columns:repeat(6, 1fr); gap:16px; width:100%; }
.kpi-card { background: var(--gfs-bg-panel); border: 1px solid var(--gfs-border); border-radius: var(--gfs-radius); padding: 16px 20px; display:flex; flex-direction:column; justify-content:center; backdrop-filter: blur(8px); box-shadow: var(--gfs-shadow); transition: var(--gfs-transition); }
.kpi-card:hover { border-color: var(--gfs-border-highlight); transform: translateY(-1px); }
.kpi-val { font-family: var(--gfs-font-display); font-size: 1.6rem; font-weight: 700; color: #fff; line-height:1.2; margin-bottom:4px; }
.kpi-val.highlight { color: var(--gfs-primary); }
.kpi-lbl { font-family: var(--gfs-font-mono); font-size: 0.7rem; color: var(--gfs-text-muted); text-transform: uppercase; letter-spacing: 0.5px; }

/* Modules Grid */
.lms-modules-grid { display:grid; grid-template-columns:repeat(4, 1fr); gap:20px; }
.lms-mod-card { background: var(--gfs-bg-panel); border: 1px solid var(--gfs-border); border-radius: var(--gfs-radius); padding: 24px; cursor:pointer; display:flex; flex-direction:column; gap: 12px; transition: var(--gfs-transition); backdrop-filter: blur(8px); box-shadow: var(--gfs-shadow); }
.lms-mod-card:hover { transform:translateY(-2px); border-color: var(--gfs-primary); box-shadow: 0 4px 20px var(--gfs-primary-dim); }

/* Status Variants */
.lms-mod-card.status-completed { border-color: var(--gfs-success); }
.lms-mod-card.status-completed .status-badge { background: var(--gfs-success-dim); color: var(--gfs-success); border-color: var(--gfs-success); }
.lms-mod-card.status-current { border-color: var(--gfs-primary); box-shadow: 0 0 15px var(--gfs-primary-dim); }
.lms-mod-card.status-current .status-badge { background: var(--gfs-primary-dim); color: var(--gfs-primary); border-color: var(--gfs-primary); }
.lms-mod-card.status-recommended { border-color: var(--gfs-warning); }
.lms-mod-card.status-recommended .status-badge { background: var(--gfs-warning-dim); color: var(--gfs-warning); border-color: var(--gfs-warning); }
.lms-mod-card.status-available .status-badge { background: rgba(255,255,255,0.05); color: var(--gfs-text-secondary); border-color: rgba(255,255,255,0.1); }

/* Card Internals */
.mod-card-header { display:flex; justify-content:space-between; align-items:flex-start; }
.status-badge { font-family: var(--gfs-font-mono); font-size: 0.65rem; padding: 4px 8px; border-radius: 4px; border: 1px solid; text-transform:uppercase; letter-spacing:0.5px; }
.mod-phase-lbl { font-family: var(--gfs-font-mono); font-size: 0.75rem; color: var(--gfs-text-secondary); margin-bottom:4px; display:block; }
.lms-mod-title { font-family: var(--gfs-font-display); font-size:1.15rem; font-weight:600; color: var(--gfs-text-primary); line-height: 1.3; }
.lms-mod-desc { font-family: var(--gfs-font-body); font-size: 0.85rem; color: var(--gfs-text-secondary); line-height: 1.5; flex:1; }
.mod-meta-row { display:flex; justify-content:space-between; font-family: var(--gfs-font-mono); font-size:0.75rem; color: var(--gfs-text-muted); margin-top:8px; }

/* Progress Bar */
.lms-mod-progress-wrap { display:flex; flex-direction:column; gap:6px; margin-top:8px; }
.progress-meta { display:flex; justify-content:space-between; font-family: var(--gfs-font-mono); font-size:0.7rem; color: var(--gfs-text-secondary); }
.lms-mod-progress { height:4px; background:rgba(255,255,255,0.1); border-radius:2px; overflow:hidden; }
.lms-mod-fill { height:100%; background:var(--gfs-primary); width:0%; transition:width 0.5s; }
.lms-mod-card.status-completed .lms-mod-fill { background: var(--gfs-success); }

/* Breakpoints */
@media (max-width: 1279px) {
  .kpi-ribbon { grid-template-columns:repeat(3, 1fr); }
  .lms-modules-grid { grid-template-columns:repeat(3, 1fr); }
}
@media (max-width: 1023px) {
  .lms-modules-grid { grid-template-columns:repeat(2, 1fr); }
}
@media (max-width: 767px) {
  .kpi-ribbon { grid-template-columns:repeat(2, 1fr); }
  .lms-modules-grid { grid-template-columns:1fr; }
  .lms-dash { padding: 16px; }
}"""

content = content.replace(old_dash_css, new_dash_css)

# 4. Replace Welcome HTML Block
old_welcome = """      <div class="lms-dash" id="welcome-screen">
        <div class="lms-hero">
          <div class="lms-hero-left">
            <h1>GLOBAL FINANCIAL SERVICES</h1>
            <p>Welcome to your first day at Global Financial Services. Track your active incidents, execute defensive operations, and master your role as a Cybersecurity Analyst.</p>
          </div>
          <div class="lms-stats">
            <div class="lms-stat"><div class="lms-stat-val" id="dash-xp">0</div><div class="lms-stat-lbl">Total XP</div></div>
            <div class="lms-stat"><div class="lms-stat-val" id="dash-rank">Script Kiddie</div><div class="lms-stat-lbl">Rank</div></div>
          </div>
        </div>
        <div class="lms-modules-grid" id="lms-modules-grid"></div>
      </div>"""

new_welcome = """      <div class="lms-dash" id="welcome-screen">
        
        <div class="kpi-ribbon">
          <div class="kpi-card">
            <div class="kpi-val highlight" id="dash-xp">0</div>
            <div class="kpi-lbl">Total XP</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-val" id="dash-rank">Trainee</div>
            <div class="kpi-lbl">Current Rank</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-val" id="dash-active-phase">01</div>
            <div class="kpi-lbl">Active Phase</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-val" id="dash-overall-prog">0%</div>
            <div class="kpi-lbl">Overall Progress</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-val" id="dash-labs">0 / 20</div>
            <div class="kpi-lbl">Labs Completed</div>
          </div>
          <div class="kpi-card" style="border-color: var(--gfs-primary);">
            <div class="kpi-val" style="font-size:1.1rem; margin-top:8px; color:var(--gfs-text-primary);" id="dash-mission">Awaiting Orders</div>
            <div class="kpi-lbl">Daily Mission</div>
          </div>
        </div>

        <div class="lms-modules-grid" id="lms-modules-grid"></div>
      </div>"""

content = content.replace(old_welcome, new_welcome)

# 5. Replace renderLMSDashboard Javascript
old_render = """function renderLMSDashboard(){
  const grid = document.getElementById('lms-modules-grid');
  if(!grid) return;
  
  let html = '';
  MODULES.forEach((m, i) => {
    let completedCount = 0;
    m.topics.forEach(t => { if(completed[t.id]) completedCount++; });
    const pct = Math.round((completedCount / m.topics.length) * 100);
    
    html += `
      <div class="lms-mod-card" onclick="toggleModule('${m.id}', document.getElementById('mod-hdr-${m.id}'))">
        <div class="lms-mod-num">PHASE ${String(i+1).padStart(2,'0')}</div>
        <div class="lms-mod-title">${m.name}</div>
        <div style="display:flex;justify-content:space-between;font-size:0.75rem;color:var(--text-muted);margin-bottom:6px;font-family:var(--mono);">
          <span>${completedCount} / ${m.topics.length} Tasks</span>
          <span>${pct}%</span>
        </div>
        <div class="lms-mod-progress"><div class="lms-mod-fill" style="width:${pct}%"></div></div>
      </div>
    `;
  });
  grid.innerHTML = html;
  
  document.getElementById('dash-xp').textContent = xp;
  document.getElementById('dash-rank').textContent = getRank(xp).name;
}"""

new_render = """function renderLMSDashboard(){
  const grid = document.getElementById('lms-modules-grid');
  if(!grid) return;
  
  let html = '';
  let activePhaseSet = false;
  let totalTopics = 0;
  let totalCompleted = 0;
  let nextMission = "Complete Trainee Onboarding";

  MODULES.forEach((m, i) => {
    let completedCount = 0;
    m.topics.forEach(t => { 
      totalTopics++;
      if(completed[t.id]) {
        completedCount++; 
        totalCompleted++;
      } else if (!activePhaseSet) {
        nextMission = t.name;
      }
    });
    
    const pct = Math.round((completedCount / m.topics.length) * 100);
    
    // Status Logic
    let statusClass = "status-available";
    let statusBadge = "Available";
    if (pct === 100) {
      statusClass = "status-completed";
      statusBadge = "✓ Completed";
    } else if (completedCount > 0) {
      statusClass = "status-current";
      statusBadge = "In Progress";
      if(!activePhaseSet) {
        document.getElementById('dash-active-phase').textContent = String(i+1).padStart(2,'0');
        activePhaseSet = true;
      }
    } else if (!activePhaseSet) {
      statusClass = "status-recommended";
      statusBadge = "★ Recommended";
      document.getElementById('dash-active-phase').textContent = String(i+1).padStart(2,'0');
      activePhaseSet = true;
    }

    // Split name for badge/title
    const parts = m.name.split(':');
    const phaseLabel = parts[0];
    const moduleTitle = parts.length > 1 ? parts[1].trim() : m.name;
    
    html += `
      <div class="lms-mod-card ${statusClass}" onclick="toggleModule('${m.id}', document.getElementById('mod-hdr-${m.id}'))">
        <div class="mod-card-header">
          <span class="mod-phase-lbl">${phaseLabel.toUpperCase()}</span>
          <span class="status-badge">${statusBadge}</span>
        </div>
        
        <div class="lms-mod-title">${moduleTitle}</div>
        
        <div class="mod-meta-row">
          <span><span style="opacity:0.5;">DUR:</span> ~${m.topics.length * 15}m</span>
          <span><span style="opacity:0.5;">Lvl:</span> ${i < 5 ? 'Entry' : i < 12 ? 'Mid' : 'Adv'}</span>
        </div>
        
        <div class="lms-mod-progress-wrap">
          <div class="progress-meta">
            <span>${completedCount} / ${m.topics.length} Tasks</span>
            <span>${pct}%</span>
          </div>
          <div class="lms-mod-progress"><div class="lms-mod-fill" style="width:${pct}%"></div></div>
        </div>
      </div>
    `;
  });
  grid.innerHTML = html;
  
  // Update KPI Ribbon
  const dashXp = document.getElementById('dash-xp');
  if(dashXp) dashXp.textContent = xp;
  
  const dashRank = document.getElementById('dash-rank');
  if(dashRank) dashRank.textContent = getRank(xp).name;

  const dashProg = document.getElementById('dash-overall-prog');
  if(dashProg) dashProg.textContent = Math.round((totalCompleted / totalTopics) * 100) + '%';
  
  const dashMission = document.getElementById('dash-mission');
  if(dashMission) dashMission.textContent = nextMission.length > 25 ? nextMission.substring(0, 22) + '...' : nextMission;
}"""

content = content.replace(old_render, new_render)

# Add Inter Font to head
if "family=Inter:wght@400;500;600" not in content:
    content = content.replace(
        "family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap",
        "family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap"
    )

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Sprint 2.1 CSS & UI refactor.")
