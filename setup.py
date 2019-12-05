infile = open("t1.txt","r")

line = infile.readline()
values = line.split(',')
destinationsStay = []
for i in range(len(values)):
    tmp = []
    core = values[i].split(' ')
    tmp.append(int(core[0]))
    tmp.append(int(core[1]))
    destinationsStay.append(tmp)

line = infile.readline()
values = line.split("'")
destinationsThrough = []
for i in range(len(values)):
    if i%2 == 1:
        destinationsThrough.append(values[i])

line = infile.readline()
values = line.split(",")
choices = []
for i in range(len(values)):
    choices.append(int(values[i]))

line = infile.readline()
values = line.split(",")
speeds = []
for i in range(len(values)):
    speeds.append(float(values[i]))
