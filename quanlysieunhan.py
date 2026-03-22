class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Siêu nhân {self.ten} | Vũ khí: {self.vu_khi} | Màu sắc: {self.mau_sac}"

danh_sach_sieu_nhan = []

print("Chương trình quản lý siêu nhân\n")
print("Nhập thông tin về các siêu nhân (nhập 'u' để dừng)\n")

while True:
    nhap_ten = input("Nhập tên siêu nhân : ")

    if nhap_ten.lower() == 'u':
        break
    nhap_vu_khi = input("Nhập vũ khí của siêu nhân : ")
    nhap_mau_sac = input("Nhập màu sắc của siêu nhân : ")

    sieu_nhan_moi = SieuNhan(nhap_ten, nhap_vu_khi, nhap_mau_sac)

    danh_sach_sieu_nhan.append(sieu_nhan_moi)
    print("Siêu nhân đã được thêm vào danh sách.\n")
print("\nDanh sách các siêu nhân đã nhập:")
if len(danh_sach_sieu_nhan) == 0:
    print("Không có siêu nhân nào được nhập.")
else:
    for sieu_nhan in danh_sach_sieu_nhan:
        print(sieu_nhan)
    


