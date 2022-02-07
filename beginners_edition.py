from random import choice, randint

bfVocabulary = "+-><{}!?"


def bf_compile(rule):
    bfCodeToReturn = ""
    for sym in rule:
        if sym not in bfVocabulary:
            continue
        bfCodeToReturn += sym
    return bfCodeToReturn


# assign 50 steps to your buffer
plbuf = []
opbuf = []

plrule = []
oprule = []

plpointer = 0
oppointer = 0

pllowrange = 0
plhighrange = 31
oplowrange = 0
ophighrange = 31

# a text to code function
def bf_interperator(plbuf, opbuf, plpointer, oppointer, pllowrange, plhighrange, bf_script, stepCap=50):

	stepsTaken = 0
	scopeStack = []

    # where in the bf code the main-thread is executing (code line:char)
	script_pointer = 0
	rule = plrule[plbuf[plpointer]]

	while (script_pointer < len(rule)):

		stepsTaken += 1

		if rule[script_pointer] == "+":
			plbuf[plpointer] += 1

		if rule[script_pointer] == "-":
			plbuf[plpointer] -= 1

		if rule[script_pointer] == ">":
			plpointer += 1

		if rule[script_pointer] == "<":
			plpointer -= 1

		if rule[script_pointer] == "!":
			opbuf[oppointer] = plbuf[plpointer]

		if rule[script_pointer] == "?":
			plbuf[plpointer] = opbuf[oppointer]
		
		if rule[script_pointer] == "{":
			scopeStack.append(script_pointer)

		if rule[script_pointer] == "}" and pllowrange < plbuf[plpointer] < plhighrange:
			script_pointer = scopeStack.pop()
		
		elif pllowrange > plbuf[plpointer]:
			pllowrange -= 32
			plhighrange -= 32
		elif plhighrange < plbuf[plpointer]:
			pllowrange += 32
			plhighrange += 32
		
		script_pointer += 1

		if stepsTaken >= stepCap:
			return stepCap

	# check for Error
	if scopeStack:
		raise "Syntax Error: expected '}', got " + rule[script_pointer]

## start a game
# both player setup initial arrangment
# shuffle half of the rules at random
# flip a coin of who starts

def start(plbuf, opbuf, plrule, oprule):
	if sum(plbuf) != 50:
		return
	if sum(opbuf) != 50:
		return
	if len(plbuf) != 8 or len(opbuf) != 8:
		return
	
	# mix 4 random rules between players
	rulepick = [0, 1, 2, 3, 4, 5, 6, 7]
	for _ in range(4):
		pick = randint(0, len(rulepick) - 1)
		temp = plrule[rulepick[pick]]
		plrule[rulepick[pick]] = oprule[rulepick[pick]]
		oprule[rulepick[pick]] = temp

def game(plbuf, opbuf, plpointer, oppointer):
	plstepsremaning = sum(plbuf)
	bf_interperator(bf_compile(plrule[input()]))
