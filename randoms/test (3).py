import numpy as np
import matplotlib.pyplot as plt

a=range(1,10)
b=range(15,24)

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x,y)
plt.plot(a,b)
plt.show()



import numpy as np
b = np.array([100], dtype = int) 
print ('The second array is:' )
print (b)

import matplotlib.pyplot as plt
x=np.arange(0,100, 15)
print (x)
y=np.delete(x,[1,5])
print(y)
plt.plot(np.sin(y*np.pi/180))
plt.show()

a=[0,1,0,1,0]
b=[-2,-1,0,1,2]
plt.plot(a,b)
plt.show()