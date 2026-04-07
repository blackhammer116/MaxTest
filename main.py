import os
import getpass

def main():
    username = os.environ.get('SUDO_USER', getpass.getuser())
    user_home = os.path.expanduser(f"~{username}")
    
    bashrc_path = os.path.join(user_home, ".bashrc")
    
    if os.path.exists(bashrc_path):
        try:
            with open(bashrc_path, "r") as f:
                content = f.read()
                modified_content = content.replace('\n', '\n# LOREM IPSUM basdbasjdkabsdiuhais dabi sbdiab sidbasbdkja bsdb akbsdj abjsbdkajbs kjbdk jasbkjd bajb dkajdbskjabdsu asjbd akjsbdk abskd baksbdk jabsd baksdbk ajbsdjk bkja bkbdkjab Story of a simple prog\n')
                print(modified_content)
        except Exception as e:
            print(f"Error reading {bashrc_path}: {e}")
    else:
        print(f"No .bashrc file found at {bashrc_path}.")

if __name__ == "__main__":
    main()