import numpy as np

output = []
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = np.array(a)

# 换列
# b[:, [0, 2]] = b[:, [2, 0]]
# b[:, [1, 3]] = b[:, [3, 1]]
# print(b)


arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr)
arr = np.delete(arr, 0, axis=1)
print(arr)