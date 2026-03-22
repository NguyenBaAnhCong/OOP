import json


class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Siêu nhân {self.ten} | Vũ khí: {self.vu_khi} | Màu sắc: {self.mau_sac}"

    def to_dict(self):
        return {
            "ten": self.ten,
            "vu_khi": self.vu_khi,
            "mau_sac": self.mau_sac,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["ten"], data["vu_khi"], data["mau_sac"])


def luu_danh_sach_vao_json(danh_sach, ten_file):
    du_lieu = [sieu_nhan.to_dict() for sieu_nhan in danh_sach]
    with open(ten_file, "w", encoding="utf-8") as file:
        json.dump(du_lieu, file, ensure_ascii=False, indent=4)


def tai_danh_sach_tu_json(ten_file):
    try:
        with open(ten_file, "r", encoding="utf-8") as file:
            du_lieu = json.load(file)
        return [SieuNhan.from_dict(item) for item in du_lieu]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Dữ liệu JSON không hợp lệ.")
        return []


TEN_FILE_JSON = "danh_sach_sieu_nhan.json"
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

luu_danh_sach_vao_json(danh_sach_sieu_nhan, TEN_FILE_JSON)
print(f"\nĐã lưu danh sách siêu nhân vào file {TEN_FILE_JSON}.")

danh_sach_tu_file = tai_danh_sach_tu_json(TEN_FILE_JSON)
print("\nDanh sách các siêu nhân đọc từ file JSON:")
if len(danh_sach_tu_file) == 0:
    print("Không có dữ liệu trong file JSON.")
else:
    for sieu_nhan in danh_sach_tu_file:
        print(sieu_nhan)



