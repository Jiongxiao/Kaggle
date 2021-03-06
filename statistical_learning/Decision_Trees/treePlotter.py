#coding: utf-8
import matplotlib.pyplot as plt
#Reference: Peter Harrington
#
# def createPlot():
#     fig=plt.figure(1,facecolor='white')
#     fig.clf()
#     createPlot.ax1=plt.subplot(111,frameon=False)
#     plotNode('a decision node', (0.5,0.1),(0.1,0.5),decisionNode)
#     plotNode('a leaf node', (0.8,0.1),(0.3,0.8),leafNode)
#     plt.show()

testTree={'no surfacing':{0:'no',1:{'flipers':{0:'no',1:{'last':{0:'no',1:'yes'}}}},3:'maybe'}}



def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',\
    xytext=centerPt,textcoords='axes fraction',va='center',ha='center',bbox=nodeType,arrowprops=arrow_args)

decisionNode=dict(boxstyle='sawtooth',fc='1')
leafNode=dict(boxstyle='round4',fc='0.8')
arrow_args=dict(arrowstyle='<-')


def getTreeDepth(myTree):
    max_Depth=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            this_Depth=1+getTreeDepth(secondDict[key])
        else:
            this_Depth=1
        if this_Depth>max_Depth:
            max_Depth=this_Depth
    return max_Depth

def getNumLeafs(myTree):
    numLeafs=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if key in secondDict.keys():
            if type(secondDict[key]).__name__!='dict':
                numLeafs+=1
            else: numLeafs=numLeafs+getNumLeafs(secondDict[key])
    return numLeafs

# getNumLeafs(train_tree)
# getTreeDepth(train_tree)
# createPlot()

#节点间填充文本
def plotMidTex(cntrPt,parentPt,txtString):
    xMid=(parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid=(parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotTree(myTree,parentPt,nodeTxt):
    numLeafs=getNumLeafs(myTree)
    depth=getTreeDepth(myTree)
    firstStr=myTree.keys()[0]
    ###cntrPt不太明白
    cntrPt=(plotTree.xOff+(1.0+float(numLeafs))/2.0/plotTree.totalW,\
    plotTree.yOff)
    plotMidTex(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict=myTree[firstStr]
    plotTree.yOff=plotTree.yOff-1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff=plotTree.xOff+1.0/plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
            plotMidTex((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff=plotTree.yOff+1.0/plotTree.totalD

def createPlot(inTree):
    fig=plt.figure(1,facecolor='white')
    fig.clf()
    axprops=dict(xticks=[],yticks=[]) ##干嘛的?
    createPlot.ax1=plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW=float(getNumLeafs(inTree))
    plotTree.totalD=float(getTreeDepth(inTree))
    plotTree.xOff=-0.5/plotTree.totalW
    plotTree.yOff=1
    plotTree(inTree,(0.5,1),'')
    plt.show()


testTree['no surfacing'][5]='LOVE'



# createPlot(testTree)
