#coding: utf-8
import calcuEntropy
import numpy as np
#输入带划分的数据集、划分数据集的特征、特征的返回值（只返回带该返回值的数据)

#format of dataSet
# array([ 1.(label),  1.,  1.,  0.,  3.,  0.,  0.])
#      Survived  Pclass  SibSp  Parch  BinFare  Gender  EM

def splitDataSet(dataSet,axis,value):
    retDataSet=dataSet[(dataSet[0:,axis].astype(int)==value)]  #这里埋了一个雷，标签一定要转化成数字！！！
    retDataSet=np.delete(retDataSet,axis,axis=1)
    return retDataSet
testset=np.array([[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']])
# print splitDataSet(testset,0,0)
# print calcuEntropy.calcShannonEnt(train_dataSet,0)   #0表示label列

def chooseBestFeat(dataSet):
    numFeat=len(dataSet[0])-1
    baseEntropy=calcShannonEnt(dataSet,0)
    bestInfoGain=0
    bestFeat=-1
    for i in range(1,numFeat+1):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcuEntropy.calcShannonEnt(subDataSet,0)
        infoGain=baseEntropy-newEntropy
        print infoGain
        if (infoGain>bestInfoGain):
            bestFeat=i
            bestInfoGain=infoGain
            # print bestFeat
    return bestFeat

#print chooseBestFeat(train_dataSet)

#获取出现次数最多的分类名称

def majorityC(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),key=lambda x: x[1],reverse=True)
    return sortedClassCount[0][0]
# classList=[1,2,1,1,2,2,2,3,3,4,5,5,5]
# print majorityC(classList)
