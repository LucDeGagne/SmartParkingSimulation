for i in range(3):
    infile = open("design.txt","r")
    name1 = str(i+1)
    content1 = ""
    line = infile.readline()
    for j in range(i):
        line = infile.readline()
    content1 += line
    infile.close()
    for i in range(4):
        content2 = ""
        infile = open("design.txt","r")
        line = infile.readline()
        for j in range(i+3):
            line = infile.readline()
        content2 += line
        infile.close()
        if(i == 0):
            name2 = "-even-"
        else:
            name2 = "-"+str(i)+"-"
        for i in range(7):
            content3 = ""
            infile = open("design.txt","r")
            for j in range(7):
                infile.readline()
            line1 = infile.readline()
            line2 = infile.readline()
            for j in range(i):
                line1 = infile.readline()
                line2 = infile.readline()
            content3 += line1 + line2
            infile.close()
            if(i == 0):
                name3 = "even"
            else:
                name3 = str(i)
            infile.close()
            outfile = open(name1+name2+name3+".txt","w+")
            outfile.write(content1+content2+content3)
            outfile.close()
