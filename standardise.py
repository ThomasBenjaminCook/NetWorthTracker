import os
import subprocess

def run_python_scripts_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                script_path = os.path.join(root, file)
                if(len(script_path.split("\\"))>8):
                    print(f"Executing {script_path}")
                    subprocess.run(["python", script_path], check=True)

# Replace 'your_directory_path' with the path to the directory you want to search
cwd = os.getcwd()
os.mkdir(os.path.join(cwd, "TEMP"))
run_python_scripts_in_directory(cwd)