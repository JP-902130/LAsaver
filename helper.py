## helper.py
import math

def is_perfect_square(num):
    if int(math.sqrt(num)) == math.sqrt(num):
        return 1
    else:
        return 0
'''
pre: a number we need to the the square root of;
post: (str) the number in the simplest form, if it can not be simplified, return decimal;
ex: print(reduce_square(32)) -> 4sqrt(2);
'''

def reduce_square(num):

    if num == 1: ## special case considering the number is 1
        return (str(1) + "\n")
    ## special case considering the number itself is a square root
    if is_perfect_square(num) == 1:
       return str(int(math.sqrt(num))) + "\n" 
    for i in range(num, 1, -1):
        if is_perfect_square(i) == 1 and int(num/i) == (num/i):
            return (str(int(math.sqrt(i))) + "sqrt(" + str(int(num/i)) + ")\n")
    return "{:.2f}\n".format(math.sqrt(num))
    ## returns two decimal places
      
