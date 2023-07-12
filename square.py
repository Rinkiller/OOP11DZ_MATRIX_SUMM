class Square:

    def __init__(self , a:int , b:int = None) -> None:
        self.a = a
        if b: 
            self.b = b
        else:
            self.b = a
    def square(self) -> int:
        return self.a * self.b
    def perimetr(self) -> int:
        return 2*(self.a + self.b)
    def __add__(self , other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Square(new_a , new_b)
    def __sub__(self , other):
        if self.a < other.a or self.b < other.b:
            raise ValueError
        return Square(self.a - other.a , self.b - other.b)
    def __eq__(self , other) -> bool:
        return self.perimetr() == other.perimetr()
    def __gt__(self , other) -> bool:
        return self.perimetr() > other.perimetr()
    
sq1 = Square(10 , 6)
sq2 = Square(4 , 2)
sq3 = sq1 + sq2
sq4 = sq1 - sq2
sq5 = sq1
print(sq3.perimetr())
print(sq4.perimetr()) 
#sq5 = sq2 - sq1
#print(sq5.perimetr())
print(sq1 > sq2)
print(sq1 == sq3)
print(sq1 == sq5)