#!/bin/bash
# ============================================================
# CEHv13 AI Platform — One-Shot Server Installer
# Run this directly on your Proxmox VM terminal as cehmaster
# ============================================================
set -e

INSTALL_DIR="/home/cehmaster/ceh-platform"
echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║   ShadowXLab CEH v13 AI Platform — Installer        ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# ── 1. Create directories ────────────────────────────────────
echo "[1/6] Creating project structure..."
mkdir -p $INSTALL_DIR/backend
mkdir -p $INSTALL_DIR/frontend

# ── 2. Write init.sql ────────────────────────────────────────
echo "[2/6] Writing database schema..."
cat > $INSTALL_DIR/init.sql << 'SQLEOF'
CREATE TABLE IF NOT EXISTS users (
  id            SERIAL PRIMARY KEY,
  email         VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role          VARCHAR(50) DEFAULT 'student' CHECK (role IN ('admin','mentor','student')),
  created_at    TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS user_progress (
  user_id          INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  total_xp         INTEGER DEFAULT 0,
  topics_completed INTEGER DEFAULT 0,
  flags_captured   INTEGER DEFAULT 0,
  updated_at       TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS topic_completions (
  id            SERIAL PRIMARY KEY,
  user_id       INTEGER REFERENCES users(id) ON DELETE CASCADE,
  topic_id      VARCHAR(100) NOT NULL,
  xp_earned     INTEGER DEFAULT 0,
  flag_captured BOOLEAN DEFAULT FALSE,
  completed_at  TIMESTAMP DEFAULT NOW(),
  UNIQUE (user_id, topic_id)
);

-- Default admin: nkyadav@shadowxlab.com / Shadowxlab@1234
INSERT INTO users (email, password_hash, role) VALUES
  ('nkyadav@shadowxlab.com', '$2b$10$Y5DGdE/fPXCcEYmALbJt4.a7wQvDLdSEiEajq6K0bGY5nkWpQgC1C', 'admin')
ON CONFLICT (email) DO NOTHING;
SQLEOF

# ── 3. Write docker-compose.yml ──────────────────────────────
echo "[3/6] Writing docker-compose.yml..."
cat > $INSTALL_DIR/docker-compose.yml << 'DCEOF'
version: '3.8'
services:
  db:
    image: postgres:15-alpine
    container_name: ceh_db
    environment:
      POSTGRES_USER: cehadmin
      POSTGRES_PASSWORD: cehpassword123
      POSTGRES_DB: cehdb
    ports:
      - "5433:5432"
    volumes:
      - cehpgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

  backend:
    build: ./backend
    container_name: ceh_backend
    ports:
      - "3001:3000"
    environment:
      - DB_HOST=db
      - DB_USER=cehadmin
      - DB_PASSWORD=cehpassword123
      - DB_NAME=cehdb
      - JWT_SECRET=ShadowXLabCEHSuperSecretKey2026
    depends_on:
      - db
    volumes:
      - ./frontend:/usr/src/app/public

volumes:
  cehpgdata:
DCEOF

# ── 4. Write backend files ───────────────────────────────────
echo "[4/6] Writing backend..."

cat > $INSTALL_DIR/backend/package.json << 'PKGEOF'
{
  "name": "ceh-backend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": { "start": "node server.js" },
  "dependencies": {
    "bcryptjs": "^2.4.3",
    "cors": "^2.8.5",
    "express": "^4.18.2",
    "jsonwebtoken": "^9.0.0",
    "pg": "^8.11.0"
  }
}
PKGEOF

cat > $INSTALL_DIR/backend/Dockerfile << 'DFEOF'
FROM node:18-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
DFEOF

cat > $INSTALL_DIR/backend/server.js << 'SRVEOF'
const express = require('express');
const { Pool } = require('pg');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));

const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  user: process.env.DB_USER || 'cehadmin',
  password: process.env.DB_PASSWORD || 'cehpassword123',
  database: process.env.DB_NAME || 'cehdb',
  port: 5432,
});

const JWT_SECRET = process.env.JWT_SECRET || 'CEHSecretKey2026';

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

app.post('/api/login', async (req, res) => {
  const { email, password } = req.body;
  try {
    const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
    if (result.rows.length === 0) return res.status(404).json({ error: 'User not found' });
    const user = result.rows[0];
    const valid = await bcrypt.compare(password, user.password_hash);
    if (!valid) return res.status(401).json({ error: 'Invalid password' });
    const token = jwt.sign({ id: user.id, role: user.role }, JWT_SECRET, { expiresIn: '24h' });
    res.json({ auth: true, token, role: user.role, email: user.email });
  } catch (err) { res.status(500).json({ error: 'Internal server error' }); }
});

app.get('/api/me', verifyToken, async (req, res) => {
  try {
    const result = await pool.query('SELECT id, email, role FROM users WHERE id = $1', [req.userId]);
    res.json(result.rows[0]);
  } catch (err) { res.status(500).json({ error: 'Internal server error' }); }
});

app.get('/api/users', [verifyToken, isAdmin], async (req, res) => {
  try {
    const result = await pool.query('SELECT u.id, u.email, u.role, u.created_at, COALESCE(p.total_xp,0) as total_xp FROM users u LEFT JOIN user_progress p ON p.user_id=u.id ORDER BY u.created_at DESC');
    res.json(result.rows);
  } catch (err) { res.status(500).json({ error: 'Internal server error' }); }
});

app.post('/api/users', [verifyToken, isAdmin], async (req, res) => {
  const { email, password, role } = req.body;
  try {
    const hash = await bcrypt.hash(password, 10);
    const result = await pool.query('INSERT INTO users (email, password_hash, role) VALUES ($1, $2, $3) RETURNING id, email, role', [email, hash, role]);
    res.status(201).json(result.rows[0]);
  } catch (err) { res.status(500).json({ error: 'Error creating user' }); }
});

app.delete('/api/users/:id', [verifyToken, isAdmin], async (req, res) => {
  const { id } = req.params;
  if (parseInt(id) === req.userId) return res.status(400).json({ error: 'Cannot delete yourself' });
  try {
    await pool.query('DELETE FROM users WHERE id = $1', [id]);
    res.json({ success: true });
  } catch (err) { res.status(500).json({ error: 'Internal server error' }); }
});

app.post('/api/ctf/submit', verifyToken, async (req, res) => {
  const { topic_id, flag } = req.body;
  const flags = {
    'info-security-overview': 'CEH{1nf0_s3cur1ty_b4s3l1n3}',
    'hacker-classes': 'CEH{wh1t3_gr3y_bl4ck_h4t}',
    'ethical-hacking-concepts': 'CEH{3th1c4l_h4ck3r_m4nd4t3}',
    'hacking-methodologies': 'CEH{r3c0n_sc4n_g41n_m41nt41n}',
    'security-controls': 'CEH{d3f3ns3_1n_d3pth_p0l1cy}',
    'security-laws': 'CEH{c0mpl14nc3_1s_k3y_2026}',
  };
  const correct = flags[topic_id];
  if (!correct) return res.json({ correct: false, message: '❌ Unknown topic flag.' });
  if (flag && flag.trim().toUpperCase() === correct.toUpperCase()) {
    res.json({ correct: true, message: '🚩 Flag captured! +150 XP', xp: 150 });
  } else {
    res.json({ correct: false, message: '❌ Incorrect flag. Keep trying!' });
  }
});

app.get('/api/admin/stats', [verifyToken, isAdmin], async (req, res) => {
  try {
    const users = await pool.query('SELECT COUNT(*) FROM users');
    res.json({ total_users: parseInt(users.rows[0].count) });
  } catch (err) { res.status(500).json({ error: 'Internal server error' }); }
});

app.get('*', (req, res) => res.sendFile(path.join(__dirname, 'public', 'index.html')));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`CEH Platform running on port ${PORT}`));
SRVEOF

# ── 5. Build and start Docker ────────────────────────────────
echo "[5/6] Building and starting Docker containers..."
cd $INSTALL_DIR
sudo docker compose down 2>/dev/null || true
sudo docker compose up -d --build

echo ""
echo "⏳ Waiting 15 seconds for containers to initialize..."
sleep 15

# ── 6. Configure Nginx ───────────────────────────────────────
echo "[6/6] Configuring Nginx for ceh.shadowxlab.com..."

sudo tee /etc/nginx/sites-available/ceh > /dev/null << 'NGINXEOF'
server {
    listen 80;
    server_name ceh.shadowxlab.com;
    location / {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_cache_bypass $http_upgrade;
    }
}
NGINXEOF

sudo ln -sf /etc/nginx/sites-available/ceh /etc/nginx/sites-enabled/ceh
sudo nginx -t && sudo systemctl reload nginx

# ── Health check ─────────────────────────────────────────────
echo ""
echo "🔍 Health check..."
sleep 3
HTTP=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3001/ 2>/dev/null || echo "failed")
echo "   Backend HTTP status: $HTTP"

CONTAINERS=$(sudo docker compose ps --format "table {{.Name}}\t{{.Status}}" 2>/dev/null)
echo "$CONTAINERS"

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║   ✅ CEH v13 Platform Deployed!                      ║"
echo "║                                                      ║"
echo "║   Local:  http://localhost:3001                      ║"
echo "║   Domain: http://ceh.shadowxlab.com                  ║"
echo "║                                                      ║"
echo "║   Login:  nkyadav@shadowxlab.com                     ║"
echo "║   Pass:   Shadowxlab@1234                            ║"
echo "║                                                      ║"
echo "║   Next: Add Cloudflare Tunnel route for              ║"
echo "║   ceh.shadowxlab.com → localhost:3001                ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""
