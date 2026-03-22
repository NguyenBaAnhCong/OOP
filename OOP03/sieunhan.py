class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Siêu nhân {self.ten} | Vũ khí: {self.vu_khi} | Màu sắc: {self.mau_sac}"

print("Thông tin về các siêu nhân\n")
sieunhanA = SieuNhan("A", "Kiếm", "Đỏ")
sieunhanB = SieuNhan("B", "khiên", "Xanh")
print(sieunhanA)
print(sieunhanB)