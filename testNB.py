# -*- coding: UTF-8 -*-
from preprocession import *
import numpy as np
from trainNB import *
import random

def test():
    decoument = []
    classify = []
    for i in range(26):
        postive = text2wordlist(open("./dataset/ham/{num}.txt".format(num=i),"r").read())
        decoument.append(postive)
        classify.append(1)
        negtive = text2wordlist(open("./dataset/spam/{num}.txt".format(num=i),"r").read())
        decoument.append(negtive)
        classify.append(0)
    word_set = create2setlist(decoument)
    testset = []
    trainmate = []
    testmate = []
    testset_classfity = []
    trainset = []
    trainset_classfity = []
    for i in range(len(decoument)):
        trainset.append(setOfwords2vec(word_set,decoument[i]))
    for i in range(10):
        index = int(random.uniform(0,len(decoument)))
        testmate.append(decoument[index])
        testset.append(setOfwords2vec(word_set,decoument[index]))
        testset_classfity.append(classify[index])
        del decoument[index]
        del classify[index]
        del trainset[index]
    trainmate = decoument
    trainset_classfity = classify

    p1gailv,p0gailv,p1sum = trainNB(np.array(trainset),np.array(trainset_classfity))

    for i in range(len(testset)):

        score = testNB(testset[i],p1gailv,p0gailv,p1sum)
        print("test is : {deco}; the score is {num}".format(deco=testmate[i],num=score))













