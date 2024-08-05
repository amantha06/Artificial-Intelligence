from heapq import heappush, heappop, heapify
import time
import sys
from math import pi , acos , sin , cos
import tkinter as tk



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

def draw(canvas, n1, n2, color):
    return canvas.create_line((-abs(float(n1[1])) * 10 + 1400), (-abs(float(n1[0])) * 10 + 700), (-abs(float(n2[1])) * 10 + 1400), (-abs(float(n2[0])) * 10 + 700), fill = color, width = 1)

root = tk.Tk()
canvas = tk.Canvas(root, height= 800, width = 800, bg='white')


lines = dict()
for f, l in edges.items():
    if l != None:
        for l2, d in l:
            potential_line = (draw(canvas, coordinates[f], coordinates[l2], "black"))
            lines[(f, l2)] = potential_line
            lines[(l2, f)] = potential_line
            #need to account for both ways of the line

def red(c, line):
    c.delete(lines[line[0], line[1]])
    draw(c, coordinates[line[0]], coordinates[line[1]], "red")
    #c.itemconfig(line, fill = "red", width = 2)


def green(c, line):
    c.delete(lines[line[0], line[1]])
    draw(c, coordinates[line[0]], coordinates[line[1]], "light green")

    #c.itemconfig(line, fill="light green", width = 2)

#same as A* in green
#edges dict is the get_children method
#coordinates dictionary gives a value for the heursitic
def astar(start, end):
    count = 0
    visited = set()
    fringe = list()
    heappush(fringe, (calcd(coordinates[start], coordinates[end]), 0, start, [start]))
    while len(fringe) != 0:
        v, depth, end_state, path = heappop(fringe)
        if end_state == end:
            for i in range(len(path) - 1):
                green(canvas, (path[i], path[i + 1]))
                if i % 50 == 0: root.update()
            return depth

        if end_state not in visited:
            visited.add(end_state)

            for i in edges[end_state]:
                if i not in visited:
                    newpath = path.copy()
                    newpath.append(i[0])
                    new_depth = depth + i[1]
                    taxicab = calcd(coordinates[i[0]], coordinates[end]) + new_depth
                    heappush(fringe, (taxicab, new_depth, i[0], newpath))
                count += 1
                red(canvas, (end_state, i[0]))
                red(canvas, (i[0], end_state))
                if count % 500 == 0:
                    root.update()

    return None


canvas.pack(expand=True)

#really similar to bfs, simialr to A star in a way
#but does not need coordinates dictionary as the heurstic

def dijkstra(start, end):
    count = 0
    #need for animation
    visited = set()
    fringe = list()
    heappush(fringe, (0, start, [start]))
    while len(fringe) != 0:
        depth, end_state, path = heappop(fringe)
        if end_state == end:
            for i in range(len(path)-1):
                green(canvas, (path[i], path[i+1]))
                root.update()
            return depth

        if not end_state in visited:
            visited.add(end_state)
            for i in edges[end_state]:
                if i[0] not in visited:
                    newpath = path.copy()
                    newpath.append(i[0])
                    heappush(fringe, (depth+i[1], i[0], newpath))
                count += 1
                red(canvas, (end_state, i[0]))
                red(canvas, (i[0], end_state))
                # print(lines[(i[0], end_state)])
                # print(i[0])
                # input()

                if count % 2000 == 0:
                    root.update()
    return None

start = sys.argv[1]
end = sys.argv[2]

start_spot = city[start]
end_spot = city[end]
print(dijkstra(start_spot, end_spot))
time.sleep(10)
canvas.delete("all")

lines = dict()
for f, l in edges.items():
    if l != None:
        for l2, d in l:
            potential_line = (draw(canvas, coordinates[f], coordinates[l2], "black"))
            lines[(f, l2)] = potential_line
            lines[(l2, f)] = potential_line
            #need to account for both ways of the line

print(astar(start_spot, end_spot))


root.mainloop()


