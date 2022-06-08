# 이미지 인식
import pyautogui as p

# locateOnScreen(path, confidence) : 캡쳐한 이미지의 화면상 좌표 구하기
# 이미지 기반이어서 해상도가 바뀐다거나 이런 경우는 잘 안됨
# 이미지 파일명은 영문으로 작성

# screen_locate = p.locateOnScreen("./rpabasic/pyautogui1/screen.png")
# print(screen_locate) # Box(left=171, top=264, width=300, height=400)


screen_locate = p.locateOnScreen("./rpabasic/pyautogui1/file_menu.png")
# print(screen_locate)  # None / Box(left=40, top=1, width=46, height=34)
p.click(screen_locate)
