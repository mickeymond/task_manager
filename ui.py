import tkinter as tk
from tkinter import messagebox
from functools import partial
import commands
import customtkinter

def handle_update(id, title, app):
    if not title:
        messagebox.showerror(
            title="Edit Task",
            message="Cannot update with empty task!",
            parent=app)
    else:
        commands.update_task(id, {"title": title})
        show_all_tasks_frame(app)

def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)

def submit_task(title, app):
    if not title:
        messagebox.showerror(
            title="Add Task",
            message="Cannnot add empty task!",
            parent=app)
    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app)

def show_edit_task_frame(task, app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text=f"Edit task: {task["title"]}", font=("Garamond", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2)
    # Add an entry widget and show the task title
    entry = tk.Entry(master=frame)
    entry.insert(0, task["title"])
    entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5,10))
    # Add a button with text Update for saving the changes
    update_btn = tk.Button(
        master=frame,
        text="Update",
        command=lambda: handle_update(task["_id"], entry.get(), app))
    update_btn.grid(row=2, column=1)
    # Add a button with text Back / Cancel for remove the frame
    cancel_btn = tk.Button(
        master=frame,
        text="Cancel",
        command=lambda: frame.destroy())
    cancel_btn.grid(row=2, column=0)

    frame.tkraise()

def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text="What do you want to do?", font=("Garamond", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2)
    entry = tk.Entry(master=frame)
    entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5,10))
    submit_btn = tk.Button(
        master=frame,
        text="Submit",
        command=lambda: submit_task(entry.get(), app))
    submit_btn.grid(row=2, column=1)
    cancel_btn = tk.Button(
        master=frame,
        text="Cancel",
        command=lambda: frame.destroy())
    cancel_btn.grid(row=2, column=0)

    frame.tkraise()

def show_all_tasks_frame(app):
    frame = customtkinter.CTkScrollableFrame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text="All Tasks", font=("Garamond", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    add_btn = tk.Button(
        master=frame,
        text="Add Task",
        command=lambda: show_add_task_frame(app))
    add_btn.grid(row=0, column=2, pady=(0, 20))

    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task) + 1, column=0)

        edit_btn = tk.Button(
            master=frame,
            text="Edit",
            command=partial(show_edit_task_frame, task, app))
        edit_btn.grid(row=tasks.index(task) + 1, column=1)

        delete_btn = tk.Button(
            master=frame,
            text="Delete",
            command=partial(handle_delete, task["_id"], app))
        delete_btn.grid(row=tasks.index(task) + 1, column=2)

    frame.tkraise()