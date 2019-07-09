import matplotlib.pyplot as plt
import numpy as np
a=np.sin(np.arange(1,21,.73))
b=np.cos(np.arange(1,21,.73))
plt.scatter(a,b)
plt.show()