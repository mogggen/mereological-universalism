from random import randint, choice
bfVocabulary = "+-><"#[].,"

mapSize = 8
distance = 5  # less than map size

actorMap = {}


def generate_script_slots(dist):
	ss = {}
	length = (0 + dist) * dist // 2
	for script in range(0, length):  # get each individual length key to distance
		ss[script] = ""
		for command in range(script):
			ss[command] += choice(bfVocabulary)
	print(F"Generated {dist} scripts with a total of {length} commands")
	return ss


# populate slots with brainFuck script
pass


script_slots = generate_script_slots(dist=distance)


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
def bf_interperator(bf_script_with_comments, Max_Iterator=2**64):
	commandsForever = 0
	ACTOR_VARIABLE = "Holy grail"
	
	scopeStack = []
	
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
			raise F"Runtime Error: number of consecutive commands of {commandsForever}, scope-depth: {len(scopeStack)}"
	
	# check for Error
	if scopeStack: raise F"Syntax Error: expected ']', got {actor_pointer}"
	

generation = 0


# run game
def step_simulation():
	global generation
	print("step simulation:", generation, end="")
	generation += 1
	# prepare to transition to the next generation of the ActorMap
	previous_actorMap = actorMap
	for _ in previous_actorMap:
		bf_compile(script_slots[previous_actorMap[_]])


# play game
def run_simulation():
	step_simulation()


def display_board(num_of_col):
	for i in actorMap:
		
		# formatting
		if i != 0:
			print(end='\t')
		if i % num_of_col == 0:
			print()
		elif i == 0:
			continue
		
		# print script holding of actor
		print(actorMap[i], end="", sep="\t")
	print()


# test run
while True:
	input()
	step_simulation()
	display_board(num_of_col=3)
