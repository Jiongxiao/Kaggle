#coding: utf-8
from numpy import *

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet | set (document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else: print 'the word: %s is not in the vocabulary!' % word
    return returnVec


def trainNBO(trainMatrix, trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    # p0Num=zeros(numWords)
    # p1Num=zeros(numWords)
    p0Num=ones(numWords)
    p1Num=ones(numWords)
    p0Denom=2.0;p1Denom=2.0;
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])  # 个人觉得这里每个特征应该分开求概率，为嘛要加到一块？
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    p1Vect=log(p1Num/p1Denom)
    p0Vect=log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive


def classifyNB(vec2Classify,p0v,p1v,pClass1):
    p1=sum(vec2Classify*p1v)+log(pClass1)
    p0=sum(vec2Classify*p0v)+log(1-pClass1)
    if p1>p0:
        return 1
    else:
        return 0

def testingNB():
    #for test
    listOPosts,listClasses=loadDataSet()
    vocabList=createVocabList(listOPosts)
    trainMatrix=[]
    for inputSet in listOPosts:
        trainMatrix.append(setOfWords2Vec(vocabList,inputSet))
    p0v,p1v,pAb=trainNBO(trainMatrix,listClasses)
    testEntry=['love','my','dalmation']
    thisDoc=array(setOfWords2Vec(vocabList,testEntry))
    print testEntry, 'classified as ', classifyNB(thisDoc,p0v,p1v,pAb)
    testEntry=['stupid','garbage']
    thisDoc=array(setOfWords2Vec(vocabList,testEntry))
    print testEntry, 'classified as ', classifyNB(thisDoc,p0v,p1v,pAb)
testingNB()
