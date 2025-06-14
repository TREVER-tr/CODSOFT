import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create the database
conn = sqlite3.connect('contacts.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                email TEXT,
                address TEXT)''')
conn.commit()

# Functions for contact operations
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)", 
                  (name, phone, email, address))
        conn.commit()
        messagebox.showinfo("Success", "Contact added successfully!")
        show_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

def show_contacts():
    listbox.delete(0, tk.END)
    c.execute("SELECT name, phone FROM contacts")
    for row in c.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

def search_contact():
    query = search_entry.get()
    listbox.delete(0, tk.END)
    c.execute("SELECT name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?", 
              ('%' + query + '%', '%' + query + '%'))
    for row in c.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

def delete_contact():
    selected = listbox.get(tk.ANCHOR)
    if selected:
        name = selected.split(" - ")[0]
        c.execute("DELETE FROM contacts WHERE name=?", (name,))
        conn.commit()
        messagebox.showinfo("Deleted", "Contact removed successfully!")
        show_contacts()

# GUI Setup
root = tk.Tk()
root.title("Contact Manager")

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone:").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address:").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2)
tk.Label(root, text="Search:").grid(row=5, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=6, column=0, columnspan=2)

listbox = tk.Listbox(root, width=40)
listbox.grid(row=7, column=0, columnspan=2)

tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=8, column=0, columnspan=2)

show_contacts()
root.mainloop()
# rock paper scissor game
import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result_text.set(f"You: {user_choice}\nComputer: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        result_text.set(result_text.get() + "\nIt's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text.set(result_text.get() + "\nYou Win!")
        user_score += 1
    else:
        result_text.set(result_text.get() + "\nComputer Wins!")
        computer_score += 1

    score_text.set(f"Your Score: {user_score} | Computer Score: {computer_score}")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack()

frame = tk.Frame(root)
frame.pack()

for choice in choices:
    tk.Button(frame, text=choice, command=lambda c=choice: play(c)).pack(side="left")

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack()

score_text = tk.StringVar()
score_text.set(f"Your Score: {user_score} | Computer Score: {computer_score}")
tk.Label(root, textvariable=score_text, font=("Arial", 12)).pack()

root.mainloop()
#password generator
import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password():
    length = int(length_entry.get())
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    password_var.set(password)

# Function to save password to a file
def save_password():
    password = password_var.get()
    if password:
        with open("saved_passwords.txt", "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Success", "Password saved successfully!")
    else:
        messagebox.showerror("Error", "No password to save!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12))
password_label.pack()

tk.Button(root, text="Save Password", command=save_password).pack()

root.mainloop()
#calculator
- User enters two numbers
- Selects an operation: Addition, Subtraction, Multiplication, or Division
- Performs the calculation and displays the result

Python Code
def calculator():
    print("Simple Calculator")
    
    # User input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Choose an operation: +, -, *, /")
    operation = input("Enter operation: ")
    
    # Perform Calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

    print("Result:", result)

# Run the calculator
calculator()
# to-do-list app
import json

# Load existing tasks
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "Pending"})
    save_tasks(tasks)
    print("Task added!")

# View all tasks
def view_tasks():
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['task']} - {task['status']}")

# Update a task
def update_task():
    view_tasks()
    idx = int(input("Enter task number to update: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["status"] = "Completed"
        save_tasks(tasks)
        print("Task updated!")
    else:
        print("Invalid task number!")

# Delete a task
def delete_task():
    view_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        del tasks[idx]
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number!")

# Main Program
tasks = load_tasks()
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "


 
