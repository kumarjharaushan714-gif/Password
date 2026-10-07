import random
import string
import json
import os
import secrets

TASK_FILE = "tasks.json"


# ==============================
# TASK MANAGER
# ==============================

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(TASK_FILE):
        return []

    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    print("\n--- Add New Task ---")

    title = input("Enter task: ").strip()

    if not title:
        print("❌ Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added successfully!")


def show_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if not tasks:
        print("📭 No tasks found.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task["completed"] else "⏳ Pending"
        print(f"{number}. {task['title']} - {status}")

    print("================================")


def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)

            print(f"🗑️ Deleted: {removed['title']}")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# ==============================
# PASSWORD GENERATOR
# ==============================

def generate_password():
    print("\n====== PASSWORD GENERATOR ======")

    try:
        length = int(input("Enter password length: "))

        if length < 6:
            print("❌ Password should be at least 6 characters.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
        use_numbers = input("Include numbers? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"

        character_pool = ""

        if use_upper:
            character_pool += string.ascii_uppercase

        if use_lower:
            character_pool += string.ascii_lowercase

        if use_numbers:
            character_pool += string.digits

        if use_symbols:
            character_pool += "!@#$%^&*()-_=+"

        if not character_pool:
            print("❌ Select at least one character type.")
            return

        password = "".join(
            secrets.choice(character_pool)
            for _ in range(length)
        )

        print("\n🔐 Generated Password:")
        print(password)

        check_password_strength(password)

    except ValueError:
        print("❌ Please enter a valid number.")


def check_password_strength(password):
    """Check basic password strength."""

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in "!@#$%^&*()-_=+" for char in password):
        score += 1

    print("\nPassword Strength:")

    if score <= 2:
        print("🟠 Weak")
    elif score == 3:
        print("🟡 Medium")
    elif score == 4:
        print("🟢 Strong")
    else:
        print("💪 Very Strong")


# ==============================
# MAIN MENU
# ==============================

def show_banner():
    print("""
╔══════════════════════════════════════╗
║      CLI TASK & PASSWORD TOOLKIT     ║
║              Python                  ║
╚══════════════════════════════════════╝
""")


def main():
    tasks = load_tasks()

    while True:

        show_banner()

        print("1. 🔐 Generate Password")
        print("2. 🛡️ Check Password Strength")
        print("3. ➕ Add Task")
        print("4. 📋 View Tasks")
        print("5. ✅ Complete Task")
        print("6. 🗑️ Delete Task")
        print("7. 🚪 Exit")

        print("\n--------------------------------------")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            generate_password()

        elif choice == "2":
            password = input("Enter password to check: ")
            check_password_strength(password)

        elif choice == "3":
            add_task(tasks)

        elif choice == "4":
            show_tasks(tasks)

        elif choice == "5":
            complete_task(tasks)

        elif choice == "6":
            delete_task(tasks)

        elif choice == "7":
            print("\n👋 Thanks for using CLI Task & Password Toolkit!")
            print("🚀 Keep learning Python!")
            break

        else:
            print("\n❌ Invalid choice. Please select 1-7.")

        input("\nPress ENTER to continue...")


# ==============================
# PROGRAM START
# ==============================

if __name__ == "__main__":
    main()