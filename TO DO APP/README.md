# To-Do List App

A simple Python CLI to-do list. You can add tasks, view them with
numbers, and delete them. Tasks are saved in a text file, so they are
still there the next time you run the program.

## Features
- Menu-based interface (Add, View, Delete, Exit)
- Tasks are shown with numbers (1, 2, 3...)
- Delete a task by its number
- Handles wrong input (invalid number or text instead of a number)
- Saves tasks to `tasks.txt` when you exit and loads them on start

## How to Run

python To-Do-App.py

## Sample Output

No saved tasks found.

To-Do List Application
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 1
Enter a new task: Buy milk
Task added successfully!

To-Do List Application
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 2
Your tasks:
1. Buy milk

To-Do List Application
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice (1-4): 4
Tasks saved to tasks.txt
Exiting the application. Goodbye!

## Tech Used
- Python 3
- Core concepts: lists, functions, while loop, conditionals (if/elif/else), try/except, file handling (read/write), f-strings

## Author
Md. Majharul Islam Porbo  
Portfolio: [porbo.cyou](https://porbo.cyou)
