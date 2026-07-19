const { Pool } = require('pg');

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'ceh_db',
  password: 'password',
  port: 5433, // Exposed port
});

async function alterDb() {
  try {
    console.log('Adding role column...');
    await pool.query(`ALTER TABLE users ADD COLUMN IF NOT EXISTS role VARCHAR(50) DEFAULT 'operator'`);
    
    console.log('Updating superadmin...');
    await pool.query(`UPDATE users SET role = 'superadmin' WHERE email = 'nkyadav@shadowxlab.com'`);
    
    console.log('Database updated successfully.');
  } catch (err) {
    console.error('Error updating DB:', err);
  } finally {
    pool.end();
  }
}

alterDb();
