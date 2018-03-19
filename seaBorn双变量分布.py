import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats, integrate
import seaborn as sns
%matplotlib inline

def_obj1 = pd.DataFrame({"x":np.random.randn(500),
                        "y":np.random.randn(500)})

def_obj2 = pd.DataFrame({"x":np.random.randn(500),
                        "y":np.random.randint(0,100,500)
                        })
                        
                        
##例子1--散布图
sns.jointplot(x="x",y="y",data=def_obj1)

##例子2--二维直方图
sns.jointplot(x="x",y="y",data=def_obj2,kind="hex")

