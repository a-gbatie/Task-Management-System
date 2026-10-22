from datetime import datetime

# Import validation functions
from .validation import (
  validate_task_title,
  validate_task_description,
  validate_due_date,
)

# Define tasks list
tasks = []

# Implement add_task function
# If statements check whether the user's inputs are valid - stop the function if inputs are invalid
def add_task(title, description, due_date):
  if not validate_task_title(title):
    print("Invalid task title.")
    return
  
  if not validate_task_description(description):
    print("Invalid task description.")
    return
  
  if not validate_due_date(due_date):
    print("Invalid due date.")
  
  task = {
    "title": title,
    "description": description,
    "due_date": due_date,
    "completed": False
  }
  
  tasks.append(task)
  print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    None
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    None

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    None
    return progress