import numpy as np

# 1-D array containing the values 1, 2, 3, 4, 5
arr1 = np.array([1, 2, 3, 4, 5])
print("One Dimensional array:")
print(arr1)

# 2-D array containing two arrays with the values 1,2,3 and 4,5,6
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Two Dimensional array:")
print(arr2)

# 3-D array containing two arrays with the values 1,2,3 and 4,5,6
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
])
print("Three Dimensional array:")
print(arr3)

# (Reshaping) Convert the following 1-D array with 9 elements into a 3x3 2D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarr = arr.reshape(3, 3)
print("Reshaping an array:\n", newarr)

# (Slicing) create a 1D array
array1 = np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])

# Slice array1 from index 2 to index 6 (exclusive)
print("Slice from index 2 to index 6:", array1[2:6])  # [5 7 8 9]

# Slice array1 from index 0 to index 8 (exclusive) with a step size of 2
print("Slice from index 0 to index 8 (exclusive) with step size 2:", array1[0:8:2])  # [1 5 8 2]

# Slice array1 from index 3 up to the last element
print("Slice array1 from index 3 up to the last element:", array1[3:])  # [7 8 9 2 4 6]

# Slice the last 3 elements of the array using the start parameter
print("Slice the last 3 elements of the array:", array1[-3:])  # [2 4 6]

# Slice elements from 2nd-to-last to 4th-to-last element
print("Slice elements from 2nd-to-last to 4th-to-last element:", array1[-5:-2])  # [9 2 4]

# Array Indexing
array1 = np.array([1, 3, 5, 7, 9])
# Access numpy elements using index
print("Position 0:", array1[0])  # prints 1
print("Position 2:", array1[2])  # prints 5
print("Position 4:", array1[4])  # prints 9

# Change the value of the third element (index 2)
array1[2] = 12
print("After modifying third element:", array1)  # prints [1 3 12 7 9]

# Negative Indexing
print("Negative Indexing:", array1[-2])  # prints 7

# Indexing in 2D array
array2 = np.array([
    [1, 3, 5],
    [7, 9, 2],
    [4, 6, 8]
])
print("Indexing in 2D Array (row 1, col 0):", array2[1, 0])  # prints 7
print("Indexing in 2D Array (row 2, col 1):", array2[2, 1])  # prints 6
