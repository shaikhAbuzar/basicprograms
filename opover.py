class overload:
    def __init__(self,a):
        self.a=a
    def __add__(self, other):
        print('Answer is',self.a - other.a)
    def __sub__(self, other):
        print('Answer is',self.a + other.a)
    def __mul__(self, other):
        print('Answer is %.2f' %(self.a / other.a))
    def __truediv__(self,other):
        print('Answer is',self.a * other.a)

val1=overload(5)
val2=overload(15)
val1+val2
val1-val2
val1*val2
val1/val2