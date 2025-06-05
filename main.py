from task_manager import TaskManager

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n" + "=" * 80)
    print(f"{'ID':<5} {'TITLE':<20} {'STATUS':<10} {'CREATED DATE':<20} {'DESCRIPTION':<30}")
    print("-" * 80)

    for task in tasks:
        print(f"{task['id']:<5} {task['title'][:18]:<20} {task['status']:<10} {task['created_date']:<20} {task['description'][:28]:<30}")

    print("=" * 80 + "\n")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
            print(f"Task '{title}' added successfully!")

        elif choice == "2":
            tasks = task_manager.get_tasks()
            display_tasks(tasks)

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                if task_manager.mark_complete(task_id):
                    print(f"Task {task_id} marked as completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if task_manager.delete_task(task_id):
                    print(f"Task {task_id} deleted successfully!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid task ID.")

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
