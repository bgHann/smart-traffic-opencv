#  Smart Traffic OpenCV

Repo lưu các bài tập nhỏ môn **Giao thông Thông minh**, sử dụng **Python + OpenCV**.

## 📘 Bài tập

### CV1.1 – Chuyển ảnh sang đen trắng
- 📄 File: `cv1_grayscale/cv1_grayscale.py`

### CV1.2 – Vẽ khung và tên sinh viên
- 📄 File: `cv2_draw_name/cv2_draw_name.py`

### CV1.3 – Nhận diện & đánh số xe
- 📄 File: `cv3_car_detection/cv3_car_numbering.py`
  
### car-tracking-assignment 
- 📄 File: `car-tracking-assignment\cv2.3-code\car_tracking.py`
- Yêu cầu:
- Đếm số lượng xe xuất hiện trong video

- Đánh chỉ số cho các xe phát hiện được trên khung hình

## ⚙ Yêu cầu
- Python 3
- OpenCV: `pip install opencv-python`

## ▶️ Cách chạy
```bash
cd <thư mục>
py <tên file>.py

```
### HELLOSUMO
- Thư mục chứa các mô phỏng giao thông
  <Hello_sumo> : Thư mục check mô phỏng
  <Drving_in_Circles> Vẽ mô phỏng chạy theo hình tròn
  <2.1phu_nhuan> Chuẩn bị dữ liệu đường Ngã tư Phú Nhuận cho mô phỏng,
  Dòng 1: Hướng vào Nguyễn Kiệm từ đường Phan Đình Phùng, lưu lượng 500 xe/h, xe màu đỏ

    Dòng 2: Hướng vào Nguyễn Kiệm từ Hoàng Văn Thụ, lưu lượng 500 xe/h, xe màu vàng

   Dòng 3: Hướng vào Nguyễn Kiệm từ  Phan Đăng Lưu, lưu lượng 500 xe/h, xe màu xanh lá
  ## ▶️ Cách chạy
```bash
cd <HELLOSUMO> cd<thư mục>
sumo-gui -c <tên file>.sumocfg 

