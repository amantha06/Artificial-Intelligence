from heapq import heappush, heappop
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

def draw(canvas, n1, n2, color, width):
    return canvas.create_line((-abs(float(n1[1])) * 10 + 1400), (-abs(float(n1[0])) * 10 + 700), (-abs(float(n2[1])) * 10 + 1400), (-abs(float(n2[0])) * 10 + 700), fill = color, width = width)

root = tk.Tk()
canvas = tk.Canvas(root, height= 800, width = 800, bg='white')

#the US map
#not being a list helps a lot
lines = dict()
for f, l in edges.items():
    if l != None:
        for l2, d in l:
            potential_line = (draw(canvas, coordinates[f], coordinates[l2], "black", 1))
            lines[(f, l2)] = potential_line
            lines[(l2, f)] = potential_line
            #need to account for both ways of the line


def red(c, line):
    c.delete(lines[line[0], line[1]])
    draw(c, coordinates[line[0]], coordinates[line[1]], "red", 2)

def green(c, line):
    c.delete(lines[line[0], line[1]])
    draw(c, coordinates[line[0]], coordinates[line[1]], "light green", 2)

canvas.pack(expand=True)

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
                root.update()
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
                if count % 2000 == 0: root.update()
    return None

def dfs(start, end):
    count = 0
    ##path = dict()
    visited = set()
    fringe = list()
    fringe.append((start, 0, [start]))
    while len(fringe) != 0:
        end_state, depth, path = fringe.pop()
        if end_state == end:
            temp = end
            newcount = 0
            for i in range(len(path) - 1):
                green(canvas, (path[i], path[i + 1]))
                root.update()
            return depth
        for i in edges[end_state]:
            if i not in visited:
                newpath = path.copy()
                newpath.append(i[0])
                visited.add(i)
                new_depth = depth + i[1]
                fringe.append((i[0], new_depth, newpath))
            count += 1
            red(canvas, (end_state, i[0]))
            red(canvas, (i[0], end_state))
            if count % 1000 == 0: root.update()
    return None

def bidirectional_dijkstra(start, end):
    counter = 0
    # dictionary to store depth and path in same structure
    visited_start = {start: (0, [start])}
    visited_goal = {end: (0, [end])}
    # normal fringe
    fringe_start = list()
    fringe_goal = list()
    heappush(fringe_start, (0, start, [start]))
    heappush(fringe_goal, (0, end, [end]))
    # need to store duplicates to solve problem
    duplicates = set()
    while len(fringe_goal) != 0 and len(fringe_start) != 0:
        v_start, end_state, end_state_path = heappop(fringe_start)
        if end_state in visited_goal:
            depth = v_start + visited_goal[end_state][0]
            path = visited_start[end_state][1] + visited_goal[end_state][1][::-1][1:]
            # Iterate through path and draw in green
            temp = start
            i=0
            while (temp != end):
                i+=1
                green(canvas, (temp, path[i]))
                green(canvas, (path[i], temp))
                temp = path[i]
                root.update()
            return depth
        duplicates.add(end_state)
        for i in edges[end_state]:
            if i[0] in duplicates: continue
                # THIS GETS RID OF THE DOUBLE COUNTING
            depth = v_start + i[1]
            if i[0] not in visited_start or visited_start[i[0]][0] > depth:
                heappush(fringe_start, (depth, i[0], end_state_path + [i[0]]))
                visited_start[i[0]] = (depth, end_state_path + [i[0]])
            counter += 1
            red(canvas, (end_state, i[0]))
            if counter % 750 == 0: root.update()
        v_goal, end_state_goal, end_state_goal_path = heappop(fringe_goal)
        if end_state_goal in visited_start:
            depth = v_goal + visited_start[end_state_goal][0]
            path = visited_goal[end_state_goal][1] + visited_start[end_state_goal][1][::-1][1:]
            # Iterate through path and draw in green
            temp = end
            i=0
            while (temp != start):
                i+=1
                green(canvas, (temp, path[i]))
                green(canvas, (path[i], temp))
                temp = path[i]
                root.update()
            return depth
        duplicates.add(end_state_goal)
        for i in edges[end_state_goal]:
            if i[0] in duplicates: continue
            depth = v_goal + i[1]
            if i[0] not in visited_goal or visited_goal[i[0]][0] > depth:
                heappush(fringe_goal, (depth, i[0], end_state_goal_path + [i[0]]))
                visited_goal[i[0]] = (depth, end_state_goal_path + [i[0]])
            counter += 1
            red(canvas, (end_state_goal, i[0]))
            if counter % 750 == 0: root.update()
    return

def reverse_astar(start, end):
    count = 0
    visited = set()
    fringe = list()
    #path = dict()
    heappush(fringe, (-calcd(coordinates[start], coordinates[end]), 0, start, [start]))
    while len(fringe) != 0:
        v, depth, end_state, path = heappop(fringe)
        if end_state == end:
            temp = end
            newcount = 0
            for i in range(len(path) - 1):
                green(canvas, (path[i], path[i + 1]))
                if i % 30 == 0:
                    root.update()
            return depth
        if end_state not in visited:
            visited.add(end_state)
            for i in edges[end_state]:
                if i not in visited:
                    newpath = path.copy()
                    newpath.append(i[0])
                    new_depth = depth + i[1]
                    taxicab = calcd(coordinates[i[0]], coordinates[end]) + new_depth
                    heappush(fringe, (-taxicab, new_depth, i[0], newpath))
                count += 1
                red(canvas, (end_state, i[0]))
                red(canvas, (i[0], end_state))
                if count % 200 == 0: root.update()
    return None

def kdfs(start, end, k):
    count = 0
    fringe = []
    visited = {start: (0, [start])}
    #path = dict()
    heappush(fringe, (0, start, [start]))
    while len(fringe) > 0:
        root.update()
        v_depth, end_state, path = heappop(fringe)
        if end_state == end:
            for i in range(len(path) - 1):
                green(canvas, (path[i], path[i + 1]))
                if i % 50 == 0: root.update()
            return v_depth
        if v_depth < k:
            for i in edges[end_state]:
                newdepth = v_depth + i[1]
                if i[0] not in visited.keys():
                    heappush(fringe, (newdepth, i[0], path + [i[0]]))
                    visited[i[0]] = (newdepth, path + [i[0]])
                    count += 1
                    red(canvas, (i[0], end_state))
                    red(canvas, (end_state, i[0]))
    return None

def iddfs(start, end):
    ipp_value = calcd(coordinates[start], coordinates[end]) // 2 #this would be maximum depth
    k = ipp_value
    #k = 0
    result = None
    while result == None:
        result = kdfs(start, end, k)
        k += ipp_value
        if k%(1000*ipp_value) == 0: root.update()
    return result
# def overestimated_bidirectional_astar(start, end):
#     counter = 0
#     # dictionary to store depth and path in same structure
#     visited_start = {start: (0, [start])}
#     visited_goal = {end: (0, [end])}
#     # normal fringe
#     fringe_start = list()
#     fringe_goal = list()
#     heappush(fringe_start, (0, start, calcd(coordinates[start], coordinates[end]), [start]))
#     heappush(fringe_goal, (0, end, calcd(coordinates[start], coordinates[end]), [end]))
#     # need to store duplicates to solve problem
#     duplicates = set()
#     while len(fringe_goal) != 0 and len(fringe_start) != 0:
#         v_start, end_state, taxicab, end_state_path = heappop(fringe_start)
#         if end_state in visited_goal:
#             depth = v_start + visited_goal[end_state][0]
#             path = visited_start[end_state][1] + visited_goal[end_state][1][::-1][1:]
#             # Iterate through path and draw in green
#             temp = start
#             i=0
#             while (temp != end):
#                 i+=1
#                 green(canvas, (temp, path[i]))
#                 green(canvas, (path[i], temp))
#                 temp = path[i]
#                 root.update()
#             return depth
#         for i in edges[end_state]:
#             depth = v_start + i[1]
#             if i[0] not in visited_start:
#                 heappush(fringe_start, (depth, i[0], taxicab + calcd(coordinates[i[0]], coordinates[end]), end_state_path + [i[0]]))
#                 visited_start[i[0]] = (depth, end_state_path + [i[0]])
#             counter += 1
#             red(canvas, (end_state, i[0]))
#             if counter % 750 == 0: root.update()
#         v_goal, end_state_goal, taxicab_goal, end_state_goal_path = heappop(fringe_goal)
#         if end_state_goal in visited_start:
#             depth = v_goal + visited_start[end_state_goal][0]
#             path = visited_goal[end_state_goal][1] + visited_start[end_state_goal][1][::-1][1:]
#             # Iterate through path and draw in green
#             temp = end
#             i=0
#             while (temp != start):
#                 i+=1
#                 green(canvas, (temp, path[i]))
#                 green(canvas, (path[i], temp))
#                 temp = path[i]
#                 root.update()
#             return depth
#         for i in edges[end_state_goal]:
#             depth = v_goal + i[1]
#             if i[0] not in visited_goal:
#                 heappush(fringe_goal, (depth, i[0], taxicab_goal + calcd(coordinates[i[0]], coordinates[start]), end_state_goal_path + [i[0]]))
#                 visited_goal[i[0]] = (depth, end_state_goal_path + [i[0]])
#             counter += 1
#             red(canvas, (end_state_goal, i[0]))
#             if counter % 750 == 0: root.update()
#     return
# def overestimated_bidirectional_astar(start, end):
#     count = 0
#     visited_start = set()
#     visited_end = set()
#     fringe_start = list()
#     fringe_end = list()
#
#     paths_completed = []
#     # path_start = dict()
#     # path_end = dict()
#
#     #did not merge path and visited in this one becuase it kept on causing errors
#     heappush(fringe_start, (calcd(coordinates[start], coordinates[end]), 0, start, []))
#     heappush(fringe_end, (calcd(coordinates[end], coordinates[start]), 0, end, []))
#     #pushed in a differnet way becuas for some reason the other orientation i used did not work
#     while len(fringe_start) != 0 and len(fringe_end) != 0:
#         v_start, depth_start, end_state_start, path_start = heappop(fringe_start)
#         v_end, depth_end, end_state_end, path_end = heappop(fringe_end)
#         #if end_state_start in visited_end or end_state_end in visited_start:
#         if end_state_start in visited_end or end_state_end in visited_start:
#             final_path = path_start
#             for i in range(len(final_path) - 1):
#                 if final_path[i] != final_path[i + 1]:
#                     green(canvas, (final_path[i], final_path[i + 1]))
#                     green(canvas, (final_path[i + 1], final_path[i]))
#                     root.update()
#             final_path = path_end  # + paths_completed[:-1][::-1]
#             for i in range(len(final_path) - 1):
#                 if final_path[i] != final_path[i + 1]:
#                     green(canvas, (final_path[i], final_path[i + 1]))
#                     green(canvas, (final_path[i + 1], final_path[i]))
#                     root.update()
#             return depth_start + depth_end
#         if end_state_start not in visited_end:
#             visited_start.add(end_state_start)
#             for i in edges[end_state_start]:
#                 if i[0] not in visited_start:
#                     newpath_start = path_start.copy()
#                     newpath_start.append(i[0])
#                     newdepth = depth_start + i[1]
#                     taxicab = calcd(coordinates[i[0]], coordinates[end]) + newdepth
#                     heappush(fringe_start, (taxicab, newdepth, i[0], newpath_start))
#                 count += 1
#                 red(canvas, (end_state_start, i[0]))
#                 red(canvas, (i[0], end_state_start))
#                 if count % 500 == 0: root.update()
#         if end_state_end not in visited_end:
#             visited_end.add(end_state_end)
#             for i in edges[end_state_end]:
#                 if i[0] not in visited_end:
#                     newpath_end = path_end.copy()
#                     newpath_end.append(i[0])
#                     newdepth = depth_end + i[1]
#                     taxicab = calcd(coordinates[i[0]], coordinates[start]) + newdepth
#                     heappush(fringe_end, (taxicab, newdepth, i[0], newpath_end))
#                 count += 1
#                 red(canvas, (end_state_end, i[0]))
#                 red(canvas, (i[0], end_state_end))
#                 if count % 500 == 0: root.update()
#
#
#     return None


# path_start = dict()
# path_end = dict()
#did not merge path and visited in this one becuase it kept on causing errors
def overestimated_bidirectional_astar(start, end):
    count = 0
    visited_start = {start: (0, [])}
    visited_goal = {end: (0, [])}
    fringe_start = list()
    fringe_end = list()
    heappush(fringe_start, (calcd(coordinates[start], coordinates[end]), 0, start, [start]))
    heappush(fringe_end, (calcd(coordinates[end], coordinates[start]), 0, end, [end]))
    #pushed in a differnet way becuas for some reason the other orientation i used did not work
    while len(fringe_start) != 0 and len(fringe_end) != 0:
        v_start, depth_start, end_state_start, path_start = heappop(fringe_start)
        v_end, depth_end, end_state_end, path_end = heappop(fringe_end)

        if end_state_start in visited_goal:
            path = path_start + visited_goal[end_state_start][1][::-1]
            temp = end
            for i in visited_goal[end_state_start][1]:
                depth_start += calcd(coordinates[temp], coordinates[i])
                temp = i
            #final_path = path_start + path_end[::-1][1:] #reverse list
            temp = start
            i = 0
            while (temp != end):
                i += 1
                green(canvas, (temp, path[i]))
                green(canvas, (path[i], temp))
                temp = path[i]
                root.update()
            return depth_start
        for i in edges[end_state_start]:
            new_taxicab_start = depth_start + calcd(coordinates[i[0]], coordinates[end])
            if i[0] not in visited_start or new_taxicab_start < visited_start[i[0]][0]:
                #THIS IF STATEMENT IS CRUTIAL
                #I NEED THE SECOND PART TO MAKE PATH WORK
                if i[0] not in visited_start:
                    visited_start[i[0]] = (new_taxicab_start, path_start + [i[0]])
                #if it is already there then just update heuristic not the path
                #THIS IS CUASING ME KEY VALUE ERROR
                elif i[0] in visited_start:
                    #HERE IF PROBLEM
                    visited_start[i[0]] = (new_taxicab_start, "")
                heappush(fringe_start, (new_taxicab_start, depth_start + calcd(coordinates[end_state_start], coordinates[i[0]]), i[0], path_start + [i[0]]))
            count += 1
            red(canvas, (end_state_start, i[0]))
            red(canvas, (i[0], end_state_start))
            if count % 500 == 0: root.update()
        if end_state_end in visited_start:
            path = visited_start[end_state_end][1] + path_end[:-1][::-1]
            temp = start
            for i in visited_start[end_state_end][1]:
                depth_end += calcd(coordinates[temp], coordinates[i])
                temp = i
            temp = start
            i = 0
            while (temp != end):
                i += 1
                green(canvas, (temp, path[i]))
                green(canvas, (path[i], temp))
                temp = path[i]
                root.update()
            return depth_end
        for i in edges[end_state_end]:
            new_taxicab = depth_end + calcd(coordinates[i[0]], coordinates[start])
            if i[0] not in visited_goal or new_taxicab < visited_goal[i[0]][0]:
                if i[0] not in visited_goal:
                    visited_goal[i[0]] = (new_taxicab, path_end + [i[0]])
                # if it is already there then just update heuristic not the path
                # THIS IS CUASING ME KEY VALUE ERROR
                elif i[0] in visited_goal:
                    #HEREE
                    visited_goal[i[0]] = (new_taxicab, "")
                heappush(fringe_end, (new_taxicab, depth_end + calcd(coordinates[end_state_end], coordinates[i[0]]), i[0], path_end + [i[0]]))
            count += 1
            red(canvas, (end_state_end, i[0]))
            red(canvas, (i[0], end_state_end))
            if count % 500 == 0: root.update()

    return None

start = sys.argv[1]
end = sys.argv[2]

print("which search do you want to see:")
whichone = input(" (1) Dijkstra \n (2) A* \n (3) DFS \n (4) Bidirectional Dijkstra \n (5) Reverse A* \n (6) IDDFS \n (7) Bidirectional A* \n"  )
start_spot = city[start]
end_spot = city[end]
if whichone == "1":
    print(dijkstra(start_spot, end_spot))  #done
    root.mainloop()
elif whichone == "2":
    print(astar(start_spot, end_spot)) #done
    root.mainloop()
elif whichone == "3":
    print(dfs(start_spot, end_spot))  #done
    root.mainloop()
elif whichone == "4":
    print(bidirectional_dijkstra(start_spot, end_spot))  #done
    root.mainloop()
elif whichone == "5":
    print(reverse_astar(start_spot, end_spot)) #done
    root.mainloop()
elif whichone == "6": #done
    print(iddfs(start_spot, end_spot))
    root.mainloop()
elif whichone == "7": #NOT
    print(overestimated_bidirectional_astar(start_spot, end_spot))
    root.mainloop()



canvas.delete("all")
root.mainloop()

