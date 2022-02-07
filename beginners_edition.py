from random import randint


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

pl_rule = []
op_rule = []

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
	rule = bf_compile(pl_rule[load_rule(pl_buf[picked_rule])])

	while (script_pointer < len(rule)):

		steps_taken += 1

		if rule[script_pointer] == "+":
			pl_buf[pl_pointer] += 1

		if rule[script_pointer] == "-":
			pl_buf[pl_pointer] -= 1

		if rule[script_pointer] == ">":
			pl_pointer += 1

		if rule[script_pointer] == "<":
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


def setup_player_buffer(buf):
	remaning = 250
	for b in range(8):
		print("byte "+str(b+1)+"/8")
		while True:
			if remaning <= 0:
				buf.append(0)
				break
			else:
				stream = input(
					"assign rule key (" + str(remaning) + " remaning): ")

			if stream == "":
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
	range_step = 32
	print("Vocabulary:", bf_vocabulary)
	for rule in range(6):
		stream = input("Write rule for keys in range " + str((rule + 1)
					   * range_step) + "-" + str((rule + 2) * range_step - 1) + ": ")
		symbols_used += len(stream)
		rules.append(stream)
	#print("symbols_used", symbols_used)


def start(pl_buf, op_buf, pl_rule, op_rule):

	setup_player_buffer(pl_buf)
	setup_player_buffer(op_buf)

	setup_rules_for_ranges(pl_rule)
	setup_rules_for_ranges(op_rule)

	if sum(pl_buf) > 50:
		return
	if sum(op_buf) > 50:
		return
	if len(pl_buf) != 8 or len(op_buf) != 8:
		return

	# mix 4 random rules between players
	rule_pick = [0, 1, 2, 3, 4, 5]
	for _ in range(3):

		pick = randint(0, len(rule_pick) - 1)

		temp = pl_rule[rule_pick[pick]]
		pl_rule[rule_pick[pick]] = op_rule[rule_pick[pick]]
		op_rule[rule_pick[pick]] = temp

		rule_pick.pop(pick)


def turn(pl_buf, op_buf, pl_pointer, op_pointer, pl_low_range, pl_high_range):
	pl_steps_remaining = sum(pl_buf)
	while pl_steps_remaining > 0:
		print(pl_buf)
		pl_steps_remaining -= bf_interperator(int(input("pick a buffer index that matches the rule you want to execute (" + str(pl_steps_remaining) + " steps remaning): ")),
						pl_buf, op_buf, pl_pointer, op_pointer, pl_low_range, pl_high_range, pl_steps_remaining)



def print_player_buffer(buf):
	for s in buf:
		print(s, end="\t")


def game(pl_buf, op_buf, pl_pointer, op_pointer):
	start(pl_buf, op_buf, pl_rule, op_rule)
	turns = 0
	pl_win = max(op_buf) < 32 and min(pl_buf) > 223
	op_win = max(pl_buf) < 32 and min(op_buf) > 223
	while (True):
		if turns % 2 == 0:
			print(pl_rule)
			turn(pl_buf, op_buf, pl_pointer, op_pointer, pl_low_range, pl_high_range)
			if (pl_win):
				print("player win!")
				break
		else:
			print(op_rule)
			turn(op_buf, pl_buf, op_pointer, pl_pointer, op_low_range, op_high_range)
			if (op_win):
				print("opponent win!")
				break
		turns += 1


if __name__ == "__main__":

	# the start of the game
	game(pl_buf, op_buf, pl_pointer, op_pointer)
