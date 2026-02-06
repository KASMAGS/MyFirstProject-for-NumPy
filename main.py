import numpy as np

# Create a one-dimensional array using the list [1,2,3,4,5].
arr1 = np.array([1,2,3,4,5])
print("One-dimensional array:")
print(arr1)      # Output: [1 2 3 4 5]

# Create a two-dimensional array using nested lists [[1,2,3,4,5],[6,7,8,9,10]].
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("\nTwo-dimensional array:")
print(arr2)      # Output: [[1 2 3 4 5]
                 #            [6 7 8 9 10]]

# Generate an array of numbers from 0 to 9 using arange() function.
arr3 = np.arange(10)
print("\nArray generated using arange():")
print(arr3)      # Output: [0 1 2 3 4 5 6 7 8 9]

# Perform arithmetic operations on arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
addition = a + b
print("\nElement-wise Addition:", addition)       # Output: [5 7 9]

# Element-wise subtraction
subtraction = a - b
print("Element-wise Subtraction:", subtraction) # Output: [-3 -3 -3]

# Element-wise multiplication
multiplication = a * b
print("Element-wise Multiplication:", multiplication) # Output: [4 10 18]

# Element-wise division
division = a / b
print("Element-wise Division:", division)          # Output: [0.25 0.4    0.5 ]

# Some useful methods in NumPy explained:

# Method: reshape()
# Reshape changes the dimensions of an array without changing its data.
reshaped_array = arr3.reshape((2, 5))    # Convert 1D array to 2D array with 2 rows and 5 columns
print("\nReshaped Array:\n", reshaped_array)

# Method: flatten() or ravel()
# These methods convert multi-dimensional arrays back to a flattened 1D array.
flattened_array = arr2.flatten()
raveled_array = arr2.ravel()
print("\nFlattened Array:", flattened_array)    # Output: [1 2 3 4 5 6 7 8 9 10]
print("Ravelling the same array gives:", raveled_array)    # Same output as above

# Method: shape
# Shape returns the current dimensions of the array.
print("\nShape of arr2:", arr2.shape)    # Output: (2, 5)

# Method: size
# Size tells us how many elements are present in the array.
print("Size of arr2:", arr2.size)    # Output: 10

# Method: dtype
# Dtype informs about the type of elements stored in the array.
print("Type of elements in arr2:", arr2.dtype)    # Output: int64

# Method: sort()
# Sort sorts the array along a specified axis.
sorted_array = np.sort(arr2, axis=None)    # Flatten and then sort
print("\nSorted Array:", sorted_array)    # Output: [1 2 3 4 5 6 7 8 9 10]

# Method: unique()
# Unique finds all unique values within an array.
unique_values = np.unique(arr2)
print("\nUnique Values:", unique_values)    # Output: [1 2 3 4 5 6 7 8 9 10]
