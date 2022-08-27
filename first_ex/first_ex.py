import random
from tkinter import *

tk = Tk()
canvas = Canvas(tk, height=750, width=750)
canvas.pack()
for _ in range(60):
    start_point = random.randint(0, 250)
    width = random.randint(0, 750)
    height = random.randint(0, 750)
    canvas.create_rectangle(start_point, start_point, height, width)
    tk.update()

tk.mainloop()
