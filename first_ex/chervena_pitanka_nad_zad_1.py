import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, height=200, width=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for _ in range(60):
    canvas.move(1, 5, 2)
    tk.update()
    time.sleep(0.1)

for _ in range(60):
    canvas.move(1, -5, -2)
    tk.update()
    time.sleep(0.1)
