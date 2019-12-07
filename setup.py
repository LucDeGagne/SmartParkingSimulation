def makeparams(filename):
    infile = open(filename,"r")

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
    values = line.split(",")
    speeds = []
    for i in range(len(values)):
        speeds.append(float(values[i]))

    line = infile.readline()
    values = line.split(",")
    choices = []
    for i in range(len(values)):
        choices.append(int(values[i]))

    line = infile.readline()
    values = line.split("'")
    destinationsThrough = []
    for i in range(len(values)):
        if i%2 == 1:
            destinationsThrough.append(values[i])

    infile.close()
    return [destinationsStay,speeds,choices,destinationsThrough]

def writeresults(log):
    outfile = open("smartspots.txt","a+")
    outfile.write(log)
    outfile.close()
