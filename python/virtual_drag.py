import cv2
import numpy as np

# Initialize Camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Create Multiple Boxes
boxes = [
    {"pos": [300, 200], "size": 150},
    {"pos": [700, 300], "size": 150},
    {"pos": [500, 500], "size": 150}
]

selected_box = None
smooth_factor = 0.2   # Lower = smoother, Higher = faster

while True:
    success, img = cap.read()
    if not success:
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Blue Color Range
    lower_blue = np.array([90, 100, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)

        if area > 1000:
            x, y, w_obj, h_obj = cv2.boundingRect(largest)
            center_x = x + w_obj // 2
            center_y = y + h_obj // 2

            cv2.circle(img, (center_x, center_y), 10, (0, 255, 0), -1)

            # Check if touching any box
            for box in boxes:
                cx, cy = box["pos"]
                size = box["size"]

                if (cx - size//2 < center_x < cx + size//2 and
                    cy - size//2 < center_y < cy + size//2):
                    selected_box = box
                    break

            # Smooth Move selected box
            if selected_box:
                old_x, old_y = selected_box["pos"]

                new_x = int(old_x + (center_x - old_x) * smooth_factor)
                new_y = int(old_y + (center_y - old_y) * smooth_factor)

                selected_box["pos"] = [new_x, new_y]

        else:
            selected_box = None
    else:
        selected_box = None

    # Draw Boxes (Highlight Selected)
    for box in boxes:
        cx, cy = box["pos"]
        size = box["size"]

        if box == selected_box:
            color = (0, 255, 0)  # Green when selected
        else:
            color = (255, 0, 255)

        cv2.rectangle(img,
                      (cx - size//2, cy - size//2),
                      (cx + size//2, cy + size//2),
                      color,
                      -1)

    cv2.imshow("Smooth Multiple Virtual Drag Boxes", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()