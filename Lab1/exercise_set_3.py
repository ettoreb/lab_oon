import numpy as np

# Create a 4X2 integer array and print its attributes
array1 = np.empty([4, 2], dtype=np.uint16)

print(array1)
print("\ nPrinting numpy array attributes")
print("Array Shape is", array1.shape)
print("Array dimensions are", array1.ndim)
print("Length of each element of array in bytes is", array1.itemsize)

# Create a 5X2 integer array from a range between 100 to 200 such that the
# difference between each element is 10

sample_array = np.arange(100, 200, 10)  # start , stop , step
sample_array = sample_array.reshape(5, 2)
print(sample_array)

# Given the following NumPy array, return the array of items in the third
# column of each row
sample_array = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

print(sample_array)
new_array = sample_array[:, 2]
print(new_array)

# Given the following numPy array, return the array of the odd rows and
# the even columns

sample_array = np.array([[3, 6, 9, 12], [15, 18, 21, 24],
                         [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

print(sample_array)

new_array = sample_array[::2, 1::2]
print(new_array)

# Add the following two numPy arrays and modify the result array by calculating the square root of each element

array1 = np.array([[5, 6, 9], [21, 18, 27]])
array2 = np.array([[15, 33, 24], [4, 7, 1]])
result_array = array1 + array2

print(result_array)
for num in np.nditer(result_array, op_flags=["readwrite"]):
    num[...] = np.sqrt(num)
print("\ nThe result array after calculating the square root of all elements")
print(result_array)

# Sort following NumPy array:

sample_array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print(sample_array)
line_array = sample_array.reshape(1, np.prod(sample_array.shape))
print(line_array)

sort_line_array = np.sort(line_array)
print(sort_line_array)

sort_array = sort_line_array.reshape(sample_array.shape)
print(sort_array)

# Given the following NumPy array, print the max of axis 0 and the min of
# axis 1
sample_array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sample_array)
min_of_axis1 = np.amin(sample_array, 1)
print(min_of_axis1)
max_of_axis1 = np.amax(sample_array, 0)
print(max_of_axis1)

# Given the following numPy array, delete the second column and insert the
# following new column in its place.

new_column = [10, 10, 10]
sample_array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sample_array)
sample_array = np.delete(sample_array, 1, axis=1)
print(sample_array)
arr = np.array([[10, 10, 10]])
sample_array = np.insert(sample_array, 1, arr, axis=1)
print(sample_array)
