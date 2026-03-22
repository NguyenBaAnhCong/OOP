class SinhVien:
    def __init__(self, ho_va_ten, ma_sinh_vien, nganh_hoc):
        self.ho_va_ten = ho_va_ten
        self.ma_sinh_vien = ma_sinh_vien
        self.nganh_hoc = nganh_hoc
    
    def hien_thi_thong_tin(self):
        print(f"Họ và tên: {self.ho_va_ten}")
        print(f"Mã số sinh viên: {self.ma_sinh_vien}")
        print(f"Ngành học: {self.nganh_hoc}")
        print("-" * 30)

sv1 = SinhVien("Nguyễn Bá Anh Công", "22110107", "BCSE")
sv1.hien_thi_thong_tin()