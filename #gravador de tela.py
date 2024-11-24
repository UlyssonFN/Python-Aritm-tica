#gravador de tela
import cv2
import numpy as np
import pyautogui
import keyboard

screen_size = pyautogui.size()
fps=20
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = "screen_recording_clcoding.avi"
out = cv2.VideoWriter(output_file, fourcc, fps, (screen_size.width, screen_size.height))

print("Gravando... Pressione 'q' para parar. ")

while True:
    screen = pyautogui.screenshot()
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)

    if keyboard.is_pressed('q'):
        print("Gravação parada")
        break
out.release()
print(f"Video saved to: {output_file}")
