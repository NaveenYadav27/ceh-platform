import re

def fix_auth(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update doLogin
    old_login = """
    if(r.ok && data.token){
      localStorage.setItem('ceh_token',data.token);
      localStorage.setItem('ceh_email',data.email);
      errEl.style.display='none';
      bootApp(data.email);
    }
"""
    new_login = """
    if(r.ok && data.token){
      localStorage.setItem('ceh_token',data.token);
      localStorage.setItem('ceh_email',data.email);
      localStorage.setItem('ceh_role',data.role);
      errEl.style.display='none';
      bootApp(data.email, data.role);
    }
"""
    html = html.replace(old_login.strip(), new_login.strip())

    # 2. Update checkAuth
    old_checkAuth = """
async function checkAuth(){
  const token = localStorage.getItem('ceh_token');
  if(!token){ showLogin(); return; }
  try {
    const r = await fetch('/api/me',{headers:{Authorization:'Bearer '+token}});
    if(r.ok){ const u=await r.json(); bootApp(u.email); }
    else { localStorage.removeItem('ceh_token'); showLogin(); }
  } catch(e){ bootApp(localStorage.getItem('ceh_email')||'operator'); }
}
"""
    new_checkAuth = """
async function checkAuth(){
  const token = localStorage.getItem('ceh_token');
  if(!token){ 
    document.getElementById('landing-page').style.display = 'flex'; 
    document.getElementById('ceh-app').style.display = 'none'; 
    return; 
  }
  try {
    const r = await fetch('/api/me',{headers:{Authorization:'Bearer '+token}});
    if(r.ok){ const u=await r.json(); bootApp(u.email, u.role); }
    else { localStorage.removeItem('ceh_token'); localStorage.removeItem('ceh_role'); document.getElementById('landing-page').style.display = 'flex'; }
  } catch(e){ bootApp(localStorage.getItem('ceh_email')||'operator', localStorage.getItem('ceh_role')||'operator'); }
}
"""
    html = html.replace(old_checkAuth.strip(), new_checkAuth.strip())

    # 3. Update bootApp
    old_bootApp = """
function bootApp(email){
  document.getElementById('ceh-login-overlay').style.display='none';
  document.getElementById('ceh-app').style.display='flex';
  document.getElementById('user-email-display').textContent = email;
  renderSidebar();
  updateTopbar();
  initParticles();
}
"""
    new_bootApp = """
function bootApp(email, role){
  document.getElementById('landing-page').style.display = 'none';
  document.getElementById('ceh-login-overlay').style.display='none';
  document.getElementById('ceh-app').style.display='flex';
  if(document.getElementById('user-email-display')) document.getElementById('user-email-display').textContent = email;
  if(document.getElementById('user-email')) document.getElementById('user-email').textContent = email;
  
  if(role === 'admin' || role === 'superadmin'){
    if(document.getElementById('btn-admin-nav')) document.getElementById('btn-admin-nav').style.display = 'inline-flex';
  }
  
  renderSidebar();
  updateTopbar();
  initParticles();
  if(typeof renderLMSDashboard === 'function') renderLMSDashboard();
}
"""
    html = html.replace(old_bootApp.strip(), new_bootApp.strip())
    
    # 4. Hide landing page function
    html = html.replace("function doLogout(){", "function doLogout(){ localStorage.removeItem('ceh_role'); ")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Auth flow fixed.")

fix_auth('frontend/index.html')
