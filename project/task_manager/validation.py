from datetime import datetime

def validate_task_title(title):
  # Check that the title is not empty
  return bool(title.strip()) # title.strip() removes whitespace - bool() converts the result into True or False
    
def validate_task_description(description):
  # Check that the description is not empty
  return bool(description.strip())    
    
def validate_due_date(due_date):
    None