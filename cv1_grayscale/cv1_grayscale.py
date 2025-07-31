import cv2

# Bước 1: Đọc ảnh từ file
image_path = "D:\GIAHAN\CN2304CLCA\smart-traffic-opencv\cv1_grayscale\car3.jpg"

# Thay bằng tên ảnh của bạn (nên để cùng thư mục với file .py)
image = cv2.imread(image_path)

# Kiểm tra nếu ảnh không tồn tại
if image is None:
    print("Không tìm thấy ảnh. Kiểm tra lại đường dẫn.")
else:
    # Bước 2: Chuyển ảnh sang ảnh đen trắng (grayscale)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Bước 3: Hiển thị ảnh gốc và ảnh đen trắng
    cv2.imshow("Ảnh gốc", image)
    cv2.imshow("Ảnh đen trắng", gray_image)

    # Bước 4: Chờ người dùng bấm phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()
