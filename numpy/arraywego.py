#!/usr/bin/python3
"""Alta3 Research | treich@alta3.com
  Numpy arrays and operations"""

import numpy as np
np.random.seed(0)
# Use the randint function to generate 1-, 2-, and 3-dimensional arrays
arr1d = np.random.randint(11, size=5) # 1-D array of 5 random integers between 0-10
arr2d = np.random.randint(11, size=(2, 3)) # 2-D array  spanning 2 rows, 3 cols
arr3d = np.random.randint(11, size=(2, 3, 4)) # 3-D array containing two 2-D arrays of 3 rows, 4 cols each 

print("One-dimensional array:", arr1d, sep="\n")
print("Two-dimensional array:", arr2d, sep="\n")
print("Three-dimensional array:", arr3d, sep="\n")
print("First element of arr1d is:", arr1d[0])
print("Element in position (0,0) of arr2d is:", arr2d[0,0])
print("Element in position (0,0,0) of arr3d is:", arr3d[0,0,0])
# Scalar operations on arrays vs. lists

# when we perform an operation on the array, like multiplication
# we end up effecting every element within the array
print(arr1d)   # display the 1-D array
print(arr1d*2) # multiply *each element* within the array by 2

# lists are different, in that they are treated as a single unit
# here we multiply by 2, which does not effect the data in the list
# but instead doubles the size of the list
print(list(arr1d)*2) # convert arr1d into a list, then multiply that list by 2

# CHALLENGE 01 - create a 4-d array using dimensions of your choosing
arr4d = np.random.randint(11, size=(2, 2, 3, 4)) # 4-D array
print("Four-dimensional array:", arr4d, sep="\n")

# CHALLENGE 02 - use array indexing to grab the last value of each array
print("Last element of arr1d", arr1d[-1])
print("Last element of arr2d", arr2d[-1,-1])
print("Last element of arr3d", arr3d[-1,-1,-1])
print("Last element of arr4d", arr4d[-1,-1,-1,-1])

# CHALLENGE 03 - create a second 1-d array of the same size
print("\nCustomization 03")
arr1d_sequel = np.random.randint(11, size=5) # create 1-D array of the same size as arr1d
print("Original arr1d:", arr1d, sep="\n")
print("New arr1d_sequel:", arr1d_sequel, sep="\n")
print("Result of addition:", arr1d_sequel + arr1d, sep="\n")
print("Result of multiplication:", arr1d_sequel * arr1d, sep="\n")

