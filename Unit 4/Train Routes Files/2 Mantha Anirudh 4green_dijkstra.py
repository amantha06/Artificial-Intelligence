from heapq import heappush, heappop, heapify
import time
from time import perf_counter
import sys
from math import pi , acos , sin , cos
from tkinter import *
from tkinter import messagebox


start_structure = time.perf_counter()

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   if node1 == node2:
       return 0


   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

city = dict()
with open("rrNodeCity.txt") as f:
    for i in f:
        i = i.strip()
        city[i[i.index(" ") + 1:]] = i[:i.index(" ")]
    #forgot dictionary comprehension


coordinates = dict()
with open("rrNodes.txt") as f:
    for i in f:
        i=i.strip()
        split_i=i.split(" ")
        coordinates[split_i[0]]=(float(split_i[1]),float(split_i[2]))
    #lat and long added to dictionary

edges = dict()
with open("rrEdges.txt") as f:
    for i in f:
        i=i.strip()
        start,end=i.split(" ")
        possible=edges.pop(start,[])
        possible.append((end,calcd(coordinates[start],coordinates[end])))
        edges[start]=possible
        possible = edges.pop(end, [])
        possible.append((start, calcd(coordinates[start],coordinates[end])))
        edges[end]= possible

#these three dictionaries are the methods getChildren and taxicab
#they are organized in a way that there is no need for external methods

end_structure = time.perf_counter()
print("Data structures created in :", end_structure-start_structure)

#same as A* in green
#edges dict is the get_children method
#coordinates dictionary gives a value for the heursitic
def astar(start, end):
    visited = set()
    fringe = list()
    heappush(fringe, (calcd(coordinates[start], coordinates[end]), 0, start))
    while len(fringe) != 0:
        v, depth, end_state = heappop(fringe)
        if end_state == end: return depth

        if end_state not in visited:
            visited.add(end_state)

            for i in edges[end_state]:
                if i not in visited:

                    new_depth = depth + i[1]
                    taxicab = calcd(coordinates[i[0]], coordinates[end]) + new_depth
                    heappush(fringe, (taxicab, new_depth, i[0]))

    return None

#really similar to bfs, simialr to A star in a way
#but does not need coordinates dictionary as the heurstic

def dijkstra(start, end):
    visited = set()
    fringe = list()
    heappush(fringe, (0, start))
    while len(fringe) != 0:
        depth, end_state = heappop(fringe)
        if end_state == end: return depth

        if not end_state in visited:
            visited.add(end_state)

            for i in edges[end_state]:

                if i not in visited:
                    heappush(fringe, (depth+i[1], i[0]))
    return None

start = sys.argv[1]
end = sys.argv[2]



astar_start_time = perf_counter()
astar = astar(city[start], city[end])
perf_counter()
print(start, "to", end, "with A star algorithm:", astar, "in", perf_counter()-astar_start_time, "seconds")

dijkstra_start_time = perf_counter()
dijstra = dijkstra(city[start], city[end])
print(start, "to", end, "with Dijkstra algorithm:", dijstra, "in", perf_counter()-dijkstra_start_time, "seconds")

