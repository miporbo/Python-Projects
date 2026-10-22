#simple to do application using python

tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

#viewing task with 1,2,3 count 
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
 #deleting task with 1,2,3 count
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

#making a menu for the user to choose from
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            save_tasks()
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




#making file to save the tasks in a text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to tasks.txt")
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks.clear()
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded from tasks.txt")
    except FileNotFoundError:
        print("No saved tasks found.")  
    except FileNotFoundError:
        print("No saved tasks found.")  

load_tasks()
main()
main()
