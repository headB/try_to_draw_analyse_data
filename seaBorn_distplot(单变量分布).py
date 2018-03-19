##注意,是在ipython3-notebook下面执行的,
##或者都可以在ipython运行,不过启动的时候,命令变了,ipython qtconsole这样启动.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

##注意,x1或者x2,x3等等,几个画图都是需要注释,只能运行其中一个,随便一个,不能同时运行两个.不行图形就会出现问题.!

x1 = np.random.normal(size=1000)
sns.distplot(x1)

x2 = np.random.randint(0,100,500)
sns.distplot(x2)

##其他测试的画图
x3 = np.random.randint(0,10,100)
sns.distplot(x3,color='b',bins=10,rug=True)
sns.distplot(x3,hist=False)


##尝试画直方图
##直方图
sns.distplot(x1,bins=20,kde=False,rug=True)

## 核密度估计 sns.distplot(hist=False) 或 sns.kdeplot()
sns.distplot(x2,hist=False,rug=True)
