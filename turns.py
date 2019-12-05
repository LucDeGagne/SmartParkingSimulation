speed = 5
turnsMade = 0
intersectionBrakes = [0,0,0,0,0,0]

def GPS(sprite, d, running, c, speed):
    l = sprite[4]
    if d == 0:
        sprite = somE_bankS(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 1:
        sprite = somE_bankN(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 2:
        sprite = somE_somE1(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 3:
        sprite = somW_bankS(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 4:
        sprite = somW_bankN(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 5:
        sprite = somW_somW1(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 6:
        sprite = bankS_bankS1(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 7:
        sprite = bankS_somE(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 8:
        sprite = bankS_somW(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 9:
        sprite = bankN_bankN1(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 10:
        sprite = bankN_somE(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 11:
        sprite = bankN_somW(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)

    elif d == 12:
        sprite = conS_conS2(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 13:
        sprite = conS_somE(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 14:
        sprite = conS_somW(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 15:
        sprite = somW_conS(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 16:
        sprite = somW_somW2(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 17:
        sprite = somE_conS(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 18:
        sprite = somE_somE2(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)

    elif d == 19:
        sprite = macW_bankN(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 20:
        sprite = macW_bankS(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 21:
        sprite = macW_macW3(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 22:
        sprite = bankN_bankN3(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 23:
        sprite = bankN_macW(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 24:
        sprite = bankS_bankS3(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 25:
        sprite = bankS_macW(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)

    elif d == 26:
        sprite = macW_macW4(sprite[0], sprite[1], sprite[2], sprite[3], running, speed)
    elif d == 27:
        sprite = macW_conS(sprite[0], sprite[1], sprite[2], sprite[3], running, speed)
    elif d == 28:
        sprite = conS_conS4(sprite[0], sprite[1], sprite[2], sprite[3], running, speed)
    elif d == 29:
        sprite = conS_macW(sprite[0], sprite[1], sprite[2], sprite[3], running, speed)

    elif d == 30:
        sprite = gilE_gilE5(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 31:
        sprite = gilE_bankN(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 32:
        sprite = bankS_gilE(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)

    elif d == 33:
        sprite = conS_gilE(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    elif d == 34:
        sprite = gilE_gilE6(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)

    elif d == 35:
        sprite = wrap_around(sprite[0], sprite[1], sprite[2], sprite[3], running, c, speed)
    sprite.append(l)
    return sprite

def north(x,y,check,inter):
    can = []
    for i in range(len(check)):
        if check[i][0] == x and check[i][1] != y:
            can.append(check[i])
    for j in range(len(can)):
        if can[j][1] < y and can[j][1] > y - 40:
            if inter != -1:
                global intersectionBrakes
                intersectionBrakes[inter-1] += 1
            return False
    return True

def south(x,y,check,inter):
    can = []
    for i in range(len(check)):
        if check[i][0] == x and check[i][1] != y:
            can.append(check[i])
    for j in range(len(can)):
        if can[j][1] > y and can[j][1] < y + 40:
            if inter != -1:
                global intersectionBrakes
                intersectionBrakes[inter-1] += 1
            return False
    return True

def east(x,y,check,inter):
    can = []
    for i in range(len(check)):
        if check[i][1] == y and check[i][0] != x:
            can.append(check[i])
    for j in range(len(can)):
        if can[j][0] > x and can[j][0] < x + 40:
            if inter != -1:
                global intersectionBrakes
                intersectionBrakes[inter-1] += 1
            return False
    return True

def west(x,y,check,inter):
    can = []
    for i in range(len(check)):
        if check[i][1] == y and check[i][0] != x:
            can.append(check[i])
    for j in range(len(can)):
        if can[j][0] < x and can[j][0] > x - 40:
            if inter != -1:
                global intersectionBrakes
                intersectionBrakes[inter-1] += 1
            return False
    return True

def conStomacWturn(check):
    for j in range(len(check)):
        if check[j][0] == 915 and check[j][1] ==  480:
            global intersectionBrakes
            intersectionBrakes[4] += 1
            return False
    return True

def somWtobankS1left(check):
    for j in range(len(check)):
        if check[j][0] == 260 and check[j][1] ==  110:
            global intersectionBrakes
            intersectionBrakes[1-1] += 1
            return False
    return True

def somEclump1(x,y,check):
    for j in range(len(check)):
        if check[j][0] == 740 and check[j][1] ==  120:
            global intersectionBrakes
            intersectionBrakes[2-1] += 1
            return False
    return True

def somEclump2(x,y,check):
    for j in range(len(check)):
        if check[j][0] == 440 and check[j][1] ==  115:
            global intersectionBrakes
            intersectionBrakes[2-1] += 1
            return False
    return True

def macWclump1(check):
    for j in range(len(check)):
        if check[j][0] == 1065 and check[j][1] ==  465:
            global intersectionBrakes
            intersectionBrakes[4-1] += 1
            return False
    return True

def macWtoconSturn(x,y,check):
    for j in range(len(check)):
        if check[j][0] < x and check[j][0] > x - 100:
            if check[j][1] < y + 100  and check[j][1] > y:
                global intersectionBrakes
                intersectionBrakes[4-1] += 1
                return False
    return True

def macWtomacW4straight(x,y,check):
    for j in range(len(check)):
        if check[j][0] < x and check[j][0] > x - 100:
            if check[j][1] < y + 100  and check[j][1] > y - 100:
                global intersectionBrakes
                intersectionBrakes[4-1] += 1
                return False
    return True

def WestLeftSouth(x,y,check):
    for j in range(len(check)):
        if check[j][0] < x + 20 and check[j][0] > x - 40:
            if check[j][1] > y and check[j][1] < y + 30:
                return False
    return True

def EastLeftNorth(x,y,check):
    for j in range(len(check)):
        if check[j][0] > x - 30 and check[j][0] < x + 50:
            if check[j][1] < y and check[j][1] > y + 40:
                return False
    return True

def NorthLeftWest(x,y,check):
    for j in range(len(check)):
        if check[j][0] < x + 30 and check[j][0] > x - 50:
            if check[j][1] < y and check[j][1] > y - 40:
                return False
    return True

def SouthLeftEast(x,y,check):
    for j in range(len(check)):
        if check[j][0] > x + 30 and check[j][0] < x - 50:
            if check[j][1] > y and check[j][1] < y + 40:
                return False
    return True


def Lights(counter):
    if (counter//200) >= 150:
        return False #Clear intersection
    if (counter//200)%2 == 0:
        return True #North South
    else:
        return False #East West

# Intersection 1
def somE_bankS(x,y,a,p,running,c,speed):
    if p==0 and east(x,y,running,1):
        if x == 50 and y != 133:
            y = 133
        if x != 105:
            x = x + speed
        else:
            p=1
    if p==1 and east(x,y,running,1) and not Lights(c):
        x = x + speed
        p = 2
    if p==2 and east(x,y,running,1):
        if x != 160 or a != -90:
            if x != 160:
                x = x + speed
            if a != -90:
                a = a - 5
        else:
            p = 3
    if p==3 and south(x,y,running,3):
        if y == 133:
            y = y + 2
        if y != 170:
            y = y + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def somE_bankN(x,y,a,p,running,c,speed):
    if p==0 and east(x,y,running,1):
        if x == 20 and y != 120:
            y = 120
        if x != 105:
            x = x + speed
        else:
            p=1
    if p==1 and east(x,y,running,1) and not Lights(c):
        x = x + speed
        p = 2
    if p==2 and east(x,y,running,1):
        if x != 185 or a != 90:
            if x != 185:
                x = x + speed
            if a != 90:
                a = a + 5
        else:
            p = 3
    if p==3 and north(x,y,running,-1) and EastLeftNorth(x,y,running):
        y = y - speed
        p = 4
    if p==4 and north(x,y,running,-1):
        if y != 0:
            y = y - speed
        else:
            p = 5
    if p==5:
        if y != -100:
            y = y - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def somE_somE1(x,y,a,p,running,c,speed):
    if p==0 and east(x,y,running,1):
        if x != 20:
            x = x + speed
        else:
            p=1
    if p==1 and east(x,y,running,1):
        y = 120
        p = 2
    if p==2 and east(x,y,running,1):
        if x != 105:
            x = x + speed
        else:
            p=3
    if p==3 and east(x,y,running,-1) and not Lights(c):
        x = x + speed
        p = 4
    if p==4 and east(x,y,running,2):
        if x != 385:
            x = x + speed
        else:
            p = -1
    return [x,y,a,p]

def bankS_bankS1(x,y,a,p,running,c,speed):
    if p==0 and south(x,y,running,1):
        if y != 55:
            y = y + speed
        else:
            p=1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p==2 and south(x,y,running,3):
        if y != 170:
            y = y + speed
        else:
            p = -1
    return [x,y,a,p]

def bankS_somE(x,y,a,p,running,c,speed):
    if p==0 and south(x,y,running,1):
        if y != 55:
            y = y + speed
        else:
            p=1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p==2 and south(x,y,running,1):
        if y != 120 or a != 0:
            if y != 120:
                y = y + speed
            if a != 0:
                a = a + 5
        else:
            p = 3
    if p==3 and east(x,y,running,-1) and SouthLeftEast(x,y,running):
        x = x + speed
        p = 4
    if p==4 and east(x,y,running,2):
        if x == 162:
            x = x + 3
        if x != 385:
            x = x + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1

    return [x,y,a,p]

def bankS_somW(x,y,a,p,running,c,speed):
    if p==0 and south(x,y,running,1):
        if y != 55:
            y = y + speed
        else:
            p=1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p==2 and south(x,y,running,-1):
        if y != 100 or a != -180:
            if y != 100:
                y = y + speed
            if a != -180:
                a = a - 5
        else:
            a = 180
            p = 3
    if p==3 and west(x,y,running,-1):
        if x >= 0:
            x = x - speed
        else:
            p = 4
    if p==4:
        if x >= -100:
            x = x - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def somW_bankS(x,y,a,p,running,c,speed):
    if p==0 and west(x,y,running,1):
        if x != 260:
            x = x - speed
        else:
            p=1
    if p==1 and west(x,y,running,1) and somWtobankS1left(running):
        y = 110
        p=2
    if p==2 and west(x,y,running,1):
        if x != 230:
            x = x - speed
        else:
            p=3
    if p==3 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        p = 4
        a = -180
    if p==4 and west(x,y,running,-1):
        if x != 160 or a != -90:
            if x != 160:
                x = x - speed
            if a != -90:
                a = a + 5
        else:
            p = 5
    if p == 5 and south(x,y,running,-1) and WestLeftSouth(x,y,running):
        y = y + speed
        p = 6
    if p==6 and south(x,y,running,3):
        if y != 170:
            y = y + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def somW_bankN(x,y,a,p,running,c,speed):
    if p==0 and west(x,y,running,1):
        if x != 230:
            x = x - speed
        else:
            p=1
    if p==1 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        a = 180
        p = 2
    if p==2 and west(x,y,running,-1):
        if x != 185 and a != -270:
            if x != 185:
                x = x - speed
            if a != 90:
                a = a - 5
        else:
            a = 90
            p = 3
    if p==3 and north(x,y,running,-1):
        if y != 0:
            y = y - speed
        else:
            p = 4
    if p==4:
        if y != -100:
            y = y - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def somW_somW1(x,y,a,p,running,c,speed):
    if p==0 and west(x,y,running,1):
        if x != 230:
            x = x - speed
        else:
            p=1
    if p==1 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        p = 2
    if p==2:
        if x >= 0 and west(x,y,running,-1):
            x = x - speed
        else:
            p = 3
    if p==3:
        if x >= -100:
            x = x - speed
        else:
            p = -1
    return [x,y,a,p]

def bankN_bankN1(x,y,a,p,running,c,speed):
    if p==0 and north(x,y,running,1):
        if y != 170:
            y = y - speed
        else:
            p=1
    if p == 1  and north(x,y,running,-1) and Lights(c):
        y = y - speed
        p = 2
    if p==2 and north(x,y,running,-1):
        if y != 0:
            y = y - speed
        else:
            p = 3
    if p==3:
        if y != -100:
            y = y - speed
        else:
            p = -1
    return [x,y,a,p]

def bankN_somE(x,y,a,p,running,c,speed):
    if p==0  and north(x,y,running,1):
        if y != 170:
            y = y - speed
        else:
            p=1
    if p==1  and north(x,y,running,-1) and Lights(c):
        y = y - speed
        p = 2
    if p==2  and north(x,y,running,-1):
        if y != 120 or a != 0:
            if y != 120:
                y = y - speed
            if a != 0:
                a = a - 5
        else:
            p=3
    if p==3 and east(x,y,running,2):
        if x != 385:
            x = x + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def bankN_somW(x,y,a,p,running,c,speed):
    if p==0 and north(x,y,running,1):
        if y != 170:
            y = y - speed
        else:
            p=1
    if p==1 and north(x,y,running,-1) and Lights(c):
        y = y - speed
        p = 2
    if p==2 and north(x,y,running,-1):
        if y != 105 or a != 180:
            if y != 105:
                y = y - speed
            if a != 180:
                a = a + 5
        else:
            p = 3
    if p==3 and west(x,y,running,-1) and NorthLeftWest(x,y,running):
        x = x - speed
        p = 4
    if p==4:
        if x != -100:
            x = x - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]


# Intersection 2
def conS_somE(x,y,a,p,running,c,speed):
    if p == 0 and south(x,y,running,2):
        if y == 20 and x != 968:
            x = 968
        if y != 55:
            y = y + speed
        else:
            p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,-1):
        if y != 125 or a != 0:
            if y != 125:
                y = y + speed
            if a != 0:
                a = a + 5
        else:
            p = 3
    if p == 3 and east(x,y,running,-1) and SouthLeftEast(x,y,running):
        x = x + speed
        p = 4
    if p == 4 and east(x,y,running,-1):
        if x != 1200:
            x = x + speed
        else:
            p = 5
    if p == 5:
        if x < 1300:
            x = x + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def conS_somW(x,y,a,p,running,c,speed):
    if p == 0 and south(x,y,running,2):
        if y != 55:
            y = y + speed
        else:
            p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,-1):
        if y != 95 or a != -180:
            if y != 95:
                y = y + speed
            if a != -180:
                a = a - 5
        else:
            a = 180
            p = 3
    if p == 3 and west(x,y,running,1):
        if x != 845:
            x = x - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def conS_conS2(x,y,a,p,running,c,speed):
    if p == 0 and south(x,y,running,2):
        if y != 55:
            y = y + speed
        else:
            p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,4):
        if y != 170:
            y = y + speed
        else:
            p = -1
    return [x,y,a,p]

def somW_conS(x,y,a,p,running,c,speed):
    if p == 0 and west(x,y,running,2):
        if x != 1035:
            x = x - speed
        else:
            a = -180
            p = 1
    if p==1 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        p = 2
    if p == 2 and west(x,y,running,-1):
        if x != 975 or a != -90:
            if x != 975:
                x = x - speed
            if a != -90:
                a = a + 5
        else:
            p = 3
    if p == 3 and south(x,y,running,-1) and WestLeftSouth(x,y,running):
        y = y + speed
        p = 4
    if p == 4 and south(x,y,running,4):
        if y != 170:
            y = y + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def somW_somW2(x,y,a,p,running,c,speed):
    if p == 0 and west(x,y,running,2):
        if x != 1035:
            x = x - speed
        else:
            p = 1
    if p==1 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        p = 2
    if p == 2 and west(x,y,running,1):
        if y != 95:
            y = 95
        if x != 845:
            x = x - speed
        else:
            p = -1
    return [x,y,a,p]

def somE_conS(x,y,a,p,running,c,speed):
    if p == 0 and east(x,y,running,2):
        if x != 405:
            x = x + speed
        else:
            p = 1
    if p == 1 and east(x,y,running,2) and somEclump2(x,y,running):
        if x != 435:
            x = x + speed
        else:
            p = 2
    if p == 2 and east(x,y,running,2) and somEclump2(x,y,running):
            y = y - 5
            x = x + speed
            p = 3
    if p == 3 and east(x,y,running,2):
        if x != 710:
            x = x + speed
        else:
            p = 4
    if p == 4 and east(x,y,running,2) and somEclump1(x,y,running):
        if x != 735:
            x = x + speed
        else:
            p = 5
    if p == 5 and east(x,y,running,2) and somEclump1(x,y,running):
        y = y + 5
        x = x + 5
        p = 6
    if p == 6 and east(x,y,running,2):
        if x != 910:
            x = x + speed
        else:
            p = 7
    if p==7 and east(x,y,running,-1) and not Lights(c):
        x = x + speed
        p = 8
    if p == 8 and east(x,y,running,-1):
        if x != 955 or a != -90:
            if x != 955:
                x = x + speed
            if a != -90:
                a = a - 5
        else:
            p = 9
    if p == 9 and south(x,y,running,4):
        if y != 185:
            y = y + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def somE_somE2(x,y,a,p,running,c,speed):
    if p == 0 and east(x,y,running,2):
        if x != 405:
            x = x + speed
        else:
            p = 1
    if p == 1 and east(x,y,running,2) and somEclump2(x,y,running):
        if x != 435:
            x = x + speed
        else:
            p = 2
    if p == 2 and east(x,y,running,2) and somEclump2(x,y,running):
            y = y - 5
            x = x + speed
            p = 3
    if p == 3 and east(x,y,running,2):
        if x != 710:
            x = x + speed
        else:
            p = 4
    if p == 4 and east(x,y,running,2) and somEclump1(x,y,running):
        if x != 735:
            x = x + speed
        else:
            p = 5
    if p == 5 and east(x,y,running,2) and somEclump1(x,y,running):
        y = y + 5
        x = x + 5
        p = 6
    if p == 6 and east(x,y,running,2):
        if x != 910:
            x = x + speed
        else:
            p = 7
    if p==7 and east(x,y,running,-1) and not Lights(c):
        x = x + speed
        p = 8
    if p==8 and east(x,y,running,-1):
        if x != 1200:
            x = x + speed
        else:
            p = 9
    if p==9:
        if x < 1300:
            x = x + speed
        else:
            p = -1
    return [x,y,a,p]

# Intersection 3
def bankN_bankN3(x,y,a,p,running,c,speed):
    if p==0 and north(x,y,running,3):
        if y != 535:
            y = y - speed
        else:
            p=1
    if p==1 and north(x,y,running,-1) and Lights(c):
        y = y - speed
        p = 2
    if p==2 and north(x,y,running,1):
        if y != 390:
            y = y - speed
        else:
            p = -1
    return [x,y,a,p]

def bankN_macW(x,y,a,p,running,c,speed):
    if p==0 and north(x,y,running,3):
        if y != 535:
            y = y - speed
        else:
            p=1
    if p==1 and north(x,y,running,-1) and Lights(c):
        y = y - speed
        p = 2
    if p==2 and north(x,y,running,-1):
        if y != 480 or a != 180:
            if y != 480:
                y = y - speed
            if a != 180:
                a = a + 5
        else:
            p = 3
    if p == 3 and west(x,y,running,-1) and NorthLeftWest(x,y,running):
        x = x - speed
        p = 4
    if p==4 and west(x,y,running,-1):
        if x != 0:
            x = x - speed
        else:
            p = 5
    if p==5:
        if x != -100:
            x = x - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def bankS_bankS3(x,y,a,p,running,c,speed):
    if p == 0 and south(x,y,running,3):
        if y != 430:
            y = y + speed
        else:
            p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,5):
        if y != 545:
            y = y + speed
        else:
            p = -1
    return [x,y,a,p]

def bankS_macW(x,y,a,p,running,c,speed):
    if p == 0 and south(x,y,running,3):
        if y != 430:
            y = y + speed
        else:
            p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,-1):
        if y != 490 or a != -180:
            if y != 490:
                y = y + speed
            if a != -180:
                a = a -5
        else:
            a = 180
            p = 3
    if p==3 and west(x,y,running,-1):
        if x != 0:
            x = x - speed
        else:
            p = 4
    if p==4:
        if x != -100:
            x = x - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def macW_bankN(x,y,a,p,running,c,speed):
    if p == 0 and west(x,y,running,3):
        if x != 230:
            x = x - speed
        else:
            p = 1
    if p==1 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        p = 2
    if p == 2 and west(x,y,running,-1):
        if x != 180 or a != 90:
            if x != 180:
                x = x - speed
            if a != 90:
                a = a - 5
        else:
            p = 3
    if p==3 and north(x,y,running,1):
        if y != 390:
            y = y - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def macW_bankS(x,y,a,p,running,c,speed):
    if p == 0 and west(x,y,running,3):
        if x != 230:
            x = x - speed
        else:
            p = 1
            a = -180
    if p==1 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        p = 2
    if p == 2 and west(x,y,running,-1):
        if x != 160 or a != -90:
            if x != 160:
                x = x - speed
            if a != -90:
                a = a + 5
        else:
            p = 3
    if p == 3 and south(x,y,running,-1) and WestLeftSouth(x,y,running):
        y = y + speed
        p = 4
    if p==4 and south(x,y,running,5):
        if y != 545:
            y = y + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def macW_macW3(x,y,a,p,running,c,speed):
    if p == 0 and west(x,y,running,3):
        if x != 230:
            x = x - speed
        else:
            p = 1
    if p==1 and west(x,y,running,-1) and not Lights(c):
        x = x - speed
        p = 2
    if p==2 and west(x,y,running,-1):
        if x != 0:
            x = x - speed
        else:
            p = 3
    if p==3:
        if x != -100:
            x = x - speed
        else:
            p = -1
    return [x,y,a,p]

# Intersection 4
# def macWtoconSclump(check):
#     for j in range(len(check)):
#         if check[j][0] == 1065 and check[j][1] ==  465:
#             return False
#     return True
def macW_conS(x,y,a,p,running,speed):
    if p == 0 and west(x,y,running,4):
        if x != 1100:
            x = x - speed
        else:
            a = -180
            p = 1
    if p == 1 and west(x,y,running,-1) and macWtoconSturn(x,y,running):
            y = 490
            p = 2
    if p == 2 and west(x,y,running,-1):
        if x != 1030:
            x = x - speed
        else:
            p = 3
    if p == 3 and west(x,y,running,-1):
        if x != 975 or a != -90:
            if x != 975:
                x = x - speed
            if a != -90:
                a = a + 5
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def macW_macW4(x,y,a,p,running,speed):
    if p == 0 and west(x,y,running,4):
        if x != 1085:
            x = x - speed
        else:
            p = 1
    if p == 1 and west(x,y,running,4) and macWclump1(running):
        if x != 1070:
            x = x - speed
        else:
            p = 2
    if p == 2 and west(x,y,running,4) and macWclump1(running):
        x = x - 5
        y = 465
        p = 3
    if p == 3 and west(x,y,running,4):
        if x != 1030:
            x = x - speed
        else:
            p = 4
    if p == 4 and west(x,y,running,4) and macWtomacW4straight(x,y,running):
        x = x - speed
        p = 5
    if p == 5 and west(x,y,running,3):
        if x == 915 and y != 480:
            y = 480
        if x != 880:
            x = x - speed
        else:
            p = -1
    return [x,y,a,p]

def conS_conS4(x,y,a,p,running,speed):
    if p == 0 and south(x,y,running,4):
        if y != 430:
            y = y + speed
        else:
            p = 1
    if p == 1 and south(x,y,running,6):
        if y == 535 and x == 955:
            x = 975
        if y != 660:
            y = y + speed
        else:
            p = -1
    return [x,y,a,p]

def conS_macW(x,y,a,p,running,speed):
    if p == 0 and south(x,y,running,4):
        if y == 395 and x != 955:
            x = 955
        if y != 430:
            y = y + speed
        else:
            p = 1
    if p == 1 and south(x,y,running,4):
        if y != 470 or a != -180:
            if y != 470:
                y = y + speed
            if a != -180:
                a = a - 5
        else:
            p = 2
    if p == 2 and west(x,y,running,4):
        if x != 910:
            x = x - speed
        else:
            p = 3
    if p == 3 and conStomacWturn(running):
        x = 915
        y = 480
        p = 4
    if p == 4 and west(x,y,running,3):
        if x != 880:
            x = x - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]


# Intersection 5
def gilE_bankN(x,y,a,p,running,c,speed):
    if p == 0 and east(x,y,running,5):
        if x != 120:
            x = x + speed
        else:
            p = 1
    if p==1 and east(x,y,running,-1) and not Lights(c):
        x = x + speed
        p = 2
    if p==2 and east(x,y,running,-1):
        if x != 180 or a != 90:
            if x != 180:
                x = x + speed
            if a != 90:
                a = a + 5
        else:
            p = 3
    if p==3 and north(x,y,running,3):
        if y != 775:
            y = y - speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def gilE_gilE5(x,y,a,p,running,c,speed):
    if p == 0 and east(x,y,running,5):
        if x != 120:
            x = x + speed
        else:
            p = 1
    if p==1 and east(x,y,running,-1) and not Lights(c):
        x = x + speed
        p = 2
    if p == 2 and east(x,y,running,6):
        if x != 265:
            x = x + speed
        else:
            p = -1
    return [x,y,a,p]

def bankS_gilE(x,y,a,p,running,c,speed):
    if p == 0 and south(x,y,running,5):
        if y != 800:
            y = y + speed
        else:
            p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,-1):
        if y != 845 or a != 0:
            if y != 845:
                y = y + speed
            if a != 0:
                a = a + 5
        else:
            p = 3
    if p == 3 and east(x,y,running,6):
        if x != 265:
            x = x + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]


# Intersection 6
def conS_gilE(x,y,a,p,running,c,speed):
    if p == 0 and south(x,y,running,5):
        if x != 975 and y ==770:
            x = 975
        if y != 795:
            y = y + speed
        else:
            p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,-1):
        if y != 845 or a != 0:
            if y != 845:
                y = y + speed
            if a != 0:
                a = a + 5
        else:
            p = 3
    if p == 3 and east(x,y,running,-1):
        if x != 1200:
            x = x + speed
        else:
            p = 4
    if p == 4:
        if x < 1300:
            x = x + speed
        else:
            global turnsMade
            turnsMade += 1
            p = -1
    return [x,y,a,p]

def gilE_gilE6(x,y,a,p,running,c,speed):
    if p == 0 and east(x,y,running,6):
        if x != 920:
            x = x + speed
        else:
            p = 1
    if p==1 and east(x,y,running,-1) and not Lights(c):
        x = x + speed
        p = 2
    if p == 2 and east(x,y,running,-1):
        if x != 1200:
            x = x + speed
        else:
            p = 3
    if p == 3:
        if x < 1300:
            x = x + speed
        else:
            p = -1
    return [x,y,a,p]

def wrap_around(x,y,a,p,running,c,speed):
    if p == 0 and east(x,y,running,-1):
        if x != 960 or a != -90:
            if x != 960:
                x = x + speed
            if a != -90 and x >= 920:
                a =  a - 5
        else:
            if y == 845:
                p = 2
            else:
                p = 1
    if p==1 and south(x,y,running,-1) and Lights(c):
        y = y + speed
        p = 2
    if p == 2 and south(x,y,running,-1):
        if y != 900:
            y = y + speed
        else:
            a = 90
            p = 3
    if p == 3 and west(x,y,running,-1):
        if x != 180:
            x = x - 5
        else:
            p = 4
    if p==4 and north(x,y,running,-1) and Lights(c):
        y = y - speed
        p = 5
    if p == 5 and north(x,y,running,-1):
        if y != 775:
            y = y - speed
        else:
            p = -1
    return [x,y,a,p]



# stall example: [[413, 128, 0, 1, 'f']]
# lot example: [[975, 671, 'q'], [1184, 805, -90, 1]]

def parking(sprite,running,park,speed):
    x = sprite[0]
    y = sprite[1]
    a = sprite[2]
    p = sprite[3]
    l = sprite[4]
    if len(park) == 2:
        if park[0][2] == 'a':
            sprite = lota(x,y,a,p,l,running,park,speed)
        elif park[0][2] == 'f':
            sprite = lotf(x,y,a,p,l,running,park,speed)
        elif park[0][2] == 'h':
            sprite = loth(x,y,a,p,l,running,park,speed)
        elif park[0][2] == 'k':
            sprite = lotk(x,y,a,p,l,running,park,speed)
        elif park[0][2] == 'p':
            sprite = lotp(x,y,a,p,l,running,park,speed)
        elif park[0][2] == 'q':
            sprite = lotq(x,y,a,p,l,running,park,speed)
    else:
        if park[0][4] == 'h' or park[0][4] == 'r':
            sprite = stallsWest(x,y,a,p,l,running,park,speed)
        else:
            sprite = stallsEast(x,y,a,p,l,running,park,speed)
    return sprite

def lota(x,y,a,p,l,running,park,speed):
    if p == 0:
        if a != 90:
            a = a - 5
        else:
            p = 1
    if p == 1 and north(x,y,running,1):
        if y != 70:
            y = y - speed
        else:
            p = 2
    if p == 2:
        x = park[1][0]
        y = park[1][1]
        a = park[1][2]
        p = -1
    return [x,y,a,p,l]

def lotf(x,y,a,p,l,running,park,speed):
    if p == 0 and east(x,y,running,2):
        if x == 435:
            y = y - 5
        if x == 735:
            y = y + 5
        if x != 810:
            x = x + speed
        else:
            p = 1
    if p == 1:
        if a != -90:
            a = a - 90
        else:
            p = 2
    if p == 2 and park[1][0] == 786:
        if y < park[1][1]:
            y = y + speed
        else:
            p = 5
    if p == 2 and park[1][0] != 786:
        if y != 265:
            y = y + speed
        else:
            p = 3
    if p == 3:
        if a != 0:
            a = a + 5
        else:
            p = 4
    if p == 4 and east(x,y,running,-1):
        if x < park[1][0]:
            x = x + speed
        else:
            p = 5
    if p == 5:
        x = park[1][0]
        y = park[1][1]
        a = park[1][2]
        p = -1
    return [x,y,a,p,l]

def loth(x,y,a,p,l,running,park,speed):
    if p == 0 and west(x,y,running,3):
        if x > park[0][0]:
            x = x - speed
        else:
            a = -180
            p = 1
    if p == 1 and park[0][1] > 485:
        if a != -90:
            a = a + 5
        else:
            p = 2
    if p == 1 and park[0][1] < 485:
        if a != -270:
            a = a - 5
        else:
            p = 2
    if p == 2 and park[1][1] > 485 and south(x,y,running,-1):
        if y < park[1][1]:
            y = y + speed
        else:
            p = 3
    if p == 2 and park[1][1] < 485 and north(x,y,running,-1):
        if y > park[1][1]:
            y = y - speed
        else:
            p = 3
    if p == 3:
        temp = [x,y,a,p,l,park]
        x = park[1][0]
        y = park[1][1]
        a = park[1][2]
        p = -1
    return [x,y,a,p,l]

def lotk(x,y,a,p,l,running,park,speed):
    if p == 0 and south(x,y,running,4):
        if y < park[0][1]:
            y = y + speed
        else:
            p = 1
    if p == 1:
        if a != -180:
            a = a - 5
        else:
            p = 2
    if p == 2 and west(x,y,running,-1):
        if x > park[1][0]:
            x = x - speed
        else:
            p = 3
    if p == 3:
        x = park[1][0]
        y = park[1][1]
        a = park[1][2]
        p = -1
    return [x,y,a,p,l]

def lotp(x,y,a,p,l,running,park,speed):
    if p == 0 and east(x,y,running,6):
        if x < park[0][0]:
            x = x + speed
        else:
            p = 1
    if p == 1 :
        if a != 90:
            a = a + 5
        else:
            p = 2
    if p == 2 and north(x,y,running,-1):
        if y > park[1][1]:
            y = y - speed
        else:
            p = 3
    if p == 3:
        x = park[1][0]
        y = park[1][1]
        a = park[1][2]
        p = -1
    return [x,y,a,p,l]

def lotq(x,y,a,p,l,running,park,speed):
    if p == 0 and south(x,y,running,6):
        if y < park[0][1]:
            y = y + speed
        else:
            p = 1
    if p == 1 :
        if a != 0:
            a = a + 5
        else:
            p = 2
    if p == 2 and east(x,y,running,-1):
        if x < park[1][0]:
            x = x + speed
        else:
            p = 3
    if p == 3:
        x = park[1][0]
        y = park[1][1]
        a = park[1][2]
        p = -1
    return [x,y,a,p,l]

def stallsEast(x,y,a,p,l,running,park,speed):
    if p == 0 and east(x,y,running,-1):
        if x < park[0][0]:
            x = x + speed
        else:
            p = 1
    if p == 1:
        x = park[0][0]
        y = park[0][1]
        a = park[0][2]
        p = -1
    return [x,y,a,p,l]

def stallsWest(x,y,a,p,l,running,park,speed):
    if p == 0 and west(x,y,running,-1):
        if x > park[0][0]:
            x = x - speed
        else:
            p = 1
    if p == 1:
        x = park[0][0]
        y = park[0][1]
        a = park[0][2]
        p = -1
    return [x,y,a,p,l]


def results():
    print("The total turns made by all cars: " + str(turnsMade))
    print("Average number of turns per car: " + str(turnsMade/440))
    print("Intersection braking: "+str(intersectionBrakes))
