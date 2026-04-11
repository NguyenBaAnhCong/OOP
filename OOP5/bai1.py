class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = float(gia)

    # Đa hình: Lớp cha định nghĩa khung hiển thị cơ bản
    def __str__(self):
        return f"[{self.ma_hang}] {self.ten_hang} | NSX: {self.nha_sx} | Giá: {self.gia:,.0f}đ"

# Các lớp con kế thừa từ HangHoa
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        # Gọi hàm khởi tạo của lớp cha
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    # Đa hình: Ghi đè (override) lại __str__ để in thêm thông số riêng
    def __str__(self):
        thong_tin_cha = super().__str__()
        return f"{thong_tin_cha} | BH: {self.tg_baohanh} tháng | {self.dien_ap}V - {self.cong_suat}W"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def __str__(self):
        return f"{super().__str__()} | Chất liệu: {self.loai_nguyenlieu}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def __str__(self):
        return f"{super().__str__()} | NSX: {self.ngay_sx} - HSD: {self.ngay_hethan}"



tv = HangDienMay("DM01", "Tivi Sony 55 inch", "Sony", 15000000, 24, 220, 150)
chen = HangSanhSu("SS01", "Bộ chén dĩa hoa văn", "Bát Tràng", 500000, "Gốm sứ cao cấp")
sua = HangThucPham("TP01", "Sữa tươi Vinamilk", "Vinamilk", 350000, "01/10/2025", "01/04/2026")

print(tv)
print(chen)
print(sua)