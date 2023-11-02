import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        to_do_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Task cannot be empty.")

def update_task():
    selected_task = to_do_list.curselection()
    if selected_task:
        index = int(selected_task[0])
        updated_task = task_entry.get()
        if updated_task:
            to_do_list.delete(index)
            to_do_list.insert(index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task cannot be empty.")
    else:
        messagebox.showerror("Error", "Select a task to update.")

def remove_task():
    selected_task = to_do_list.curselection()
    if selected_task:
        index = int(selected_task[0])
        to_do_list.delete(index)
    else:
        messagebox.showerror("Error", "Select a task to remove.")

app = tk.Tk()
app.title("To-Do List")

task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
update_button = tk.Button(app, text="Update Task", command=update_task)
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
add_button.pack()
update_button.pack()
remove_button.pack()

to_do_list = tk.Listbox(app, selectmode=tk.SINGLE)
to_do_list.pack()

app.mainloop()
