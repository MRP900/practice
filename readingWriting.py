

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





while True:
	choice = input(
		"Type 'a' to add entries to list, 'l' to show entries or 'e' to exit: ")

	if choice == 'a':
		
		while True:
			entry = input("Enter a string or type 'exit': ")
			if entry == 'exit':
				break
			else:
				with open('data.txt', 'a') as w:	
					w.writelines(entry + "\n")
	elif choice == 'l':
		with open('data.txt', 'r') as r:
			data = r.read()
			print(data)

	else:
		break 				
    						

