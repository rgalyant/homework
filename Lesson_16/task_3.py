class TriangleChecker:
    __slots__ = ("a", "b", "c")

    def __init__(self):
        self.a = input("Введите длинну стороны A: ")
        self.b = input("Введите длинну стороны B: ")
        self.c = input("Введите длинну стороны C: ")
    
    def is_triangle(self):
        try:
            a = float(self.a)
            b = float(self.b)
            c = float(self.c)
        except Exception:
            return "Нужно вводить только числа!"
            
        if a < 0 or b < 0 or c < 0:
            return "С отрицательными числами ничего не выйдет!"
        
        if a < b + c and b < a + c and c < a + b:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

if __name__ == "__main__":
    triangle = TriangleChecker()
    print(triangle.is_triangle())