import os
import sys
import shutil
import getpass
import time

def md(path):
    if not os.path.exists(path):
        os.makedirs(path)

def rp(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
sore = str(rp("data"))
t1 = input("모드 폴더 입력(기본은 엔터)")
if t1 == "":
    md(f"C:/Users/{getpass.getuser()}/AppData/Roaming/.minecraft/mods")
    if os.path.exists(f"C:/Users/{getpass.getuser()}/AppData/Roaming/.minecraft/mods"):
        for file in os.scandir(f"C:/Users/{getpass.getuser()}/AppData/Roaming/.minecraft/mods"):
            shutil.rmtree(file)
    t = f"C:/Users/{getpass.getuser()}/AppData/Roaming/.minecraft/mods"
else:
    t = t1
shutil.copytree(sore, t, dirs_exist_ok=True)
print("완료. 5초 후 종료")
time.sleep(5)
exit()
