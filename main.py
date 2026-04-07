import os
import getpass

def main():
    username = os.environ.get('SUDO_USER', getpass.getuser())
    user_home = os.path.expanduser(f"~{username}")
    
    bashrc_path = os.path.join(user_home, ".bashrc")
    
    if os.path.exists(bashrc_path):
        try:
            with open(bashrc_path, "r") as f:
                print(f.read())
        except Exception as e:
            print(f"Error reading {bashrc_path}: {e}")
    else:
        print(f"No .bashrc file found at {bashrc_path}.")

if __name__ == "__main__":
    main()