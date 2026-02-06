Introduction to NumPy Arrays
This project provides an introduction to working with NumPy arrays in Python. It covers basic operations such as creating arrays, performing arithmetic operations, and exploring some essential methods provided by the NumPy library.

Table of Contents
Installation
Usage
Basic Operations
Methods Explained
Contributing
License
Installation
To run this code, ensure you have Python installed along with the NumPy package. Install NumPy via pip:

bash
Копировать
pip install numpy
Usage
Simply execute the script in your preferred Python environment. The script demonstrates various aspects of working with NumPy arrays including creation, manipulation, and transformation.

python
Копировать
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr3 = np.arange(10)

# Arithmetic operations
addition = arr1 + arr2[0]
subtraction = arr1 - arr2[0]
multiplication = arr1 * arr2[0]
division = arr1 / arr2[0]

# Methods like reshape(), flatten(), etc.
reshaped_array = arr3.reshape((2, 5))
flattened_array = arr2.flatten()

# Other attributes and methods
print("Shape of arr2:", arr2.shape)
print("Size of arr2:", arr2.size)
print("Type of elements in arr2:", arr2.dtype)

# Sorting and finding unique values
sorted_array = np.sort(arr2, axis=None)
unique_values = np.unique(arr2)
Basic Operations
The following operations are demonstrated in the example:

Creating One-Dimensional and Two-Dimensional Arrays: Using np.array().
Arithmetic Operations: Adding, subtracting, multiplying, dividing arrays element-wise.
Reshaping Arrays: Changing the shape of an array with reshape().
Flattening Multi-Dimensional Arrays: Converting them to 1D arrays using flatten() or ravel().
Sorting Elements: Using np.sort().
Finding Unique Values: With np.unique().
Methods Explained
Here’s what each method does:

reshape(): Changes the shape of an array without altering its content.
flatten(): Flattens a multi-dimensional array into a 1D array.
ravel(): Also converts multi-dimensional arrays to 1D, similar to flatten().
shape: Provides information about the dimensions of the array.
size: Counts the total number of elements in the array.
dtype: Shows the data type of elements in the array.
sort(): Sorts the array along a specific axis.
unique(): Extracts unique values from the array.
Contributing
Feel free to contribute to this project by submitting pull requests. Any improvements, bug fixes, or additional examples will be appreciated.

License
This project is licensed under the MIT License—see the LICENSE file for details.
