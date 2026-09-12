tasks = []

while True:
    choice = input("Type 'add', 'view', 'remove', or 'exit': ")
    if choice == "exit":
        break
    elif choice == "add":
        add_task = input("Enter a task to add: ")  
        tasks.append(add_task)
    elif choice == "view":
        print (tasks)
    elif choice == "remove":
        remove_task = input(f"Choose what to remove in {tasks}: ")
        if remove_task in tasks:
         tasks.remove(remove_task)
        else:
            print(f"'{remove_task}' wasn't found in your list. Try again.")

