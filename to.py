def display_menu():
    print("to do list")
    print("1. Add Task")
    print("2. Delete Last Task")
    print("3. View All Tasks")
    print("4. Exit") 

def addtask(stack):
    task=input("Enter a new task: ")
    stack.append(task)
    print(f"task '{task}' added successfully ")

def deletetask(stack):
    if stack:
        removed=stack.pop()
        print(f"task {removed} deleted")
    else:
        print("no tasks there to delete")

def showtasks(stack):
    i=1
    if stack:
        print("your tasks")
        for task in stack:
            print(str(i) + ". " + task)
            i += 1
    else:
        print("no tasks available")

def main():
    stack = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            addtask(stack)
        elif choice == "2":
            deletetask(stack)
        elif choice == "3":
            showtasks(stack)
        elif choice == "4":
            print("bye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()