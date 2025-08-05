import os
import pytest
import json
from TaskManager import TaskManager  
import psycopg2
from psycopg2 import sql

TEST_FILE = "tasks.json"

@pytest.fixture
# Funcion que prueba si existe el archivo json
def task_manager():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    tm = TaskManager(file_name=TEST_FILE)
    return tm

# Verifica que el codigo si marque como completadas tareas
def test_mark_complete(task_manager):
    task_manager.add_task("Test", "Task to complete.")
    result = task_manager.mark_complete(1)
    tasks = task_manager.list_tasks()
    assert result is True

 # Verifica eliminacion de tareas
def test_delete_task(task_manager):
    task_manager.add_task("Test", "Task to delete.")
    result = task_manager.delete_task(1)
    assert result is True
    assert len(task_manager.list_tasks()) == 0

# Verifica que no te permita marcar tareas que no existen
def test_mark_nonexistent_task(task_manager):
    result = task_manager.mark_complete(999)
    assert result is False

# Verifica que no te permita eliminar tareas que no existen
def test_delete_nonexistent_task(task_manager):
    result = task_manager.delete_task(999)
    assert result is False



