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
def bf_interperator(plbuf, opbuf, plpointer, oppointer, bf_script, stepCap=50):
    stepsTaken = 0
	scopeStack = []
	
	script_pointer = 0  # where in the bf code the main-thread is executing (code line:char)
	actor_pointer = 0  # where on the actorMap the script is being executed on (buffer caret)
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
		
		if rule[script_pointer] == "}" and pllowrange < plbuf[script_pointer] < plhighrange:
			actor_pointer = scopeStack.pop()
		elif pllowrange > plbuf[script_pointer]:
			pllowrange -= 32
			plhighrange -= 32
		elif plhighrange < plbuf[script_pointer]:
			pllowrange += 32
			plhighrange += 32
		script_pointer += 1
		
		if stepsTaken >= stepCap:
			break
	
	# check for Error
	if scopeStack: raise F"Syntax Error: expected ']', got {actor_pointer}"



