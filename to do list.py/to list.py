"""
todo.py - Console-based To-Do List Application (with colors using ANSI codes)

Features:
✅ View tasks
✅ Add tasks
✅ Remove tasks
✅ Save tasks persistently in a file (tasks.txt)
"""

# ANSI color codes
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# File where tasks are stored
TODO_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file into a list."""
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks into the file."""
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print(YELLOW + "\n📂 No tasks found!\n" + RESET)
    else:
        print(CYAN + "\n📋 Your To-Do List:" + RESET)
        for index, task in enumerate(tasks, start=1):
            print(WHITE + f"{index}. {task}" + RESET)
        print()


def add_task(tasks):
    """Add a new task to the list."""
    task = input(GREEN + "Enter new task: " + RESET).strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(GREEN + "✅ Task added!\n" + RESET)
    else:
        print(RED + "⚠️ Empty task not allowed!\n" + RESET)


def remove_task(tasks):
    """Remove a task by its number."""
    show_tasks(tasks)
    try:
        task_number = int(input(MAGENTA + "Enter task number to remove: " + RESET))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(RED + f"🗑️ Removed: {removed}\n" + RESET)
        else:
            print(RED + "⚠️ Invalid task number!\n" + RESET)
    except ValueError:
        print(RED + "⚠️ Please enter a valid number!\n" + RESET)


def main():
    """Main function that runs the To-Do List application."""
    tasks = load_tasks()

    while True:
        print(BLUE + "====== TO-DO LIST APP ======" + RESET)
        print(YELLOW + "1. View Tasks" + RESET)
        print(GREEN + "2. Add Task" + RESET)
        print(RED + "3. Remove Task" + RESET)
        print(CYAN + "4. Exit" + RESET)

        choice = input(WHITE + "Choose an option (1-4): " + RESET).strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print(CYAN + "👋 Exiting... Have a productive day!" + RESET)
            break
        else:
            print(RED + "⚠️ Invalid choice! Try again.\n" + RESET)


if __name__ == "__main__":
    main()
