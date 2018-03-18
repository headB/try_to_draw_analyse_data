import matplotlib.pyplot as plt 
import numpy as np

fig,subplot_arr = plt.subplots(2,2)
##bins为显示个数,一般小于等于数值个数
subplot_arr[0,0].hist(np.random.randn(100),bins=10,color='b',alpha=0.3)
subplot_arr[0,1].hist(np.random.randn(100),bins=10,color='g',alpha=0.3)
subplot_arr[1,0].hist(np.random.randn(100),bins=10,color='r',alpha=0.3)
subplot_arr[1,1].hist(np.random.randn(100),bins=10,color='pink',alpha=0.3)
plt.show()
