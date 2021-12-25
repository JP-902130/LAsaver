import numpy as np
import os
import sys
os.system('cls')
red = "\033[0;31m"
white = "\033[0;37m"

# the function ask for input from user and return a matrix object
def matrix_create():
    
    n = int(input("Please give the number of rows: \n"))
    m = int(input("Please give the number of columns: \n"))
    print("Now please input your matrix, separated by space\n")
    array = np.array([input().strip().split() for _ in range(n)], int)
    return array
    
        
      

# matrix addtion, subtraction and multiplication
def add_matrix(matrix1,matrix2): #1
    
    return matrix1 + matrix2
    
def subt_matrix(matrix1,matrix2): #2
    
    return matrix1 - matrix2

def mult_matrix(matrix1,matrix2): #3
    matrix1 = np.squeeze(np.asarray(matrix1))
    matrix2 = np.squeeze(np.asarray(matrix2))
    return np.dot(matrix1, matrix2)
# function that takes only 1 parameter;
def matrix_transpose(matrix1): #4
    return matrix1.transpose()
def matrix_trace(matrix1): #5
    return np.trace(matrix1)
def matrix_rank(matrix1): #6
    return np.linalg.matrix_rank(matrix1)
def matrix_rref(matrix1):
    res = matrix1.rref()
    return res

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = ' ')
            
        print()
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i],)
        

def calculate():
    try:
        print()
        print("Here are some operations you can choose. Please select the correct NUMBER\n")
        print("Here are some matrix operations you can choose\n")
        choice = input("1) Addition 2) Subtraction 3) Multiplication 4) Transpose 5) Trace 6) Rank 7) Quit \n")

        if choice == '1' or choice == '2' or choice == '3':
            arr1 = matrix_create()
            arr2 = matrix_create()
            
            print("----Your result is----")
            if choice == '1':
                res = add_matrix(arr1, arr2)
            if choice == '2':
                res = subt_matrix(arr1, arr2)
            if choice == '3':
                res = mult_matrix(arr1, arr2)
                if type(res[0]) == np.int64:
                    print_arr(res)
                else: 
                    print_matrix(res)
                ask = input("Do you want to calculate it again? Press 1 to play, Press 0 to quit.\n")
                if ask == '1':
                    calculate()
                else:
                    return     
        elif choice == '4' or choice == '5' or choice == '6':
            arr1 = matrix_create()
            if choice == '4':
                res = matrix_transpose(arr1)
            if choice == '5':
                res = matrix_trace(arr1)
                print("The result is:")
                print(res)
                ask = input("Do you want to calculate it again? Press 1 to play, Press 0 to quit.\n")
                if ask == '1':
                    calculate()
                else:
                    return                 
            if choice == '6':
                res = matrix_rank(arr1)
                print("The result is:")
                print(res)
                ask = input("Do you want to calculate it again? Press 1 to play, Press 0 to quit.\n")
                if ask == '1':
                    calculate()
                else:
                    return            
            
        elif choice == '7':
            return

        else:
            print(red, "Please input correctly!", white)
            calculate()


        print_matrix(res)
        
        ask = input("Do you want to calculate it again? Press 1 to play, Press 0 to quit.\n")
        if ask == '1':
            calculate()
        else:
            return                         

    except:
        print(red, "An error occured, please check your input format",white)
        calculate()

    