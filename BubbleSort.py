#!/usr/bin/python3
import random
import matplotlib.pyplot as plt

#filling list with random numbers
def fillList(sampleList, N, Y):
    assert type(sampleList) == list
    for i in range(0, N):
        i = random.randrange(0, Y)
        sampleList.append(i)
    return sampleList

def bubbleSort(sampleList):
    assert type(sampleList) == list
    n = len(sampleList)
    for i in range(n-1):
        for j in range(n-i-1):
            if sampleList[j] > sampleList[j+1]:
                sampleList[j], sampleList[j+1] = sampleList[j+1], sampleList[j]
            updateGraph(sampleList)
    return sampleList

def updateGraph(sampleList):
    plt.bar(range(0, N), sampleList)
    plt.draw()
    plt.pause(0.1)
    plt.clf()

if __name__== '__main__':
    N = int(input("Number of N numbers to sort => "))
    Y = int(input("Max value => "))
    sampleList = []
    sampleList = fillList(sampleList, N, Y)
    bubbleSort(sampleList)
    print(sampleList)
