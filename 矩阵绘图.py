import matplotlib.pyplot as plt
import numpy as np

m = np.random.rand(10,10)
print(m)

#plt.imshow(m,interpolation='nearest',cmap=plt.cm.afmhot)
plt.imshow(m,interpolation='nearest',cmap=plt.cm.Accent)
plt.colorbar()
plt.show()
