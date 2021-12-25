
#main
import math
import helper
import complex
import numpy
import matrix
import vector
import os
os.system('cls')
red = "\033[0;31m"
white = "\033[0;37m"


def main():
    while(True):
        answer = (input('''
                           Symbolab Minus Minus

                           Type 1 to do vector Calculation
                           Type 2 to do matrix Calculation
                           Type 3 to do complex Calculation
                           Type 0 to quit Calculator\n'''))
        if answer== '1':
            vector.calculate()
        elif answer=='2':
            matrix.calculate()
        elif answer=='3':
            complex.calculate()
        elif answer=='0':
            break
        else:
            print("Input error try again")
            main()
    
  
  
    

main()

