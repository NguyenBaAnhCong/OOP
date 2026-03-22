import copy

# Kế thừa lại lớp Point từ bài tập trước để làm vật liệu xây dựng LineSegment
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"


class LineSegment:
    # Dùng *args để nhận vào số lượng đối số tùy ý
    def __init__(self, *args):
        # 1. Hàm xây dựng mặc định (0 đối số)
        if len(args) == 0:
            # Thuộc tính private: thêm __ phía trước
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        
        # 2. Hàm xây dựng sao chép sâu (1 đối số là một LineSegment khác)
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            S = args[0]
            # Sao chép sâu: Tạo ra 2 vùng nhớ Point hoàn toàn MỚI có cùng tọa độ
            # Cách 1: Tự khởi tạo Point mới
            self.__d1 = Point(S.get_d1().x, S.get_d1().y)
            self.__d2 = Point(S.get_d2().x, S.get_d2().y)
            # Cách 2: Dùng thư viện copy: self.__d1 = copy.deepcopy(S.get_d1())

        # 3. Hàm xây dựng có đối số: 2 đối tượng Point
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            # Gán trực tiếp, không tạo điểm mới theo đúng yêu cầu đề bài
            self.__d1 = args[0]
            self.__d2 = args[1]
            
        # 4. Hàm xây dựng 4 đối số (x1, y1, x2, y2)
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
            
        else:
            raise ValueError("Tham số truyền vào không hợp lệ!")

    # Getter để hỗ trợ hàm sao chép sâu lấy được tọa độ
    def get_d1(self):
        return self.__d1
        
    def get_d2(self):
        return self.__d2

    # In thông tin đoạn thẳng ra màn hình
    def __str__(self):
        return f"LineSegment nối từ {self.__d1} đến {self.__d2}"


# ==========================================
# PHẦN THỰC THI CHƯƠNG TRÌNH KIỂM TRA
# ==========================================

print("1. Khởi tạo mặc định:")
line1 = LineSegment()
print(line1)

print("\n2. Khởi tạo bằng 4 tọa độ:")
line2 = LineSegment(0, 0, 10, 10)
print(line2)

print("\n3. Khởi tạo bằng 2 đối tượng Point:")
pA = Point(3, 4)
pB = Point(7, 8)
line3 = LineSegment(pA, pB)
print(line3)

print("\n4. Khởi tạo bằng sao chép sâu (Deep Copy) từ line3:")
line4 = LineSegment(line3)
print(line4)