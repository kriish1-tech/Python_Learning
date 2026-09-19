print("Welcome to the To-Do List!")

tasks = {}

print('''Please choose an option:
1. Add a task
2. View tasks
3. Remove a task
4. Exit
''')

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task_name = input("Enter the task name: ")
        task_description = input("Enter the task description: ")
        tasks[task_name] = task_description
        print(f"Task '{task_name}' added successfully!")

    elif choice == '2':
        if tasks == {}:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for task, description in tasks.items():
                print(f"- {task}: {description}")

    elif choice == '3':
        task_name = input("Enter the task name to remove: ")
        if task_name in tasks:
            del tasks[task_name]
            print(f"Task '{task_name}' removed successfully!")
        else:
            print(f"Task '{task_name}' not found.")

    elif choice == '4':
        print("Exiting the To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


print("Thank you for using the To-Do List!")