# rules/counters 5
# canvas 4x4
# 4 rulers
import random

class ruler:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

some = []

for s in range(0, 1):
    some.append(ruler(s, random.randint(0, 4), random.randint(0, 4)))
    print(some[s].R, some[s].G, some[s].B)

def nextAction(current):
    actions = []
    for c in current:
        if c.G == 0:
            if c.R == 15:
                c.B = 2
            elif c.B == 4:
                c.R = c.G
        elif c.G == 1:
            c.R = 3
        elif c.G == 2:
            if c.B == 2:
                c.R = c.G
            elif c.R == 1:
                c.R = 0
            c.B = c.G
        elif c.G == 3:
            c.R = c.B
        elif c.G == 4:
            if c.R == 0:
                c.B = 3
            elif c.R == 2:
                c.G = 0

nextAction(some)

for i in range(10):
    for s in range(0, 1):
        print(some[s].R, some[s].G, some[s].B)
