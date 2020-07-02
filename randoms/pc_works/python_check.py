import numpy as np
import matplotlib.pyplot as plt

a=np.cos(np.arange(1.2,42, 0.74))
b=np.sin(np.arange(1.2,42, 0.74))

plt.figure(figsize=(9,6))

plt.subplot(221)
plt.title("a,b")
plt.plot(a,b)

plt.subplot(222)
plt.title("b,a")
plt.plot(b,a)

plt.subplot(223)
plt.title("a")
plt.plot(a)

plt.subplot(224)
plt.title("b")
plt.plot(b)
plt.show()
