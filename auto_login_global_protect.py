import pyautogui
import time, os
import subprocess

from dotenv import load_dotenv

load_dotenv()

def open_globalprotect_vpn():
    '''open program'''
    try:
        subprocess.Popen(['/usr/bin/gpclient'])
        print("GlobalProtect VPN is now open.")
    except FileNotFoundError:
        print("GlobalProtect command not found. Please ensure GlobalProtect is installed.")


def find_element(img_path, do_click = False):
    pos = None
    while pos is None:
        time.sleep(3) 
        print("waiting ", img_path, pos)
        pos = pyautogui.locateOnScreen(img_path)
    if do_click:
        pyautogui.click(pos)
    return pos


open_globalprotect_vpn()
find_element("connect.png", True)
find_element("login.png")
pyautogui.write(os.getenv("USER"))
pyautogui.press("tab")
pyautogui.write(os.getenv("PASS"))
pyautogui.press("enter")


