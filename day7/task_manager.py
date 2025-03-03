import os
import json

file_name = "task.json"

def load_task():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read().strip()
            if content:  # Jika file tidak kosong
                tasks = json.loads(content)  # Parse JSON
                if isinstance(tasks, list):  # Pastikan file JSON adalah array of objects
                    return tasks
                else:
                    print("Warning: Invalid data format in task.json. Resetting tasks.")
                    return []
            else:
                return []  # Jika file kosong, kembalikan list kosong
    return []  # Jika file tidak ada, kembalikan list kosong


# Save tasks to a JSON file
def save_tasks(tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)  # Save the Python dictionary as JSON

# Add a new task
def add_task(tasks):
    title = input("Enter task: ")
    task_id = len(tasks) + 1  # Gunakan panjang array sebagai task_id
    tasks.append({"task_id": task_id, "title": title, "status": "incomplete"})
    print(f"Task '{title}' added!")
    
def view_task(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"[{task['task_id']}] {task['title']} - {task['status']}")


def mark_task_complete(tasks):
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
        task_found = False
        for task in tasks:
            if task['task_id'] == task_id:
                task['status'] = "complete"
                print(f"Task '{task['title']}' marked as complete.")
                task_found = True
                break
        if not task_found:
            print("Task ID not found!")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def deleted_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))
        task_found = False
        for i, task in enumerate(tasks):
            if task['task_id'] == task_id:
                deleted_task = tasks.pop(i)
                print(f"Task '{deleted_task['title']}' deleted!")
                task_found = True
                break
        if not task_found:
            print("Task ID not found!")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")



def main():
    tasks = load_task()
    try:
        while True:
            print("\nMENU")
            print("1. ADD TASK")
            print("2. VIEW TASK")
            print("3. MARK TASK AS COMPLETE")
            print("4. DELETE TASK")
            print("5. EXIT")
            user = input("Enter your choice (1-5): ")

            if user == "1":
                add_task(tasks)
            elif user == "2":
                view_task(tasks)
            elif user == "3":
                mark_task_complete(tasks)
            elif user == "4":
                deleted_task(tasks)
            elif user == "5":
                save_tasks(tasks)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nGoodbye! Exiting program...")
        save_tasks(tasks)

main()
