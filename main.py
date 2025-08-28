import tkinter as tk
import ui

app = tk.Tk()
app.title("Task Manager")
app.geometry("720x480")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

ui.show_all_tasks_frame(app)

app.mainloop()