import tkinter as tk
from tkinter import scrolledtext
import threading
import time

class Technique(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.handling_data_between_classes = HandlingDataBetweenClasses(self)
        self.handling_data_between_classes.pack()
        
        self.handling_data_between_classes_event_generate = HandlingDataBetweenClassesWithEventGenerate(self)
        self.handling_data_between_classes_event_generate.pack()
        
        self.watching_text_editor = WatchingTextEditor(self)
        self.watching_text_editor.pack()

class HandlingDataBetweenClasses(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Handling data between classes")
        
        # クラス間共通の変数を用意
        props = {}
        editor1 = Editor1(self, props, text="Editor1")
        editor1.grid(row=0, column=0, padx=10, pady=5)
        viewer1 = Viewer1(self, props, text="Viewer1")
        viewer1.grid(row=0, column=1, padx=10, pady=5)
        # Editor1のwidgetで実行したい関数をViewer1から渡す
        editor1.button['command'] = viewer1.set_label
        
class Editor1(tk.LabelFrame):
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
        
class Viewer1(tk.LabelFrame):
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
        
class HandlingDataBetweenClassesWithEventGenerate(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Handling data between classes with event generation")
        
        # クラス間共通の変数を用意
        props = {}
        editor1 = Editor2(self, props, text="Editor2")
        editor1.grid(row=0, column=0, padx=10, pady=5)
        viewer2 = Viewer2(self, props, text="Viewer2")
        viewer2.grid(row=0, column=1, padx=10, pady=5)
        
class Editor2(tk.LabelFrame):
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
        self.button = tk.Button(self, 
                                text="OK", 
                                command=lambda: self.master.event_generate('<<Editor2Button>>'))
        self.button.pack(padx=10, pady=5)
        
class Viewer2(tk.LabelFrame):
    def __init__(self, master, props: dict, *args, **kargs):
        super().__init__(master, *args, **kargs)
        
        self.props = props
        
        self.label1 = tk.Label(self, text='', width=20)
        self.label1.pack()
        self.label2 = tk.Label(self, text='', width=20)
        self.label2.pack()
        self.label3 = tk.Label(self, text='', width=20)
        self.label3.pack()
        
        self.master.bind('<<Editor2Button>>', lambda _: self.set_label())
        
    def set_label(self):
        self.label1['text'] = self.props['var1'].get()
        self.label2['text'] = self.props['var2'].get()
        self.label3['text'] = self.props['var3'].get()
        
class Technique2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.watching_text_editor = WatchingTextEditor(self)
        self.watching_text_editor.pack()

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