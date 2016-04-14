#coding: utf-8
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

def createDataSet():
    group=array([[1,1.1],[1,1],[0,0],[1,0.1]])
    labels=['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k): #重点！！核心部分
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

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio=0.1
    datingDataMat,DatingLabels=file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    errorCont=0
    for i in range(numTestVecs):
        classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],\
        DatingLabels[numTestVecs:m],5)
        print 'the classifier came back with %d, the real answer is : %d'\
        % (classifierResult,DatingLabels[i])
        if (classifierResult != DatingLabels[i]): errorCont+=1
    print 'the total error rate is: %f' % (errorCont/float(numTestVecs))

datingDataMat,DatingLabels=file2matrix('datingTestSet2.txt')
normMat, ranges, minVals=autoNorm(datingDataMat)
#
#
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,0],20*array(DatingLabels),20*array(DatingLabels))
# plt.show()
# datingClassTest()

def classifyPerson():
    resultList=['not at all', 'in small doses', 'in large doses']
    percentTats=float(raw_input('percentage of time spent playing video games?'))
    ffMiles=float(raw_input('Frequent flier miles earned per year?'))
    iceCream=float(raw_input('liters of ice cream consumed per year?'))
    datingDataMat,DatingLabels=file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals=autoNorm(datingDataMat)
    inArr=array([ffMiles,percentTats,iceCream])
    classifierResult=classify0((inArr-minVals)/ranges,normMat,DatingLabels,3)
    print 'you will probably like this person:', resultList[classifierResult-1]
# classifyPerson()

def img2vector(filename):
    returnVect=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect
# filename='digits/trainingDigits/0_100.txt'
# trainVector=img2vector(filename)
def handWritingClassTest():
    hwLabels=[]
    trainingFileList=listdir('digits/trainingDigits')
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    # print trainingFileList
    for i in range(1,m):#mac 系统下 里面会出现一个名为.Ds_Store 的文件
        fileName=trainingFileList[i]
        fileStr=fileName.split('.')[0] #文件名去掉后缀
        classNum=int(fileStr.split('_')[0])
        hwLabels.append(classNum)
        trainingMat[i,:]=img2vector('digits/trainingDigits/%s' % fileName)
    testFieldList=listdir('digits/testDigits')
    error=0
    mTest=len(testFieldList)
    for i in range(1,mTest):
        fileName=testFieldList[i]
        fileStr=fileName.split('.')[0] #文件名去掉后缀
        classNum=int(fileStr.split('_')[0])
        testVector=img2vector('digits/testDigits/%s' %fileName)
        classifierResult=classify0(testVector,trainingMat,hwLabels,3)
        print 'the classifier came back with: %d, the real answer is : %d' %(classifierResult,classNum)
        if (classifierResult!= classNum): error+=1
    print 'the total number of errors is: %d' % error
    print '\nthe total error rate is %f' %(error/float(mTest-1))
handWritingClassTest()
