from utils import logger

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Loads tasks from a txt file and returns a list."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f.readlines()]
            logger.info("Tasks loaded successfully.")
            return tasks
    except FileNotFoundError:
        logger.warning("tasks.txt not found. Creating a new one.")
        return []


def save_tasks(tasks):
    """Saves the list of tasks into a txt file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")
        logger.info("Tasks saved successfully.")


def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        logger.info(f"Task added: {task}")
        print(f"Task added: '{task}'")
    else:
        logger.error("Empty task input.")
        print("Task cannot be empty. Please try again.")


def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\n--- Today's Tasks ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("---------------------\n")
