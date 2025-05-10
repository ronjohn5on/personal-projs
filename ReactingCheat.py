# This is a script to cheat the reaction time on human calculator
# made to learn pyautogui
# mouse control and screenshot functions

import pyautogui

# pos = pyautogui.position()
# print(pos)
# im = pyautogui.screenshot()
# print("color: "+str(im.getpixel(pos)))

green = (75, 219, 106)
blue = (43, 135, 209)

while True:
    pos = pyautogui.position()
    # print(pos)
    im = pyautogui.screenshot()
    print("color: "+str(im.getpixel(pos)))
    if im.getpixel(pos) == green:
        pyautogui.click(pos)
        break
    elif im.getpixel(pos) == blue:
        pyautogui.click(pos)
        
