numberOfRules = 1
ruleRange = 5
#rules sit on target
#every rule on every target is triggered every epoch

class Ruler:
    dead = rule(0)
    #you can combine previous rules
    
    idle = rule(1)
    up = rule(2)
    down1right3 = rule(3)
    attack = rule(4)

    revieve = rule(3
    #you can add rules, but two many rules are costly, so only add the neccesery ones.
    #when all rules on one side reach 0 that person loses.
    #there could be biomes or epoches with enviormental or cronological rules.

def rule(i, target):
    if i == 0:
        continue
    if i == 1:
        if target == 2:
            target = i
        if target == 3:
            target = i
            i = i - 1
    if i == 2:
        target
