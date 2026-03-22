import math
class Point:
    """ Repersent a point in 2-D Geometry"""
    x = int
    y = int
    # Hàm khởi tạo
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    # Hàm trả về
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
    # Phương thức nhập điểm từ bàn phím
    def read(self):
        print("\nNhập tọa độ cho điểm B")
        self.x = int(input("Nhap x: "))
        self.y = int(input("Nhap y: "))
    # Hàm tính khoảng cách 
    def distance(self, point):
        d = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return d

DiemA = Point(3, 4)
print("Tọa độ của điểm A là: ",DiemA)

DiemB = Point()
DiemB.read()
print("Tọa độ của điểm B là: ",DiemB)

DiemC = Point(-DiemB.x, -DiemB.y)
print("\nTọa độ của C đối xứng với B qua O",)
print("Tọa độ của điểm C là: ",DiemC)

gocToaDo = Point()
print("\nKhoảng cách từ điểm B đến gốc tọa độ là: ",DiemB.distance(gocToaDo))
print("Khoảng cách từ điểm A đến điểm B là: ",DiemA.distance(DiemB))