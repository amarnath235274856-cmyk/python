# To-Do List Project

tasks = []


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\n----- Your Tasks -----")

        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)


def remove_task():
    view_tasks()

    if len(tasks) > 0:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print("Removed:", removed_task)
        else:
            print("Invalid task number.")


while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Try again.")