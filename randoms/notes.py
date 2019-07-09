#numpy notes
#-----------

#ch.4
a1 = np.array(rage(24))

#flattens array to one dim
a2 = A.flatten()

#eturns one dim array
a1.ravel()

#reshape array
X = np.array(range(24))
Y = X.reshape((3,4,2))

#array concatenation
x = np.array([11,22])
y = np.array([18,7,6])
z = np.array([1,3,5])
c = np.concatenate((x,y,z))

#adding New Dimensions
x = np.array([2,5,18,14,4])
y = x[:, np.newaxis]

#ector Stacking
A = np.array([3, 4, 5])
B = np.array([1,9,0])
print(np.row_stack((A, B)))
print(np.column_stack((A, B)))

#repeating Patterns, The "tile" Method
x = np.array([ [1, 2], [3, 4]])
np.tile(x, (3,4))