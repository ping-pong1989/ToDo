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

def main():
    """Main function to run the simple To-Do application."""
    tasks = []

    print("Welcome to the Simple Task Collector!")
    
    while True:
        print("\n--- Menu ---")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            print("Don't forget to do them all you lazy ah")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()