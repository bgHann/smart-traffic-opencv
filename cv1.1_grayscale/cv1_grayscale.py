import cv2

image = cv2.imread("D:\GIAHAN\CN2304CLCA\smart-traffic-opencv\cv1_grayscale\car3.jpg")
if image is None:
    print("Không tìm thấy ảnh. Kiểm tra lại đường dẫn.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Ảnh gốc", image)
    cv2.imshow("Ảnh đen trắng", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
