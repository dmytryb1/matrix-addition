import random

#Code seems solid, but if i generate two matrices that are of different sizes, then I can catch an Index
#out of range error. One fix could be to make sure the matrix gets added to the second one with the top left corner
#being of priority and everything that falls out gets filled as if it were zeros and added on by the extra slots on the
#bigger. For example
#    1  1  +  1  1  1  =  2  2  1
#    1  1     1  1  1     2  2  1
#    1  1                 1  1  0*
#  something of the sort... though that zero does kind of appear out of nowhere...

#==============================================================

def matrix1_create():
    print('Lets create the first Matrix, enter the dimensions.')
    m = int(input('m = '))
    n = int(input('n = '))
    matrix_1 = []
    matrix_1=[[random.randint(-99, 100) for j in range(n)] for i in range(m) ]
    print('Matrix # 1:')
    for a in matrix_1:
        print(a)
    
    return matrix_1

#==============================================================

def matrix2_create():
    print('Lets create the second Matrix, enter the dimensions.')
    m = int(input('m = '))
    n = int(input('n = '))
    matrix_2 = []
    matrix_2=[[random.randint(-99, 100) for j in range(n)] for i in range(m) ]
    print('Matrix # 2:')
    for b in matrix_2:
        print(b)
    return matrix_2

#==============================================================

def matrix_add():
    matrix_1 = matrix1_create()
    matrix_2 = matrix2_create()
    result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
    print('This is both matrixes added together:')
    for r in result:
        print(r)
    return result

#==============================================================

matrix_add()

