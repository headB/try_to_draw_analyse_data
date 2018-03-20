import numpy as np

fileName = './presidential_polls.csv'

##通过loadtxt()读取本地csv文件

data_array = np.loadtxt(fileName,delimiter=',',##f分隔符
                        dtype=str,##数据类型,数据是unicode字符串
                        usecols=(0,2,3))##指定读取的序号

##打印ndarray数据,保留第一行
print(data_array)

