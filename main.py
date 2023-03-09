import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])

print(x)
print(type(x))

arr = np.array(10)

print(arr)

y = np.array([[1, 2, 5], [3, 9, 4]])
print(y)

z = np.array([[[1, 2], [3, 4]], [[5, 9], [7, 8]]])
print(z)

print(x.ndim, arr.ndim, y.ndim, z.ndim)

# index
print(x[0])
print(y[1, 1])
print(z[0, 1, 0])

# slicing
print(x[:-1])
print(x[:3])
print(x[1:])

print(x[::2])

print(y[1, 0:2])

# copy
copy = x.copy()
copy[0] = 24

print(x)
print(copy)

# view
view = x.view()
view[0] = 9

print(x)
print(view)

# shape
print(z.shape)

# reshape
print(x)
print(view.reshape(2, 3))

# search
par = np.array([1, 2, 3, 2, 5, 2 ])

print(np.where(par == 2))

print(np.where(par % 2 == 1))

# split
parList = np.array_split(par, 3)

for par in parList:
    print(par)

# sort
num = np.array([4, 2, 5, 1, 3, 7])

print(np.sort(num))

boll = np.array([True, False, False, True])

print(np.sort(boll))

str = np.array(['Pasta', 'apple', "Cake"])

print(np.sort(str))