import zipfile
import os 
import pandas as pd
import matplotlib.pyplot as plt

##处理zip文件...问题是,,,,自己不可以事先解压的吗?哎呀,真伤脑筋.
def unzip(zip_filepath,dest_path):
    with zipfile.ZipFile(zip_filepath) as zf:
        zf.extractall(path=dest_path)
        
        
def get_dataset_filename(zip_filepath):
    with zipfile.ZipFile(zip_filepath) as zf:
        return zf.namelist()[0]
    
    
def run_main():
    
    ##不要
    #dataset_path = './'
    
    ##上面的什么解压缩代码,哎呀,为了节省时间,不写了,节省时间吧.
    ##还是写吧.不过就是直接复制了.!!
    
    
    # 声明变量
    dataset_path = './data'  # 数据集路径
    zip_filename = 'open-food-facts.zip'  # zip文件名
    zip_filepath = os.path.join(dataset_path, zip_filename)  # zip文件路径
    dataset_filename = get_dataset_filename(zip_filepath)  # 数据集文件名（在zip中）
    dataset_filepath = os.path.join(dataset_path, dataset_filename)  # 数据集文件路径

    print('解压zip...', end='')
    unzip(zip_filepath, dataset_path)
    print('完成.')    
    
    
    ##读取数据,
    data = pd.read_csv(dataset_filepath,usecols=['countries_en','additives_n'])
    
    ##分析国家食物中的食品添加剂种类个数
    #1.数据清理
    ##去除缺失数据.
    data = data.dropna()
    
    ##讲国家名称转换为小写
    ##哎.省略吧.....注释不想写了
    data['countries_en'] = data['countries_en'].str.lower()
    
    ## 2. 数据分组统计
    country_additives = data['additives_n'].groupby(data['countries_en']).mean()
    
    ##3.按值从大到小排序
    result = country_additives.sort_values(ascending=False)
    
    ##4. pandas可视化top10
    result.iloc[:10].plot.bar()
    plt.show()
    
    ##5.保存处理结果
    result.to_csv("./country_additives.csv")
    
    ##删除解压数据,清理空间
    
    if os.path.exists(dataset_filepath):
        os.remove(dataset_filepath)
        
        
if __name__ == '__main__':
    run_main()
    
