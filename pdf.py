import pyautogui
import time
import sys

delay = 2 

print('Press Ctrl-C to quit')

try:
    while True:
        pyautogui.click()
        time.sleep(delay)
except KeyboardInterrupt:
    print('Auto clicker stopped')
    sys.exit()
