import json
import csv
def create_tasks_json():
    tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("tasks.json created successfully!")
def load_tasks():
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    return tasks
def display_tasks(tasks):
    print("\nAll Tasks:")
    print("ID | Task Name         | Completed | Priority")
    print("-" * 45)
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:<17} | {str(task['completed']):<9} | {task['priority']}")
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4 )
        print("\n Changes saved to tasks.json file")
def tasks_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0
    print("\nTask Completion Statistics:")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {average_priority:.2f}")
def convert_to_csv(tasks):
    with open("tasks.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print("task.csv created successfully!")
def main():
    create_tasks_json()
    tasks = load_tasks()
    display_tasks(tasks)
    tasks_stats(tasks)
    save_tasks(tasks)
    convert_to_csv(tasks)
if __name__ == "__main__":
    main()
