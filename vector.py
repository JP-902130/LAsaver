import numpy as np


def vector_create():
    n = int(input("Please give the number of rows: \n"))
    print("Now please input your vector, separated by space\n")
    array = np.array([input().strip().split() for _ in range(n)], int)
    return array

def add_vector(vector1,vector2):
    return vector1 + vector2

def subt_vector(vector1,vector2):
    return (vector1-vector2)
    

def mult_vector(n,vector2):
    return (n*vector2)


def magni_vector(vector1):
   return (np.linalg.norm(vector1))

def dot_vector(vector1,vector2):
    return np.dot(vector1,vector2)

def print_vector(vector):
    for i in range(len(vector)):
        for j in range(len(vector[0])):
            print(vector[i][j], end = ' ')
            
        print()

def calculate():
    
    print()
    print("Here are some operations you can choose. Please select the correct NUMBER\n")
    print("Here are some vector operations you can choose\n")
    choice = input("1) Addition 2) Multiplication  3) Subtraction 4) Module 5) Dot Product\n")
    
    if choice == '1' or choice == '2' or choice == '3' or choice =='5':
        arr1 = vector_create()
        arr2 = vector_create()
        
        print("----Your result is----")
        if choice == '1':
            res = add_vector(arr1, arr2)
        if choice == '2':
            res = mult_vector(arr1, arr2)
        if choice == '3':
            res = subt_vector(arr1, arr2)
        if choice =='5':
            res = dot_vector(arr1,arr2)
        
        print_vector(res)
        
            
    elif choice == '4':
        arr3 = vector_create()
        res = magni_vector(arr3)    
        print (res)   
    
    

     