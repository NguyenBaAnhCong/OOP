class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = int(tuoi)
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def __str__(self):
        return f"Họ tên: {self.ho_ten} | Tuổi: {self.tuoi} | Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi}"

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= int(bac) <= 10):
            raise ValueError("Bậc công nhân phải từ 1 đến 10")
        self.bac = bac
        
    def __str__(self):
        return f"[Công Nhân] {super().__str__()} | Bậc: {self.bac}/10"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def __str__(self):
        return f"[Kỹ Sư] {super().__str__()} | Ngành: {self.nganh_dao_tao}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def __str__(self):
        return f"[Nhân Viên] {super().__str__()} | Công việc: {self.cong_viec}"

# --- Lớp Quản Lý (Kết tập danh sách cán bộ) ---
class QLCB:
    def __init__(self):
        # Thuộc tính này là một list, lưu trữ các Object CanBo
        self.danh_sach_can_bo = []

    def them_moi_can_bo(self, can_bo_moi):
        self.danh_sach_can_bo.append(can_bo_moi)
        print(f"Đã thêm thành công: {can_bo_moi.ho_ten}")

    def tim_kiem_theo_ten(self, ten_can_tim):
        print(f"\n--- Kết quả tìm kiếm cho '{ten_can_tim}': ---")
        tim_thay = False
        for cb in self.danh_sach_can_bo:
            # Dùng in để tìm kiếm tên có chứa từ khóa (không cần gõ chính xác 100%)
            if ten_can_tim.lower() in cb.ho_ten.lower():
                print(cb)
                tim_thay = True
        
        if not tim_thay:
            print("Không tìm thấy cán bộ nào khớp với từ khóa.")

    def hien_thi_danh_sach(self):
        print("\n=== DANH SÁCH TOÀN BỘ CÁN BỘ ===")
        for cb in self.danh_sach_can_bo:
            print(cb)
        print("=================================")

quan_ly = QLCB()

# 1. Thêm cán bộ
quan_ly.them_moi_can_bo(KySu("Kỹ sư Công", 22, "Nam", "Hà Nội", "Khoa học Máy tính"))
quan_ly.them_moi_can_bo(CongNhan("Trần Văn B", 35, "Nam", "Hải Phòng", 5))
quan_ly.them_moi_can_bo(NhanVien("Lê Thị C", 28, "Nữ", "Đà Nẵng", "Kế toán"))

# 2. Hiển thị danh sách
quan_ly.hien_thi_danh_sach()

# 3. Tìm kiếm
quan_ly.tim_kiem_theo_ten("Công")