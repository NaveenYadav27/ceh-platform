-- CEHv13 AI Platform Database Schema

-- Users table
CREATE TABLE IF NOT EXISTS users (
  id            SERIAL PRIMARY KEY,
  email         VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role          VARCHAR(50) DEFAULT 'student' CHECK (role IN ('admin','mentor','student')),
  created_at    TIMESTAMP DEFAULT NOW()
);

-- User aggregate progress
CREATE TABLE IF NOT EXISTS user_progress (
  user_id          INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  total_xp         INTEGER DEFAULT 0,
  topics_completed INTEGER DEFAULT 0,
  flags_captured   INTEGER DEFAULT 0,
  updated_at       TIMESTAMP DEFAULT NOW()
);

-- Per-topic completion records
CREATE TABLE IF NOT EXISTS topic_completions (
  id            SERIAL PRIMARY KEY,
  user_id       INTEGER REFERENCES users(id) ON DELETE CASCADE,
  topic_id      VARCHAR(100) NOT NULL,
  xp_earned     INTEGER DEFAULT 0,
  flag_captured BOOLEAN DEFAULT FALSE,
  completed_at  TIMESTAMP DEFAULT NOW(),
  UNIQUE (user_id, topic_id)
);

-- Seed default admin user
-- Password: Shadowxlab@1234
INSERT INTO users (email, password_hash, role) VALUES
  ('nkyadav@shadowxlab.com', '$2b$10$IMhpLcQuFId10RGWqQAHi.AcfX5IVDYGcB4nl6BI13NXA9xWtGn2.', 'admin')
ON CONFLICT (email) DO NOTHING;
