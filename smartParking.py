import math
#x,y,a,occupied
somW = [[809,0,180,0], [809,10,180,0], [809,21,180,0], [809,31,180,0], [809,42,180,0], [809,52,180,0], [809,63,180,0], [913,40,0,0], [913,50,0,0], [913,61,0,0], [859,0,0,0], [859,10,0,0], [859,21,0,0], [859,31,0,0], [859,42,0,0], [859,52,0,0], [859,63,0,0]]
somE = [[786,162,180,0], [786,172,180,0], [786,183,180,0], [786,193,180,0], [786,204,180,0], [786,214,180,0], [786,225,180,0], [786,235,180,0], [786,246,180,0], [786,256,180,0], [810,285,-90,0], [821,285,-90,0], [832,285,-90,0], [843,285,-90,0], [854,285,-90,0], [865,285,-90,0], [876,285,-90,0]]
conS1 = [[786,305,180,0], [786,316,180,0], [786,327,180,0]]
conS2 = [[1063,661,90,0], [1074,661,90,0], [1085,661,90,0], [1096,661,90,0], [1107,661,90,0], [1118,661,90,0], [1129,661,90,0], [1140,661,90,0], [1151,661,90,0], [1018,724,-90,0], [1029,724,-90,0], [1040,724,-90,0], [1051,724,-90,0], [1062,724,-90,0], [1073,724,-90,0], [1084,724,-90,0], [1095,724,-90,0], [1106,724,-90,0], [1117,724,-90,0], [1128,724,-90,0], [1139,724,-90,0], [1150,724,-90,0], [1161,724,-90,0], [1018,747,-90,0], [1029,747,-90,0], [1040,747,-90,0], [1051,747,-90,0], [1062,747,-90,0], [1073,747,-90,0], [1084,747,-90,0], [1095,747,-90,0], [1106,747,-90,0], [1117,747,-90,0], [1128,747,-90,0], [1139,747,-90,0], [1150,747,-90,0], [1161,747,90,0], [1030,805,-90,0], [1041,805,-90,0], [1052,805,-90,0], [1063,805,-90,0], [1074,805,-90,0], [1085,805,-90,0], [1096,805,-90,0], [1107,805,-90,0], [1118,805,-90,0], [1129,805,-90,0], [1140,805,-90,0], [1151,805,-90,0], [1162,805,-90,0], [1173,805,-90,0], [1184,805,-90,0]]
macW1 = [[780,564,0,0], [780,574,0,0], [780,585,0,0], [780,596,0,0]]
macW2 = [[620,313,90,0], [631,313,90,0], [642,313,90,0], [653,313,90,0], [664,313,90,0], [675,313,90,0], [686,313,90,0], [697,313,90,0], [708,313,90,0], [719,313,90,0], [730,313,90,0], [741,313,90,0], [752,313,90,0], [763,313,90,0]]
macW3 = [[463,316,90,0], [474,316,90,0], [485,316,90,0], [496,316,90,0], [509,316,90,0], [520,316,90,0], [550,316,90,0], [562,316,90,0], [573,316,90,0]]
macW4 = [[450,175,0,0], [450,185,0,0], [450,196,0,0], [450,206,0,0], [450,217,0,0], [450,227,0,0], [450,237,0,0], [450,248,0,0], [450,258,0,0], [450,269,0,0], [450,279,0,0], [450,291,0,0], [443,313,0,0], [443,323,0,0], [443,334,0,0], [443,344,0,0], [443,355,0,0], [443,365,0,0], [443,376,0,0], [443,386,0,0], [443,397,0,0], [443,407,0,0], [443,418,0,0], [443,428,0,0], [443,439,0,0], [383,175,180,0], [383,175,0,0], [383,185,0,0], [383,196,0,0], [383,206,0,0], [383,217,0,0], [383,227,0,0], [383,237,0,0], [383,248,0,0], [383,258,0,0], [383,269,0,0], [383,279,0,0], [383,291,0,0], [383,313,0,0], [383,323,0,0], [383,334,0,0], [383,344,0,0], [383,355,0,0], [383,365,0,0], [383,376,0,0], [383,386,0,0], [383,397,0,0], [383,407,0,0], [383,418,0,0], [383,428,0,0], [383,439,0,0]]
macW5 = [[312,535,90,0], [323,535,90,0], [334,535,90,0], [345,535,90,0], [356,535,90,0], [302,582,-90,0], [313,582,-90,0], [324,582,-90,0], [335,582,-90,0], [346,582,-90,0], [357,582,-90,0], [368,582,-90,0]]
gilE = [[549,674,180,0], [549,685,180,0], [549,696,180,0], [606,672,0,0], [606,684,0,0], [606,695,0,0]]

streetparking = [[413,128,0,0,'f'], [438,128,0,0,'f'], [463,128,0,0,'f'], [488,128,0,0,'f'], [513,128,0,0,'f'], [540,467,180,0,'h'], [565,467,180,0,'h'], [590,467,180,0,'h'], [615,467,180,0,'h'], [640,467,180,0,'h'], [685,467,180,0,'h'], [710,467,180,0,'h'], [735,467,180,0,'h'], [760,467,180,0,'h'], [785,467,180,0,'h'], [810,467,180,0,'h'], [835,467,180,0,'h'], [860,467,180,0,'h'], [885,467,180,0,'h'], [463,497,180,0,'h'], [488,497,180,0,'h'], [513,497,180,0,'h'], [538,497,180,0,'h'], [563,497,180,0,'h'], [588,497,180,0,'h'], [613,497,180,0,'h'], [638,497,180,0,'h'], [663,497,180,0,'h'], [688,497,180,0,'h'], [713,497,180,0,'h'], [807,497,180,0,'h'], [832,497,180,0,'h'], [857,497,180,0,'h'], [882,497,180,0,'h'], [273,493,-120,0,'h'], [286,493,-120,0,'h'], [299,493,-120,0,'h'], [312,493,-120,0,'h'], [325,493,-120,0,'h'], [101,465,120,0,'r'], [88,465,120,0,'r'], [75,465,120,0,'r'], [62,465,120,0,'r'], [305,831,0,0,'p'], [330,831,0,0,'p'], [419,831,0,0,'p'], [444,831,0,0,'p'], [469,831,0,0,'p'], [494,831,0,0,'p'], [615,831,0,0,'p'], [640,831,0,0,'p'], [688,831,0,0,'p'], [743,831,0,0,'p'], [844,831,0,0,'p'], [869,831,0,0,'p'], [894,831,0,0,'p']]
# streetparking = [[413,128,0,1,'f']]
# lots = [[850,105,'a'], [799,120,'f'], [955,314,'k'], [975,689,'q'], [760,490,'h'], [669,480,'h'], [517,480,'h'], [411,480,'h'], [377,490,'h'], [572,845,'p']]
# lotparking = [somW, somE, conS1, conS2, macW1, macW2, macW3, macW4, macW5, gilE]
lots = [[799,120,'f'], [955,314,'k'], [975,689,'q'], [760,490,'h'], [669,480,'h'], [517,480,'h'], [411,480,'h'], [377,490,'h'], [572,845,'p']]
lotparking = [somE, conS1, conS2, macW1, macW2, macW3, macW4, macW5, gilE]

def coordinates(x1,y1):
    v = -1
    min = 1800
    possible = []
    check = False
    for i in range(len(streetparking)):
        x2 = streetparking[i][0]
        y2 = streetparking[i][1]
        dist_x = abs(x1-x2)
        dist_y = abs(y1-y2)
        dist = math.sqrt((dist_x**2)+(dist_y**2))
        if streetparking[i][3] == 0 and dist < min:
            v = i
            min = dist
    if v != -1:
        check = True
        streetmin = min
        streetloc = v
        street = [streetparking[streetloc]]
        v = -1
        min = 1800
    dist = []
    for i in range(len(lots)):
        x2 = lots[i][0]
        y2 = lots[i][1]
        dist_x = abs(x1-x2)
        dist_y = abs(y1-y2)
        dist.append(math.sqrt((dist_x**2)+(dist_y**2)))
    for k in range(len(dist)):
        if dist[k] < min:
            for j in range(len(lotparking[k])):
                if lotparking[k][j][3] == 0:
                    v = k
                    l = j
                    min = dist[k]
    if check:
        if streetmin < min:
            streetparking[streetloc][3] = 1
            return street
        else:
            lotparking[v][l][3] = 1
            return [lots[v],lotparking[v][l]]
    lotparking[v][l][3] = 1
    return [lots[v],lotparking[v][l]]


#Intersection 1     Intersection 2      Intersection 3       Intersection 4     Intersection 5      Intersection 6
# a=somW1           e=conS2             h=macW3              k=conS4            n=gilE5             p=gilE6
# b=somE1           f=somE2             i=bankN3             l=macW4            o=bankN5            q=conS6
# c=bankN1          g=somW2             j=bankS3             m=macE4
# d=bankS1


def entry_street(car, park):
    #becomes smart GPS maybe
    #ending case is letters!
    #Each stall should have a destination letter!
    path = []
    if (len(park) == 2):
        x = park[0][0]
        y = park[0][1]
        destination = park[0][2]
    else:
        x =  park[0][0]
        y = park[0][1]
        destination = park[0][4]
    location = car[4]
    while location != destination:
        if(location == 'a'):
            # somW1
            # bankS
            path.append(3)
            location = 'j'
        elif(location == 'b'):
            #somE1
            #Choices: somE1 or bankS1
            if((y < 800 and x < 230) or y > 800):
                #bankS1
                path.append(0)
                location = 'j'
            else:
                #somE1
                path.append(2)
                location = 'f'
        elif(location == 'c'):
            # bankN1
            # somE1
            path.append(10)
            location = 'f'
        elif(location == 'd'):
            #bankS1
            if((y < 800 and x < 230) or y > 800):
                #bankS1
                path.append(6)
                location = 'j'
            else:
                #somE1
                path.append(7)
                location = 'f'
        elif(location == 'e'):
            # conS2
            # conS2 or somW2
            if(y < 350 or y > 800):
                #somW2
                path.append(14)
                location = 'a'
            else:
                #cons2
                path.append(12)
                location = 'k'
        elif(location == 'f'):
            # somE2
            # conS2
            path.append(17)
            location = 'k'
        elif(location == 'g'):
            # somW2
            # conS2 or somW2
            if(y < 350 or y > 800):
                #somW2
                path.append(16)
                location = 'a'
            else:
                #cons2
                path.append(15)
                location = 'k'
        elif(location == 'h'):
            # macW3
            #bankN3 or bankS3
            if(y < 350):
                # bankN3
                path.append(19)
                location = 'c'
            elif(x < 230):
                #macW3
                path.append(21)
                location = 'r'
            else:
                #bankS3
                path.append(20)
                location = 'n'
        elif(location == 'i'):
            # bankN3
            # macW3 or bankN3
            if(x < 230):
                #macW3
                path.append(23)
                location = 'r'
            else:
                #bankN3
                path.append(22)
                location = 'c'
        elif(location == 'j'):
            # bankS3
            # macW3 or bankS3
            if(x < 230):
                #macW3
                path.append(25)
                location = 'r'
            else:
                #bankS3
                path.append(24)
                location = 'n'
        elif(location == 'k'):
            # conS4
            # macW4 or conS4
            if(x > 950):
                #conS4
                path.append(28)
                location = 'q'
            else:
                #macW4
                path.append(29)
                location = 'h'
        elif(location == 'l'):
            # macW4
            # macW4 or conS4
            if(x > 950):
                #conS4
                path.append(27)
                location = 'q'
            else:
                #macW4
                path.append(26)
                location = 'h'
        elif(location == 'm'):
            # gilE5
            # bankN5 or gilE5
            if(y > 800):
                #gilE5
                path.append(30)
                location = 'p'
            else:
                #bankN5
                path.append(31)
                location = 'i'
        elif(location == 'n'):
            # bankS5
            # gilE5
            path.append(32)
            location = 'p'
        elif(location == 'p' or location == 'q'):
            # bankS5
            # gilE5
            path.append(35)
            location = 'i'
    return [path,park]

def exit_street(car, destination):
    #becomes smart GPS maybe
    #ending case is letters!
    #Each stall should have a destination letter!
    path = []
    location = car[4]
    count = 0
    while location != destination:
        if count < 4:
            count = count + 1
        if(location == 'a'):
            # somW1
            # somW1
            if destination == 'v':
                path.append(5)
                location = 'v'
            elif destination == 'w':
                path.append(4)
                location = 'w'
            else:
                path.append(3)
                location = 'j'
        elif(location == 'b'):
            #somE1
            if destination == 'w':
                path.append(1)
                location = 'w'
            elif destination == 'x':
                path.append(2)
                location = 'f'
            else:
                path.append(0)
                location = 'j'
        elif(location == 'c'):
            # bankN1
            if destination == 'v':
                path.append(11)
                location = 'v'
            elif destination == 'w':
                path.append(9)
                location = 'w'
            else:
                path.append(10)
                location = 'f'
        elif(location == 'd'):
            #bankS1
            if destination == 'v':
                path.append(8)
                location = 'v'
            elif destination == 'x':
                path.append(10)
                location = 'f'
            else:
                path.append(6)
                location = 'j'
        elif(location == 'e'):
            # conS2
            if destination == 'x':
                path.append(13)
                location = 'x'
            elif destination == 'y':
                path.append(12)
                location = 'k'
            else:
                path.append(14)
                location = 'a'
        elif(location == 'f'):
            # somE2
            if destination == 'x':
                path.append(18)
                location = 'x'
            else:
                path.append(17)
                location = 'k'
        elif(location == 'g'):
            # somW2
            if destination == 'y':
                path.append(15)
                location = 'k'
            else:
                path.append(16)
                location = 'a'
        elif(location == 'h'):
            # macW3
            if destination == 'z':
                path.append(21)
                location = 'z'
            elif destination == 'y':
                path.append(20)
                location = 'n'
            else:
                path.append(19)
                location = 'c'
        elif(location == 'i'):
            # bankN3
            if destination == 'z':
                path.append(23)
                location = 'z'
            else:
                path.append(22)
                location = 'c'
        elif(location == 'j'):
            # bankS3
            if destination == 'z':
                path.append(25)
                location = 'z'
            else:
                path.append(24)
                location = 'n'
        elif(location == 'k'):
            # conS4
            if destination == 'y':
                path.append(28)
                location = 'q'
            else:
                path.append(29)
                location = 'h'
        elif(location == 'l'):
            # macW4
            if destination == 'y':
                path.append(27)
                location = 'q'
            else:
                path.append(26)
                location = 'h'
        elif(location == 'm'):
            # gilE5
            if destination == 'y':
                path.append(30)
                location = 'p'
            else:
                path.append(31)
                location = 'i'
        elif(location == 'n'):
            # bankS5
            # gilE5
            path.append(32)
            location = 'p'
        elif(location == 'p'):
            # gilE6
            if destination == 'y':
                path.append(34)
                location = 'y'
            else:
                path.append(35)
                location = 'i'
        elif(location == 'q'):
            # conS6
            if destination == 'y':
                path.append(33)
                location = 'y'
            else:
                path.append(35)
                location = 'i'
    return path

# x = 850
# y = 105
# sprite = [0,120,0,0,'b']
def test (car, x, y):
    coord = coordinates(x,y)
    return entry_street(car, coord)

def test2 (car, dest):
    return exit_street(car, dest)
# print(test(sprite,x,y))
