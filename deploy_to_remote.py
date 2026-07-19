import os
import paramiko

hostname = '100.91.75.27'
port = 22
username = 'cehmaster'
password = 'Shadowxlab@1705'

tmp_remote_dir = '/tmp/ceh-frontend'
final_remote_dir = '/home/cehmaster/Shadowxlab-projects/ceh-platform/ceh-deploy/frontend'
local_base_dir = 'frontend'

def mkdir_p(sftp, remote_directory):
    if remote_directory == '/':
        sftp.chdir('/')
        return
    if remote_directory == '':
        return
    try:
        sftp.chdir(remote_directory)
    except IOError:
        dirname, basename = os.path.split(remote_directory.rstrip('/'))
        mkdir_p(sftp, dirname)
        sftp.mkdir(basename)
        sftp.chdir(basename)
        return True

def sftp_upload_dir(sftp, local_dir, remote_dir):
    mkdir_p(sftp, remote_dir)
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        remote_path = f"{remote_dir}/{item}"

        if os.path.isfile(local_path):
            print(f"Uploading {local_path} to {remote_path}...")
            sftp.put(local_path, remote_path)
        elif os.path.isdir(local_path):
            sftp_upload_dir(sftp, local_path, remote_path)

def execute(ssh, command):
    print(f"Executing: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.write(password + '\n')
    stdin.flush()
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode()
    err = stderr.read().decode()
    if out: print(f"STDOUT: {out}")
    if err: print(f"STDERR: {err}")
    return exit_status

def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print(f"Connecting to {hostname}...")
    try:
        ssh.connect(hostname, port, username, password)
        print("Connected!")
        
        # Clean tmp
        execute(ssh, f'rm -rf {tmp_remote_dir}')
        
        sftp = ssh.open_sftp()
        print("Starting upload of frontend directory to /tmp...")
        sftp_upload_dir(sftp, local_base_dir, tmp_remote_dir)
        print("Upload complete.")
        sftp.close()
        
        # Move to final destination
        print("Moving to final destination using sudo...")
        execute(ssh, f'sudo -S rm -rf {final_remote_dir}')
        execute(ssh, f'sudo -S cp -r {tmp_remote_dir} {final_remote_dir}')
        execute(ssh, f'sudo -S chown -R $USER:$USER {final_remote_dir}')
        
        # Now restart the containers
        print("Restarting docker containers...")
        execute(ssh, f'cd ~/Shadowxlab-projects/ceh-platform/ceh-deploy && sudo -S docker compose restart')
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    main()
