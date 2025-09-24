class CalculateArea:
    def RectangleArea(self, w, h):
        return w * h
    @classmethod
    def TriangleArea(cls, b, h):
        return 0.5 * b * h
    @staticmethod
    def CircleArea(r):
        return 3.14 * r * r
cal = CalculateArea()
calRec = cal.RectangleArea(4, 5)
calTri = cal.TriangleArea(4, 5)
calCir = cal.CircleArea(5)

print("Rectangle Area:", calRec)
print("Triangle Area:", calTri)
print("Circle Area:", calCir)