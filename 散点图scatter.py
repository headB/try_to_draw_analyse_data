import matplotlib.pyplot as plt
import numpy as np

##绘制散点图
x = np.arange(50)
y = x+5*np.random.rand(50)

plt.scatter(x,y)
plt.show()
