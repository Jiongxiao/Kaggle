#coding: utf-8
from numpy import *
import operator

def createDataSet():
    group=array([[1,1.1],[1,1],[0,0],[1,0.1]])
    labels=['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize=dataSet.shape[0]
    diff=tile(inx,(dataSetSize,1))-dataSet
    sqDiff=diff**2
    sqDistance=sqDiff.sum(axis=1)
    distance=sqDistance**0.5
    sortedDistIndex=distance.argsort()#用来得到排序的索引值
    classCount={}
    for i in rank(k):
        voteIlabel=labels[sortedDistIndex[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount, key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

group, labels= createDataSet()
