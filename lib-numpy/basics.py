import numpy as np 

a = np.array([0, 1, 2, 3, 4])
a.size
a.ndim
a.shape

a[0]
a[1:4]
a[1:5:2]

a[1:5] = 100  #assings 100 to all elements in slice

#BASIC OPERATIONS ON VECTORS/ARRAYS
########################################################################################
u = np.array([1,0])
z = np.array([0,2])

z = u + v
z = u - v
x = u + 1  #adding constant / broadcasting (add constant to each element of the array)
x = u * 2  #multiplication
x = u * v  #product of two vectors (arrays)
result = np.dot(u,v)  #dot product / inner product / projection product (iloczyn skalarny)

#FUNCTIONS
########################################################################################

#Below works just like using mathematical operators described above
np.add(u,v)  #[1,0] + [0,1] = [1,1]
np.subtract(u,v)
np.multiply(u,v)
np.divide(u,v)

a.mean()
a.max()
a.min()
a.sum()
a.sin()
a.std()
#and many others

a.linspace(start, end, num=number of samples)  #returns evenly spaced numbers over specified interval
a.linspace(-2, 2, num=5)

