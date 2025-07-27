from task_manager import TaskTracker
from datetime import datetime

# Entry point
task_coordinator = TaskTracker()

print(task_coordinator.welcome_msg)
name = input('Hi, please enter your name: ')
print(f'Welcome {name.title()}')

def new_operation():
    # load_tasks()
    options = ['Add Task', 'Remove Task', 'View Task', 'Update Task or Mark as done', 'save and exit']

    for index, option in enumerate(options):
        print(f'{index + 1}. {option}')

    try:
        select_option = int(input("What would you like to do? Please select an option by index number:\n "))
    except ValueError:  # this catches type errors that is if the usere enters a letter rather tan a number since we already declared input as int
        print("Invalid input. Please enter a number.")
        return new_operation()  # this takes it to the beginning of the function

    if select_option == 1:
        print("Enter tasks one by one. Type 'done' as task name when you're finished:")
        while True:
            title = input("→ Task name: ").strip()
            if title.lower() == 'done':
                break
            if not title:
                continue

            due_date = input("Due date (dd/mm/yyyy): ").strip()
            priority = input("Priority (L = Low, M = Medium, H = High): ").strip().upper()

            # Normalize priority input
            if priority == 'L':
                priority = 'Low'
            elif priority == 'M':
                priority = 'Medium'
            elif priority == 'H':
                priority = 'High'
            else:
                priority = 'Unknown'
        task_coordinator.add_task()

    elif select_option == 2:
        task_coordinator.remove_task(tasks)

    elif select_option == 3:
        task_coordinator.displayTask()

    elif select_option == 4:
        task_coordinator.update_task()

    elif select_option == 5:
        task_coordinator.save_tasks()
        print("👋 Tasks saved and exiting. Goodbye!")
        return

    else:
        print("Invalid option selected.")
        new_operation()

new_operation()
