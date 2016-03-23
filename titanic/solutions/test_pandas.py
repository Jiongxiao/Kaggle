#coding:utf-8
import csv as csv
import numpy as np
import pandas as pd

# Open up the csv file in to a Python object
train_file=open('train.csv', 'rb')
train_file_object = csv.reader(train_file)
header = train_file_object.next()  # The next() command just skips the
data=[]

df=pd.read_csv('train.csv',header=0)
df['Gender']=df['Sex'].map({'female':0,'male':1}).astype(int)

median_ages=np.zeros((2,3))
for i in range(2): #gender
    for j in range(3): #class
        median_ages[i,j]=df[(df.Gender==i) & (df.Pclass==j+1)]['Age'].dropna().median()

df['AgeFill']=df['Age']

for i in range(2):
    for j in range(3):
        df.loc[(df.Age.isnull()) & (df.Gender== i) & (df.Pclass== j+1),'AgeFill']=median_ages[i,j]
        # df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),'AgeFill'] = median_ages[i,j]
df['AgeIsNull']=pd.isnull(df.Age).astype(int)
df['FamilySize']=df['SibSp']+df['Parch']
df=df.drop(['Name','Sex','Ticket','Cabin','Embarked'], axis=1)
