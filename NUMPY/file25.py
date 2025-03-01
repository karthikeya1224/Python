import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.size)
# print(arr.nbytes)
# print(arr.dtype)
# print(arr[0,3])
# print(arr[0])
# print(arr[0,:])
# print(arr[::-1])
# print(arr[:,2])
# print(arr[1,:])
# arr=np.zeros([3,3])
# print(arr)
# arr=np.full((2,3),75)
# print(arr)
# arr=np.random.rand(0,4)
# print(arr)
# arr=np.random.randint(0,4,size=(2,3))
# print(arr)
# arr=np.random.rand(3, 3)
# arr=np.random.randint(1, 100, (3,3))
# arr=np.random.randn(3) 
# print(arr)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)  # Matrix multiplication
print(np.dot(A, B))  # Alternative method

