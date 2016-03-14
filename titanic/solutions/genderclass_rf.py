import csv as csv
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#using random forest

df=pd.read_csv('train.csv',header=0)

def AddBinFare(frame,fare_bracket_size=10, number_of_fares=4):
    frame['BinFare']=((frame.Fare/fare_bracket_size).clip_upper(number_of_fares-1).fillna(3-frame.Pclass).astype(int))

def transfer(frame,number_of_classes):              #clean and fill
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
train_data=train_data.values

AddBinFare(test_data,fare_bracket_size=fare_bracket_size,number_of_fares=number_of_fares)
test_data=transfer(test_data,number_of_classes)
test_index=test_data.index.values
test_data=test_data.values

forest=RandomForestClassifier(n_estimators=100)
forest=forest.fit(train_data[0::,1::],train_data[0::,0])

output=forest.predict(test_data)
out=pd.DataFrame(output,index=test_index)
out.to_csv('genderclassmodel-pandas_rf.csv')
