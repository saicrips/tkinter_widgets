import tkinter as tk

class Canvas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(self, width=800, height=600, bg="cyan")

        self.canvas.create_rectangle(0, 0, 800, 450, fill='green')
        self.canvas.create_oval(10, 10, 140, 140, tag="oval")

        self.canvas.pack()
        

class Canvas2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(self, width=800, height=600, bg="cyan")

        x, y = 50, 50
        width = 200
        height = 150
        arrow_length = 50
        margin = 10
        rectangle_width = width - arrow_length
        arrow1, text1 = create_rectangle_arrow(self.canvas, 
                                               x, y, width, height, arrow_length, 
                                               text="Plan", font=('Helvetica', 24), fg="cyan" ,fill='#1F27EB')
        arrow2, text2 = create_rectangle_arrow(self.canvas,
                                               x + rectangle_width + margin, y, width, height, arrow_length, dent=True, 
                                               text="Do", font=('Helvetica', 24), fg="cyan", fill='#1469CF')
        arrow3, text3 = create_rectangle_arrow(self.canvas,
                                               x + (rectangle_width + margin)*2, y, width, height, arrow_length, dent=True, 
                                               text="Check", font=('Helvetica', 24), fg="cyan", fill='#00BFA9')
        arrow4, text4 = create_rectangle_arrow(self.canvas,
                                               x + (rectangle_width + margin)*3, y, width, height, arrow_length, dent=True, 
                                               text="Action", font=('Helvetica', 24), fg="cyan", fill='#00E496')
        
        self.canvas.tag_bind(arrow1, '<Button-1>', lambda _: print("clicked arrow1"))
        self.canvas.tag_bind(text1, '<Button-1>', lambda _: print("clicked arrow1"))
        self.canvas.tag_bind(arrow2, '<Button-1>', lambda _: print("clicked arrow2"))
        self.canvas.tag_bind(text2, '<Button-1>', lambda _: print("clicked arrow2"))
        self.canvas.tag_bind(arrow3, '<Button-1>', lambda _: print("clicked arrow3"))
        self.canvas.tag_bind(text3, '<Button-1>', lambda _: print("clicked arrow3"))
        self.canvas.tag_bind(arrow4, '<Button-1>', lambda _: print("clicked arrow4"))
        self.canvas.tag_bind(text4, '<Button-1>', lambda _: print("clicked arrow4"))
        
        self.canvas.pack(side = tk.TOP, anchor = tk.NW, padx = 10, pady = 10)
        
def create_rectangle_arrow(canvas: tk.Canvas, 
                            x, y, # 左上の座標
                            width, height, # 全体の幅と高さ
                            arrow_length, # 三角形部分の長さ
                            dent: bool=False, # arrow_lengthで指定した分だけ、凹ます
                            text="",
                            font="",
                            fg="",
                            **kwargs):
    
    rectangle_width = width - arrow_length
    
    if dent:
        arrow_id = canvas.create_polygon(x, y, 
                                         x + rectangle_width, y, 
                                         x + width, y + height/2, 
                                         x + rectangle_width, y + height,
                                         x, y + height,
                                         x + arrow_length, y + height/2,
                                         **kwargs)
    else:
        arrow_id = canvas.create_polygon(x, y, 
                                         x + rectangle_width, y, 
                                         x + width, y + height/2, 
                                         x + rectangle_width, y + height, 
                                         x, y + height,
                                         **kwargs)
    
    if dent:
        text_x = x+rectangle_width/2+arrow_length/2
    else:
        text_x = x+rectangle_width/2            
    text_y = y+height/2
    text_id = canvas.create_text(text_x, text_y, text=text, font=font, fill=fg)
        
    return arrow_id, text_id