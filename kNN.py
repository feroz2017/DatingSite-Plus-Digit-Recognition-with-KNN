#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:50:32 2020

@author: MFeroz
"""

from numpy import *
import operator
from io import *
import matplotlib.pyplot as plt


def createDataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    print('Success createDataset()')
    return labels, group

def autoNorm(dataset):
    minVals = dataset.min(axis = 0)
    maxVals = dataset.max(axis = 0)
    ranges = maxVals - minVals
    normMatrix = zeros(dataset.shape)
    rows = dataset.shape[0]
    normMatrix = dataset - tile(minVals,(rows,1))
    normMatrix = normMatrix / tile(ranges,(rows,1))
    print('Success autoNorm()')
    return normMatrix,ranges,minVals
    

def fileToMatrix(filename):
    file = open(filename)
    numberOfLines = len(file.readlines())
    retMatrix = zeros((numberOfLines,3))
    classLabel = []
    file.close()
    file = open(filename)
    index = 0
    for line in file.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        retMatrix[index,:] = listFromLine[0:3]
        classLabel.append(listFromLine[-1])
        index = index + 1
    print('Success fileToMatrix(filename)')
    return retMatrix,classLabel
    
def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    differenceMatrix = tile(inX,(dataSetSize,1)) - dataSet
    squareMatrix = differenceMatrix**2
    squareDistances = squareMatrix.sum(axis = 1)
    distances = squareDistances**0.5
    sortedDistances = distances.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistances[i]]
        classCount[votelabel]=classCount.get(votelabel,0)+1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    print('Success classify()')
    return sortedClassCount[0]
def datingClassTest():
    splitRatio = 0.1
    retMatrix , classLabel = fileToMatrix('dataset.txt')
    normMatrix, ranges ,minVals = autoNorm(retMatrix)
    testCases = int(splitRatio * normMatrix.shape[0])
    error = 0.0
    for i in range(testCases):
        classifierResult = classify(normMatrix[i,:],normMatrix[testCases:m,:],classLabel[testCases:m],3)
        print('Classifier came back with: ',classifierResult,' But Original: ',classLabel[i])
        if(classifierResult != classLabel[i]):
            error = error + 1
    print("Totla Error is ",error/normMatrix.shape[0])
#labels,group = createDataset()
##print(classify([0,0],group,labels,3))
#datingDataMat,datingLabels = fileToMatrix('dataset.txt')
#normMatrix,ranges,minVals = autoNorm(datingDataMat)
#print(normMatrix)
datingClassTest()

