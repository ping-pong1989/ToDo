class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def list_tasks(self):
        return self.tasks

    def load_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(task + "\n")
