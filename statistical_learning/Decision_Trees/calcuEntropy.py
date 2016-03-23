#coding: utf-8

import pandas as pd
from math import log
import numpy as np

def AddBinFare(frame,fare_bracket_size=10, number_of_fares=4):
    frame['BinFare']=((frame.Fare/fare_bracket_size).clip_upper(number_of_fares-1).fillna(3-frame.Pclass).astype(int))

def transfer(frame,number_of_classes):              #clean and fill
    # frame['Gender']=(frame['Sex'].map(lambda x: x=='male')).astype(int) both ok!!!
    frame['Gender']=(frame[['Sex']].apply(lambda x: x=='male')).astype(int)
    frame['EM']=frame['Embarked'].map({'C':0,'S':1,'Q':2})
    frame['EM']=frame['EM'].fillna(1)

    def fillAge(frame, number_of_classes):
        frame['AgeFill']=frame['Age']
        median_ages=np.zeros((2,number_of_classes))
        for i in range(2):
            for j in range(number_of_classes):
                median_ages[i,j]=frame[(frame['Gender']==i) & (frame.Pclass==j+1)].Age.dropna().median()
                frame.loc[(frame.Age.isnull()) & (frame['Gender']==i) & (frame.Pclass==j+1),'AgeFill']=median_ages[i,j]
        # print median_ages
    frame=frame.drop(['Age','Sex','Ticket','Cabin','Embarked','Name','Fare'], axis=1)
    return frame

fare_ceiling=40
fare_bracket_size=10
number_of_fares=fare_ceiling/fare_bracket_size
number_of_classes=3

train_data=pd.read_csv('train.csv', header=0, index_col=[0])
test_data=pd.read_csv('test.csv',header=0,index_col=[0])

AddBinFare(train_data,fare_bracket_size=fare_bracket_size,number_of_fares=number_of_fares)
train_data=transfer(train_data,number_of_classes)
train_dataSet=train_data.values

#clean data

# to calculate Entropy
def calcShannonEnt(dataset,axis):
    numEntries=len(dataset)
    labelCounts={}
    for featVec in dataset:
        currentLabel=featVec[axis]   #It is important to know where the label is.
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt
# dataSet=[[1,1,1],[1,1,1],[1,0,0],[0,1,0],[0,1,0]]
# print calcShannonEnt(dataSet,0)   for test
# print calcShannonEnt(train_dataSet,0)
