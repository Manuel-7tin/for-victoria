import json

class TaskTracker:

    def __init__(self):
        # Initial task list (empty)
        self.tasks = []
        self.name = "lingerie"
        self.welcome_msg = "Welcome to Your No'1 Personal Task Tracker"

    def add_task(self):


            task = {
                "title": title,
                "due_date": due_date,
                "priority": priority,
                "status": "Pending"
            }

            tasks.append(task)

        self.displayTask()

    def displayTask(self):
        print('\nYour Tasks:')

        if not tasks:
            print("No tasks added yet.\n")
        else:
            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}: {task['title']} | Due: {task['due_date']} | Priority: {task['priority']} | Status: {task['status']}")

        while True:
            something_else = input('Would you like to do something else? (y/n): ').strip().lower()
            if something_else == "y":
                self.new_operation()
                return
            elif something_else == "n":
                print('👋 Have a productive day.')
                return
            else:
                print("Invalid input. Try again.")
                return

    # Function to remove task
    def remove_task(self, all_task):
        try:
            task_num = int(input('Enter the task number you want to delete: '))
            if 1 <= task_num <= len(all_task):
                removed = all_task.pop(task_num - 1)
                print(f"Task '{removed}' deleted successfully.")
            else:
                print("Task number out of range.")
        except ValueError:
            print("Invalid input. Enter a number.")

        while True:
            something_else = input("Would you like to do something else? (y/n): ").strip().lower()

            if something_else == 'y':
                self.new_operation(tasks)
                return
            elif something_else == 'n':
                print("👋 Have a productive day.")
                return
            else:
                print("Invalid input. Try again.")
                return

    # Update Task
    def update_task(self):
        self.displayTask()
        try:
            task_num = int(input("Enter the task number to update/mark as done: "))
            if 1 <= task_num <= len(tasks):
                task = tasks[task_num - 1]

                print("What do you want to update?")
                print("1. Mark as Done")
                print("2. Change Due Date")
                print("3. Change Priority")

                choice = input("Enter option number: ").strip()

                if choice == '1':
                    task['status'] = 'Done'
                    print("Task marked as done.")
                elif choice == '2':
                    task['due_date'] = input("New due date (dd/mm/yyyy): ")
                elif choice == '3':
                    new_priority = input("New priority (L/M/H): ").strip().upper()
                    if new_priority == 'L':
                        task['priority'] = 'Low'
                    elif new_priority == 'M':
                        task['priority'] = 'Medium'
                    elif new_priority == 'H':
                        task['priority'] = 'High'
                    else:
                        print("Invalid priority.")
                else:
                    print("Invalid option.")
            else:
                print("Task number out of range.")
        except ValueError:
            print("Please enter a valid number.")

        # Ask for next action
        while True:
            something_else = input("Would you like to do something else? (y/n): ").strip().lower()
            if something_else == 'y':
                self.new_operation()
                return
            elif something_else == 'n':
                print("👋 Have a productive day.")
                return
            else:
                print("Invalid input. Try again.")
                return

    # load task
    def load_tasks(self, filename="tasks.json"):
        global tasks  # allow updating the tasks list
        try:
            with open(filename, "r") as f:
                tasks = json.load(f)
            print("📁 Tasks loaded successfully.")
        except FileNotFoundError:
            print("🆕 No saved tasks found. Starting fresh.")


    # save task
    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(tasks, f, indent=4)
        print("✅ Tasks saved.")


    # Search task by task name
    def find_task(self, task_name: str, filename: str) -> dict:
        with open(filename, mode="r") as json_file:
            tasks = json.load(json_file)
        for task in tasks:
            if task_name.lower() == task.get("title").lower():
                return task
        return False
