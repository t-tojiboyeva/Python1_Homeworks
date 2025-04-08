
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"  # default status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, task_title):
        for task in self.tasks:
            if task.title.lower() == task_title.lower():
                task.mark_complete()
                print("Task marked as complete.")
                return
        print("Task not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def list_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if task.status == "Incomplete":
                print(task)
                found = True
        if not found:
            print("No incomplete tasks.")


def main():
    todo = ToDoList()

    while True:
        print("\nToDo List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            task_title = input("Enter the title of the task to mark as complete: ")
            todo.mark_task_complete(task_title)

        elif choice == "3":
            print("\nAll Tasks:")
            todo.list_all_tasks()

        elif choice == "4":
            print("\nIncomplete Tasks:")
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose between 1-5.")


main()
