from tasks import TaskManager
from utils_apy import get_quote


def main():
    manager = TaskManager("tasks.txt")

    print("Welcome to the Simple Task Collector!")

    while True:
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        print("4. Get Quote of the Day")


        choice = input("Choose an option: ").strip()

        if choice == "1":
            task_name = input("Enter task: ")
            manager.add_task(task_name)
            manager.save_to_file()
            print("Task added!")

        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\n--- Your Tasks ---")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            print("Gbye, dont forget to do them you lazy ah")
        elif choice == "4":
            print(get_quote())
            manager.save_to_file()
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
