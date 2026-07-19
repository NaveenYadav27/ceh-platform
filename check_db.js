const {Client} = require('ssh2'); 
const conn = new Client(); 
conn.on('ready', () => { 
  conn.exec('docker logs --tail 50 ceh_backend', (err, stream) => { 
    if (err) throw err; 
    stream.on('close', () => { conn.end(); })
          .on('data', (data) => { console.log(data.toString()); })
          .stderr.on('data', (data) => { console.error(data.toString()); }); 
  }); 
}).connect({host: '100.91.75.27', port: 22, username: 'cehmaster', password: 'Shadowxlab@1705'});
