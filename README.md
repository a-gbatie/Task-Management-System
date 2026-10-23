# Task Management System

## Project Description

This is a simple command-line Task Management System built using Python.

The program allows users to add tasks, mark tasks as complete, view pending tasks, and track their overall task completion progress.

## Features

- **Add Task:** Create a task with a title, description, and due date.
- **Mark Task as Complete:** Mark an existing task as completed using its index.
- **View Pending Tasks:** Display tasks that have not been completed.
- **View Progress:** Calculate and display the percentage of completed tasks.
- **Input Validation:** Check that task titles and descriptions are not empty and that due dates use a valid date format.

## Project Structure

```text
task-management-system/
├── README.md
└── project/
    ├── main.py
    └── task_manager/
        ├── __init__.py
        ├── task_utils.py
        └── validation.py
```

## How to Run the Program

1. Open the project in VS Code.
2. Open the terminal.
3. Navigate to the `project` directory:

   ```bash
   cd project
   ```

4. Run the program:

   ```bash
   python3 main.py
   ```

5. Follow the menu instructions to manage your tasks.

## Menu Options

```text
Task Management System
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View Progress
5. Exit
```

Enter a number from 1 to 5 to select an option.

**Note:** Task indexes start at `0`, so the first task has index `0`.

## Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub