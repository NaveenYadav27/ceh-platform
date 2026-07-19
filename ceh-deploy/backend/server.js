const express = require('express');
const { Pool } = require('pg');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const path = require('path');

const app = express();

// Security Headers
app.use(helmet({
  contentSecurityPolicy: false // Disabled to allow inline scripts/styles for the LMS
}));

app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));

// Rate Limiting
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 10, // Limit each IP to 10 requests per window
  message: { error: 'Too many login attempts, please try again later' }
});

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100 // 100 API requests per 15 minutes
});


const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  user: process.env.DB_USER || 'cehadmin',
  password: process.env.DB_PASSWORD || 'cehpassword123',
  database: process.env.DB_NAME || 'cehdb',
  port: 5432,
});

const JWT_SECRET = process.env.JWT_SECRET || 'CEHSecretKey2026';

// ── Middleware ──────────────────────────────────────────────────────────────
const verifyToken = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token) return res.status(403).json({ error: 'No token provided' });
  jwt.verify(token.split(' ')[1], JWT_SECRET, (err, decoded) => {
    if (err) return res.status(401).json({ error: 'Unauthorized' });
    req.userId = decoded.id;
    req.userRole = decoded.role;
    next();
  });
};

const isAdmin = (req, res, next) => {
  if (req.userRole !== 'admin') return res.status(403).json({ error: 'Requires admin role' });
  next();
};

// ── Auth Routes ─────────────────────────────────────────────────────────────
app.post('/api/login', authLimiter, async (req, res) => {
  const { email, password } = req.body;
  try {
    const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
    if (result.rows.length === 0) return res.status(404).json({ error: 'User not found' });
    const user = result.rows[0];
    const valid = await bcrypt.compare(password, user.password_hash);
    if (!valid) return res.status(401).json({ error: 'Invalid password' });
    const token = jwt.sign({ id: user.id, role: user.role }, JWT_SECRET, { expiresIn: '24h' });
    res.json({ auth: true, token, role: user.role, email: user.email });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/me', verifyToken, async (req, res) => {
  try {
    const result = await pool.query('SELECT id, email, role FROM users WHERE id = $1', [req.userId]);
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// ── User Management (Admin) ─────────────────────────────────────────────────
app.get('/api/users', [verifyToken, isAdmin], async (req, res) => {
  try {
    const result = await pool.query(`
      SELECT u.id, u.email, u.role, u.created_at,
        COALESCE(p.total_xp, 0) as total_xp,
        COALESCE(p.topics_completed, 0) as topics_completed
      FROM users u
      LEFT JOIN user_progress p ON p.user_id = u.id
      ORDER BY u.created_at DESC
    `);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/users', [verifyToken, isAdmin], async (req, res) => {
  const { email, password, role } = req.body;
  try {
    const hash = await bcrypt.hash(password, 10);
    const result = await pool.query(
      'INSERT INTO users (email, password_hash, role) VALUES ($1, $2, $3) RETURNING id, email, role',
      [email, hash, role]
    );
    res.status(201).json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: 'Error creating user' });
  }
});

app.delete('/api/users/:id', [verifyToken, isAdmin], async (req, res) => {
  const { id } = req.params;
  if (parseInt(id) === req.userId) return res.status(400).json({ error: 'Cannot delete yourself' });
  try {
    await pool.query('DELETE FROM users WHERE id = $1', [id]);
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// ── XP & Progress Routes ────────────────────────────────────────────────────
app.get('/api/progress', verifyToken, async (req, res) => {
  try {
    const result = await pool.query(
      'SELECT * FROM user_progress WHERE user_id = $1',
      [req.userId]
    );
    if (result.rows.length === 0) {
      return res.json({ total_xp: 0, topics_completed: 0, flags_captured: 0, completed_topics: [] });
    }
    const prog = result.rows[0];
    const topics = await pool.query(
      'SELECT topic_id, xp_earned, flag_captured FROM topic_completions WHERE user_id = $1',
      [req.userId]
    );
    res.json({
      total_xp: prog.total_xp,
      topics_completed: prog.topics_completed,
      flags_captured: prog.flags_captured,
      completed_topics: topics.rows
    });
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/progress/topic', verifyToken, async (req, res) => {
  const { topic_id, xp_earned, flag_captured } = req.body;
  try {
    // Upsert topic completion
    await pool.query(`
      INSERT INTO topic_completions (user_id, topic_id, xp_earned, flag_captured)
      VALUES ($1, $2, $3, $4)
      ON CONFLICT (user_id, topic_id) DO UPDATE
      SET xp_earned = GREATEST(topic_completions.xp_earned, $3),
          flag_captured = topic_completions.flag_captured OR $4,
          completed_at = NOW()
    `, [req.userId, topic_id, xp_earned || 0, flag_captured || false]);

    // Recalculate totals
    const totals = await pool.query(`
      SELECT SUM(xp_earned) as total_xp,
             COUNT(*) as topics_completed,
             SUM(CASE WHEN flag_captured THEN 1 ELSE 0 END) as flags_captured
      FROM topic_completions WHERE user_id = $1
    `, [req.userId]);

    const t = totals.rows[0];
    await pool.query(`
      INSERT INTO user_progress (user_id, total_xp, topics_completed, flags_captured)
      VALUES ($1, $2, $3, $4)
      ON CONFLICT (user_id) DO UPDATE
      SET total_xp = $2, topics_completed = $3, flags_captured = $4, updated_at = NOW()
    `, [req.userId, t.total_xp, t.topics_completed, t.flags_captured]);

    res.json({ success: true, total_xp: parseInt(t.total_xp), topics_completed: parseInt(t.topics_completed) });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// ── CTF Flag Submission ─────────────────────────────────────────────────────
app.post('/api/ctf/submit', [verifyToken, apiLimiter], async (req, res) => {
  const { topic_id, flag } = req.body;

  // All 90 topic CTF flags — Module 01-20
  const knownFlags = {
    // Module 01
    'info-security-overview':       'CEH{1nf0_s3cur1ty_b4s3l1n3}',
    'hacker-classes':               'CEH{wh1t3_gr3y_bl4ck_h4t}',
    'ethical-hacking-concepts':     'CEH{3th1c4l_h4ck3r_m4nd4t3}',
    'hacking-methodologies':        'CEH{r3c0n_sc4n_g41n_m41nt41n}',
    'security-controls':            'CEH{d3f3ns3_1n_d3pth_p0l1cy}',
    'security-laws':                'CEH{c0mpl14nc3_1s_k3y_2026}',
    // Module 02
    'footprinting-concepts':        'CEH{f00tpr1nt_c0nc3pts_2026}',
    'osint-techniques':             'CEH{0s1nt_m4st3r_t3chn1qu3s}',
    'whois-dns':                    'CEH{wh01s_dns_r3c0n_2026}',
    'google-hacking':               'CEH{g00gl3_d0rk_m4st3r_2026}',
    'shodan-recon':                 'CEH{sh0d4n_10t_r3c0n_2026}',
    'social-media-recon':           'CEH{s0c14l_m3d14_0s1nt_2026}',
    // Module 03
    'network-scanning-overview':    'CEH{n3tw0rk_sc4n_0v3rv13w}',
    'tcp-ip-scanning':              'CEH{tcp_1p_p0rt_sc4nn3r}',
    'nmap-techniques':              'CEH{nm4p_m4st3r_sc4nn3r}',
    'hping3-scanning':              'CEH{hp1ng3_st34lth_sc4n}',
    'banner-grabbing':              'CEH{b4nn3r_gr4bb1ng_0sf1ng}',
    // Module 04
    'enumeration-overview':         'CEH{3num3r4t10n_c0nc3pts}',
    'netbios-smb':                  'CEH{n3tb10s_smb_3num3r8}',
    'snmp-ldap':                    'CEH{snmp_ld4p_3xp0s3d}',
    'smtp-dns-enum':                'CEH{smtp_dns_3num3r4t10n}',
    // Module 05
    'vuln-concepts':                'CEH{vuln_4ss3ssm3nt_c0r3}',
    'cve-cvss':                     'CEH{cv3_cvss_nvd_2026}',
    'nessus-openvas':               'CEH{n3ssus_0p3nv4s_sc4n}',
    // Module 06
    'password-cracking':            'CEH{p4ssw0rd_cr4ck1ng_2026}',
    'privilege-escalation':         'CEH{pr1v_3sc_r00t_2026}',
    'maintaining-access':           'CEH{m41nt41n_4cc3ss_r00tk1t}',
    'steganography':                'CEH{st3g0_c0v3r_tr4cks}',
    // Module 07
    'malware-concepts':             'CEH{m4lw4r3_typ3s_2026}',
    'trojans-rats':                 'CEH{tr0j4n_r4t_c2_2026}',
    'ransomware-apts':              'CEH{r4ns0mw4r3_4pt_2026}',
    'fileless-malware':             'CEH{f1l3l3ss_m4lw4r3_2026}',
    // Module 08
    'sniffing-concepts':            'CEH{sn1ff1ng_c0nc3pts_2026}',
    'arp-mac-attacks':              'CEH{4rp_m4c_fl00d_2026}',
    'mitm-attacks':                 'CEH{m1tm_4tt4ck_2026}',
    'wireshark-analysis':           'CEH{w1r3sh4rk_4n4lys1s}',
    // Module 09
    'social-eng-concepts':          'CEH{s0c14l_3ng_c0nc3pts}',
    'phishing-vishing':             'CEH{ph1sh1ng_v1sh1ng_2026}',
    'insider-threats':              'CEH{1ns1d3r_thr34t_2026}',
    // Module 10
    'dos-concepts':                 'CEH{d0s_ddos_c0nc3pts}',
    'botnet-attacks':               'CEH{b0tn3t_4mpl1f1c4t10n}',
    'syn-flood':                    'CEH{syn_fl00d_v0lum3tr1c}',
    // Module 11
    'session-concepts':             'CEH{s3ss10n_h1j4ck_c0r3}',
    'tcp-hijacking':                'CEH{tcp_s3ss10n_h1j4ck}',
    'cookie-theft-xss':             'CEH{c00k13_th3ft_xss}',
    // Module 12
    'ids-evasion':                  'CEH{1ds_1ps_3v4s10n}',
    'firewall-bypass':              'CEH{f1r3w4ll_w4f_byp4ss}',
    'tunneling-obfuscation':        'CEH{tunn3l1ng_0bfusc4t10n}',
    // Module 13
    'web-server-attacks':           'CEH{w3b_s3rv3r_4tt4ck}',
    'directory-traversal':          'CEH{d1r_tr4v3rs4l_sh3ll}',
    // Module 14
    'owasp-top10':                  'CEH{0w4sp_t0p_10_2026}',
    'xss-csrf':                     'CEH{xss_csrf_1d0r_2026}',
    'web-app-methodology':          'CEH{w3b_4pp_m3th0d0l0gy}',
    // Module 15
    'sqli-concepts':                'CEH{sql1_c0nc3pts_2026}',
    'sqli-techniques':              'CEH{bl1nd_t1m3_sql1_2026}',
    'sqlmap':                       'CEH{sqlm4p_4ut0m4t3d}',
    // Module 16
    'wireless-concepts':            'CEH{w1r3l3ss_c0nc3pts}',
    'wpa2-cracking':                'CEH{wp42_3v1l_tw1n_2026}',
    'aircrack-suite':               'CEH{41rcr4ck_ng_su1t3}',
    // Module 17
    'mobile-threats':               'CEH{m0b1l3_thr34ts_2026}',
    'android-hacking':              'CEH{4ndr01d_h4ck1ng_2026}',
    'ios-hacking':                  'CEH{10s_h4ck1ng_2026}',
    // Module 18
    'iot-concepts':                 'CEH{10t_4tt4ck_surf4c3}',
    'scada-ot':                     'CEH{sc4d4_0t_s3cur1ty}',
    'mqtt-protocols':               'CEH{mqtt_1ndustr14l_pr0t}',
    // Module 19
    'cloud-concepts':               'CEH{cl0ud_s3cur1ty_c0r3}',
    'aws-misconfigs':               'CEH{4ws_4zur3_m1sc0nf1g}',
    'iam-abuse':                    'CEH{14m_4bus3_s3_buck3t}',
    // Module 20
    'crypto-concepts':              'CEH{crypt0_c0nc3pts_2026}',
    'pki-certificates':             'CEH{pk1_d1g1t4l_c3rts}',
    'crypto-attacks':               'CEH{crypt0_4tt4cks_2026}',
  };


  const correctFlag = knownFlags[topic_id];
  if (!correctFlag) return res.status(404).json({ error: 'Unknown topic', correct: false });

  if (flag.trim().toUpperCase() === correctFlag.toUpperCase()) {
    res.json({ correct: true, message: '🚩 Flag captured! +150 XP', xp: 150 });
  } else {
    res.json({ correct: false, message: '❌ Incorrect flag. Keep trying!' });
  }
});

// ── Admin Stats ──────────────────────────────────────────────────────────────
app.get('/api/admin/stats', [verifyToken, isAdmin], async (req, res) => {
  try {
    const users = await pool.query('SELECT COUNT(*) FROM users');
    const completions = await pool.query('SELECT COUNT(*) FROM topic_completions');
    const flags = await pool.query('SELECT COUNT(*) FROM topic_completions WHERE flag_captured = true');
    const topUsers = await pool.query(`
      SELECT u.email, p.total_xp, p.topics_completed, p.flags_captured
      FROM users u JOIN user_progress p ON p.user_id = u.id
      ORDER BY p.total_xp DESC LIMIT 5
    `);
    res.json({
      total_users: parseInt(users.rows[0].count),
      total_completions: parseInt(completions.rows[0].count),
      total_flags: parseInt(flags.rows[0].count),
      top_users: topUsers.rows
    });
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// ── Fallback ────────────────────────────────────────────────────────────────
app.use((req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.min.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`CEH Platform Backend running on port ${PORT}`));
