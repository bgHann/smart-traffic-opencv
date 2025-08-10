import cv2
import numpy as np

CASCADE_PATH = "D:/GIAHAN/CN2304CLCA/smart-traffic-opencv/car-tracking-assignment/cv2.3-code/cars.xml"
VIDEO_PATH   = "D:/GIAHAN/CN2304CLCA/smart-traffic-opencv/car-tracking-assignment/cv2.3-code/road.mp4"

car_cascade = cv2.CascadeClassifier(CASCADE_PATH)
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Không thể mở video!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    # Đánh số ID từ 1 đến số lượng xe hiện tại
    for idx, (x, y, w, h) in enumerate(cars, start=1):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, f"ID {idx}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.putText(frame, f"Cars: {len(cars)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Car Tracking", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
