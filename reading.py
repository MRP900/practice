# List contents of specified file
def list_entries(file):
	with open(file, 'r') as r:
		data = r.readlines()
		if not data:
			print(f"\n{file} is empty.\n")
		else:
			print(f"\n{file} Contents")
			line_count = 0
			for line in data:
				line_count += 1
				print(f"{line_count} - {line}", end='')
			print("\n")

# Append to file
def append_file(file, entry):
	with open(file, 'a') as w:
		output = f"{entry}\n"
		w.writelines(output)

# Count lines in file
def count_lines(file):
	line_count = 0
	with open(file, 'r') as w:
		lines = w.readlines()
		if not lines:
			return line_count
		else:
			for line in lines:
				line_count +=1
	return line_count

# Delete a line in a append_file
def delete_line(file, entry):
	stripped_list = []
	with open(file, 'r') as f:
		data = f.readlines()
		stripped_list = [item.strip() for item in data]
		stripped_list.remove(entry)
	with open(file, 'w') as w:
		for item in stripped_list:
			output = f"{item}\n"
			w.writelines(output)

# Replace an entry in the list_entries
def replace_line(file, line_to_find, replacement):
	with open(file, 'r') as f:
		data = f.readlines()
		stripped_list = [item.strip() for item in data]
		final_list = [replacement if x == line_to_find else x for x in stripped_list]
	with open(file, 'w') as f:
		for item in final_list:
			output = f"{item}\n"
			f.writelines(output)
