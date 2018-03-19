##注意,是在ipython3-notebook下面执行的
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

##注意,x1或者x2,随便一个,不能同时运行两个.不行图形就会出现问题.!

x1 = np.random.normal(size=1000)
sns.distplot(x1)

#x2 = np.random.randint(0,100,500)
#sns.distplot(x2)
