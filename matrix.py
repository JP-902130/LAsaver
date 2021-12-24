import numpy as np

def matrix_create():
    n = int(input("Please give the number of rows: \n"))
    m = int(input("Please give the number of columns: \n"))
    print("Now please input your matrix, separated by space\n")
    array = np.array([input().strip().split() for _ in range(n)], int)
    return array

def add_matrix(vector1,vector2):
    return vector1 + vector2

def subt_matrix(vector1,vector2):
    return (vector1-vector2)
    

def mult_matrix(vector1,vector2):
    return (vector1*vector2)
   

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = ' ')
            
        print()


def calculate():
    
    print()
    print("Here are some operations you can choose. Please select the correct NUMBER\n")
    print("Here are some matrix operations you can choose\n")
    choice = input("1) Addition 2) Subtraction 3) Multiplication")
    
    if choice == '1' or choice == '2' or choice == '3':
        arr1 = matrix_create()
        arr2 = matrix_create()
        
        print("----Your result is----")
        if choice == '1':
            res = add_matrix(arr1, arr2)
        if choice == '2':
            res = mult_matrix(arr1, arr2)
        if choice == '3':
            res == subt_matrix(arr1, arr2)
    

            
    
    print_matrix(res)