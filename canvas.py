import tkinter as tk

class Canvas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(self, width=800, height=600, bg="cyan")

        self.canvas.create_rectangle(0, 0, 800, 450, fill='green')
        self.canvas.create_oval(10, 10, 140, 140, tag="oval")

        self.canvas.pack()