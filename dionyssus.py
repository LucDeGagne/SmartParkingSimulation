import pygame
import os
import time
from turns import GPS
from turns import parking
from turns import results
import smartParking
import datetime
import math
import sys
import setup

log = ""
open = [[0,133,0,0,'b'], [0,120,0,0,'b'], [160,0,-90,0,'d'], [955,0,-90,0,'e'], [975,0,-90,0,'e'], [1180,105,180,0,'g'], [1180,485,180,0,'l'], [0,845,0,0,'m']]
close = ['v','w','x','y','z']

set = setup.makeparams("./testsuite/"+sys.argv[1])
log += sys.argv[1]+","
destinationsStay = set[0]
speeds = set[1]
choices = set[2]
destinationsThrough = set[3]

start = []
destinations = []
for i in range(len(choices)):
    start.append(open[choices[i]])
for i in range(len(destinationsStay)):
    destinations.append(destinationsStay[i])
    destinations.append(destinationsThrough[i])

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                image = image.convert_alpha()
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((1200, 865))
done = False
clock = pygame.time.Clock()
counter = 0
k = []
path = []
park = []
for i in range(len(start)):
    if i%2 == 0:
        temp = smartParking.test(start[i],destinations[i][0],destinations[i][1])
        park.append(temp[1])
        path.append(temp[0])
        k.append(0)
    else:
        temp = smartParking.test2(start[i],destinations[i])
        park.append([])
        path.append(temp)
        k.append(0)

for i in range(len(start)):
    if start[i][4] == 'e' and path[i][0] == 14:
        start[i] = open[3]
    if start[i][4] == 'e' and (path[i][0] == 12 or path[i][0] == 13):
        start[i] = open[4]
    if start[i][4] == 'b' and path[i][0] == 0:
        start[i] = open[0]
    if start[i][4] == 'b' and (path[i][0] == 1 or path[i][0] == 2):
        start[i] = open[1]
# print(len(start))
# print(len(park))
# print(len(path))
# print(len(k))
# print(park)
# print(path)
# print(k)
running = []
travelTimeB = []
travelTimeR = []
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        if counter%20 == 0:# and counter < 10:
            if len(start) > 0:
                running.append(start.pop(0))
        screen.fill((255, 255, 255))
        screen.blit(get_image('test-dim-med.png'), (0, 0))
        sprite = []
        for i in range(len(running)):
            if i%2 == 0:
                sprite.append(pygame.transform.scale(get_image('bluecar.png'), (21,21)))
                sprite[i] = pygame.transform.rotate(sprite[i], running[i][2])
                screen.blit(sprite[i], (running[i][0], running[i][1]))
                if k[i] < len(path[i]):
                    running[i] = GPS(running[i], path[i][k[i]], running, counter,speeds[i])
                    if running[i][3] == -1:
                        running[i][3] = 0
                        k[i] = k[i] + 1
                else:
                    running[i] = parking(running[i], running, park[i],speeds[i])
                    if(running[i][3] == -1):
                        travelTimeB.append(counter - (i*20))
                        running[i][3] = 100

            else:
                sprite.append(pygame.transform.scale(get_image('redcar.png'), (21,21)))
                sprite[i] = pygame.transform.rotate(sprite[i], running[i][2])
                screen.blit(sprite[i], (running[i][0], running[i][1]))
                if k[i] < len(path[i]):
                    running[i] = GPS(running[i], path[i][k[i]], running, counter,speeds[i])
                    if running[i][3] == -1 and k[i] == len(path[i]) - 1:
                        travelTimeR.append(counter - (i*10))
                    if running[i][3] == -1:
                        running[i][3] = 0
                        k[i] = k[i] + 1




        # else:
        #     if counter > 0:
        #         start[value] = turns.parking(start[value], park)
        #         if start[value][3] == -1:
        #             counter = counter - 1
        #     else:
        #         if start[value][3] == -1 and last == -1:
        #             start[value][3] = 0
        #             start[value] = leave.lotparking(start[value],park)
        #             last = start[value][5]
        #         else:
        #             start[value] = turns.GPS(start[value], last)

        counter = counter + 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            screen.blit(sprite[1], event.pos)
        pygame.display.flip()
        clock.tick(60)
        if len(travelTimeB) == len(running)/2:
            done = True

# print(len(travelTimeB))
# print(len(travelTimeR))
blueCars = []
metric = []
for i in range(len(running)):
    if i%2 == 0:
        metric.append(running[i])
        blueCars.append(running[i])
spots = str(blueCars)
# log += "Blue car locations:\n"
# log += str(blueCars)
# log += "\nTotal time units for all cars to be parked: " + str(counter)+"\n"
log += str(counter)+","
avgTB = sum(travelTimeB)/len(travelTimeB)
# log += "The average travel time units from when the car enters the screen to when it is parked: "+ str(avgTB) +"\n"
log += str(avgTB)+","
avgTR = sum(travelTimeR)/len(travelTimeR)
# log += "The average travel time units from when the car enters the screen to when it leaves the screen: "+str(avgTR)+"\n"
log += str(avgTR)+","
total = 0
for j in range(len(metric)):
    x1 = metric[j][0]
    x2 = destinationsStay[j][0]
    y1 = metric[j][1]
    y2 = destinationsStay[j][1]
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    total = total + distance
avgD = total/len(metric)
# log += "The average distance from parking spot to destination: " + str(avgD)+"\n"
log += str(avgD)+","
log += results()
# print(log)
# setup.writeresults(spots + "\n")
setup.writeresults(log + "\n")
