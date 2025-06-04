import os
import pytest
import json
from TaskManager import TaskManager  
TEST_FILE = "test_tasks.json"

@pytest.fixture
def task_manager():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    tm = TaskManager(file_name=TEST_FILE)
    return tm

def test_add_task(task_manager):
    task_manager.add_task("Test", "This is a test task.")
    tasks = task_manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test"
    assert tasks[0]["status"] == "Pending"

def test_mark_complete(task_manager):
    task_manager.add_task("Test", "Task to complete.")
    result = task_manager.mark_complete(1)
    tasks = task_manager.list_tasks()
    assert result is True
    assert tasks[0]["status"] == "Completed"

def test_delete_task(task_manager):
    task_manager.add_task("Test", "Task to delete.")
    result = task_manager.delete_task(1)
    assert result is True
    assert len(task_manager.list_tasks()) == 0

def test_mark_nonexistent_task(task_manager):
    result = task_manager.mark_complete(999)
    assert result is False

def test_delete_nonexistent_task(task_manager):
    result = task_manager.delete_task(999)
    assert result is False
