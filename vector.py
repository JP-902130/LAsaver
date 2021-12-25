import numpy as np
from numpy.core.numeric import cross
import sympy as sy
#functions:
#+-*
# moudlus,dot, cross
# check parallel, find theta, find orthogonal
#parallelgram area
# proj, perp
#volume


#special input process
def vector_create():
    n = int(input("Please give the number of rows: \n"))
    print("Now please input your vector, separated by space\n")
    array = np.array([input().strip().split() for _ in range(n)], int)
    return array

#vector addition/subtraction from numpy
def add_vector(vector1,vector2):
    return vector1 + vector2

def subt_vector(vector1,vector2):
    return (vector1-vector2)
    
#vector multiolication/moudlus from numpy
def mult_vector(n,vector2):
    return (n*vector2)


def magni_vector(vector1):
   return (np.linalg.norm(vector1))

# dot, cross
def dot_vector(vector1,vector2):
    arr2 = np.squeeze(np.asarray(vector1))
    arr1 = np.squeeze(np.asarray(vector2))
    return np.dot(arr1,arr2)

def cross_vector(vector1,vector2):
    res =  np.cross(vector1.T,vector2.T)
    res = res[0]
    return res.T

# proj, perp
def proj_vector(vector,d):
    numrator = dot_vector(vector,d)
    denominator = magni_vector(d)**2
    proj = ((numrator/denominator)*d)
    return  proj

 
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
    print("Here are some vector operations you can choose\n")
    choice = input("1) Addition 2) Multiplication  3) Subtraction 4) Norm 5) Dot Product 6) Cross Product\n")
    
    if choice == '1' or choice == '3' or choice == '6':
        arr1 = vector_create()
        arr2 = vector_create()
        
        
       
        if choice == '1':
            res = add_vector(arr1, arr2)
    
        elif choice == '3':
            res = subt_vector(arr1, arr2)

        elif choice == '6':
            res = cross_vector(arr1,arr2)
            
            
        
        

    elif choice =='2':
        n = int(input("give the coefficient\n"))
        arr1 = vector_create()
        res = mult_vector(n,arr1)
       
            
            
    elif choice == '4':
        arr2 = vector_create()
        res = magni_vector(arr2)    
  
           
    
    elif  choice =='5':
        Arr1 = vector_create()
        Arr2 = vector_create()
      
        
        res = dot_vector(Arr1,Arr2)
        
    if type(res[0]) == np.int64:
        print_matrix(res)
    else: 
        print_arr(res)

        

vector = vector_create()
d = vector_create()
res = proj_vector(vector,d)
if type(res[0]) == np.int64:
        print_matrix(res)
else: 
        print_arr(res)
