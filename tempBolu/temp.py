import json
from datetime import datetime

# # Search task by task name
# def find_task(task_name: str, filename: str) -> dict:
#     with open(filename, mode="r") as json_file:
#         tasks = json.load(json_file)
#     for task in tasks:
#         if task_name.lower() == task.get("title").lower():
#             return task
#     return False
# 
# task_title = input("Search for a task: ")
# task = find_task(task_title, "tasks.json")
# if task:
#     print(f"Found task {task.get("title")},  due by {task.get("due_date")}")
# else:
#     print("No such task")
inp = input("-> ")
time = datetime.strptime(inp, "%d/%m/%Y")
# time = datetime.now()
day_num = time.strftime("%d")
month_full = time.strftime("%B")
year_full = time.strftime("%Y")

print(f"This task was created on the {day_num} {month_full}, year {year_full}.")