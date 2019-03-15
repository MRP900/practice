from reading import list_entries, append_file, count_lines, \
    delete_line, replace_line, make_inventory

while True:
    choice = input(
        "-----Menu----- \
        \n'a' to add entries to list \
        \n'l' to list entries \
        \n'd' to delete \
        \n'r' to replace \
        \n'e' to exit \
        \n'c' count entries \
        \n'm' make an inventory from list \
        \n\nEnter your choice: ")

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
        while True:
            choice = input("Enter the line you wish to delete or 'exit': ")
            if choice == 'exit':
                break
            else:
                delete_line('data.txt', choice)

    elif choice == 'c':
        lines = count_lines('data.txt')
        print(f"\nNumber of Entries: {lines}\n")

    elif choice == 'r':
        while True:
            entry1 = input("Enter an item to replace or 'exit': ")
            if entry1 == 'exit':
                break
            entry2 = input("Enter the replacement or 'exit': ")
            if entry2 == 'exit':
                break
            replace_line('data.txt', entry1, entry2)

    elif choice == 'm':
        make_inventory('data.txt')

    else:
        break
