# -*- coding: utf-8 -*-
# coding: utf-8
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/91691/Desktop/test.csv',encoding='gbk')
a = df.head()
print(a)
print(type(df))

# 列名 columns 索引 index
print(df.index)

print(df.loc[0])

# 筛选华数
a = df[df.宽带归属 == '华数']
print(a)
# 复杂筛选
a = df[(df.宽带归属 =='华数')&(df.地址 =='瓜沥')]
print(a)



# 排序
a = df.sort_values(['编号'])
print(a)

# 访问 按照索引定位
a = df.loc[1]
print(a)

# 更改索引为字母

scores = {
    'name':['zhu','jun','jie'],
    'English':[90,87,89],
    'maths':[64,77,98]
}

# df = pd.DataFrame(scores,index=['one','two','three'])
# print(df.loc['one'])
print(df.iloc[0])
# print(df.ix[0]) # 合并了loc与iloc的功能 可以用切片访问多行，单独无切片访问单行不可以

print(df.电话.values)
new = df[['编号','电话']].head() # 提取多列

print(new*2)

# 按照数据分类
def func(score):
    if score == '电信':
        return 'A'
    elif score == '移动':
        return  'B'
    else:
        return 'C'


# map函数 根据原有数据生成新数据 【重点】
df['宽带分类'] = df.宽带归属.map(func)
print(df)

func = lambda number: number+10
a = df.applymap(lambda x:str(x) +'-') # 对所有数据进行操作
print(a)

# apply 根据多列生成新列
# pandas中的dataframe的操作很大一部分与numpy的二维数组是近似的

