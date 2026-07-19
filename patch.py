import re

with open('frontend/index.min.html', encoding='utf8') as f:
    content = f.read()

# Instead of complex regex, let's just do text replacement
# The bug is in buildCommandsHTML where it maps c => ... c.replace(...) ... ${c}

old_win = """${cmds.win&&cmds.win.length?cmds.win.map(c=>`<div class="cmd-line clickable-cmd" onclick="runCommand('win', '${c.replace(/'/g,"\\'").replace(/"/g,'&quot;')}')">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Windows commands.</div>'}"""

new_win = """${cmds.win&&cmds.win.length?cmds.win.map(c=>{let s=typeof c==='string'?c:(c.cmd||'');return `<div class="cmd-line clickable-cmd" onclick="runCommand('win', '${s.replace(/'/g,"\\'").replace(/"/g,'&quot;')}')">${s}</div>`}).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Windows commands.</div>'}"""

old_lin = """${cmds.lin&&cmds.lin.length?cmds.lin.map(c=>`<div class="cmd-line clickable-cmd" onclick="runCommand('lin', '${c.replace(/'/g,"\\'").replace(/"/g,'&quot;')}')">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Linux commands.</div>'}"""

new_lin = """${cmds.lin&&cmds.lin.length?cmds.lin.map(c=>{let s=typeof c==='string'?c:(c.cmd||'');return `<div class="cmd-line clickable-cmd" onclick="runCommand('lin', '${s.replace(/'/g,"\\'").replace(/"/g,'&quot;')}')">${s}</div>`}).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Linux commands.</div>'}"""

if old_win in content:
    content = content.replace(old_win, new_win)
    print("Patched win commands!")
else:
    print("Could not find old_win")

if old_lin in content:
    content = content.replace(old_lin, new_lin)
    print("Patched lin commands!")
else:
    print("Could not find old_lin")

with open('frontend/index.min.html', 'w', encoding='utf8') as f:
    f.write(content)
