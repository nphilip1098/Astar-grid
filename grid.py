import cv2
import matplotlib.pyplot as plt
import numpy as np
import heapq

originalImage = cv2.imread('grid.jpeg',1)# input the grid
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)#by default 0--> black and 255--> white, so we need to perform an inversion to mark the obstacles as 1 
img_reverted= cv2.bitwise_not(grayImage)
  
(thresh, blackAndWhiteImage) = cv2.threshold(img_reverted, 127, 255, cv2.THRESH_BINARY)
 
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)

binarymap=blackAndWhiteImage/255
print(binarymap)

dimension=binarymap.shape

print(dimension)


start=(56,55)# assigning the start position
goal=(197,293)# assigning the goal postion

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(binarymap,cmap=plt.cm.Dark2)
ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 100)
ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 100)
plt.show()

def heuristic(a, b):

    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) # calculating the euclidean distance


def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()

    came_from = {}

    gscore = {start:0}

    fscore = {start:heuristic(start, goal)}

    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
 

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:

            data = []

            while current in came_from:

                data.append(current)

                current = came_from[current]

            return data

        close_set.add(current)

        for i, j in neighbors:

            neighbor = current[0] + i, current[1] + j

            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array.shape[0]:

                if 0 <= neighbor[1] < array.shape[1]:                

                    if array[neighbor[0]][neighbor[1]] == 1:

                        continue

                else:

                    # array bound y walls

                    continue

            else:

                # array bound x walls

                continue
 

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):

                continue
 

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:

                came_from[neighbor] = current

                gscore[neighbor] = tentative_g_score

                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                heapq.heappush(oheap, (fscore[neighbor], neighbor))
 

    return False

route = astar(binarymap, start, goal)

route = route + [start]

route = route[::-1]

print(route)

x_coords = []

y_coords = []

for i in (range(0,len(route))):

    x = route[i][0]

    y = route[i][1]

    x_coords.append(x)

    y_coords.append(y)

# plot map and path

fig, ax = plt.subplots(figsize=(20,20))

ax.imshow(binarymap, cmap=plt.cm.Dark2)
ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)
ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)
ax.plot(y_coords,x_coords, color = "black")
plt.show() 

  
cv2.waitKey(0)
cv2.destroyAllWindows()

