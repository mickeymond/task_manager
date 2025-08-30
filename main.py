import tkinter as tk
import ui
import customtkinter

app = tk.Tk()
app.title("Task Manager")
app.geometry("720x480")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

customtkinter.set_default_color_theme("themes/coffee.json")

ui.show_all_tasks_frame(app)

app.mainloop()