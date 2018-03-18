import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y1,y2 = np.random.randint(1,25,size=(2,5))
width = 0.25
ax = plt.subplot(1,1,1)
ax.bar(x,y1,width,color='r')
ax.bar(x+width,y2,width,color='g')
ax.set_xticks(x+width)
ax.set_xticklabels(['a','b','c','d','e'])
plt.show()
