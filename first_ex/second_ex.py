import random
from tkinter import *

colours = ["blue", "red", "orange", "yellow", "green", ]
tk = Tk()
canvas = Canvas(tk, height=500, width=500)
canvas.pack()
for i in range(5):
    start_point = random.randint(0, 500)
    second_start_point = random.randint(100, 200)
    second_point = random.randint(100, 500)
    third_point = random.randint(100, 500)
    color = colours[i]
    canvas.create_polygon(start_point, second_start_point, second_point, third_point, third_point + 30, second_point + 10, fill=color)
    tk.update()

tk.mainloop()
