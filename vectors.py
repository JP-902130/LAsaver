import numpy as np

def vector_input():
    n = int(input("what is the row number of your vector?\n"))
    vector1 = np.ones((n,1))
    for i in range(n):
        vector1[i,0] = int(input("now type in number in each row\n"))
    print("your {} dimension vector is\n {}".format(n,vector1))
    return vector1
       

   

def add_vector(vector1,vector2):
    if (vector1+vector2):
        return (vector1+vector2)
    else:
        return ("Error")

def subt_vector(vector1,vector2):
    if (vector1-vector2):
        return (vector1-vector2)
    else:
        return ("Error")

def mult_vector(vector1,vector2):
    if (vector1*vector2):
        return (vector1*vector2)
    else:
        return ("Error")

def magni_vector(vector1):
   return (np.linalg.norm(vector1))



def calculate_vector():
    print("Here are some operations you can choose. Please select the correct NUMBER")
    choice = input(" 1) addtion\n 2) multiplication\n 3) exponentential\n 4) division\n 5) Modulus\n ")
 

num_vector = int(input("give the number of vectors you will create?\n"))
array = [[1]]*num_vector
for i in range(num_vector):
    
    array[i]=(vector_input())
print(array)
print (array[1]+array[0])
x = add_vector(array[1],array[0])
print (x)

    

