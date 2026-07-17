const { Client } = require('ssh2');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const SSH = {
  host: '100.91.75.27',
  username: 'cehmaster',
  password: 'Shadowxlab@1705',
  readyTimeout: 30000
};

const LOCAL_DIR = path.join(__dirname);
const REMOTE_DIR = '/home/cehmaster/ceh-platform';

function exec(conn, cmd, label) {
  return new Promise((resolve, reject) => {
    console.log(`  ▶ ${label || cmd}`);
    conn.exec(cmd, (err, stream) => {
      if (err) return reject(err);
      let out = '';
      stream.on('data', d => out += d);
      stream.stderr.on('data', d => out += d);
      stream.on('close', () => { console.log(out.trim() ? `    ${out.trim()}` : ''); resolve(out.trim()); });
    });
  });
}

function uploadDir(sftp, localDir, remoteDir) {
  return new Promise(async (resolve, reject) => {
    try {
      // Create remote dir
      await new Promise(r => sftp.mkdir(remoteDir, () => r()));
      
      const items = fs.readdirSync(localDir);
      for (const item of items) {
        if (item === 'node_modules' || item === '.git') continue;
        const localPath = path.join(localDir, item);
        const remotePath = `${remoteDir}/${item}`;
        const stat = fs.statSync(localPath);
        
        if (stat.isDirectory()) {
          await uploadDir(sftp, localPath, remotePath);
        } else {
          await new Promise((res, rej) => {
            sftp.fastPut(localPath, remotePath, err => err ? rej(err) : res());
          });
          console.log(`    ✅ ${item}`);
        }
      }
      resolve();
    } catch (err) { reject(err); }
  });
}

function getSftp(conn) {
  return new Promise((resolve, reject) => {
    conn.sftp((err, sftp) => err ? reject(err) : resolve(sftp));
  });
}

const conn = new Client();

conn.on('ready', async () => {
  console.log('\n✅ SSH Connected to cehmaster server\n');
  try {
    const sftp = await getSftp(conn);

    console.log('📁 Creating remote directory...');
    await exec(conn, `mkdir -p ${REMOTE_DIR}`, 'mkdir ceh-platform');

    console.log('\n📤 Uploading project files...');
    await uploadDir(sftp, LOCAL_DIR, REMOTE_DIR);
    console.log('✅ All files uploaded!\n');

    console.log('🐳 Building & starting Docker containers...');
    const build = await exec(conn,
      `cd ${REMOTE_DIR} && echo 'Shadowxlab@1705' | sudo -S docker compose up -d --build 2>&1`,
      'docker compose up -d --build'
    );
    console.log(build);

    console.log('\n⏳ Waiting 10s for containers to start...');
    await new Promise(r => setTimeout(r, 10000));

    console.log('🔍 Checking container health...');
    const ps = await exec(conn, `echo 'Shadowxlab@1705' | sudo -S docker compose -f ${REMOTE_DIR}/docker-compose.yml ps 2>&1`, 'docker ps');
    console.log(ps);

    const curl = await exec(conn, `curl -s -o /dev/null -w "HTTP %{http_code}" http://localhost:3001/`, 'curl health check');
    console.log('\nHealth check:', curl);

    console.log('\n🌐 Configuring Nginx for ceh.shadowxlab.com...');
    const nginxConf = `server {
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
}`;
    
    // Write nginx config
    await exec(conn, `cat > /home/cehmaster/ceh.nginx.conf << 'NGINXEOF'\n${nginxConf}\nNGINXEOF`, 'write nginx config');
    await exec(conn, `echo 'Shadowxlab@1705' | sudo -S cp /home/cehmaster/ceh.nginx.conf /etc/nginx/sites-available/ceh`, 'install nginx config');
    await exec(conn, `echo 'Shadowxlab@1705' | sudo -S ln -sf /etc/nginx/sites-available/ceh /etc/nginx/sites-enabled/ceh`, 'enable site');
    
    const nginxTest = await exec(conn, `echo 'Shadowxlab@1705' | sudo -S nginx -t 2>&1`, 'nginx test');
    console.log(nginxTest);
    
    if (nginxTest.includes('test is successful')) {
      await exec(conn, `echo 'Shadowxlab@1705' | sudo -S systemctl reload nginx`, 'reload nginx');
      console.log('\n✅ Nginx configured and reloaded!');
    }

    console.log('\n🎉 ==========================================');
    console.log('   CEHv13 Platform is LIVE!');
    console.log('   URL: http://ceh.shadowxlab.com');
    console.log('   Local: http://100.91.75.27:3001');
    console.log('==========================================\n');
    
    console.log('Next: Add Cloudflare Tunnel route for ceh.shadowxlab.com → localhost:3001');

  } catch (err) {
    console.error('❌ Deployment failed:', err.message);
  } finally {
    conn.end();
  }
});

conn.on('error', err => console.error('❌ SSH error:', err.message));
conn.connect(SSH);
