## complex number calculators;
import math
import helper
import re
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
        return complex_num(404, 404)
    newx = round(((a*c + b*d) / (c**2 + d**2)),2)
    newy = round(((b*c - a*d) / (c**2 + d**2)),2)
    newcomp = complex_num(newx, newy)
    return newcomp


def print_complex(complex):
    if complex.x == 404 and complex.y == 404:
        return "invalid complex number"
    if complex.y == 0:
        print(str(complex.x) + '\n')
    elif complex.y > 0:
        print(str(complex.x) +  ' + ' + str(complex.y) + 'i\n')
    else:
        print(str(complex.x) +  ' - ' + str(abs(complex.y)) + 'i\n')

def convert_object(sentence): #ask for a string input and convert to object
    
    # YOU MUST input the complex number in the form of x +- bi;
    symbols = []
    numbers = []
    string = input(sentence + '\n')
    index_symbol = 0
    index_i = 0
    temp_string = ''
    for i in range(len(string)):
        
        if string[i] == '+' or string[i] == '-':
            symbols.append(string[i])
            index_symbol = i
        if string[i] == 'i':
            index_i = i

    for i in range(len(string)):
        
        if helper.is_num(string[i]) == 1:
            temp_string = temp_string + string[i]
        else:
            numbers.append(temp_string)
            temp_string = ''
    numbers = [int(x) for x in numbers if len(x) != 0]
    if len(symbols) == 1:
        temp = symbols[0]
        symbols[0] = '+'
        symbols.append(temp)
    
    for i in range(len(symbols)):
        if symbols[i] == '-':
            numbers[i] *= -1
    
    return complex_num(numbers[0], numbers[1])

def calculate():
    # Get input from the user
    while(1):
        print()
        print("Here are some operations you can choose. Please select the correct NUMBER")
        choice = input(" 1) addtion\n 2) multiplication\n 3) exponentential\n 4) division\n 5) Modulus\n 6) Conjugate\n ")
        print()
        while( helper.is_num(choice) != 1 or (int(choice) < 1 or int(choice) > 6)):
            print("Please give valid input")
            choice = input(" 1) addtion\n 2) multiplication\n 3) exponentential\n 4) division\n 5) Modulus\n 6) Conjugate\n ")
        

        #evaluate
        

        if choice == '1':
            comp1 = convert_object("Please input your first number")
            comp2 = convert_object("Please input your second number")
            print("The result is:\n")
            print_complex(complex_add(comp1, comp2))
        elif choice == '2':
            comp1 = convert_object("Please input your first number")
            comp2 = convert_object("Please input your second number")
            print("The result is:\n")
            print_complex(complex_mul(comp1, comp2))
        elif choice == '4':
            comp1 = convert_object("Please input your numerator number")
            comp2 = convert_object("Please input your denominator number")
            print("The result is:\n")
            print_complex(complex_div(comp1, comp2))    
        elif choice == '3':
            comp1 = convert_object("Please input your base")
            n = int(input("Please input the exponent"))
            print("The result is:\n")
            print_complex(complex_pow(comp1, n))
        elif choice == '5':
            comp1 = convert_object("Please input a complex number")
            print("The result is:\n")
            print(GetModulus(comp1))
        elif choice == '6':
            comp1 = convert_object("Please input a complex number")
            print("The result is:\n")
            print_complex(GetConjugate(comp1))
        
        q = input("Do you want to make another comnplex number calculation? Press 1 to continue, press 0 to quit")
        
        while (helper.is_num(q) == 0 or (int(q) != 0 and int(q) != 1)):
            q = input("Please enter valid input")

        if int(q) == 1:
            continue
        elif int(q) == 0:
            print("Thank you")
            break
        