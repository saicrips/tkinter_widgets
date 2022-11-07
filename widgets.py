import tkinter as tk
from tkinter import ttk

class Widgets(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.combobox_frame = tk.LabelFrame(self, text="Combobox")
        self.combobox_frame.grid(row=0, column=0, padx=10, pady=5)
        self.combobox_list = ["リスト1", "リスト2", "リスト3"]
        self.combobox = ttk.Combobox(self.combobox_frame, values=self.combobox_list)
        self.combobox.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        # 選択されたテキストまたは入力したテキストを取得する
        tk.Button(self.combobox_frame, text="取得", command=lambda: print(self.combobox.get())).grid(row=1, column=0, padx=10, pady=5)
        # Comboboxのリストを動的に追加する
        tk.Button(self.combobox_frame, text="追加", command=self.add_combobox_list).grid(row=1, column=1, padx=10, pady=5)
        # 選択された直後にアクションしたい場合に利用する
        self.combobox.bind('<<ComboboxSelected>>', lambda _: print(self.combobox.get()))
        
        self.spinbox_frame = tk.LabelFrame(self, text="Spinbox")
        self.spinbox_frame.grid(row=0, column=1, padx=10, pady=5)
        self.spinbox_list = ["リスト1", "リスト2", "リスト3"]
        self.spinbox = ttk.Spinbox(self.spinbox_frame, values=self.spinbox_list)
        self.spinbox.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        # 選択されたテキストまたは入力したテキストを取得する
        tk.Button(self.spinbox_frame, text="取得", command=lambda: print(self.spinbox.get())).grid(row=1, column=0, padx=10, pady=5)
        # Spinboxのリストを動的に追加する
        tk.Button(self.spinbox_frame, text="追加", command=self.add_spinbox_list).grid(row=1, column=1, padx=10, pady=5)
        
        self.notebook_frame = tk.LabelFrame(self, text="Notebook")
        self.notebook_frame.grid(row=0, column=2, padx=10, pady=5)
        self.notebook = ttk.Notebook(self.notebook_frame)
        self.note1 = tk.Label(self.notebook, text="note1")
        self.note1.pack(padx=10, pady=10)
        self.notebook.add(self.note1, text="note1")
        self.note2 = tk.Label(self.notebook, text="note2")
        self.note2.pack(padx=10, pady=10)
        self.notebook.add(self.note2, text="note2")
        self.note3 = tk.Label(self.notebook, text="note3")
        self.note3.pack(padx=10, pady=10)
        self.notebook.add(self.note3, text="note3")
        self.notebook.grid(row=0, column=2, padx=10, pady=5)
        
    def add_combobox_list(self):
        self.combobox_list.append("リスト" + str(len(self.combobox_list)+1))
        self.combobox['values'] = self.combobox_list
        
    def add_spinbox_list(self):
        self.spinbox_list.append("リスト" + str(len(self.spinbox_list)+1))
        self.spinbox['values'] = self.spinbox_list