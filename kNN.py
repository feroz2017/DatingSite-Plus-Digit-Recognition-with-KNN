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

from os import listdir


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
    m = normMatrix.shape[0]
    for i in range(testCases):
        classifierResult = classify(normMatrix[i,:],normMatrix[testCases:m,:],classLabel[testCases:m],3)
        print('Classifier came back with: ',classifierResult[0],' But Original: ',classLabel[i])
        if(classifierResult[0] != classLabel[i]):
            error = error + 1
    print("Totla Error is %:",(error/m)*100)
def classifyPerson():
    
    #10
    resultList = ['didntLike','smallDoses', 'largeDoses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = fileToMatrix('dataset.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify((inArr-\
                                  minVals)/ranges,normMat,datingLabels,3)
    #print(classifierResult)
    print ("You will probably like this person: ",classifierResult[0])
def imgToVector(filename):
    file = open(filename)
    vectorImg = zeros((1,1024))
    for i in range(32):
        line = file.readline() 
        #print(line)
        for j in range(32):
            vectorImg[0,32*i+j] = int(line[j])
    file.close()
    return vectorImg
def handwritingClassTest():
    trainingList = listdir('digits/trainingDigits')
    testingList = listdir('digits/testDigits')
    trainingNum = len(trainingList)
    trainVector = zeros((trainingNum,1024))
    labels = []
    for i in range(trainingNum):
        imgname = trainingList[i]
        img = imgname.split('.')[0]
        label = img.split('_')[0]
        labels.append(label)
        trainVector[i,:] = imgToVector('digits/trainingDigits/%s' % imgname)
    error = 0.0
    testingNum = len(testingList)
    for i in range(testingNum):
        imgname =testingList[i]
        img = imgname.split('.')[0]
        label = img.split('_')[0]
        testvector = imgToVector('digits/testDigits/%s' %imgname)
        classifierResult = classify(testvector,trainVector,labels,3)
        if (classifierResult[0]!=label):
            error = error + 1
        print('Classifier Resutl: ',classifierResult[0],' And Original ',label)
    print('Error Percentage: ',(error/testingNum)*100)
    #print(len(testingList))
# Testing Different Functions
#labels,group = createDataset()
##print(classify([0,0],group,labels,3))
#datingDataMat,datingLabels = fileToMatrix('dataset.txt')
#normMatrix,ranges,minVals = autoNorm(datingDataMat)
#print(normMatrix)
#datingClassTest()
#classifyPerson()
#vectorImg=imgToVector('digits/trainingDigits/0_2.txt')
#print(vectorImg[0,0:3])
#handwritingClassTest()
datingClassTest()
