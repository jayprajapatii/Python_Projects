import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("test1.mp4", f, 20.0, dim)
dur = 40
now_start_time = time.time()

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)

    if time.time() - now_start_time >= dur:
        break

output.release()
print("video created")
