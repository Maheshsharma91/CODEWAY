tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def complete_task():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    if task_number > 0 and task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if task_number > 0 and task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
