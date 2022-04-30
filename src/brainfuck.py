def brainfuck(code):
	array, pointer, i = [0], 0, 0
	bmap = bracemap(code)
	length = len(code)

	while pointer < length:
		cmd = code[pointer]

		if cmd == ">":
			i += 1

			if i == len(array):
				array.append(0)

		elif cmd == "<":
			i = 0 if i <= 0 else i - 1

		elif cmd == "+":
			array[i] = array[i] + 1 if array[i] < 255 else 0

		elif cmd == "-":
			array[i] = array[i] - 1 if array[i] > 0 else 255

		elif cmd == "[" and array[i] == 0:
			pointer = bmap[pointer]

		elif cmd == "]" and array[i] != 0:
			pointer = bmap[pointer]

		elif cmd == ".":
			print(chr(array[i]), end='')

		elif cmd == ",":
			array[i] = ord(input())

		pointer += 1

def bracemap(code):
	stack, bracemap = [], {}

	for pos, cmd in enumerate(code):
		if cmd == '[':
			stack.append(pos)

		if cmd == ']':
			if len(stack) > 0:
				bracemap[start := stack.pop()] = pos
				bracemap[pos] = start
			else:
				raise Exception('Error! Missing [')

	if len(stack) > 0:
		raise Exception('Error! Missing ]')

	return bracemap
