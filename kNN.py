#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:50:32 2020

@author: MFeroz
"""

from numpy import *
import operator

def createDataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    print('Success createDataset()')
    return labels, group

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
    
labels,group = createDataset()
print(classify([0,0],group,labels,3))


