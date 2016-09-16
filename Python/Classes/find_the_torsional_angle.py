import math
class Vect():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __mul__(self, o):
        return self.x * o.x + self.y * o.y + self.z * o.z
    def __sub__(self, o):
        return Vect(o.x - self.x, o.y - self.y, o.z - self.z)
    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def cross(self, o):
        return Vect(self.y*o.z-self.z*o.y, self.z*o.x-self.x*o.z, self.x*o.y-self.y*o.x)

A = Vect(*map(float,  input().split()))
B = Vect(*map(float,  input().split()))
C = Vect(*map(float,  input().split()))
D = Vect(*map(float,  input().split()))

X = (B - A).cross(C - B)
Y = (C - B).cross(D - C)

print('{0:.2f}'.format(math.degrees(math.acos((X * Y)/ (abs(X) * abs(Y))))))