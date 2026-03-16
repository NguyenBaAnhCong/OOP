import math

# --- Bài 1: Thể tích hình cầu ---
r = 5
v = (4/3) * math.pi * r**3
# Dùng f-string để định dạng chuỗi và làm tròn 2 chữ số thập phân trực tiếp
print(f"The tich cua hinh cau ban kinh {r} la: {v:.2f}")

# --- Bài 2: Chi phí nhập sách ---
gia_bia = 24.95
so_sach = 60
# Tối ưu logic: Tính số sách còn lại thay vì fix cứng con số 59
phi_van_chuyen = 3 + (so_sach - 1) * 0.75 
tong_chi_phi = (gia_bia * 0.6 * so_sach) + phi_van_chuyen
print(f"Tong chi phi nhap sach la: {tong_chi_phi:.2f} dollars")

# --- Bài 3: Thời gian chạy bộ ---
start_time = 6 * 3600 + 52 * 60
easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12

total_time = (tempo_pace * 3) + (easy_pace * 2)
finish_time = start_time + total_time

# Tối ưu toán học: Dùng hàm divmod() để lấy cả phần nguyên và phần dư cùng lúc
finish_hour, remainder = divmod(finish_time, 3600)
finish_minute, finish_second = divmod(remainder, 60)

print(f"Finish time is: {finish_hour:02d}:{finish_minute:02d}:{finish_second:02d}")