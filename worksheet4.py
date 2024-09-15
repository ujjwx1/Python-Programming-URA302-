import numpy as np

# 1.1 
array1d = np.arange(5, 26)
print("1D array:", array1d)

# 1.2 
array2d = np.random.randint(10, 51, (3, 4))
print("2D array:\n", array2d)


# 2.1 
print("Shape:", array1d.shape)
print("Size:", array1d.size)
print("Data type:", array1d.dtype)

# 2.2 
print("Shape:", array2d.shape)
print("Size:", array2d.size)
print("Data type:", array2d.dtype)


array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])

# 3.2 
print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Element-wise multiplication:", array1 * array2)
print("Element-wise division:", array1 / array2)


array2d = np.arange(1, 10).reshape(3, 3)

# 4.2 
result = array2d * 5
print("Result:\n", result)



array2d = np.arange(10, 26).reshape(4, 4)

# 5.2 
second_row = array2d[1, :]
last_column = array2d[:, -1]
print("Second row:", second_row)
print("Last column:", last_column)

# 5.3 
array2d[0, :] = 0
print("Modified array:\n", array2d)



array1d = np.random.randint(20, 41, 10)

# 6.2 
elements_greater_than_30 = array1d[array1d > 30]
print("Elements greater than 30:", elements_greater_than_30)


array1d = np.arange(11, 23)

# 7.2 
array2d = array1d.reshape(3, 4)
print("Reshaped array:\n", array2d)



matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# 8.2 
print("Matrix multiplication:\n", np.dot(matrix_a, matrix_b))
print("Transpose of Matrix A:\n", matrix_a.T)




array1d = np.random.randint(10, 61, 15)

# 9.2 
mean = np.mean(array1d)
median = np.median(array1d)
std_dev = np.std(array1d)
print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", std_dev)



matrix_a = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])

# 10.2 
determinant = np.linalg.det(matrix_a)
inverse = np.linalg.inv(matrix_a)
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)

print("Determinant:", determinant)
print("Inverse:\n", inverse)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)