class NhanVienPhongBan:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        # Bắt ngoại lệ nếu hệ số lương không hợp lệ
        if float(he_so_luong) <= 0:
            raise ValueError(f"Lỗi khởi tạo {ho_ten}: Hệ số lương phải lớn hơn 0!")
            
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = float(he_so_luong)
        self.luong_toi_da = float(luong_toi_da)

    def __str__(self):
        return f"{self.ma_nv} - {self.ho_ten} (Hệ số: {self.he_so_luong})"

class CongTacVien(NhanVienPhongBan):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han, phu_cap):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        # Bắt lỗi nếu thời hạn nhập vào không khớp chuẩn
        if thoi_han not in ["3 tháng", "6 tháng", "1 năm"]:
            raise ValueError("Thời hạn hợp đồng chỉ được là: '3 tháng', '6 tháng', hoặc '1 năm'.")
        self.thoi_han = thoi_han
        self.phu_cap = float(phu_cap)

class NhanVienChinhThuc(NhanVienPhongBan):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri = vi_tri

class TruongPhong(NhanVienPhongBan):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bat_dau = ngay_bat_dau
        self.phu_cap_ql = float(phu_cap_ql)


try:
    nv1 = NhanVienChinhThuc("NV01", "Nguyễn Văn A", 1995, "Nam", "Hà Nội", 2.5, 20000000, "Lập trình viên")
    ctv = CongTacVien("CTV01", "Trần Thị B", 2002, "Nữ", "Hà Nội", 1.2, 10000000, "6 tháng", 500000)
    print("Khởi tạo thành công:")
    print(nv1)
    print(ctv)
    
    # Dòng này sẽ kích hoạt Exception (báo lỗi màu đỏ và dừng chương trình) vì hệ số lương = 0
    # nv_loi = NhanVienPhongBan("NV02", "Lê Văn C", 1990, "Nam", "Đà Nẵng", 0, 15000000)
except ValueError as e:
    print(f"BẮT ĐƯỢC LỖI: {e}")