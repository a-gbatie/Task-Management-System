from datetime import datetime

def validate_task_title(title):
  # Check that the title is not empty
  return bool(title.strip()) # title.strip() removes whitespace - bool() converts the result into True or False
    
def validate_task_description(description):
  # Check that the description is not empty
  return bool(description.strip())    
    
def validate_due_date(due_date):
  # Check that the date uses the correct format
  try: # attempts to run code - might produce an error
    datetime.strptime(due_date, "%Y-%m-%d") # converts date string into Python date/time object
    return True # the date was accepted
  except (ValueError, TypeError): # catches invalid input or date (February 30)
    return False # returns False insted of crashing