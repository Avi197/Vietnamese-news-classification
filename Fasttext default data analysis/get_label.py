
import re
import collections

cooking = '/home/pham/NLU/data/cooking.stackexchange.txt'
cooking_label = '/home/pham/NLU/data/cooking_label.txt'
cooking_label_uniq = '/home/pham/NLU/data/cooking_label_uniq.txt'
cooking_label_count = '/home/pham/NLU/data/cooking_label_count.txt'
cooking_question = '/home/pham/NLU/data/cooking_question.txt'
cooking_count_length = '/home/pham/NLU/data/cooking_count_length.txt'
cooking_count_only = '/home/pham/NLU/data/cooking_count_only.txt'


def get_label():
	with open(cooking) as infile:
		with open(cooking_label, 'w') as outfile:
			for line in infile:
				for string in line.split():
					if "__label__" in string:
						outfile.write(f'{string}\n')


def count_label():
	with open(cooking_label_uniq) as label_uniq:
		with open(cooking_label) as label:
			with open(cooking_label_count, 'w') as outfile:
				for line_label_uniq in label_uniq:
					count = 0
					for line_label in label:
						if line_label_uniq == line_label:
							count += 1
					outfile.write(f'{count} {line_label_uniq}')


def count():
	with open(cooking_label) as infile:
		with open(cooking_label_count, 'w') as outfile:
			counts = collections.Counter(l.strip() for l in infile)
			for line, count in counts.most_common():
				outfile.write(f'{count} {line}\n')


def get_question():
	with open(cooking) as infile:
		with open(cooking_question, 'w') as outfile:
			for line in infile:
				for string in line.split():
					if not "__label__" in string:
						outfile.write(f'{string} ')
				outfile.write('\n')


def count_length_question():
	with open(cooking_question) as infile:
		with open(cooking_count_length, 'w') as outfile:
			for line in infile:
				outfile.write(f'__count__{len(line)} {line}')


def count_length_only():
	with open(cooking_question) as infile:
		with open(cooking_count_only, 'w') as outfile:
			for line in infile:
				outfile.write(f'{len(line)}\n')







# get_question()
# count_length_question()
count_length_only()
# count()

# import re
# p =re.compile(r'__label__(\d+)')
# with open('infile') as infile:
#     for line in infile:
#         m = p.match(line)
#         if m:
#            print m.groups[0]