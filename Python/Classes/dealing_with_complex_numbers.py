from math import pow
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other):
        return Complex(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other):
        return Complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __truediv__(self, other):
        try: 
            return self.__mul__(Complex(other.real, -1*other.imag)).__mul__(Complex(1.0/(other.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None
    def __str__(self):
        return '{0:.2f}{1:+.2f}i'.format(self.real,self.imag)
    def mod(self):
        return Complex(pow(self.real**2+self.imag**2, 0.5), 0)
    

    
A = Complex(*map(float, input().strip().split()))
B = Complex(*map(float, input().strip().split()))

print('\n'.join(map(str,[A+B, A-B, A*B, A/B, A.mod(), B.mod()])))