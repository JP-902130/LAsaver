import numpy as np
from numpy.core.numeric import cross
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
    return res.T

#proj perp
def proj_vector(vector,d):
    numrator = dot_vector(vector,d)
    denominator = magni_vector(d)**2
    proj = ((numrator/denominator)*d)
    return  proj

def perp_vector(vector,d):
    proj = proj_vector(vector,d)
    perp = vector-proj
    return perp

def print_vector(vector):
   
    for j in range(len(vector)):   
        print(vector[j][0], end = ' ')
            
        print()

def calculate():
    
    print()
    print("Here are some operations you can choose. Please select the correct NUMBER\n")
    print("Here are some vector operations you can choose\n")
    choice = input("1) Addition 2) Multiplication  3) Subtraction 4) Norm 5) Dot Product 6) Cross Product 7) Projection 8) Perpendicular\n")
    
    if choice == '1' or choice == '3' or choice == '6' or choice =='7' or choice =='8':
        arr1 = vector_create()
        arr2 = vector_create()
        
        
        print("----Your result is----")
        if choice == '1':
            res = add_vector(arr1, arr2)
    
        elif choice == '3':
            res = subt_vector(arr1, arr2)

        elif choice == '6':
            res = cross_vector(arr1,arr2)
        
        elif choice == '7':
            res = proj_vector(arr1,arr2)
        
        elif choice =='8':
            res = perp_vector(arr1,arr2)
            
        print_vector(res)

    elif choice =='2':
        n = int(input("give the coefficient\n"))
        arr1 = vector_create()
        res = mult_vector(n,arr1)
        print("----Your result is----")
        print_vector(res)    
            
    elif choice == '4':
        arr2 = vector_create()
        res = magni_vector(arr2)    
        print("----Your result is----")
        print (res)   
    
    elif  choice =='5':
        Arr1 = vector_create()
        Arr2 = vector_create()
        print("----Your result is----")
        
        res = dot_vector(Arr1,Arr2)
        
        print(res)

  


