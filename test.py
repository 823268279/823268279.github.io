# x = 5
# if x<3:
#     print('小')
# elif x>5:
#     print('中')
# else:
#     print('大')


# def test(x,y=3):
#     print(x)
#     print(y)
# test(2)

import pyautogui
img=pyautogui.screenshot(region=(x1,y1,x2,y2))
color=img.getpixel(x,y)
print(color)