import win32api, win32con, pyautogui, time

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


time.sleep(5)
for i in range(10000):
    pos = pyautogui.position()
    click(pos[0], pos[1])