import cv2

# Load mô hình Haar cascade nhận diện xe
car_cascade = cv2.CascadeClassifier("D:\GIAHAN\CN2304CLCA\smart-traffic-opencv\cv3_car_detection\cars.xml")

image = cv2.imread("D:\GIAHAN\CN2304CLCA\smart-traffic-opencv\cv2_draw_name\car3.jpg")
if image is None:
    print("Không tìm thấy ảnh!")
    exit()
    
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# nhận diện các xe
cars = car_cascade.detectMultiScale(gray, 1.1, 3)

# vẽ khung và đánh số từng xe
for i, (x, y, w, h) in enumerate(cars, start=1):
 #khung
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Tính vị trí để đặt số
    center_x = x + w // 2
    center_y = y + h // 2

    # Vẽ số thứ tự ngay giữa khung
    cv2.putText(image, str(i), (center_x - 10, center_y + 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)


cv2.imshow("Car Detection - Numbered", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
