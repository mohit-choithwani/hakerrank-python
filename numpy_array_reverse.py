Numpy.flip to reverse the numpy array

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    num_arr = numpy.array(arr, float)
    return numpy.flip(num_arr, axis=0)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


##Numpy Reshape operation

import numpy

N = list(map(int, input().split(' ')))

num_arr = numpy.array(N)
num_arr = num_arr.reshape((3,3))

print(num_arr)

#Numpy flatten and transpose

import numpy

row_and_column = list(map(int, input().split(' ')))

empty_list = []

for i in range(int(row_and_column[0])):
    row_elements = list(map(int, input().split(' ')))
    empty_list.append(row_elements)
    
num_arr = numpy.array(empty_list)

print(num_arr.T)
print(num_arr.flatten())
