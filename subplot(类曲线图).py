import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

##指定切分区域的位置
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

#在subplot上作图
##感觉这是用numpy去创建数据???
random_arr = np.random.randn(100)

#print random_arr

##默认是在最后一次使用subplot的位置上作图.但是在jupter notebook里可能显示有误
plt.plot(random_arr)

##可以指定在某个或者多个subplot位置上作图
#ax1 = fig.plot(random_arr)
#ax2 = fig.plot(random_arr)
#ax3 = fig.plot(random_arr)

plt.show()
