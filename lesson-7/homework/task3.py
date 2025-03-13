class TodoApp:
    def __init__(self, task_id="", title="", description="", status="Pending", filename="tasks.txt", due_date=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.tasks = {}
        self.filename = filename
        self.load_task()

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"
    def add_task(self):
        self.tasks[self.task_id] = {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
            }
        print("Tasks added successfully")
    def view_task(self):
        if not self.tasks:
            print("no task found")
            return
        for task_id, task in self.tasks.items():
            print("tasks:")
            print(f"{task_id}, {task["title"]}, {task["description"]}, {task["due_date"]}, {task["status"]} ")
    def update_task(self):
        if self.task_id not in self.tasks:
            print("Task not found")
            return
        task = self.tasks[self.task_id]
        if self.title: task["title"] = self.title
        if self.description: task["description"] = self.description
        if self.due_date: task["due_date"] = self.due_date
        if self.status: task["status"] = self.status
        print("tasks updated successfully")

    def delete_task(self):
        if self.task_id in self.tasks:
            del self.tasks[self.task_id]
            print("task deleted successfully")
        else:
            print("task not found")

    def filter_task(self):
        filtered = {tid: task for tid, task in self.tasks.items() if task["status"] == self.status }
        if not filtered:
            print(f"no task found with {self.status}")
            return
        for task_id, task in filtered.items():
            print(f"{task_id}, {task["title"]}, {task["description"]}, {task["due date"]}, {task["status"]}")

    def save_task(self):
        with open(self.filename, "w") as f:
            for task_id, task in self.tasks.items():
                line = f"{task_id[task_id]}, {task["title"]}, {task["description"]}, {task["due date"]}, {task["status"]} \n"
                f.write(line)
        print("tasks saved successfully")

    def load_task(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if line.strip():
                        task_id, title, description, due_date, status = line.strip().split()
                        self.tasks[task_id] ={
                        "task_id": task_id,
                        "title": title,
                        "description": description,
                        "due_date": due_date,
                        "status": status
                        }
        except FileNotFoundError:
            print("file not found")
            self.tasks = {}





def main():
    app = TodoApp()
    while True:
        print("""
        \nWelcome to the To-Do Application!")
        1. Add a new task
        2. View all tasks
        3. Update a task
        4. Delete a task
        5. Filter tasks by status
        6. Save tasks
        7. Load tasks
        8. Exit
              """)
        choice = input("Enter your choice: ")
        if choice == "1":
            app.task_id = input("Enter Task ID: ")
            app.title = input("Enter Title: ")
            app.description = input("Enter Description: ")
            app.due_date = input("Enter Due Date (or press Enter): ") or "None"
            app.status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
            app.add_task()
        elif choice == "2":
            app.view_task()
        elif choice == "3":
            app.task_id = input("Enter Task ID to update: ")
            app.title = input("Enter new Title (or press Enter): ") or None
            app.description = input("Enter new Description (or press Enter): ") or None
            app.due_date = input("Enter new Due Date (or press Enter): ") or None
            app.status = input("Enter new Status (or press Enter): ") or None
            app.update_task()
        elif choice == "4":
            app.task_id = input("Enter Task ID to delete: ")
            app.delete_task()
        elif choice == "5":
            app.status = input("Enter Status to filter by: ")
            app.filter_task()
        elif choice == "6":
            app.save_task()
        elif choice == "7":
            app.load_task()
            print("Tasks loaded successfully!")
        elif choice == "8":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



    