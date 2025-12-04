import tkinter
import turtle
from GraphGen import gen_graph, zoom_amount, zoom
root = tkinter.Tk()


def on_scroll(event):
    if event.delta > 0:
        zoom(1)
    elif event.delta < 0 and zoom_amount > 10:  # max zoom out = 10
        zoom(-1)


canvas = turtle.getcanvas()
canvas.bind("<MouseWheel>", on_scroll)

turtle.update()
turtle.mainloop()

