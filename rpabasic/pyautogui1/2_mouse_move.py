import pyautogui

# 좌표 인식 - position()

# pos = pyautogui.position()
# print(pos)  # Point(x=3044, y=71)
# print(pos.x, ", ", pos.y)

# 마우스 이동 - moveTo(x,y,시간) / moveRel()
# pyautogui.moveTo(100, 100, duration=1)
# pyautogui.moveTo(200, 200, duration=1)
# pyautogui.moveTo(300, 300, duration=1)


pyautogui.moveTo(300, 300, duration=1)
pyautogui.moveRel(100, 100, duration=0.5)
print(pyautogui.position())
