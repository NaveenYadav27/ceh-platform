import re

def upgrade(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # --- 1. CSS INJECTION ---
    css = """
/* ── NEW CYBERPUNK REFERENCE STYLES ── */
:root {
  --cyber-deep: #1e1e2f;
  --cyber-panel: #2a2a40;
  --cyber-blue: #00BFFF;
  --cyber-cyan: #00E5FF;
  --cyber-red: #FF3B30;
  --cyber-ember: #FF8C00;
  --cyber-gold: #FFC857;
}
.cyber-grid {
  background-image:
    linear-gradient(rgba(0,229,255,0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,229,255,0.1) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse 70% 60% at 50% 40%, #000 30%, transparent 80%);
  -webkit-mask-image: radial-gradient(ellipse 70% 60% at 50% 40%, #000 30%, transparent 80%);
}
.glass-panel {
  background: linear-gradient(135deg, rgba(42,42,64,0.8), rgba(30,30,47,0.6));
  backdrop-filter: blur(14px);
  border: 1px solid rgba(0,229,255,0.22);
  box-shadow: 0 0 0 1px rgba(0,229,255,0.08) inset, 0 20px 60px -20px rgba(0,191,255,0.3);
}
.glass-panel-red {
  background: linear-gradient(135deg, rgba(42,42,64,0.8), rgba(30,30,47,0.6));
  backdrop-filter: blur(14px);
  border: 1px solid rgba(255,59,48,0.3);
  box-shadow: 0 0 0 1px rgba(255,59,48,0.1) inset, 0 20px 60px -20px rgba(255,59,48,0.3);
}
.neon-text-cyan { color: var(--cyber-cyan); text-shadow: 0 0 12px rgba(0,229,255,0.7); }
.neon-text-red { color: var(--cyber-red); text-shadow: 0 0 12px rgba(255,59,48,0.7); }

.btn-cyber {
  position: relative;
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  padding: 0.85rem 1.6rem; font-family: var(--font); font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase; font-size: 0.78rem;
  color: #fff; background: linear-gradient(135deg, rgba(0,191,255,0.3), rgba(0,229,255,0.18));
  border: 1px solid rgba(0,229,255,0.6); cursor: pointer;
  clip-path: polygon(8px 0, 100% 0, 100% calc(100% - 8px), calc(100% - 8px) 100%, 0 100%, 0 8px);
  transition: all 0.25s ease; box-shadow: 0 0 24px -6px rgba(0,229,255,0.6);
}
.btn-cyber:hover { transform: translateY(-2px); box-shadow: 0 0 36px -4px var(--cyber-cyan); }
.btn-cyber-red {
  background: linear-gradient(135deg, rgba(255,59,48,0.35), rgba(255,140,0,0.22));
  border-color: rgba(255,59,48,0.7); box-shadow: 0 0 24px -6px rgba(255,59,48,0.6);
}
.btn-cyber-red:hover { box-shadow: 0 0 36px -4px var(--cyber-red); }
.btn-cyber-ghost { background: transparent; border-color: rgba(0,229,255,0.35); box-shadow: none; }
.btn-cyber-ghost:hover { background: rgba(0,229,255,0.1); }

.scan-line::after {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(180deg, transparent, rgba(0,229,255,0.18), transparent);
  animation: scan 3.5s linear infinite; pointer-events: none;
}
@keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
@keyframes pulse-glow { 0%, 100% { opacity: 0.6; } 50% { opacity: 1; } }
.pulse-glow { animation: pulse-glow 2.4s ease-in-out infinite; }
@keyframes float-y { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
.float-y { animation: float-y 5s ease-in-out infinite; }

.corner-frame { position: relative; padding: 12px; }
.corner-frame::before, .corner-frame::after { content: ""; position: absolute; width: 14px; height: 14px; border: 1px solid var(--cyber-cyan); }
.corner-frame::before { top: -1px; left: -1px; border-right: 0; border-bottom: 0; }
.corner-frame::after { bottom: -1px; right: -1px; border-left: 0; border-top: 0; box-shadow: 0 0 8px var(--cyber-red); border-color: var(--cyber-red); }

#landing-page { position: fixed; inset: 0; z-index: 100; overflow-y: auto; background: var(--bg); display: flex; flex-direction: column; }
.nav-bar { position: fixed; top: 0; width: 100%; z-index: 101; padding: 12px; }
.nav-inner { display: flex; align-items: center; justify-content: space-between; padding: 10px 24px; border-radius: 12px; margin: 0 auto; max-width: 1280px; }
.nav-links { display: flex; gap: 28px; }
.nav-link { font-family: var(--mono); font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 2px; cursor: pointer; transition: color 0.2s; }
.nav-link:hover { color: var(--cyber-cyan); }
.hero-section { position: relative; flex: 1; display: flex; align-items: center; padding: 120px 24px 60px; max-width: 1280px; margin: 0 auto; width: 100%; }
.hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; width: 100%; align-items: center; }
@media(max-width: 900px) { .hero-grid { grid-template-columns: 1fr; } }
"""
    # Inject CSS
    html = html.replace('</style>', css + '\n</style>')

    # --- 2. HTML INJECTION (Landing Page) ---
    landing_html = """
<div id="landing-page">
  <div class="cyber-grid" style="position:absolute;inset:0;"></div>
  
  <div class="nav-bar">
    <div class="nav-inner glass-panel">
      <div style="color:var(--cyber-cyan);font-weight:700;font-size:1.4rem;letter-spacing:1px;display:flex;align-items:center;gap:10px;">
        <span style="color:var(--cyber-red);">X</span> SHADOWXLAB
      </div>
      <div class="nav-links">
        <span class="nav-link">Cyber Range</span>
        <span class="nav-link">Modules</span>
        <span class="nav-link">Labs</span>
        <span class="nav-link">AI Ops</span>
        <span class="nav-link">SOC</span>
      </div>
      <div style="display:flex;gap:12px;">
        <button class="btn-cyber btn-cyber-ghost" onclick="showLogin()">Login</button>
        <button class="btn-cyber" onclick="showLogin()">Enroll</button>
      </div>
    </div>
  </div>

  <div class="hero-section">
    <div class="hero-grid">
      <!-- LEFT -->
      <div>
        <div style="display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(0,229,255,0.4);background:rgba(0,229,255,0.1);border-radius:20px;margin-bottom:24px;">
          <span class="pulse-glow" style="width:6px;height:6px;background:var(--cyber-red);border-radius:50%;"></span>
          <span style="font-family:var(--mono);font-size:0.65rem;color:var(--cyber-cyan);letter-spacing:3px;">CLASSIFIED // OPERATIONAL</span>
        </div>
        <h1 style="font-size:4rem;line-height:1;font-weight:900;margin-bottom:24px;letter-spacing:-1px;">
          CEH v13<br/>
          <span class="neon-text-cyan">AI POWERED</span><br/>
          ETHICAL <span class="neon-text-red">HACKING</span>
        </h1>
        <p style="color:var(--text-dim);font-size:1.1rem;line-height:1.6;margin-bottom:32px;max-width:500px;">
          Train inside a real-world AI-powered cyber range with enterprise-grade labs, Red Team attack simulations, SOC integrations, cloud exploitation, Active Directory attacks, AI threat hunting, and browser-based hacking environments.
        </p>
        <div style="display:flex;gap:16px;margin-bottom:40px;">
          <button class="btn-cyber" onclick="showLogin()">Launch Cyber Range</button>
          <button class="btn-cyber btn-cyber-red" onclick="showLogin()">Explore Labs</button>
        </div>
        <div style="display:flex;gap:24px;">
          <div class="corner-frame"><div class="neon-text-cyan" style="font-size:1.8rem;font-weight:700;">12.5K+</div><div style="font-family:var(--mono);font-size:0.6rem;color:var(--text-muted);letter-spacing:2px;text-transform:uppercase;">Operators Trained</div></div>
          <div class="corner-frame"><div class="neon-text-cyan" style="font-size:1.8rem;font-weight:700;">246+</div><div style="font-family:var(--mono);font-size:0.6rem;color:var(--text-muted);letter-spacing:2px;text-transform:uppercase;">Live Labs</div></div>
          <div class="corner-frame"><div class="neon-text-cyan" style="font-size:1.8rem;font-weight:700;">99.9%</div><div style="font-family:var(--mono);font-size:0.6rem;color:var(--text-muted);letter-spacing:2px;text-transform:uppercase;">Range Uptime</div></div>
        </div>
      </div>
      
      <!-- RIGHT -->
      <div style="position:relative;">
        <div class="glass-panel scan-line" style="border-radius:12px;padding:20px;position:relative;overflow:hidden;">
          <div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(0,229,255,0.2);padding-bottom:12px;margin-bottom:16px;">
            <div style="display:flex;gap:8px;align-items:center;">
              <span style="width:10px;height:10px;background:var(--cyber-red);border-radius:50%;"></span>
              <span style="width:10px;height:10px;background:var(--cyber-ember);border-radius:50%;"></span>
              <span style="width:10px;height:10px;background:var(--cyber-cyan);border-radius:50%;"></span>
              <span style="font-family:var(--mono);font-size:0.6rem;color:var(--text-muted);letter-spacing:2px;margin-left:12px;">shadowx://ops/cyber-range/session-0xA31F</span>
            </div>
            <span class="pulse-glow" style="color:var(--cyber-cyan);font-family:var(--mono);font-size:0.6rem;">● REC</span>
          </div>
          
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
            <!-- Terminal -->
            <div style="grid-column:1/-1;background:rgba(0,0,0,0.6);border:1px solid rgba(0,229,255,0.2);border-radius:8px;padding:12px;min-height:220px;font-family:var(--mono);font-size:0.75rem;">
              <div style="color:var(--cyber-cyan);margin-bottom:8px;font-size:0.65rem;">> KALI@SHADOWX — LIVE SESSION</div>
              <div id="mock-terminal-feed" style="line-height:1.6;"></div>
              <div style="color:var(--cyber-cyan);">$ <span class="pulse-glow">▌</span></div>
            </div>
            
            <!-- Alerts -->
            <div style="background:rgba(30,30,47,0.6);border:1px solid rgba(0,229,255,0.2);border-radius:8px;padding:12px;">
              <div style="color:var(--cyber-cyan);font-family:var(--mono);font-size:0.65rem;margin-bottom:12px;display:flex;justify-content:space-between;"><span>SIEM ALERTS</span><span style="color:var(--cyber-red);">16 CRIT</span></div>
              <div id="siem-alerts-feed" style="display:flex;flex-direction:column;gap:8px;"></div>
            </div>
            
            <!-- AI SOC -->
            <div style="background:rgba(30,30,47,0.6);border:1px solid rgba(255,59,48,0.3);border-radius:8px;padding:12px;">
              <div style="color:var(--cyber-red);font-family:var(--mono);font-size:0.65rem;margin-bottom:12px;">AI SOC</div>
              <div style="margin-bottom:8px;">
                <div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:0.55rem;color:var(--text-muted);margin-bottom:4px;"><span>Threat Score</span><span style="color:var(--cyber-red);">95%</span></div>
                <div style="height:4px;background:rgba(0,0,0,0.5);border-radius:4px;overflow:hidden;"><div style="height:100%;width:95%;background:var(--cyber-red);box-shadow:0 0 8px var(--cyber-red);"></div></div>
              </div>
              <div style="margin-bottom:8px;">
                <div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:0.55rem;color:var(--text-muted);margin-bottom:4px;"><span>Detection</span><span style="color:var(--cyber-cyan);">87%</span></div>
                <div style="height:4px;background:rgba(0,0,0,0.5);border-radius:4px;overflow:hidden;"><div style="height:100%;width:87%;background:var(--cyber-cyan);box-shadow:0 0 8px var(--cyber-cyan);"></div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
"""
    # Inject landing page right after <body>
    html = html.replace('<body>', '<body>\n' + landing_html)

    # --- 3. ADMIN PANEL INJECTION ---
    admin_html = """
      <!-- ADMIN DASHBOARD -->
      <div class="lms-dash" id="admin-panel" style="display:none;">
        <div class="lms-hero" style="background:linear-gradient(135deg, rgba(255,59,92,0.1), rgba(0,0,0,0));border-color:rgba(255,59,92,0.3);">
          <div class="lms-hero-left">
            <div style="color:var(--red);font-family:var(--mono);font-size:0.75rem;margin-bottom:8px;letter-spacing:2px;">shadowx://admin/console</div>
            <h1 style="color:#fff;">Admin Console</h1>
            <p>Cohort telemetry and access control panel.</p>
          </div>
          <div class="lms-stats">
            <div class="lms-stat"><div class="lms-stat-val" id="admin-tot-ops">0</div><div class="lms-stat-lbl">Operators</div></div>
            <div class="lms-stat"><div class="lms-stat-val" id="admin-tot-xp" style="color:var(--cyan)">0</div><div class="lms-stat-lbl">Total XP Mined</div></div>
          </div>
        </div>
        
        <h2 style="font-family:var(--font);font-size:1.5rem;margin-bottom:16px;">Operators Database</h2>
        <div class="glass-panel" style="border-radius:12px;overflow:hidden;">
          <table style="width:100%;text-align:left;border-collapse:collapse;font-size:0.85rem;">
            <thead style="background:rgba(0,255,136,0.1);font-family:var(--mono);font-size:0.65rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px;">
              <tr><th style="padding:16px;">Operator</th><th style="padding:16px;">Role</th><th style="padding:16px;">XP</th><th style="padding:16px;">Topics</th><th style="padding:16px;">Joined</th></tr>
            </thead>
            <tbody id="admin-users-list">
              <!-- Users populated here -->
            </tbody>
          </table>
        </div>
      </div>
"""
    # Inject admin-panel after welcome-screen inside #content-area
    html = html.replace('<div class="lms-dash" id="welcome-screen">', admin_html + '\n      <div class="lms-dash" id="welcome-screen">')

    # --- 4. TOPBAR ADMIN BUTTON & LOGIC ---
    # Add an admin button to the topbar that is hidden by default
    html = html.replace('<button class="logout-btn" onclick="doLogout()">LOGOUT</button>', '<button id="btn-admin-nav" class="btn-cyber btn-cyber-ghost" style="display:none;padding:6px 12px;font-size:0.65rem;" onclick="showAdminPanel()">ADMIN</button>\n        <button class="logout-btn" onclick="doLogout()">LOGOUT</button>')

    # Update bootApp to hide landing page and show Admin button if superadmin
    js_bootApp = """
function bootApp(email, role){
  document.getElementById('landing-page').style.display = 'none';
  document.getElementById('ceh-login-overlay').style.display = 'none';
  document.getElementById('ceh-app').style.display = 'flex';
  document.getElementById('user-email').textContent = email;
  if(role === 'admin' || role === 'superadmin'){
    document.getElementById('btn-admin-nav').style.display = 'inline-flex';
  }
  updateProgress();
}
"""
    # Replace bootApp
    html = re.sub(r'function bootApp\(email\)\{.*?(?=\nfunction renderLMSDashboard)', js_bootApp.strip(), html, flags=re.DOTALL)

    # Change how auth handles role
    html = html.replace('bootApp(email);', 'bootApp(email, res.role);')
    html = html.replace("const role=localStorage.getItem('ceh_role');\n  if(!token){", "const role=localStorage.getItem('ceh_role');\n  if(!token){ document.getElementById('landing-page').style.display = 'flex'; document.getElementById('ceh-app').style.display = 'none'; return;")

    # Add showAdminPanel() logic
    js_admin = """
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
      trs += `<tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:16px;">${u.email}</td><td style="padding:16px;">${roleHtml}</td><td style="padding:16px;color:var(--green);font-family:var(--mono);">${u.total_xp || 0}</td><td style="padding:16px;">${u.topics_completed || 0}</td><td style="padding:16px;color:var(--text-muted);font-size:0.7rem;">${new Date(u.created_at).toLocaleDateString()}</td></tr>`;
    });
    
    document.getElementById('admin-tot-xp').textContent = totalXp;
    document.getElementById('admin-users-list').innerHTML = trs;
  } catch(e) {
    console.error(e);
  }
}
"""
    html = html.replace('// ── TAB WIRING ──', js_admin + '\n// ── TAB WIRING ──')

    # Add terminal animation scripts
    js_anim = """
const SCRIPT = [
  { c: "var(--cyber-cyan)", t: "$ nmap -sS -A 10.10.42.0/24 --script vuln" },
  { c: "var(--text-muted)", t: "Starting Nmap 7.94 ( https://nmap.org )" },
  { c: "#fff", t: "Host 10.10.42.17 up (0.0021s latency)" },
  { c: "var(--cyber-red)", t: "[!] VULN: CVE-2024-38063 — KERBEROS RCE detected" },
  { c: "var(--cyber-ember)", t: "[+] Suggested chain: kerberoast → DCSync → golden-ticket" },
  { c: "var(--cyber-cyan)", t: "$ bloodhound-python -d corp.shadowx.lab -c All" },
  { c: "#fff", t: "INFO: Found 312 users, 47 groups, 18 computers" },
  { c: "var(--cyber-cyan)", t: "$ impacket-GetUserSPNs corp.shadowx.lab/operator" },
];
const ALERTS = [
  { sev: "CRIT", t: "Lateral movement", c: "var(--cyber-red)" },
  { sev: "HIGH", t: "Kerberoast attempt", c: "var(--cyber-ember)" },
  { sev: "MED",  t: "Anomalous DNS", c: "var(--cyber-cyan)" },
  { sev: "CRIT", t: "C2 beacon detected", c: "var(--cyber-red)" }
];

let termIdx = 0;
setInterval(() => {
  const el = document.getElementById('mock-terminal-feed');
  if(!el) return;
  el.innerHTML += `<div style="color:${SCRIPT[termIdx].c}">${SCRIPT[termIdx].t}</div>`;
  termIdx++;
  if(termIdx >= SCRIPT.length) { termIdx = 0; el.innerHTML = ''; }
}, 1200);

setInterval(() => {
  const el = document.getElementById('siem-alerts-feed');
  if(!el) return;
  const a = ALERTS[Math.floor(Math.random() * ALERTS.length)];
  el.innerHTML = `<div style="display:flex;justify-content:space-between;background:rgba(0,0,0,0.4);padding:4px 8px;border-radius:4px;font-family:var(--mono);font-size:0.6rem;animation:pulse-glow 1s;"><span style="color:${a.c}">${a.sev}</span><span style="color:#fff">${a.t}</span></div>` + el.innerHTML;
  if(el.children.length > 4) el.lastChild.remove();
}, 2500);
"""
    html = html.replace('// ── TERMINAL ──', js_anim + '\n// ── TERMINAL ──')
    
    # Finally, make sure #ceh-app is hidden by default
    html = html.replace('<div id="ceh-app">', '<div id="ceh-app" style="display:none;">')
    # Actually wait, in CSS I had `#ceh-app{...display:flex}`. I will update the CSS:
    html = html.replace('#ceh-app{position:fixed;inset:0;z-index:1;display:flex;flex-direction:column;}', '#ceh-app{position:fixed;inset:0;z-index:1;display:none;flex-direction:column;}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Native Landing Page and Admin Panel injected successfully.")

upgrade('frontend/index.html')
