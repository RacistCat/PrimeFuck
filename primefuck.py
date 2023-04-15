# # # # # # # # #
# PrimeFuck     #
# # # # # # # # #

from sympy import prime
from collections import defaultdict
from sys import argv

def find_matching_braces(program):
	if program.count("[") != program.count("]"):
		raise Exception("unmatched bracket")
	matching_braces = {}
	stack = []
	for i in range(len(program)):
		if program[i] == "[":
			stack.append(i)
		elif program[i] == "]":
			try:
				x = stack.pop()
			except:
				raise Exception("unmatched bracket")
			matching_braces[i] = x
			matching_braces[x] = i
	return matching_braces
def interpreter(program):
	input_ = None
	input_ptr = 0
	matching_braces = find_matching_braces(program)
	instr_ptr = 0
	data_ptr = 0
	mem = defaultdict(int)
	while instr_ptr < len(program):
		instr = program[instr_ptr]
		if instr == "p":
			mem[data_ptr] = prime(mem[data_ptr] + 1)
		elif instr == "d":
			mem[data_ptr] //= 2
		elif instr == "^":
			data_ptr = prime(data_ptr + 1)
		elif instr == "v":
			data_ptr //= 2
		elif (instr == "[" and mem[data_ptr] == 0) or (instr == "]" and mem[data_ptr]  != 0):
			instr_ptr = matching_braces[instr_ptr]
		elif instr == ".":
			print(chr(mem[data_ptr]), end = '')
		elif instr == ",":
			if input_ == None or input_ptr >= len(input_):
				input_ = input(">> ")
				input_ptr = 0
			mem[data_ptr] = prime(ord(input_[input_ptr]))
		instr_ptr += 1
if __name__ == "__main__":
	f = open(argv[1], "r")
	interpreter(f.read())
	f.close()