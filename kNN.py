#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:50:32 2020

@author: MFeroz
"""

from numpy import *
import operator
from io import *
def createDataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    #print('Success createDataset()')
    return labels, group
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
    return sortedClassCount[0]
    
#labels,group = createDataset()
#print(classify([0,0],group,labels,3))
group,labels = fileToMatrix('dataset.txt')
print(group,labels[0:20])



