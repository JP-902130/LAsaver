## complex number calculators;
import math
import helper
'''
pre: two integers; x stands for real part and y stands for imagnary part;
post:(str) the modulus in the simplest form;
'''
class complex_num:
 
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    
    
# return the modulus of the complex number (in string)
def GetModulus(complex):
    sum_sqaure = complex.x**2 + complex.y**2
    return helper.reduce_square(sum_sqaure)    
# get the real part
def GetReal(comp):
    return comp.x
# get the complex part
def GetComplex(comp):
    return comp.y
# get conjugate
def GetConjugate(comp):
    NewComp = complex_num(comp.x, -comp.y)
    return NewComp
# take two complex numbers, return the addition/ substraction of the two numbers
def complex_add(comp_1, comp_2):
    x = comp_1.x
    y = comp_1.y
    u = comp_2.x
    v = comp_2.y
    newcomp = complex_num(x+u, y+v)
    return newcomp
# take two complex numbers, return the product of the two numbers
def complex_mul(comp_1, comp_2):
    x = comp_1.x
    y = comp_1.y
    u = comp_2.x
    v = comp_2.y

    newcomp = complex_num(x*u - y*v, x*v + y*u)
    return newcomp

# take a complex number, calculate its nth power;
def complex_pow(comp, n):
    newcomp = complex_num(1,0)
    for i in range(n):
        newcomp = complex_mul(newcomp, comp)
    return newcomp
# take two complex numbers, return the quotient of the two numbers
def complex_div(comp_1, comp_2):
    
    a = comp_1.x
    b = comp_1.y
    c = comp_2.x
    d = comp_2.y 
    if c == 0 and d == 0:
        print("The denominator is zero, invalid operation")
        return complex_num(0, 0)
    newx = round(((a*c + b*d) / (c**2 + d**2)),2)
    newy = round(((b*c - a*d) / (c**2 + d**2)),2)
    newcomp = complex_num(newx, newy)
    return newcomp


def print_complex(complex):
    
    if complex.y == 0:
        print(str(complex.x) + '\n')
    elif complex.y > 0:
        print(str(complex.x) +  ' + ' + str(complex.y) + 'i\n')
    else:
        print(str(complex.x) +  ' - ' + str(abs(complex.y)) + 'i\n')
   