from brainfuck import brainfuck
import argparse, sys

parser = argparse.ArgumentParser()
p = parser.add_mutually_exclusive_group()

p.add_argument('-f', '--file', help='evaluate a file')
p.add_argument('-s', '--string', help='evaluate a string')

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

if args.file:
	with open(args.file, 'r') as file:
		code = (file.read().replace('\n', '')).replace(' ', '')

	brainfuck(code)

elif args.string:
	brainfuck((args.string.replace('\n', '')).replace(' ', ''))
