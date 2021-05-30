import random as R

def generateRules():

    nani = []
    sub = []

    for i in range(16 * 6):
        if i % 16 == 0 and i != 0:
            nani.append(sub)
            sub = []    
        sub.append(i % 16)

    for i in nani:
        R.shuffle(i)

    print(nani)

    for j in enumerate(nani):
        for i in j[1]:
            if j[0] == 0:
                print("if c.R == " + str(i))
            if j[0] == 1:
                print("if c.G == " + str(i))
            if j[0] == 2:
                print("if c.B == " + str(i))

            if j[0] == 3:
                print("c.R = " + str(i))
            if j[0] == 4:
                print("c.G = " + str(i))
            if j[0] == 5:
                print("c.G = " + str(i))

generateRules()
