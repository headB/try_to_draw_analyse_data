import numpy as np
##读取列名,即第一行数据

filename = './presidential_polls.csv'

with open(filename,'r') as f:
    col_names_str = f.readline()[:-1]##表示不读取末尾的换行符
    
##
col_name_list = col_names_str.split(',')

#print(col_name_list)

##使用的列名,结束时间,  等等标题
use_col_name_list = ['enddate','rawpoll_clinton','rawpoll_trump','adjpoll_clinton','adjpoll_trump']

##获取相应列名的索引号
use_col_index_list = [col_name_list.index(use_col_name) for use_col_name in use_col_name_list ]

#print(use_col_index_list)

data_array = np.genfromtxt(filename,
                          delimiter=',',##分隔符
                           ##skuprows=1,##就是跳过第一行
                           dtype=str,
                           usecols=use_col_index_list
                          )

##去掉第一行
data_array = data_array[1:]

##打印ndarray数据

print(data_array[1:],data_array.shape)
