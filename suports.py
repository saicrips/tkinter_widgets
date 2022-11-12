import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, simpledialog, scrolledtext

class Suports(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.colorchooser_frame = tk.LabelFrame(self, text="colorchooser")
        tk.Button(self.colorchooser_frame, text="colorchooser", command=self.colorchooser).grid(row=0, column=0, padx=10, pady=10)
        self.colorchooser_label = tk.Label(self.colorchooser_frame, text="")
        self.colorchooser_label.grid(row=1, column=0, padx=10, pady=10)
        self.colorchooser_frame.grid(row=0, column=0, padx=10, pady=5)
        
        self.fileopen_frame = tk.LabelFrame(self, text="File/Directory Open")
        tk.Button(self.fileopen_frame, text="askopenfile", command=lambda: print(filedialog.askopenfile())).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.fileopen_frame, text="askopenfiles", command=lambda: print(filedialog.askopenfiles())).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.fileopen_frame, text="asksaveasfile", command=lambda: print(filedialog.asksaveasfile())).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(self.fileopen_frame, text="askopenfilename", command=lambda: print(filedialog.askopenfilename())).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.fileopen_frame, text="askopenfilenames", command=lambda: print(filedialog.askopenfilenames())).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.fileopen_frame, text="asksaveasfilename", command=lambda: print(filedialog.asksaveasfilename())).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self.fileopen_frame, text="askdirectory", command=lambda: print(filedialog.askdirectory())).grid(row=2, column=1, padx=10, pady=5)
        self.fileopen_frame.grid(row=0, column=1, padx=10, pady=5)
        
        self.font_frame = tk.LabelFrame(self, text="font")
        tk.Label(self.font_frame, text="あいうえお(Times)", font=("Times", 10)).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(ＭＳ明朝)", font=("ＭＳ明朝", 10)).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(Helvetiva)", font=("Helvetiva", 10)).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(ＭＳゴシック)", font=("ＭＳゴシック", 10)).grid(row=1, column=1, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(Courier)", font=("Courier", 10)).grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(Times New s)", font=("Times New s", 10)).grid(row=2, column=1, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(Times bold)", font=("Times", 10, "bold")).grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(Times ovferstrike)", font=("Times", 10, "overstrike")).grid(row=3, column=1, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(Times italic)", font=("Times", 10, "italic")).grid(row=4, column=0, padx=10, pady=5)
        tk.Label(self.font_frame, text="あいうえお(Times underline)", font=("Times", 10, "underline")).grid(row=4, column=1, padx=10, pady=5)
        self.font_frame.grid(row=1, column=0, padx=10, pady=5, rowspan=2)
        
        self.messagebox_frame = tk.LabelFrame(self, text="Message Box")
        tk.Button(self.messagebox_frame, text="showinfo", command=lambda: print(messagebox.showinfo(title="info", message="showinfo"))).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.messagebox_frame, text="showwarning", command=lambda: print(messagebox.showwarning(title="warning", message="showwarning"))).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.messagebox_frame, text="showerror", command=lambda: print(messagebox.showerror(title="error", message="showerror"))).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(self.messagebox_frame, text="askquestion", command=lambda: print(messagebox.askquestion(title="question", message="askquestion"))).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.messagebox_frame, text="askokcancel", command=lambda: print(messagebox.askokcancel(title="okcancel", message="askokcancel"))).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.messagebox_frame, text="askretrycancel", command=lambda: print(messagebox.askretrycancel(title="retrycancel", message="askretrycancel"))).grid(row=1, column=2, padx=10, pady=5)
        tk.Button(self.messagebox_frame, text="askyesno", command=lambda: print(messagebox.askyesno(title="yesno", message="askyesno"))).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self.messagebox_frame, text="askyesnocancel", command=lambda: print(messagebox.askyesnocancel(title="yesnocancel", message="askyesnocancel"))).grid(row=2, column=1, padx=10, pady=5)
        self.messagebox_frame.grid(row=1, column=1, padx=10, pady=5)
        
        self.simpledialog_frame = tk.LabelFrame(self, text="Simple Dialog")
        tk.Button(self.simpledialog_frame, text="askfloat", command=lambda: print(simpledialog.askfloat(title="float", prompt="Plese input float"))).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.simpledialog_frame, text="askinteger", command=lambda: print(simpledialog.askinteger(title="integer", prompt="Please input integer"))).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.simpledialog_frame, text="askstring", command=lambda: print(simpledialog.askstring(title="string", prompt="Please input string"))).grid(row=0, column=2, padx=10, pady=5)
        self.simpledialog_frame.grid(row=2, column=1, padx=10, pady=5)
        
        self.scrolledtext_frame = tk.LabelFrame(self, text="Scrolled Text")
        self.scrolledtext = scrolledtext.ScrolledText(self.scrolledtext_frame, height=10)
        self.scrolledtext.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
        self.copy_text_button = tk.Button(self.scrolledtext_frame, text="コピー", command=self.copy_text)
        self.copy_text_button.grid(row=1, column=0, padx=10, pady=5)
        self.paste_text_button = tk.Button(self.scrolledtext_frame, text="ペースト", command=self.paste_text)
        self.paste_text_button.grid(row=1, column=1, padx=10, pady=5)
        self.clear_text_button = tk.Button(self.scrolledtext_frame, text="クリア", command=self.clear_text)
        self.clear_text_button.grid(row=1, column=2, padx=10, pady=5)
        self.scrolledtext_frame.grid(row=3, column=0, padx=10, pady=5, columnspan=2)
        
    def colorchooser(self):
        color = colorchooser.askcolor()
        self.colorchooser_label['text'] = color
        self.colorchooser_label['background'] = color[1]
        
    def copy_text(self):
        text = self.scrolledtext.get('0.0', tk.END).strip()
        print(text)
        self.master.clipboard_append(text)
        
    def paste_text(self):
        try:
            text = self.master.clipboard_get().strip()
        except:
            return
        print(text)
        self.scrolledtext.insert(tk.INSERT, text)
        
    def clear_text(self):
        self.scrolledtext.delete('0.0', tk.END)
        