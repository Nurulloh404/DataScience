import os
import sys
import subprocess

def main():
    
        venv_path = os.environ.get('VIRTUAL_ENV')
        if(venv_path == None):
            raise Exception("Xato muhit!")
        else:
            print(f"Your current virtual env is {venv_path}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

            installed_packages = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode("utf-8")

            print(installed_packages)
            with open("requirements.txt", "w") as f:
                f.write(installed_packages)

        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    main()