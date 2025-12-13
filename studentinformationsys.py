import os

def login():
    print("\n===== STUDENT LOGIN =====")
    name = input("Enter your name: ")
    roll = input("Enter roll number: ")
    return name, roll


def save_profile(name, roll):
    with open("profile.txt", "w") as f:
        f.write(f"Name: {name}\nRoll: {roll}")


def view_profile():
    if os.path.exists("profile.txt"):
        with open("profile.txt", "r") as f:
            print("\n--- STUDENT PROFILE ---")
            print(f.read())
    else:
        print("No profile found!")


def attendance():
    days = int(input("Total working days: "))
    present = int(input("Days present: "))
    percent = (present / days) * 100
    print(f"Attendance Percentage: {percent:.2f}%")

    with open("attendance.txt", "w") as f:
        f.write(f"Attendance: {percent:.2f}%")


def marks():
    m1 = int(input("Subject 1 marks: "))
    m2 = int(input("Subject 2 marks: "))
    m3 = int(input("Subject 3 marks: "))
    total = m1 + m2 + m3
    percent = total / 3
    print(f"Average Marks: {percent:.2f}")

    with open("marks.txt", "w") as f:
        f.write(f"Average Marks: {percent:.2f}")


def todo():
    task = input("Enter your task: ")
    with open("todo.txt", "a") as f:
        f.write(task + "\n")
    print("Task added successfully!")


def view_tasks():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as f:
            print("\n--- TO-DO LIST ---")
            print(f.read())
    else:
        print("No tasks found!")


def menu():
    print("""
===== SMART STUDENT ASSISTANT =====
1. View Profile
2. Attendance Tracker
3. Marks Calculator
4. Add To-Do Task
5. View To-Do Tasks
6. Exit
""")


# MAIN PROGRAM
name, roll = login()
save_profile(name, roll)

while True:
    menu()
    choice = input("Enter choice (1-6): ")

    if choice == "1":
        view_profile()
    elif choice == "2":
        attendance()
    elif choice == "3":
        marks()
    elif choice == "4":
        todo()
    elif choice == "5":
        view_tasks()
    elif choice == "6":
        print("Thank you for using Student Assistant!")
        break
    else:
        print("Invalid choice!")
