from TaskManager import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)

        elif choice == "2":
            task_manager.list_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                task_manager.mark_complete(task_id)
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
