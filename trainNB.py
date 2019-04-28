# -*- coding: UTF-8 -*-
from preprocession import *
import numpy as np

def trainNB(trainMatrix,trainCategory):  #训练模型
    numof_trainMatrix = len(trainMatrix)
    num_words = len(trainMatrix[0])
    p1sum = sum(trainCategory) / len(trainCategory)   #垃圾邮件的概率
    p1 = np.ones(num_words)
    p0 = np.ones(num_words)
    p1fenmu = 2.0
    p0fenmu = 2.0

    for i in range(numof_trainMatrix):
        if trainCategory[i] == 1:
            p1 += trainMatrix[i]
            p1fenmu += sum(trainMatrix[i])
        else:
            p0 += trainMatrix[i]
            p0fenmu += 1
    p1gailv = np.log(p1 / p1fenmu)
    p0gailv = np.log(p0 / p0fenmu)
    return  p1gailv,p0gailv,p1sum

def testNB(testset,p1gailv,p0gailv,p1sum):
    p1 = sum(testset*p1gailv) + np.log(p1sum)
    p0 = sum(testset*p0gailv) + np.log(1-p1sum)
    if p1 > p0:
        return 1
    if p1 < p0:
        return 0
