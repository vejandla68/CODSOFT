# -----------------------------------------
# Project : To-Do List
# Internship : CodSoft Python Programming
# Name : Vejandla Mukthesh Kumar
# -----------------------------------------

tasks = []


def add_task():
    task = input("Enter the task: ").strip()

    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List")
        print("-" * 30)

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def update_task():
    if len(tasks) == 0:
        print("\nNo tasks available to update.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to update: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ").strip()

            if new_task == "":
                print("Task cannot be empty.")
            else:
                tasks[task_number - 1] = new_task
                print("Task updated successfully.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if len(tasks) == 0:
        print("\nNo tasks available to delete.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'"{removed_task}" deleted successfully.')

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def menu():

    while True:

        print("\n" + "=" * 35)
        print("         TO-DO LIST")
        print("=" * 35)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("\nThank you for using the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
