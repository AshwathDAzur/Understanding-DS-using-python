import numpy as np
# print("Path of the Package : ",np.__file__)
# print("Numpy Version : ",np.__version__)


# 1D Array

arr = np.array([3.6,"1", 2.8, True, 4, 5])
print("Array : ",arr)
for item in arr:
    print(type(item))

arr = np.array([3.6,"1", 2.8, True, 4, 5])
print("Array : ",arr[len(arr)-1])
for i in range(len(arr)):
    print(arr[i])

m = np.zeros(5) # 1D Array with 5 elements as 0
print(m)
n = np.ones(5) # 1D Array with 5 elements as 1
print(n)
