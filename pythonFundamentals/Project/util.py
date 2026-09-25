import platform
import subprocess

def clear_screen():
    if platform.system()=="Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True) #win 10 fix
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else: #Linux and Mac
        print("\033c", end="")