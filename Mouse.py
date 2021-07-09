import pyautogui
width,height=pyautogui.size()
print(width,height)
pyautogui.position()#to check the position of mouse pointer
#pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10,duration=1.5)
pyautogui.moveRel(200,0,duration=2)
pyautogui.moveTo(260,260,duration=1.5)
pyautogui.click(878,71)
pyautogui.doubleClick(878,71)
pyautogui.rightClick(878,71)
pyautogui.dragRel(100,0,duration=1.2)

