import numpy as np


# the function ask for input from user and return a matrix object
def matrix_create():
    n = int(input("Please give the number of rows: \n"))
    m = int(input("Please give the number of columns: \n"))
    print("Now please input your matrix, separated by space\n")
    array = np.array([input().strip().split() for _ in range(n)], int)
    return array
# matrix addtion, subtraction and multiplication
def add_matrix(vector1,vector2): #1
    return vector1 + vector2

def subt_matrix(vector1,vector2): #2
    return (vector1-vector2)
    

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

'''
def magni_vector(vector1):
   return (np.linalg.norm(vector1))
'''
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = ' ')
            
        print()
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i],)
        

def calculate():
    
    print()
    print("Here are some operations you can choose. Please select the correct NUMBER\n")
    print("Here are some matrix operations you can choose\n")
    choice = input("1) Addition 2) Subtraction 3) Multiplication 4) Transpose 5) Trace 6) Rank 7) RREF\n")
    
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
            return 0
    else:
        arr1 = matrix_create()
        if choice == '4':
            res = matrix_transpose(arr1)
        if choice == '5':
            res = matrix_trace(arr1)
            print("The result is:")
            print(res)
            return 0
        if choice == '6':
            res = matrix_rank(arr1)
            print("The result is:")
            print(res)
            return 0
        if choice == '7':
            res = matrix_rref(arr1)
    
    print_matrix(res)
    
   