import cv2
import numpy as np
import time
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Volume Setup
devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume
volume = cast(volume, POINTER(IAudioEndpointVolume))
minVol, maxVol, _ = volume.GetVolumeRange()


# Face Detector (Haar Cascade)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Camera Setup

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

prev_time = 0
smooth_volume = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    volume_percent = 0

    if len(faces) > 0:
        (x, y, w, h) = faces[0]   # Take first detected face

        cx = x + w // 2
        cy = y + h // 2

        # Draw face box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 100), 2)
        cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)

        # Convert vertical position to volume
        volume_percent = np.interp(cy, [0, 480], [100, 0])
        target_volume = np.interp(volume_percent, [0, 100], [minVol, maxVol])

        # Smooth transition
        smooth_volume += (target_volume - smooth_volume) * 0.2
        volume.SetMasterVolumeLevel(smooth_volume, None)

        volume.SetMute(0, None)

    else:
        volume.SetMute(1, None)


    # UI Volume Bar

    bar_height = int(np.interp(volume_percent, [0, 100], [400, 150]))

    cv2.rectangle(frame, (20, 100), (100, 420), (40, 40, 40), -1)
    cv2.rectangle(frame, (20, 100), (100, 420), (100, 100, 100), 2)
    cv2.rectangle(frame, (20, bar_height), (100, 420), (0, 255, 150), -1)

    cv2.putText(frame, f"{int(volume_percent)}%",
                (25, 460),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 150),
                2)

    # Title
    cv2.putText(frame, "FACE VOLUME CONTROL",
                (160, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)

    # Status
    status = "FACE DETECTED" if len(faces) > 0 else "MUTED"
    color = (0, 255, 0) if len(faces) > 0 else (0, 0, 255)

    cv2.putText(frame, f"Status: {status}",
                (380, 460),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2)

    # FPS Counter
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if current_time != prev_time else 0
    prev_time = current_time

    cv2.putText(frame, f"FPS: {int(fps)}",
                (520, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2)

    cv2.imshow("Professional Face Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
