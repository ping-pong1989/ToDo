def add_task(todo_list):
    """Prompts the user for a new task and adds it to the list."""
    task = input("Enter the new task: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task added: '{task}'")
    else:
        print("Task cannot be empty. Please try again.")

def view_tasks(todo_list):
    """Displays all current tasks in the list."""
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\n--- Today's Tasks ---")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")
        print("---------------------\n")
