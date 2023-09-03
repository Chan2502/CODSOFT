import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Function to add a task
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        task_list.append(task)
        listbox.insert(END, task)
        saveTasks()

# Function to delete a task
def deleteTask():
    selected_task = listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        listbox.delete(task_index)
        task_list.pop(task_index)
        saveTasks()

# Function to save tasks to a file
def saveTasks():
    with open("tasklist.txt", 'w') as taskfile:
        for task in task_list:
            taskfile.write(f"{task}\n")

# Function to load tasks from a file
def loadTasks():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            for task in tasks:
                if task.strip():
                    task_list.append(task.strip())
                    listbox.insert(END, task.strip())
    except FileNotFoundError:
        pass

root = Tk()
root.title("TO-DO LIST")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

# Configure the root window background color
root.configure(bg="#f0f0f0")

# Set an icon for the application
Image_icon = PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

# Create a top bar
top_bar = Frame(root, height=60, bg="#b3ccff")
top_bar.pack(fill="x")

# Add a title label
title_label = Label(top_bar, text="TO-DO LIST", font=("Helvetica", 22, "bold"), fg="black", bg="#b3ccff")
title_label.pack(pady=10)

# Create a task entry and "Add" button
entry_frame = Frame(root, bg="#f0f0f0")
entry_frame.pack(fill="x")

task_entry = Entry(entry_frame, font=("Helvetica", 15), bd=0, highlightthickness=2,borderwidth=2, relief=SUNKEN)
task_entry.pack(side=LEFT, padx=20, pady=40, fill="x", expand=True)

add_button = Button(entry_frame, text="ADD", font=("Helvetica", 13, "bold"), bg="#5a95ff", fg="white", bd=0, command=addTask)
add_button.pack(side=RIGHT, padx=20, pady=10)

# Create a list frame
list_frame = Frame(root, bg="#f0f0f0")
list_frame.pack(fill="both", expand=True)

# Create a listbox and scrollbar
listbox = Listbox(list_frame, font=("Helvetica", 14), bg="#f0f0f0", selectbackground="#5a95ff", selectmode=SINGLE, bd=0)
listbox.pack(fill="both", expand=True, padx=20, pady=(0, 10), side=LEFT)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Load existing tasks
loadTasks()

# Create a "Delete" button
delete_button = Button(root, text="DELETE", font=("Helvetica", 14, "bold"), bg="#ff6b6b", fg="white", bd=0, command=deleteTask)
delete_button.pack(pady=10, fill="x")

root.mainloop()
