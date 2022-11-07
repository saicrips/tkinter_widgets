import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
try:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
except ImportError:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Graphs(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.graph_frame = tk.LabelFrame(self, text="Graph")
        fig = Figure()
        self.ax = fig.add_subplot(1, 1, 1)
        self.fig_canvas = FigureCanvasTkAgg(fig, self.graph_frame)
        self.toolbar = NavigationToolbar2TkAgg(self.fig_canvas, self.graph_frame)
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.graph_frame.pack()
        self.button = tk.Button(self, text="グラフの表示", command=self.show_graph)
        self.button.pack()
        
    def show_graph(self):
        x = np.arange(-np.pi, np.pi, 0.1)
        y = np.sin(x)
        self.ax.plot(x, y)
        self.fig_canvas.draw()
        