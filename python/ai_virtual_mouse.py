import cv2
import numpy as np
import pyautogui


screen_w, screen_h = pyautogui.size()

cap = cv2.VideoCapture(0)


prev_x, prev_y = 0, 0
smoothening = 7   


frame_reduction = 100

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue color range
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw control area
    cv2.rectangle(frame,
                  (frame_reduction, frame_reduction),
                  (frame_w - frame_reduction, frame_h - frame_reduction),
                  (255, 0, 255), 2)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 1500:
            x, y, w, h = cv2.boundingRect(cnt)
            cx = x + w // 2
            cy = y + h // 2

            # Draw detection
            cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)

            # Convert coordinates
            screen_x = np.interp(cx,
                                 (frame_reduction, frame_w - frame_reduction),
                                 (0, screen_w))
            screen_y = np.interp(cy,
                                 (frame_reduction, frame_h - frame_reduction),
                                 (0, screen_h))

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)

            prev_x, prev_y = curr_x, curr_y

            # Click if object close
            if area > 9000:
                pyautogui.click()
                cv2.putText(frame, "CLICK", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Smooth AI Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()