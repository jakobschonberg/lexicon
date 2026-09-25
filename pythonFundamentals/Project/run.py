import subprocess
import pathlib
print(pathlib.Path().resolve())
subprocess.call('start pythonw -i main.py', shell=True)
