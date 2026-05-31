# CLI To-Do App

import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{index}. [{status}] {task['title']}")
    print()

# Add a task

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!\n")

# Mark task as complete

def complete_task(tasks):
    show_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark complete: "))
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# Delete a task

def delete_task(tasks):
    show_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# Main program

def main():
    tasks = load_tasks()

    while True:
        print("===== CLI TO-DO APP =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Try again.\n")

if __name__ == "__main__":
    main()

