import pyautogui
import time
import pyperclip

## pyautogui pause between two actions
pyautogui.PAUSE = 0.2

## Get current position of the mouse
def getMouseXY(secondsDelay):
    time.sleep(secondsDelay)
    print(pyautogui.position())

def copyAndPaste(content,secondsDelay):
    pyperclip.copy(content)
    pyautogui.hotkey('ctrl','v')
    time.sleep(secondsDelay)
