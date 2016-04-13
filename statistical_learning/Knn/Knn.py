#coding: utf-8
from numpy import *
import operator

def createDataSet():
    group=array([[1,1.1],[1,1],[0,0],[1,0.1]])
    labels=['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize=dataSet.shape[0]
    diff=tile(inX,(dataSetSize,1))-dataSet
    sqDiff=diff**2
    sqDistance=sqDiff.sum(axis=1)
    distance=sqDistance**0.5
    sortedDistIndex=distance.argsort()#用来得到排序的索引值
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndex[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

group, labels= createDataSet()
# print classify0([0,0],group,labels,3)

def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index +=1
    return returnMat,classLabelVector
datingDataMat,DatingLabels=file2matrix('datingTestSet2.txt')
