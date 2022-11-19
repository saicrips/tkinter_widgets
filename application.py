import tkinter as tk
from tkinter import ttk

from suports import Suports
from widgets import Widgets
from graphs import Graphs
from technique import Technique, Technique2
from canvas import Canvas, Canvas2

class Application(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.title = "Tkinter Application"
        
        master.geometry("800x600")
        master.title(self.title)
        
        self.page_manager = PageManager(self)
        self.page_manager.pack()
        self.pages = []
        
        self.mainframe = tk.Frame(self)
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.pack()
        
        self.suports_pages = Suports(self.mainframe)
        self.pages.append(self.suports_pages)
        self.suports_pages.grid(row=0, column=0, sticky="nsew")
        
        self.widgets_pages = Widgets(self.mainframe)
        self.pages.append(self.widgets_pages)
        self.widgets_pages.grid(row=0, column=0, sticky="nsew")
        
        self.graphs_pages = Graphs(self.mainframe)
        self.pages.append(self.graphs_pages)
        self.graphs_pages.grid(row=0, column=0, sticky="nsew")
        
        self.technique_pages = Technique(self.mainframe)
        self.pages.append(self.technique_pages)
        self.technique_pages.grid(row=0, column=0, sticky="nsew")
        
        self.technique_pages = Technique2(self.mainframe)
        self.pages.append(self.technique_pages)
        self.technique_pages.grid(row=0, column=0, sticky="nsew")
        
        self.canvas_pages = Canvas(self.mainframe)
        self.pages.append(self.canvas_pages)
        self.canvas_pages.grid(row=0, column=0, sticky="nsew")
        
        self.canvas_pages = Canvas2(self.mainframe)
        self.pages.append(self.canvas_pages)
        self.canvas_pages.grid(row=0, column=0, sticky="nsew")
        
        self.page_manager.set_pages(self.pages)
        
        
        
class PageManager(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.page_counter = 0
        self.page_length = 0
        
        self.back = tk.Button(self, text="戻る", command=self.back)
        self.next = tk.Button(self, text="次へ", command=self.next)
        self.back.grid(row=0, column=0)
        tk.Frame(self, width=700).grid(row=0, column=1)
        self.next.grid(row=0, column=2)
    
    def set_pages(self, pages: list[tk.Frame]):
        self.pages = pages
        self.page_counter = 0
        self.page_length = len(pages)
        self.pages[self.page_counter].tkraise()
    
    def back(self):
        self.page_counter -= 1
        if self.page_counter < 0:
            self.page_counter = self.page_length - 1
        self.pages[self.page_counter].tkraise()
    
    def next(self):
        self.page_counter += 1
        if self.page_counter >= self.page_length:
            self.page_counter = 0
        self.pages[self.page_counter].tkraise()