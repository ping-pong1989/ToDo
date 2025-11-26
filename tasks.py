from utils import logger

TASKS_FILE = "tasks.txt"

class Task:
    def __init__(self, description):
        self.description = description.strip()

    def __str__(self):
        return self.description

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                tasks = [Task(line) for line in f.readlines()]
                logger.info("Tasks loaded successfully.")
                return tasks
        except FileNotFoundError:
            logger.warning("tasks.txt not found. Starting with empty list.")
            return []

    def save_tasks(self):
        """Save tasks to TXT file."""
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(str(task) + "\n")
        logger.info("Tasks saved successfully.")

    def add_task(self, description):
        if description.strip():
            task = Task(description)
            self.tasks.append(task)
            logger.info(f"Task added: {description}")
            print(f"Task added: '{description}'")
        else:
            logger.error("Empty task input.")
            print("Task cannot be empty. Please try again.")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\nYour to-do list is empty.")
        else:
            print("\n--- Today's Tasks ---")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print("---------------------\n")


class AdvancedTaskManager(TaskManager):
    def task_count(self):
        """Return number of tasks."""
        count = len(self.tasks)
        logger.info(f"Task count requested: {count}")
        return count
