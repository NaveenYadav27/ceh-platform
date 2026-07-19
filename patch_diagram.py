import re

with open('frontend/index.min.html', encoding='utf8') as f:
    content = f.read()

old_func_regex = r'function buildDiagramHTML\(d\)\{\s*if\(!d\.diagram\|\|!d\.diagram\.steps\|\|!d\.diagram\.steps\.length\)\s*return buildComingSoonHTML.*?\}'

new_func = r"""function buildDiagramHTML(d){
  if(d.diagram && d.diagram.svg) {
    return `<div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
      <div style="font-size:1rem;font-weight:700;color:var(--blue);margin-bottom:24px;font-family:var(--mono);">${d.diagram.title||'Architecture & Flow'}</div>
      <div class="diagram-svg-container" style="text-align:center;">
        ${d.diagram.svg}
      </div>
      ${d.diagram.caption ? `<div style="text-align:center;color:var(--text-muted);font-size:0.85rem;margin-top:16px;">${d.diagram.caption}</div>` : ''}
    </div>`;
  }
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
}"""

content = re.sub(old_func_regex, lambda _: new_func, content, flags=re.DOTALL)

with open('frontend/index.min.html', 'w', encoding='utf8') as f:
    f.write(content)

with open('frontend/index.html', encoding='utf8') as f:
    content_html = f.read()
    
content_html = re.sub(old_func_regex, lambda _: new_func, content_html, flags=re.DOTALL)
with open('frontend/index.html', 'w', encoding='utf8') as f:
    f.write(content_html)
