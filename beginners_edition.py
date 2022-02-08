from random import randint

# global restrictions
range_step = 32
bf_vocabulary = "+-><{}!?"


def bf_compile(rule):
	bf_code_to_return = ""
	for sym in rule:
		if sym not in bf_vocabulary:
			continue
		bf_code_to_return += sym
	return bf_code_to_return


# assign 50 steps to your buffer
pl_buf = []
op_buf = []

pl_rules = []
op_rules = []

pl_pointer = 0
op_pointer = 0

pl_low_range = 0
pl_high_range = 31
op_low_range = 0
op_high_range = 31

def load_rule(the_range_of_the_byte_value):
	return the_range_of_the_byte_value >> 5


# a text to code function
def bf_interperator(picked_rule, pl_buf, op_buf, pl_pointer, op_pointer, pl_low_range, pl_high_range, step_cap):

	steps_taken = 0
	scope_stack = []

	# where in the bf code the main-thread is executing (code line:char)
	script_pointer = 0
	rule = bf_compile(pl_rules[load_rule(pl_buf[picked_rule])])

	while (script_pointer < len(rule)):

		steps_taken += 1

		if rule[script_pointer] == "+":
			if pl_buf[pl_pointer] < 255:
				pl_buf[pl_pointer] += 1

		if rule[script_pointer] == "-":
			if pl_buf[pl_pointer] > 0:
				pl_buf[pl_pointer] -= 1

		if rule[script_pointer] == ">":
			if pl_pointer < 7:
				pl_pointer += 1

		if rule[script_pointer] == "<":
			if pl_pointer > 0:
				pl_pointer -= 1

		if rule[script_pointer] == "!":
			op_buf[op_pointer] = pl_buf[pl_pointer]

		if rule[script_pointer] == "?":
			pl_buf[pl_pointer] = op_buf[op_pointer]

		if rule[script_pointer] == "{":
			scope_stack.append(script_pointer)

		if rule[script_pointer] == "}" and pl_low_range <= pl_buf[pl_pointer] < pl_high_range:
			script_pointer = scope_stack.pop()

		elif pl_low_range > pl_buf[pl_pointer]:
			pl_low_range -= 32
			pl_high_range -= 32
		elif pl_high_range < pl_buf[pl_pointer]:
			pl_low_range += 32
			pl_high_range += 32

		script_pointer += 1

	# check for Error
	if scope_stack:
		raise "Syntax Error: expected '}', got " + rule[script_pointer]
	
	if steps_taken >= step_cap:
		return step_cap
	return steps_taken


# start a game
# both player setup initial arrangment
# shuffle half of the rules at random
# flip a coin of who starts


def set_player_buffer(buf):
	buf.clear()
	remaning = 250
	for b in range(8):
		print("byte "+str(b+1)+"/8")
		while True:
			if remaning <= 0:
				buf.append(0)
				break
			else:
				stream = input(
					"assign rule key value (" + str(remaning) + " value(s) remaning): ")

			if stream == "":
				buf.append(0)
				break
			attempt = int(stream)

			if attempt <= remaning:
				buf.append(attempt)
				remaning -= attempt
				break
			else:
				print("Error: use a integer less than " +
					  str(remaning + 1) + ".")


def setup_rules_for_ranges(rules):
	symbols_used = 0
	print("Vocabulary:", bf_vocabulary)
	for rule in range(6):
		stream = input("Write rule for keys in range " + str((rule + 1)
					   * range_step) + "-" + str((rule + 2) * range_step - 1) + ": ")
		symbols_used += len(stream)
		rules.append(stream)
	#print("symbols_used", symbols_used)


# mix 3 random rules between players
def mix_rules(pl_rules, op_rules):
	
	rule_pick = [0, 1, 2, 3, 4, 5]
	for _ in range(3):

		pick = randint(0, len(rule_pick) - 1)

		temp = pl_rules[rule_pick[pick]]
		pl_rules[rule_pick[pick]] = op_rules[rule_pick[pick]]
		op_rules[rule_pick[pick]] = temp

		rule_pick.pop(pick)


def ready(pl_buf, op_buf, pl_rules, op_rules):

	return\
	len(pl_buf) == 8 and\
	len(op_buf) == 8 and\
	len(pl_rules) == 6 and\
	len(op_rules) == 6


def print_player_buffer(buf):
	for s in buf:
		print(s, end="\t")


def turn(pl_buf, op_buf, pl_pointer, op_pointer, pl_low_range, pl_high_range):

	pl_steps_remaining = sum(pl_buf)
	
	while pl_steps_remaining > 0:

		print_player_buffer(op_buf)
		print()
		print_player_buffer(pl_buf)
		print()
		
		stream = input("pick a buffer index that matches the rule you want to execute (" + str(pl_steps_remaining) + " steps remaning): ")
		if stream == '':
			print("'Enter' entered, ending turn...")
			break
		
		pl_steps_remaining -= bf_interperator(int(stream), pl_buf, op_buf, pl_pointer, op_pointer, pl_low_range, pl_high_range, pl_steps_remaining)


def game(pl_buf, op_buf, pl_pointer, op_pointer):
	if not ready(pl_buf, op_buf, pl_rules, op_rules):
		print("--set_rules and --set_buffer values before playing")
		return
	turns = 0

	pl_win = max(op_buf) < 32 and min(pl_buf) > 223
	op_win = max(pl_buf) < 32 and min(op_buf) > 223
	
	while (True):
		if turns % 2 == 0:
			# prints available rules
			for rule in range(6):
				print(str((rule + 1) * range_step) + "-" + str((rule + 2) * range_step - 1) + ": " + str(pl_rules[rule]))

			turn(pl_buf, op_buf, pl_pointer, op_pointer, pl_low_range, pl_high_range)

			if (pl_win):
				print("player win!")
				break
		else:
			# prints available rules
			for rule in range(6):
				print(str((rule + 1) * range_step) + "-" + str((rule + 2) * range_step - 1) + ": " + str(op_rules[rule]))

			turn(op_buf, pl_buf, op_pointer, pl_pointer, op_low_range, op_high_range)

			if (op_win):
				print("opponent win!")
				break
		turns += 1

def show_help():
	print(
""" 
-h, --help	display this text
--set_rules	each player sets 6
		rules between key
		values of 32-223
--set_buffer	each player
		distributes 50
		key values among
		8 bytes within
		their buffer."""
	)

if __name__ == "__main__":
	while True:
		
		# main prompt
		stream = input('> ')
	
		# help prompt
		if stream in ("-h", "--help"):
			show_help()
		
		# set rules prompt
		elif stream == "--set_rules":

			print("0: pl_rules:", "set" if len(pl_rules) else "not set")
			print("1: op_rules:", "set" if len(op_rules) else "not set")
			print("2: back")

			stream = input("which player (0-2): ")
			
			if stream == "0":
				setup_rules_for_ranges(pl_rules)
			elif stream == "1":
				setup_rules_for_ranges(op_rules)
			else:
				continue
		
		# set buffer values prompt
		elif stream == "--set_buffer":

			print("0: pl_buffer:", "set" if len(pl_buf) == 8 else "not set")
			print("1: op_buffer:", "set" if len(op_buf) == 8 else "not set")
			print("2: back")

			stream = input("which player(0-2): ")

			if stream == "0":
				set_player_buffer(pl_buf)
			if stream == "1":
				set_player_buffer(op_buf)
			else:
				continue


		# start game prompt
		elif stream in ("-s", "--start"):
			
			print("0: pl")
			print("1: op")
			print("2: back")
			
			stream = input("which player goes first: (0-2): ")
			
			if stream == "0":
				game(pl_buf, op_buf, pl_pointer, op_pointer)
			elif stream == "1":
				game(op_buf, pl_buf, op_pointer, pl_pointer)
			else:
				continue
		
		elif stream in ("-q", "--quit"):
			break

		# exception prompt	
		else:
			print("-h or --help for help")
