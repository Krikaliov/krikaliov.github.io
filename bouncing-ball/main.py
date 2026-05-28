import tkinter as tk

from time import time

class Ball(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.fps:int = 50
        self.tick_rate:int = int(1000 / self.fps)
        
        self.env_g:int = 1
        self.rolling:bool = False
        self.restitution:float = 0.8
        
        # Make Window headless
        self.overrideredirect(True)
        
        self.inner_image = tk.PhotoImage(file="image.png")
        tk.Label(self, image=self.inner_image, bg='green').pack()
        
        self.w:int = self.inner_image.width()
        self.h:int = self.inner_image.height()
        
        self.p_x:int = 0
        self.p_y:int = 0
        
        self.v_x:int = 0
        self.v_y:int = 0
        
        self.move(int(self.parent_w() / 2), int(self.parent_h() / 2))
        
        self.bind("<ButtonPress-1>", self.drag_init)
        self.bind("<ButtonRelease-1>", self.drag_stop)
        self.bind("<B1-Motion>", self.drag)
        
        self.config(cursor="hand2")
        self.resizable(False, False)
        self.attributes('-topmost', 1)
        self.wm_attributes("-transparentcolor", "green")
        
        self.dragging:bool = False
        self.after(self.tick_rate, self.tick)
    
    def parent_w(self) -> int:
        return self.winfo_screenwidth()
    def parent_h(self) -> int:
        return self.winfo_screenheight()
    
    def move(self, dx:int, dy:int):
        self.p_x += dx
        self.p_y += dy
        self.geometry(f"+{self.p_x - int(self.w / 2)}+{self.p_y - int(self.h / 2)}")
    
    def drag_init(self, event):
        self.dragging:bool = True
        self.config(cursor="fleur")
        self.move(event.x_root - self.p_x, event.y_root - self.p_y)
    
    def drag_stop(self, event):
        self.dragging:bool = False
        self.config(cursor="hand2")
    
    def drag(self, event):
        self.v_x = event.x_root - self.p_x
        self.v_y = event.y_root - self.p_y
        self.move(self.v_x, self.v_y)
    
    def tick(self):
        start:int = int(time() * 1000)
        if not(self.dragging):
            screen_h:int = self.parent_h()
            screen_w:int = self.parent_w()
            # Bottom collision
            if self.p_y + int(self.h / 2) >= screen_h and not(self.rolling):
                self.p_y = screen_h - int(self.h / 2)
                self.v_y = -int(self.v_y * self.restitution)
            else:
                self.v_y += self.env_g
            # Side collision
            if self.p_x <= int(self.w / 2) or self.p_x + int(self.w / 2) >= screen_w:
                self.v_x = -int(self.v_x * self.restitution)
                self.v_y = int(self.v_y * self.restitution)
            self.move(self.v_x, self.v_y)
        end:int = int(time() * 1000)
        self.after(self.tick_rate - (start - end), self.tick)

if __name__ == "__main__":
    ball:Ball = Ball()
    ball.mainloop()
