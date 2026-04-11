class NhanVien:
    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong, luong_max):
        # Thuộc tính Private (tương ứng với dấu -)
        self.__ten_nhan_vien = ten_nhan_vien
        self.__luong_co_ban = float(luong_co_ban)
        self.__he_so_luong = float(he_so_luong)
        
        # Thuộc tính Public (tương ứng với dấu +)
        self.LUONG_MAX = float(luong_max)

    # ==========================================
    # CÁC PHƯƠNG THỨC GET / SET
    # ==========================================
    def get_tenNhanVien(self):
        return self.__ten_nhan_vien
        
    def set_tenNhanVien(self, ten_moi):
        self.__ten_nhan_vien = ten_moi

    def get_luongCoBan(self):
        return self.__luong_co_ban

    def set_luongCoBan(self, luong_moi):
        self.__luong_co_ban = float(luong_moi)

    def get_heSoLuong(self):
        return self.__he_so_luong

    def set_heSoLuong(self, he_so_moi):
        self.__he_so_luong = float(he_so_moi)

    # ==========================================
    # CÁC PHƯƠNG THỨC NGHIỆP VỤ 
    # ==========================================
    def tinhLuong(self):
        return self.__luong_co_ban * self.__he_so_luong

    def tangLuong(self, muc_tang):
        he_so_moi = self.__he_so_luong + muc_tang
        luong_du_kien = self.__luong_co_ban * he_so_moi
        
        # Kiểm tra điều kiện vượt mức lương tối đa
        if luong_du_kien > self.LUONG_MAX:
            print(f"Cảnh báo: Tăng hệ số lương thêm {muc_tang} khiến lương vượt mốc tối đa ({self.LUONG_MAX:,.0f})!")
            return False
        else:
            self.__he_so_luong = he_so_moi
            return True

    def inTTin(self):
        print("\n--- THÔNG TIN NHÂN VIÊN ---")
        print(f"Tên nhân viên : {self.__ten_nhan_vien}")
        print(f"Lương cơ bản  : {self.__luong_co_ban:,.0f}")
        print(f"Hệ số lương   : {self.__he_so_luong}")
        print(f"Lương tối đa  : {self.LUONG_MAX:,.0f}")
        print(f"Lương thực lãnh: {self.tinhLuong():,.0f}")
        print("---------------------------")


# ==========================================
# PHẦN THỰC THI CHƯƠNG TRÌNH KIỂM TRA
# ==========================================

# 1. Tạo một nhân viên mới
nv1 = NhanVien(ten_nhan_vien="Nguyễn Văn A", luong_co_ban=5000000, he_so_luong=2.0, luong_max=15000000)
nv1.inTTin()

# 2. Thử tăng lương ở mức hợp lệ (tăng thêm hệ số 0.5)
print("\n=> Yêu cầu tăng hệ số lương thêm 0.5...")
hop_le = nv1.tangLuong(0.5)
if hop_le:
    print("Tăng lương thành công!")
nv1.inTTin()

# 3. Thử tăng lương vượt mốc tối đa (tăng thêm hệ số 1.5 nữa)
print("\n=> Yêu cầu tăng hệ số lương thêm 1.5...")
hop_le_2 = nv1.tangLuong(1.5)
if hop_le_2:
    print("Tăng lương thành công!")
else:
    print("Thao tác tăng lương bị hủy bỏ.")
nv1.inTTin()