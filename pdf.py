import pyautogui
import time

delay = 60

print('Press Ctrl-C or KeyboardInterrupt to quit') 

try:
    while True:
        pyautogui.click()
        time.sleep(delay)
except KeyboardInterrupt:
    print('Auto clicker stopped')
