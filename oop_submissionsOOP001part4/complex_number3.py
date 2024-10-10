import math
class ComplexNumber:
    def __init__(self, real=0, imag=0):
        if type(real)==int:
            self.real = real
        
        if type(imag)==int:
            self.imag = imag
        elif type(real)==str and type(imag)==str:
            print("ValueError: Invalid value for real and imaginary part")
        elif type(real)==str:
            print("ValueError: Invalid value for real part")
        elif type(imag)==str:
            print("ValueError: Invalid value for imag part")


    def __str__(self):
        if self.imag>0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self,other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self,other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self,other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag, self.imag*other.real + other.imag*self.real)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __abs__(self):
        return math.sqrt(self.real*self.real+ self.imag*self.imag)
    
    def __eq__(self,other):
        return self.real == other.real and self.imag == other.imag

    


    