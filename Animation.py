import time, sys
from tkinter import *
import Equations as eq

root = Tk()
root.title("Animation")

canvas = Canvas(root, width=1024, height=720)
canvas.pack()
circle1 = canvas.create_oval(1,1, 10, 10, fill="red")
circle2 = canvas.create_oval(1,2,3,4, fill = "blue")

x_mov = 1
y_mov = 1
max_tm = 100
for i in range(10*max_tm):
    canvas.move(circle1, eq.movement_equation(0, 2, 0, max_tm)[i], eq.movement_equation(0, 0, 10, max_tm)[i])
    canvas.move(circle2, eq.movement_equation(0, 1, 100, max_tm)[i], eq.movement_equation(0, 10, 1, max_tm)[i])
    root.update()
    time.sleep(0.00001)

sys.exit()