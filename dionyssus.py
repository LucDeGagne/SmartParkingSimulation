import pygame
import os
import time
from turns import GPS
from turns import parking
from turns import results
import smartParking
import datetime
import math

# [x,y,angle,position,location]
open = [[0,133,0,0,'b'], [0,120,0,0,'b'], [160,0,-90,0,'d'], [955,0,-90,0,'e'], [975,0,-90,0,'e'], [1180,105,180,0,'g'], [1180,485,180,0,'l'], [0,845,0,0,'m']]
close = ['v','w','x','y','z']
# destinations = [[82, 766], [473, 265], [520, 483], [826, 338]]
destinationsStay = [[82, 766], [473, 265], [520, 483], [826, 338], [1177, 364], [939, 270], [738, 251], [579, 266], [584, 262], [930, 729], [685, 354], [310, 374], [870, 761], [205, 564], [1183, 243], [474, 489], [1118, 479], [567, 427], [783, 571], [918, 850], [233, 452], [17, 735], [986, 449], [845, 589], [51, 232], [847, 758], [414, 577], [1020, 695], [862, 423], [323, 337], [598, 228], [522, 799], [827, 765], [461, 329], [1041, 261], [457, 781], [307, 304], [460, 542], [240, 418], [91, 500], [80, 296], [681, 422], [75, 255], [14, 717], [197, 830], [314, 421], [779, 221], [1069, 797], [553, 253], [826, 634], [194, 218], [1174, 708], [341, 713], [480, 389], [920, 482], [83, 250], [5, 405], [394, 621], [65, 663], [677, 422], [644, 597], [294, 827], [282, 712], [708, 506], [1165, 449], [278, 857], [1174, 501], [312, 421], [492, 392], [193, 376], [345, 630], [1107, 819], [633, 570], [369, 302], [683, 304], [653, 263], [127, 388], [676, 534], [1152, 623], [597, 592], [1031, 768], [922, 342], [933, 627], [429, 747], [190, 261], [855, 818], [101, 292], [569, 522], [859, 384], [1149, 808], [360, 849], [205, 307], [291, 412], [378, 250], [1013, 265], [464, 644], [2, 851], [1162, 529], [10, 471], [882, 209], [1196, 284], [598, 441], [12, 402], [319, 664], [760, 745], [616, 556], [859, 487], [47, 300], [361, 771], [972, 349], [612, 733], [1052, 216], [1171, 590], [267, 674], [668, 670], [45, 663], [1072, 313], [1032, 699], [452, 745], [609, 591], [339, 842], [503, 847], [1193, 230], [550, 391], [622, 441], [40, 402], [405, 248], [417, 783], [508, 714], [757, 475], [1039, 282], [1088, 820], [598, 430], [751, 204], [1153, 519], [1036, 315], [370, 569], [1086, 460], [524, 448], [823, 783], [1046, 368], [366, 505], [910, 698], [960, 857], [772, 862], [510, 557], [489, 545], [75, 486], [473, 855], [848, 252], [230, 631], [685, 582], [848, 604], [401, 650], [276, 534], [700, 392], [582, 285], [529, 718], [1013, 717], [720, 664], [145, 608], [162, 701], [349, 664], [335, 360], [723, 436], [555, 317], [740, 280], [693, 246], [727, 421], [1176, 790], [575, 501], [579, 589], [700, 228], [750, 420], [807, 618], [636, 790], [526, 623], [405, 602], [861, 302], [279, 453], [155, 676], [432, 595], [1163, 642], [201, 243], [609, 764], [477, 556], [447, 591], [1137, 281], [1191, 741], [23, 440], [48, 430], [520, 272], [138, 705], [114, 472], [81, 620], [905, 556], [346, 766], [1083, 449], [109, 412], [947, 719], [397, 261], [487, 521], [276, 700], [1063, 274], [1078, 819], [1088, 700], [828, 471], [995, 249], [539, 820], [747, 667], [964, 403], [29, 754], [1191, 714], [979, 304], [185, 814], [278, 377], [815, 857], [230, 857], [866, 750], [326, 743]]

destinationsThrough = ['w', 'z', 'w', 'v', 'x', 'z', 'y', 'w', 'w', 'x', 'z', 'v', 'z', 'v', 'v', 'y', 'w', 'y', 'v', 'y', 'x', 'x', 'x', 'v', 'y', 'w', 'x', 'y', 'x', 'w', 'y', 'y', 'z', 'w', 'y', 'v', 'y', 'x', 'z', 'y', 'x', 'x', 'w', 'y', 'x', 'w', 'x', 'v', 'z', 'z', 'x', 'z', 'z', 'w', 'y', 'x', 'w', 'v', 'y', 'y', 'y', 'v', 'v', 'w', 'v', 'x', 'x', 'v', 'x', 'v', 'z', 'v', 'x', 'v', 'w', 'v', 'z', 'y', 'z', 'z', 'z', 'w', 'x', 'v', 'x', 'z', 'y', 'v', 'y', 'y', 'z', 'w', 'y', 'x', 'z', 'z', 'z', 'w', 'x', 'z', 'x', 'v', 'z', 'z', 'w', 'v', 'w', 'w', 'y', 'w', 'z', 'z', 'w', 'x', 'z', 'w', 'z', 'y', 'w', 'z', 'z', 'y', 'z', 'z', 'x', 'w', 'x', 'x', 'z', 'x', 'z', 'x', 'x', 'z', 'z', 'w', 'x', 'x', 'z', 'y', 'w', 'x', 'z', 'y', 'w', 'z', 'z', 'w', 'y', 'x', 'x', 'x', 'z', 'v', 'v', 'y', 'y', 'z', 'v', 'w', 'w', 'v', 'y', 'w', 'w', 'w', 'y', 'w', 'z', 'v', 'y', 'w', 'z', 'w', 'v', 'x', 'z', 'w', 'w', 'w', 'w', 'x', 'z', 'w', 'x', 'z', 'x', 'x', 'v', 'z', 'w', 'z', 'z', 'z', 'z', 'z', 'v', 'x', 'x', 'v', 'v', 'x', 'z', 'v', 'v', 'w', 'x', 'v', 'v', 'z', 'y', 'y', 'w', 'z', 'v', 'x', 'v', 'w', 'v', 'w']
# choices = [3,4,3,4]
choices = [3, 4, 4, 4, 1, 3, 5, 1, 4, 3, 7, 6, 7, 3, 4, 3, 3, 6, 7, 5, 4, 3, 4, 3, 6, 3, 6, 1, 2, 6, 0, 5, 1, 0, 5, 3, 4, 4, 7, 2, 0, 7, 0, 0, 1, 3, 0, 3, 4, 3, 1, 2, 4, 3, 6, 6, 4, 3, 1, 3, 0, 4, 5, 5, 6, 4, 7, 6, 7, 4, 4, 5, 0, 2, 4, 7, 1, 6, 6, 4, 3, 5, 1, 5, 4, 7, 6, 3, 5, 4 , 0, 4, 6, 3, 0, 1, 1, 4, 2, 4, 6, 6, 6, 0, 1, 4, 1, 4, 4, 6, 6, 5, 3, 3, 2, 4, 0, 4, 6, 5, 0, 0, 1, 7, 2, 1, 0, 3, 3, 1, 5, 6, 0, 0, 7, 6, 6, 6, 6, 3, 7, 6, 5, 7, 0, 6, 5, 3, 0, 7, 0, 3, 5, 5, 7, 5, 2, 6, 2, 6, 5, 2, 2, 5, 1, 0, 3, 1, 4, 6, 2, 5, 2, 1, 5, 0, 7, 3, 0, 0, 0, 6, 5, 1, 7, 1, 4, 2, 7, 0, 1, 7, 1, 3, 7, 2, 7, 0, 0, 2, 3, 4, 1, 6, 6, 3, 0, 3, 7, 7, 6, 3, 1, 0, 3, 1, 2, 5, 2, 6]
start = []
destinations = []
for i in range(len(choices)):
    start.append(open[choices[i]])
    start.append(open[choices[len(choices)-i-1]])
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
        if counter%10 == 0:
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
                    running[i] = GPS(running[i], path[i][k[i]], running, counter)
                    if running[i][3] == -1:
                        running[i][3] = 0
                        k[i] = k[i] + 1
                else:
                    running[i] = parking(running[i], running, park[i])
                    if(running[i][3] == -1):
                        travelTimeB.append(counter - (i*10))
                        running[i][3] = 100

            else:
                sprite.append(pygame.transform.scale(get_image('redcar.png'), (21,21)))
                sprite[i] = pygame.transform.rotate(sprite[i], running[i][2])
                screen.blit(sprite[i], (running[i][0], running[i][1]))
                if k[i] < len(path[i]):
                    running[i] = GPS(running[i], path[i][k[i]], running, counter)
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

print("Total time units for all cars to be parked: " + str(counter))
# print(len(travelTimeB))
# print(len(travelTimeR))
metric = []
for i in range(len(running)):
    if i%2 == 0:
        metric.append(running[i])
total = 0
avgTB = sum(travelTimeB)/len(travelTimeB)
print("The average travel time units from when the car enters the screen to when it is parked: "+ str(avgTB))
avgTR = sum(travelTimeR)/len(travelTimeR)
print("The average travel time units from when the car enters the screen to when it leaves the screen: "+ str(avgTR))
for j in range(len(metric)):
    x1 = metric[j][0]
    x2 = destinationsStay[j][0]
    y1 = metric[j][1]
    y2 = destinationsStay[j][1]
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    total = total + distance
avgD = total/len(metric)
print("The average distance from parking spot to destination: " + str(avgD))
results()