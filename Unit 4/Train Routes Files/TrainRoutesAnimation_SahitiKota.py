# Sahiti Kota
# 12/21/2021

import sys
import heapq
import time
import tkinter as tk
from math import pi, acos, sin, cos

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos(sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1)) * R

nodeDictionary = dict()
with open('rrNodes.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        currentJunction = "".join(lineList[lineNum][0])
        nodeDictionary[currentJunction] = (float(lineList[lineNum][1]), float(lineList[lineNum][2]))

junctionDictionary = dict()
junctionDictionary.setdefault(list)
start = time.perf_counter()
with open('rrEdges.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        startJunction = "".join(lineList[lineNum][0])
        endJunction = "".join(lineList[lineNum][1])
        if startJunction in junctionDictionary:
            junctionDictionary[startJunction].append((endJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction])))
        else:
            junctionDictionary[startJunction] = [(endJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction]))]
        if endJunction in junctionDictionary:
            junctionDictionary[endJunction].append((startJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction])))
        else:
            junctionDictionary[endJunction] = [(startJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction]))]
end = time.perf_counter()

print("Time to create data structure: " + str(end - start))

def drawLine(c, node1, node2, color):
    x1 = -abs(float(node1[1])) * 10 + 1300
    y1 = -abs(float(node1[0])) * 10 + 650
    x2 = -abs(float(node2[1])) * 10 + 1300
    y2 = -abs(float(node2[0])) * 10 + 650
    line = c.create_line(x1, y1, x2, y2, fill = color, width = 1)
    return line

root = tk.Tk() #creates the frame
canvas = tk.Canvas(root, height= 70 * 8, width = 90 * 8, bg='white')
lines = {}
for start, endList in junctionDictionary.items():
    if endList != None:
        for end, dist in endList:
            # print(start, end)
            # print(nodeDictionary[start], nodeDictionary[end])
            line = (drawLine(canvas, nodeDictionary[start], nodeDictionary[end], "black"))
            lines[(start, end)] = line
            lines[(end, start)] = line
canvas.pack(expand=True)
# root.mainloop()

def makeRed(r, c, line):
    c.itemconfig(line, fill = "red")

def makeBlue(r, c, line):
    c.itemconfig(line, fill = "blue")

def makeGreen(r, c, line):
    c.itemconfig(line, fill = "medium spring green")
    r.update()

junctionCityDictionary = dict()
with open('rrNodeCity.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        junction = "".join(lineList[lineNum][0])
        junctionCity = " ".join(lineList[lineNum][1:])
        junctionCityDictionary[junction] = junctionCity

flippedJunctionCityDictionary = dict()
with open('rrNodeCity.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        junction = "".join(lineList[lineNum][0])
        junctionCity = " ".join(lineList[lineNum][1:])
        flippedJunctionCityDictionary[junctionCity] = junction

def goalTest(currentJunction, endJunction):
    if currentJunction == endJunction:
        return True

def getChildren(currentJunction):
    endNamesList = []
    endJunctionsList = junctionDictionary[currentJunction]
    for junction in endJunctionsList:
        name, distance = junction
        endNamesList += [name]
    return endNamesList

def djikstra(startJunction, endJunction):
    updateCount = 0
    start = time.perf_counter()
    closed = set()
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (0, startJunction, [startJunction]))
    while fringe:
        parentDepth, parent, parentPath = heapq.heappop(fringe)
        if goalTest(parent, endJunction) == True:
            end = time.perf_counter()
            for n in range(len(parentPath) - 1):
                makeGreen(root, canvas, lines[(parentPath[n], parentPath[n + 1])])
            return junctionCityDictionary[startJunction] + " to " + junctionCityDictionary[endJunction] + " with Djikstra: " + str(parentDepth) + " in " + str(end - start) + " seconds"
        if parent not in closed:
            closed.add(parent)
            for child in getChildren(parent):
                if child not in closed:
                    parentJunctionDict = junctionDictionary[parent]
                    for item in parentJunctionDict:
                        if item[0] == child:
                            childDepth = parentDepth + item[1]
                    childPath = parentPath.copy()
                    childPath.append(child)
                    heapq.heappush(fringe, (childDepth, child, childPath))
                    updateCount += 1

                    makeRed(root, canvas, lines[(parent, child)])
                    if updateCount % 5000 == 0:
                        root.update()
    return None

def aStar(startJunction, endJunction):
    updateCount = 0
    start = time.perf_counter()
    closed = set()
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (calcd(nodeDictionary[endJunction], nodeDictionary[startJunction]), 0, startJunction, [startJunction]))
    while fringe:
        parentEstimateGreatCircle, parentDepth, parent, parentPath = heapq.heappop(fringe)
        if goalTest(parent, endJunction) == True:
            end = time.perf_counter()
            for n in range(len(parentPath) - 1):
                makeGreen(root, canvas, lines[(parentPath[n], parentPath[n + 1])])
            return junctionCityDictionary[startJunction] + " to " + junctionCityDictionary[endJunction] + " with A*: " + str(parentDepth) + " in " + str(end - start) + " seconds"
        if parent not in closed:
            closed.add(parent)
            for child in getChildren(parent):
                if child not in closed:
                    parentJunctionDict = junctionDictionary[parent]
                    for item in parentJunctionDict:
                        if item[0] == child:
                            childDepth = parentDepth + item[1]
                    childEstimateGreatCircle = childDepth + calcd(nodeDictionary[endJunction], nodeDictionary[child])
                    childPath = parentPath.copy()
                    childPath.append(child)
                    heapq.heappush(fringe, (childEstimateGreatCircle, childDepth, child, childPath))
                    updateCount += 1
                    makeBlue(root, canvas, lines[(parent, child)])
                    if updateCount % 5000 == 0:
                        root.update()
    return None

startCityName = sys.argv[1]
endCityName =  sys.argv[2]

startJunction = flippedJunctionCityDictionary[startCityName]
endJunction = flippedJunctionCityDictionary[endCityName]
print(djikstra(startJunction, endJunction))
print(aStar(startJunction, endJunction))

root.mainloop()