import tkinter as tk
from tkinter import scrolledtext
import threading
import time

class Technique(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.handling_data_between_classes = HandlingDataBetweenClasses(self)
        self.handling_data_between_classes.pack()
        
        self.watching_text_editor = WatchingTextEditor(self)
        self.watching_text_editor.pack()

class HandlingDataBetweenClasses(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Handling data between classes")
        
        # クラス間共通の変数を用意
        props = {}
        class1 = Class1(self, props, text="Class1")
        class1.grid(row=0, column=0, padx=10, pady=5)
        class2 = Class2(self, props, text="Class2")
        class2.grid(row=0, column=1, padx=10, pady=5)
        # Class1のwidgetで実行したい関数をClass2から渡す
        class1.button['command'] = class2.set_label
        
class Class1(tk.LabelFrame):
    def __init__(self, master, props: dict, *args, **kargs):
        super().__init__(master, *args, **kargs)
        
        props['var1'] = tk.StringVar()
        props['var2'] = tk.StringVar()
        props['var3'] = tk.StringVar()
        self.entry1 = tk.Entry(self, textvariable=props['var1'])
        self.entry1.pack(padx=10, pady=5)
        self.entry2 = tk.Entry(self, textvariable=props['var2'])
        self.entry2.pack(padx=10, pady=5)
        self.entry3 = tk.Entry(self, textvariable=props['var3'])
        self.entry3.pack(padx=10, pady=5)
        self.button = tk.Button(self, text="OK")
        self.button.pack(padx=10, pady=5)
        
class Class2(tk.LabelFrame):
    def __init__(self, master, props: dict, *args, **kargs):
        super().__init__(master, *args, **kargs)
        
        self.props = props
        
        self.label1 = tk.Label(self, text='', width=20)
        self.label1.pack()
        self.label2 = tk.Label(self, text='', width=20)
        self.label2.pack()
        self.label3 = tk.Label(self, text='', width=20)
        self.label3.pack()
        
    def set_label(self):
        self.label1['text'] = self.props['var1'].get()
        self.label2['text'] = self.props['var2'].get()
        self.label3['text'] = self.props['var3'].get()
        
class WatchingTextEditor(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Watching Text Editor")
        
        props = {}
        
        self.text_editor = TextEditor(self, props, text="Editor")
        self.text_editor.grid(row=0, column=0, padx=5, pady=5)
        self.text_viewer = TextViewer(self, props, text="Preview")
        self.text_viewer.grid(row=0, column=1, padx=5, pady=5)
        
class TextEditor(tk.LabelFrame):
    def __init__(self, master, props, *args, **kargs):
        super().__init__(master, *args, **kargs)
        
        self.props = props
        
        self.text = tk.Text(self, width=50)
        self.text.pack(padx=5, pady=5)
        
        self.watch_text = threading.Thread(target=self.watch_text_thread)
        self.watch_text.setDaemon(True)
        self.watch_text.start()
        
        self.props['contents'] = self.text.get('0.0', tk.END).strip()
    
    def __del__(self):
        self.running = False
        
    def watch_text_thread(self):
        old_text = ""
        self.running = True
        while self.running:
            text = self.text.get('0.0', tk.END).strip()
            if old_text != text:
                self.master.event_generate('<<TextEditorChanged>>', when='tail')
            old_text = text
            self.props['contents'] = text
            time.sleep(0.1)

class TextViewer(tk.LabelFrame):
    def __init__(self, master, props: dict, *args, **kargs):
        super().__init__(master, *args, **kargs)
        
        self.props = props
        
        self.text_viewer = tk.Label(self, text='', width=50, height=21, wraplength=350, anchor=tk.N+tk.W, justify=tk.LEFT)
        self.text_viewer.pack(padx=5, pady=5)
        
        self.master.bind('<<TextEditorChanged>>', lambda _: self.set_label())
        
    def set_label(self):
        self.text_viewer['text'] = self.props['contents']