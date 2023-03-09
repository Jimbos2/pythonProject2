import numpy as np

# of each element in 2 arrays

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

print(np.add(arr1,arr2))  # of each element in 2 arrays

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print(np.subtract(arr1,arr2))  # of each element in 2 arrays

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

print(np.multiply(arr1,arr2))  # of each element in 2 arrays

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print(np.divide(arr1,arr2))  # of each element in 2 arrays

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

print(np.power(arr1,arr2))  # of each element in 2 arrays

arr1 = np.array([10, 10, 10, 10])
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([-1, -2, -3, -4])

print(np.mod(arr1,arr2))  # of each element in 2 arrays
print(np.absolute(arr3))  # of each element in 2 arrays

arr = np.array([1.23, 3.442, 6.747])

print(np.trunc(arr))
print(np.fix(arr))
print(np.around(arr, 1))
print(np.floor(arr))
print(np.ceil(arr))  # of each element in 2 arrays

# log
arr = np.array([1, 2, 3, 4])

print(np.log(arr))
print(np.log2(arr))
print(np.log10(arr))



arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print(np.sum([arr1, arr2]))  # sum of all elements from all arrays
print(np.sum([arr1, arr2], axis = 1))  # sum of all elements in each array

print(np.cumsum(arr))  # addition of each element with previous one

# product
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print(np.prod([arr1, arr2]))  # multiplication of all the elements from all arrays
print(np.prod([arr1, arr2], axis=1))  # multiplication of all the elements in each array

print(np.cumprod([arr1]))  # multiplication of each element with previous one



arr = np.array([1, 2, 3, 4, 5])

print(np.lcm.reduce(arr))  # Lowest Common Multiple (LCM)
print(np.gcd.reduce(arr))  # Greatest Common Denominator (GCD)

arr = np.array([np.pi/2, np.pi/3, np.pi/4])

print(np.around(np.sin(arr), 8))
print(np.around(np.cos(arr), 8))

arr = np.array([90, 180, 360])

arr = np.deg2rad(arr)
print(arr)

arr = np.rad2deg(arr)
print(arr)

print(np.hypot(3, 4))
