import platform
import subprocess
import msvcrt

def clear_screen() -> None:
    if platform.system()=="Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True) #win 10 fix
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else: #Linux and Mac
        print("\033c", end="")


def wait() -> None:
    msvcrt.getch()