tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i, task)

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("4. diplay name")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    elif choice == "4":
        print("Student Task Tracker ")
    else:
        print("Invalid choice!")