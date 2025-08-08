import cv2

image = cv2.imread("D:\GIAHAN\CN2304CLCA\smart-traffic-opencv\cv2_draw_name\car3.jpg")
if image is None:
    print("Không tìm thấy ảnh, vui lòng kiểm tra lại")
    exit()

# Kích thước ảnh
h, w = image.shape[:2]

# Tính vị trí khung chữ nhật giữa ảnh
top_left = (w // 4, h // 4)
bottom_right = (3 * w // 4, 3 * h // 4)

# Vẽ khung màu vàng
cv2.rectangle(image, top_left, bottom_right, (0, 255, 255), 3)

text = "Bui Gia Han"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2

# Tính kích thước chữ (dùng để canh giữa)
(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

# Tính vị trí để chữ nằm giữa khung
x_text = top_left[0] + (bottom_right[0] - top_left[0] - text_width) // 2
y_text = top_left[1] + (bottom_right[1] - top_left[1] + text_height) // 2

# Viết chữ màu đỏ
cv2.putText(image, text, (x_text, y_text), font, font_scale, (0, 0, 255), thickness)

cv2.imshow("Ảnh kết quả", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
