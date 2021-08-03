from random import randint, choice
bfVocabulary = "+-><[].,"

mapSize = 8

actorMap = {}


def generate_script_slots(distance):
	ss = {}
	length = (0 + distance) * distance // 2
	for script in range(length): # get each individual length key to distance
		ss[script] = ""
		for command in range(script):
			ss[command] += choice(bfVocabulary)
	print(ss)
	return ss


# populate slots with brainFuck script
pass


script_slots = generate_script_slots(distance=40)


# generate map slots
for i in range(mapSize):
	actorMap[i] = randint(0, len(script_slots))  # length of script to load

# write a bf compiler in python
def bf_compile(plain_text):
	bfCodeToReturn = ""
	for p in plain_text:
		if p not in bfVocabulary:
			continue
		bfCodeToReturn += p
	return bfCodeToReturn


# a text to code function
def bf_interperator(bf_script_with_comments, Max_Iterator=2048):
	commandsForever = 0
	ACTOR_VARIABLE = "Holy grail"
	
	scopeStackIndex = 0
	
	script_pointer = 0  # where in the bf code the main-thread is executing (code line:char)
	actor_pointer = 0  # where on the ActorMap the script is being executed on (buffer caret)
	
	while script_pointer < len(bf_script_with_comments):
		
		commandsForever += 1
		
		char = bf_script_with_comments[actor_pointer]
		if char == "+":
			ActorMap[actor_pointer] += 1
		
		if char == "-":
			ActorMap[actor_pointer] -= 1
		
		if char == ">":
			actor_pointer += 1
		
		if char == "<":
			actor_pointer -= 1
		
		if char == ".":
			ACTOR_VARIABLE = ActorMap[actor_pointer]
		
		if char == ",":
			ActorMap[actor_pointer] = ACTOR_VARIABLE
			
		if char == "[":
			scopeStack.append(script_pointer)
		
		if char == "]" and bf_script_with_comments[script_pointer]:
			actor_pointer = scopeStack.pop()
		script_pointer += 1
		
		if commandsForever >= Max_Iterator:
			raise F"Runtime Error: number of consecutive commands of {commandsForever}, may contain an infinite loop. scope-depth: {len(scopeStack)}"
		
	# check for Error
	if scopeStack: raise F"Syntax Error: expected ']', got {actor_pointer}"
	

generation = 0


# run game
def step_simulation():
	global generation
	generation += 1
	print(generation)
	
	# prepare to transition to the next generation of the ActorMap
	previous_actorMap = actorMap
	for _ in previous_actorMap:
		bf_compile(script_slots[previous_actorMap[_]])


step_simulation()


# play game
def run_simulation():
	step_simulation()
