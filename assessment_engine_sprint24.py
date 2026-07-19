with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. EXTEND QUIZ/ASSESSMENT CSS ───────────────────────────────────────────
old_quiz_css = """/* ── QUIZ TAB ── */
.quiz-q{background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:20px;margin-bottom:14px;}
.quiz-q-text{font-size:0.9rem;font-weight:600;margin-bottom:14px;line-height:1.5;}
.quiz-q-num{font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-success);margin-bottom:6px;letter-spacing:1px;}
.quiz-opts{display:flex;flex-direction:column;gap:8px;}
.quiz-opt{background:rgba(0,0,0,0.3);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:10px 14px;cursor:pointer;font-size:0.85rem;transition:all .2s;text-align:left;}
.quiz-opt:hover:not([disabled]){border-color:var(--gfs-info);background:var(--gfs-info-dim);}
.quiz-opt.correct{border-color:var(--gfs-success);background:var(--gfs-success-dim);color:var(--gfs-success);}
.quiz-opt.wrong{border-color:var(--gfs-danger);background:var(--gfs-danger-dim);color:var(--gfs-danger);}
.quiz-fb{margin-top:10px;padding:10px 14px;background:rgba(0,0,0,0.3);border-left:3px solid var(--gfs-success);border-radius:0 var(--gfs-radius) var(--gfs-radius) 0;font-size:0.82rem;color:var(--gfs-text-secondary);display:none;line-height:1.6;}
.quiz-score{text-align:center;font-family:var(--gfs-font-mono);font-size:0.85rem;color:var(--gfs-success);margin-bottom:16px;padding:10px;background:var(--gfs-success-dim);border-radius:var(--gfs-radius);}"""

new_quiz_css = """/* ── ENTERPRISE ASSESSMENT ENGINE ── */

/* Question Card */
.quiz-q{background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:24px;margin-bottom:16px;transition:var(--gfs-transition);}
.quiz-q.answered{border-color:rgba(255,255,255,0.15);}
.quiz-q-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;}
.quiz-q-num{font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-primary);letter-spacing:1px;}
.quiz-q-type-badge{font-family:var(--gfs-font-mono);font-size:0.6rem;padding:3px 8px;border-radius:20px;border:1px solid var(--gfs-border);color:var(--gfs-text-muted);text-transform:uppercase;}
.quiz-q-meta{display:flex;gap:16px;margin-bottom:14px;}
.quiz-q-diff{font-family:var(--gfs-font-mono);font-size:0.7rem;}
.quiz-q-text{font-family:var(--gfs-font-body);font-size:0.95rem;font-weight:600;margin-bottom:16px;line-height:1.6;color:var(--gfs-text-primary);}

/* Answer Options */
.quiz-opts{display:flex;flex-direction:column;gap:8px;}
.quiz-opt{background:rgba(0,0,0,0.3);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:12px 16px;cursor:pointer;font-size:0.88rem;transition:var(--gfs-transition);text-align:left;color:var(--gfs-text-secondary);display:flex;align-items:center;gap:12px;}
.quiz-opt::before{content:attr(data-letter);width:24px;height:24px;border-radius:50%;border:1px solid var(--gfs-border);display:flex;align-items:center;justify-content:center;font-family:var(--gfs-font-mono);font-size:0.7rem;flex-shrink:0;transition:var(--gfs-transition);}
.quiz-opt:hover:not([disabled]){border-color:var(--gfs-primary);background:var(--gfs-primary-dim);color:var(--gfs-text-primary);}
.quiz-opt:hover:not([disabled])::before{border-color:var(--gfs-primary);color:var(--gfs-primary);}
.quiz-opt.correct{border-color:var(--gfs-success);background:var(--gfs-success-dim);color:var(--gfs-success);}
.quiz-opt.correct::before{border-color:var(--gfs-success);background:var(--gfs-success);color:#000;}
.quiz-opt.wrong{border-color:var(--gfs-danger);background:var(--gfs-danger-dim);color:var(--gfs-danger);}
.quiz-opt.wrong::before{border-color:var(--gfs-danger);background:var(--gfs-danger);color:#fff;}
.quiz-opt.selected-wrong{border-color:var(--gfs-danger);background:var(--gfs-danger-dim);color:var(--gfs-danger);}

/* True/False Options */
.quiz-tf-opts{display:flex;gap:12px;}
.quiz-tf-opt{flex:1;padding:14px;border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);cursor:pointer;text-align:center;font-family:var(--gfs-font-display);font-weight:600;font-size:1rem;transition:var(--gfs-transition);background:rgba(0,0,0,0.3);}
.quiz-tf-opt:hover:not([disabled]){border-color:var(--gfs-primary);}
.quiz-tf-opt[data-val="true"]{color:var(--gfs-success);}
.quiz-tf-opt[data-val="false"]{color:var(--gfs-danger);}
.quiz-tf-opt.correct{background:var(--gfs-success-dim);border-color:var(--gfs-success);}
.quiz-tf-opt.wrong{background:var(--gfs-danger-dim);border-color:var(--gfs-danger);}

/* Explanation Panel */
.quiz-fb{margin-top:14px;padding:14px 18px;background:rgba(0,0,0,0.3);border-left:3px solid var(--gfs-primary);border-radius:0 var(--gfs-radius) var(--gfs-radius) 0;font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-secondary);display:none;line-height:1.6;}
.quiz-fb .fb-label{font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-primary);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;}
.quiz-fb.correct-fb{border-left-color:var(--gfs-success);}
.quiz-fb.correct-fb .fb-label{color:var(--gfs-success);}
.quiz-fb.wrong-fb{border-left-color:var(--gfs-danger);}
.quiz-fb.wrong-fb .fb-label{color:var(--gfs-danger);}

/* Score Summary */
.quiz-score{font-family:var(--gfs-font-mono);font-size:0.85rem;color:var(--gfs-success);margin-bottom:16px;padding:16px 20px;background:var(--gfs-success-dim);border:1px solid var(--gfs-success);border-radius:var(--gfs-radius);display:flex;justify-content:space-between;align-items:center;}

/* Assessment Header */
.assessment-header{background:var(--gfs-bg-panel);border:1px solid var(--gfs-border);border-radius:var(--gfs-radius);padding:24px;margin-bottom:28px;}
.assessment-type-badge{display:inline-block;font-family:var(--gfs-font-mono);font-size:0.7rem;padding:4px 12px;border-radius:20px;border:1px solid var(--gfs-primary);color:var(--gfs-primary);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:12px;}
.assessment-instructions{font-family:var(--gfs-font-body);font-size:0.9rem;color:var(--gfs-text-secondary);line-height:1.6;}

/* Recommendation Card */
.recommendation-card{background:var(--gfs-bg-panel);border:1px solid var(--gfs-primary);border-radius:var(--gfs-radius);padding:20px;margin-top:16px;}
.recommendation-header{font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-primary);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:10px;}
.recommendation-item{font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-secondary);padding:6px 0;display:flex;gap:10px;align-items:flex-start;}"""

content = content.replace(old_quiz_css, new_quiz_css)
print("CSS replaced:", "QUIZ TAB" not in content)

# ─── 2. REWRITE buildAssessmentHTML + buildQuizHTML ────────────────────────────
old_assess_fn = """function buildAssessmentHTML(d){
  return `
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--gfs-font-mono);font-size:0.72rem;color:var(--gfs-text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 1 OF 3 — KNOWLEDGE CHECK</div>
    <div class="quiz-score" id="quiz-score" style="display:none;"></div>
    ${buildQuizHTML(d)}
  </div>
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--gfs-font-mono);font-size:0.72rem;color:var(--gfs-text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 2 OF 3 — FLASHCARDS (hover to flip)</div>
    ${buildFlashcardsHTML(d)}
  </div>
  <div>
    <div style="font-family:var(--gfs-font-mono);font-size:0.72rem;color:var(--gfs-text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 3 OF 3 — CAPTURE THE FLAG</div>
    ${buildCTFHTML(d)}
  </div>`;
}"""

new_assess_fn = """/* ── ENTERPRISE ASSESSMENT ENGINE ─────────────────────────────── */

function buildAssessmentHTML(d) {
  const questions = d.quiz || [];
  const hasQuestions = questions.length > 0;
  const hasFlashcards = d.flashcards && d.flashcards.length > 0;

  return `
  <div style="display:flex;flex-direction:column;gap:40px;">

    <!-- Assessment Header -->
    <div class="assessment-header">
      <span class="assessment-type-badge">Knowledge Check</span>
      <h4 style="font-family:var(--gfs-font-display);color:var(--gfs-text-primary);font-size:1.1rem;margin-bottom:8px;">Topic Assessment</h4>
      <div class="assessment-instructions">
        Answer each question and review the explanation before continuing.
        Correct answers are revealed immediately with context to reinforce learning.
      </div>
      <div id="quiz-score" class="quiz-score" style="display:none;margin-top:16px;"></div>
    </div>

    <!-- Questions -->
    <div style="display:flex;flex-direction:column;gap:16px;">
      ${hasQuestions ? buildQuizHTML(d) : buildAssessmentPending()}
    </div>

    <!-- Flashcards -->
    ${hasFlashcards ? `
    <div>
      <h4 style="font-family:var(--gfs-font-display);color:var(--gfs-text-primary);border-bottom:1px solid rgba(255,255,255,0.08);padding-bottom:8px;margin-bottom:20px;font-size:1.1rem;">
        Key Term Flashcards
        <span style="font-family:var(--gfs-font-mono);font-size:0.7rem;color:var(--gfs-text-muted);font-weight:400;margin-left:8px;">hover to reveal</span>
      </h4>
      ${buildFlashcardsHTML(d)}
    </div>` : ''}

    <!-- CTF Challenge -->
    <div>
      <h4 style="font-family:var(--gfs-font-display);color:var(--gfs-text-primary);border-bottom:1px solid rgba(255,255,255,0.08);padding-bottom:8px;margin-bottom:20px;font-size:1.1rem;">Intelligence Challenge</h4>
      ${buildCTFHTML(d)}
    </div>

  </div>`;
}

function buildAssessmentPending() {
  return `<div style="background:var(--gfs-bg-panel);border:1px dashed rgba(255,255,255,0.12);border-radius:var(--gfs-radius);padding:40px;text-align:center;">
    <div style="font-size:2rem;margin-bottom:12px;">📋</div>
    <div style="font-family:var(--gfs-font-display);font-size:1rem;color:var(--gfs-text-primary);margin-bottom:6px;">Assessment Framework Ready</div>
    <div style="font-family:var(--gfs-font-body);font-size:0.88rem;color:var(--gfs-text-muted);line-height:1.6;max-width:380px;margin:0 auto;">Questions will be authored during the Content Completion Sprint (Sprint 3). The Assessment Engine is fully operational.</div>
  </div>`;
}

// -- QUIZ RENDERER (supports: multiple-choice, true-false) --
function buildQuizHTML(d){
  if(!d.quiz || !d.quiz.length) return buildAssessmentPending();
  const letters = ['A','B','C','D','E','F'];
  return d.quiz.map((q, i) => {
    const type = q.type || 'multiple-choice';
    const diffColor = q.difficulty === 'Advanced' ? 'var(--gfs-danger)' : q.difficulty === 'Intermediate' ? 'var(--gfs-warning)' : 'var(--gfs-info)';
    const typeBadge = { 'multiple-choice':'MCQ', 'true-false':'T/F', 'multi-select':'Multi', 'scenario':'Scenario' }[type] || 'MCQ';

    let optsHtml = '';
    if (type === 'true-false') {
      optsHtml = `<div class="quiz-tf-opts">
        <button class="quiz-tf-opt" data-val="true" data-qi="${i}" onclick="answerQuiz(this,${i},'true')">✓ True</button>
        <button class="quiz-tf-opt" data-val="false" data-qi="${i}" onclick="answerQuiz(this,${i},'false')">✗ False</button>
      </div>`;
    } else {
      optsHtml = `<div class="quiz-opts">${(q.opts||[]).map((o,oi)=>`
        <button class="quiz-opt" data-oi="${oi}" data-qi="${i}" data-letter="${letters[oi]}" onclick="answerQuiz(this,${i},${oi})">${o}</button>
      `).join('')}</div>`;
    }

    return `
    <div class="quiz-q" data-qi="${i}" data-correct="${q.correct}" data-type="${type}">
      <div class="quiz-q-header">
        <span class="quiz-q-num">Q ${String(i+1).padStart(2,'0')} / ${d.quiz.length}</span>
        <div style="display:flex;gap:8px;align-items:center;">
          ${q.difficulty ? `<span class="quiz-q-diff" style="color:${diffColor};">● ${q.difficulty}</span>` : ''}
          <span class="quiz-q-type-badge">${typeBadge}</span>
        </div>
      </div>
      <div class="quiz-q-text">${q.q}</div>
      ${optsHtml}
      <div class="quiz-fb">
        <div class="fb-label">Explanation</div>
        ${q.fb || 'Explanation pending.'}
      </div>
    </div>`;
  }).join('');
}"""

if old_assess_fn in content:
    content = content.replace(old_assess_fn, new_assess_fn)
    print("Assessment engine: buildAssessmentHTML + buildQuizHTML replaced.")
else:
    print("ERROR: buildAssessmentHTML not matched. Checking partial...")
    idx = content.find("function buildAssessmentHTML")
    print(f"  Found at char index: {idx}")

# ─── 3. EXTEND wireQuiz TO HANDLE TYPE-AWARE ANSWERS ────────────────────────
old_wire = """function wireQuiz(id, d){
  let score=0, answered=0;
  document.querySelectorAll('.quiz-q').forEach(qEl=>{
    const qi = parseInt(qEl.dataset.qi);
    const correct = parseInt(qEl.dataset.correct);
    qEl.querySelectorAll('.quiz-opt').forEach(opt=>{
      opt.addEventListener('click', ()=>{
        if(qEl.dataset.answered) return;
        qEl.dataset.answered = '1';
        answered++;
        const oi = parseInt(opt.dataset.oi);
        if(oi===correct){ opt.classList.add('correct'); score++; }
        else { opt.classList.add('wrong'); qEl.querySelectorAll('.quiz-opt')[correct].classList.add('correct'); }
        qEl.querySelector('.quiz-fb').style.display = 'block';
        qEl.querySelectorAll('.quiz-opt').forEach(o=>o.setAttribute('disabled',''));
        const total = d.quiz.length;
        const scoreEl = document.getElementById('quiz-score');
        if(scoreEl){ scoreEl.textContent = `Score: ${score} / ${answered} answered`; scoreEl.style.display='block'; }
        if(answered===total && score>=8 && !completed[id]){
          addXP(100, '📝 Quiz Passed!');
          completed[id] = true;
          localStorage.setItem('ceh_completed',JSON.stringify(completed));
          updateProgress();
        }
      });
    });
  });
}

function answerQuiz(el, qi, oi){ el.click(); }"""

new_wire = """function wireQuiz(id, d){
  if(!d || !d.quiz || !d.quiz.length) return;
  let score = 0, answered = 0;
  const total = d.quiz.length;

  document.querySelectorAll('.quiz-q').forEach(qEl => {
    const qi = parseInt(qEl.dataset.qi);
    const qData = d.quiz[qi];
    if(!qData) return;
    const correct = qData.correct;
    const type = qEl.dataset.type || 'multiple-choice';

    const lockQuestion = () => {
      qEl.classList.add('answered');
      qEl.dataset.answered = '1';
      if(type === 'true-false') {
        qEl.querySelectorAll('.quiz-tf-opt').forEach(o => o.setAttribute('disabled',''));
      } else {
        qEl.querySelectorAll('.quiz-opt').forEach(o => o.setAttribute('disabled',''));
      }
      const fb = qEl.querySelector('.quiz-fb');
      if(fb) fb.style.display = 'block';
    };

    const updateScore = (isCorrect) => {
      answered++;
      if(isCorrect) score++;
      const scoreEl = document.getElementById('quiz-score');
      if(scoreEl){
        const pct = Math.round((score/answered)*100);
        scoreEl.innerHTML = `<span>Score: ${score} / ${answered}</span><span style="color:${pct>=80?'var(--gfs-success)':'var(--gfs-warning)'};">${pct}%</span>`;
        scoreEl.style.display = 'flex';
      }
      if(answered === total && score >= Math.ceil(total*0.8) && !completed[id]){
        addXP(100, '📝 Assessment Passed!');
        completed[id] = true;
        localStorage.setItem('ceh_completed', JSON.stringify(completed));
        if(typeof updateProgress === 'function') updateProgress();
      }
    };

    if(type === 'true-false') {
      qEl.querySelectorAll('.quiz-tf-opt').forEach(opt => {
        opt.addEventListener('click', () => {
          if(qEl.dataset.answered) return;
          const val = opt.dataset.val;
          const isCorrect = val === String(correct);
          opt.classList.add(isCorrect ? 'correct' : 'wrong');
          const fb = qEl.querySelector('.quiz-fb');
          if(fb){ fb.classList.add(isCorrect ? 'correct-fb' : 'wrong-fb'); }
          lockQuestion();
          updateScore(isCorrect);
        });
      });
    } else {
      qEl.querySelectorAll('.quiz-opt').forEach(opt => {
        opt.addEventListener('click', () => {
          if(qEl.dataset.answered) return;
          const oi = parseInt(opt.dataset.oi);
          const isCorrect = oi === parseInt(correct);
          opt.classList.add(isCorrect ? 'correct' : 'selected-wrong');
          if(!isCorrect){
            const correctOpt = qEl.querySelectorAll('.quiz-opt')[correct];
            if(correctOpt) correctOpt.classList.add('correct');
          }
          const fb = qEl.querySelector('.quiz-fb');
          if(fb){ fb.classList.add(isCorrect ? 'correct-fb' : 'wrong-fb'); }
          lockQuestion();
          updateScore(isCorrect);
        });
      });
    }
  });
}

function answerQuiz(el, qi, oi){ el.click(); }"""

if old_wire in content:
    content = content.replace(old_wire, new_wire)
    print("wireQuiz: extended successfully.")
else:
    print("WARNING: wireQuiz not matched exactly — skipping.")

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Sprint 2.4 Assessment Engine applied.")
