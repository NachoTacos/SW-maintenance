from datetime import datetime
from colorama import Fore, Style, init
import psycopg2
from psycopg2 import sql


# class for database connection
class Database:
    def __init__(self, dbname="task-manager", user="postgres", password="admin", host="localhost", port="5432"):
        self.connection = psycopg2.connect(
            dbname = dbname,
            user = user, 
            password = password,
            host = host,
            port = port
        )
        self.cursor = self.connection.cursor()


    # To read schemas for opening tables | 'schema.sql' is the route of the schemas
    def create_table(self):
        with open('schema.sql','r') as f:
            self.cursor.execute(f.read())
            self.connection.commit()


    # Function for SQL query to insert data into the postgres database
    # Takes in the following args: title, description, status and the created date
    def insert_task(self, task_name, description, status="Pending", creation_date=None):
        try:
            if creation_date is None:
                creation_date = datetime.now().date()  # Use .date() for date columns
                
            self.cursor.execute(
                """INSERT INTO the_tasks_table 
                (task_name, description, status, creation_date)
                VALUES (%s, %s, %s, %s) RETURNING issue_id""",
                (task_name, description, status, creation_date)
            )
            issue_id = self.cursor.fetchone()[0]
            self.connection.commit()
            return issue_id
        except Exception as e:
            self.connection.rollback()
            print(f"Database error: {e}")
            raise


    # SQL query to retrieve all the entries on the table
    def fetch_tasks(self):
        self.cursor.execute("SELECT * FROM the_tasks_table;")
        return self.cursor.fetchall()


    # SQL query to update the task status into postgres
    def update_task_status(self, issue_id,status):
        self.cursor.execute(
            sql.SQL("UPDATE the_tasks_table SET status  = %s WHERE issue_id = %s;"),(status, issue_id)
        )
        self.connection.commit()


    # SQL query to delete the task from the table
    def delete_task(self, issue_id):
        try:
            # Execute deletion with proper parameter formatting
            self.cursor.execute(
                "DELETE FROM the_tasks_table WHERE issue_id = %s",
                (issue_id,)  # Note the comma to make it a tuple
            )
            
            # Check if any rows were affected
            if self.cursor.rowcount == 0:
                print(f"No task found with ID {issue_id}")
                return False
                
            self.connection.commit()
            print(f"Task ID {issue_id} deleted successfully!")
            return True
            
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting task: {e}")
            return False


    # Closing the database connection and cursor
    def close(self):
        self.cursor.close()
        self.connection.close()
