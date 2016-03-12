#coding:utf-8
import csv as csv
import numpy as np

# Open up the csv file in to a Python object
train_file=open('train.csv', 'rb')
train_file_object = csv.reader(train_file)
header = train_file_object.next()  # The next() command just skips the
data=[]

for row in train_file_object:
    data.append(row)
data=np.array(data)

fare_ceiling=40
data[data[0:,9].astype(float) >= fare_ceiling, 9]=fare_ceiling -1.0
fare_bracket_size=10
number_of_price_brackets=fare_ceiling/fare_bracket_size

number_of_classes=3
survival_table=np.zeros([2,number_of_classes,number_of_price_brackets],float)

for i in xrange(number_of_classes):
    for j in xrange(number_of_price_brackets):
        women=data[(data[0:,4]=='female') & (data[0:,2].astype(np.float)==i+1) & (data[0:,9].astype(np.float)> j*fare_bracket_size)\
        & (data[0:,9].astype(np.float)<(j+1)*fare_bracket_size),1]

        men=data[(data[0:,4]=='male') & (data[0:,2].astype(np.float)==i+1) & (data[0:,9].astype(np.float)> j*fare_bracket_size)\
        & (data[0:,9].astype(np.float)<(j+1)*fare_bracket_size),1]

        survival_table[0,i,j]=np.mean(women.astype(np.float))
        survival_table[1,i,j]=np.mean(men.astype(np.float))

survival_table[survival_table!=survival_table]=0 #空数组求平均值会出现问题
print survival_table
