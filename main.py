from tasks import add_task, view_tasks

def main():
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
            print("Don't forget to do them all, you lazy ah")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
