tasks = []

# Display tasks
def show_tasks():
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{index}. [{status}] {task['title']}")
    print()

# Add task
def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!\n")

# Complete task
def complete_task():
    show_tasks()

    try:
        task_num = int(input("Enter task number to mark complete: "))
        tasks[task_num - 1]["done"] = True
        print("Task marked as completed!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# Delete task
def delete_task():
    show_tasks()

    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"Deleted task: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# Main menu
while True:
    print("===== CLI TO-DO APP =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option! Try again.\n")