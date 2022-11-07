import tkinter as tk

class Technique(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.handling_data_between_classes = tk.LabelFrame(self, text="Handling data between classes")
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