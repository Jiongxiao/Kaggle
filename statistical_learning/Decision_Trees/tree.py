#coding: utf-8
import calcuEntropy
#输入带划分的数据集、划分数据集的特征、特征的返回值（只返回带该返回值的数据)
def splitDataSet(dataSet,axis,value):
    retDataSet=dataSet[(dataSet[0:,axis].astype(int)==value)]
    retDataSet=np.delete(retDataSet,axis,axis=1)
    return retDataSet
# testset=np.array([[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']])
# print splitDataSet(testset,0,0)
print calcuEntropy.calcShannonEnt(train_dataSet,0)   #0表示label列
