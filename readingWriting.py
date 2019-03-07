

# with open('data.txt', 'w') as f:
# 	data = [
# 		'functions',
# 		'classes',
# 		'methods',
# 		'decorators',
# 	]
# 	for i in data:
# 		f.writelines(i + "\n")

# with open('data.txt', 'r') as f:
# 	data = f.read()
# 	print(data)

# with open('data.txt', 'a') as f:
# 	f.write('Import')

# with open('data.txt', 'r') as f:
# 	data = f.read()
# 	print(data)


# List contents of specified file
def list_entries(file):
	with open(file, 'r') as r:
		data = r.readlines()
		for line in data:
			print(line, end='')


# Write
def write_to_file(file):
	line_count = 0
	with open(file, 'a') as w:
		line_count += 1
		output = f"{line_count} - {entry}"
		w.writelines(output)


# Append


def append_file(file, entry):
	line_count = count_lines(file)
	with open(file, 'a') as w:
		line_count += 1
		output = f"{line_count} - {entry} \n"
		w.writelines(output)

# Count number of lines in file


def count_lines(file):
	line_count = 0
	with open(file, 'r') as w:
		lines = w.readlines()
		for line in lines:
			line_count += 1
	return line_count


while True:
	choice = input(
		"Type 'a' to add entries to list, \n'l' to list entries, \n'd' to delete, \n'r' to replace, \nor 'e' to exit: ")
	
	if choice == 'a':
		while True:
			entry = input("Enter a string or type 'exit': ")
			if entry == 'exit':
				break
			else:
				append_file('data.txt', entry)

	elif choice == 'l':
		list_entries('data.txt')
	
	elif choice == 'd':
		with open('data.txt', "r+") as r:
			data = r.readlines()
			for line in data:
				if line.startswith(choice):
					line.remove()
			r.writelines(data)

	# elif choice == 'r':
	# 	# some code
    					
	else:
		break 				

