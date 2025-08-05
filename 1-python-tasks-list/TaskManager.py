import os
from datetime import datetime
from database_implementation import Database

class TaskManager:
    def __init__(self):
        self.db = Database()  # Initialize database connection
    
    # Insert a new task into PostgreSQL
    def add_task(self, task_name, description):
        try:
            issue_id = self.db.insert_task(
                task_name=task_name,  # Changed from 'name' to 'task_name'
                description=description,
                status="Pending",
                creation_date=datetime.now().date()
            )
            print(f"Task '{task_name}' added successfully (ID: {issue_id})!")
        except Exception as e:
            print(f"Error adding task: {e}")

    # List all tasks from PostgreSQL
    def list_tasks(self):
        try:
            tasks = self.db.fetch_tasks()
            
            if not tasks:
                print("No tasks found.")
                return
            
            print("\n" + "=" * 80)
            print(f"{'ID':<5} {'TITLE':<20} {'STATUS':<10} {'CREATED DATE':<20} {'DESCRIPTION':<30}")
            print("-" * 80)
            
            for task in tasks:
                print(
                    f"{task[0]:<5} {task[1][:18]:<20} "  # id, title
                    f"{task[3]:<10} {task[4]:<20} "      # status, created_date
                    f"{task[2][:28]:<30}"                 # description
                )
            
            print("=" * 80 + "\n")
        except Exception as e:
            print(f"Error listing tasks: {e}")

    # Update task status in PostgreSQL
    def mark_complete(self, issue_id):
        try:
            self.db.update_task_status(issue_id, "Completed")
            print(f"Task ID {issue_id} marked as completed!")
        except Exception as e:
            print(f"Error updating task: {e}")

    # Delete a task from PostgreSQL
    def delete_task(self, issue_id):
        try:
            self.db.delete_task(issue_id)
            print(f"Task ID {issue_id} deleted successfully!")
        except Exception as e:
            print(f"Error deleting task: {e}")

    # Close database connection
    def close(self):
        self.db.close()

# Interface function 
def manager_interface(task_manager):
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
            task_id = int(input("Enter task ID to mark as complete: "))
            task_manager.mark_complete(task_id)
        
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            task_manager.close()  # Proper cleanup
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_manager = TaskManager()
    manager_interface(task_manager)