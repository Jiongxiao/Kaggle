#coding:utf-8
#Reference: Kaggle forum

import csv as csv
import numpy as np
import pandas as pd

df=pd.read_csv('train.csv',header=0)

#in order to analyse the price collumn I need to bin up that data
#here are my binning parameters the problem we face is some of the fares are very large
#So we can either have a lot of bins with nothing in them or we can just absorb some
#information and just say anythng over 30 is just in the last bin so we add a ceiling

fare_ceiling=40
df[df['Fare']>=fare_ceiling]=fare_ceiling-1.0
fare_bracket_size=10
number_of_price_brackets=fare_ceiling/fare_bracket_size
number_of_classes=3

df['BinFare']=(df['Fare']/fare_bracket_size).fillna(3-df.Pclass).astype(int)

index=[]
survival_list=[]
gender=['female','male']

for sex in range(2):
    for classid in range(number_of_classes):
        for fareid in range(number_of_price_brackets):
            index.append((sex,classid,fareid))
            survival_probability=(df.Survived[(df.Sex==gender[sex]) & (df.Pclass==fareid+1) \
            & (df.BinFare==fareid)].mean())
            survival_list+=[survival_probability]

survival_index=pd.MultiIndex.from_tuples(index,names=['Gender','Class','PriceBracket'])
survival_table=(pd.Series(survival_list, index=survival_index, name='Survival table').fillna(0)>0.5).astype(int)

test=pd.read_csv('test.csv',index_col=[0])
test['BinFare']=(test['Fare']/fare_bracket_size).clip_upper(number_of_price_brackets-1).fillna(3-test.Pclass).astype(int)
# test[['Fare','Pclass','BinFare']].head(10)

test['Survived']=(test[['Sex','Pclass','BinFare']].apply(lambda x: survival_table[(x[0]=='male',x[1]-1,x[2])],axis=1))

# test['Survived'].to_csv('tjx_genderclassmodel-pandas.csv')木有标题！！！！！
test[['Survived']].to_csv('tjx_genderclassmodel-pandas.csv')#有标题！！！

# df.head(20)
