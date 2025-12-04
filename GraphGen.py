from FuncParser import points
import tkinter
import turtle


turt1 = turtle.Turtle()
turt1.penup()
turtle.tracer(0)

def generate_grid():
    graph_size_x = 1000
    graph_size_y = 1000
    grid_size = 10
    turt1.speed(0)
    turt1.penup()
    turt1.pencolor("light grey")
    # generate grid
    for i in range(-graph_size_y, graph_size_y + grid_size, grid_size):
        turt1.penup()
        # verticals
        turt1.setpos(i, -graph_size_y)
        turt1.pendown()
        turt1.goto(i, graph_size_y)
        turt1.penup()

        # horizontal
        turt1.setpos(-graph_size_x, i)
        turt1.pendown()
        turt1.goto(graph_size_x, i)
        turt1.penup()

    turt1.pencolor("black")
    turt1.setpos(-graph_size_x, 0)
    turt1.pendown()
    turt1.goto(graph_size_x, 0)
    turt1.penup()
    turt1.goto(0, graph_size_y)
    turt1.pendown()
    turt1.goto(0, -graph_size_y)
    turt1.penup()


turt2 = turtle.Turtle()
turt2.pencolor("red")


def gen_graph(points, zoom_amount):
    turt2.penup()
    for point in points:
        if point[1] is None or (point[1] > 200 or point[1] < -200):
            turt2.penup()
        else:
            if -200 < point[0] < 200: # why? well it's off-screen
                turt2.goto(point[0] * zoom_amount, point[1] * zoom_amount)
                turt2.pendown()


zoom_amount = 40 #40    # default zoom
turt3 = turtle.Turtle()

def draw_squares(d_x, y):
    turt3.penup()
    for i in range(1, 5):
        turt3.pendown()
        if i > 0:
            turt3.right(90)
        if i % 2 == 0:
            turt3.forward(d_x)
        elif i % 2 != 0:
            turt3.forward(y * zoom_amount)


start_point = int(len(points) / 2)


def riemann_sum(n, low_lim, up_lim):
    ctr = 0
    d_x = (up_lim-low_lim) / n
    d_x *= zoom_amount
    d_x = int(d_x)
    low_lim *= 100  # scaling from the 0.01 steps
    up_lim *= 100
    for i in range(1, 1 + n):
        x_cor = start_point + low_lim + int(d_x * 100/zoom_amount) * i
        turt3.penup()
        turt3.goto(points[x_cor][0] * zoom_amount, points[x_cor][1] * zoom_amount)
        draw_squares(d_x, points[x_cor][1])
        ctr += 1


def zoom(z):
    global zoom_amount
    if z > 0:
        zoom_amount += 1
    else:
        zoom_amount -= 1
    turt2.clear()
    gen_graph(points, zoom_amount)
    turt2.screen.update()


def on_scroll(event):
    if event.delta > 0:
        zoom(1)
    elif event.delta < 0 and zoom_amount > 10:  # max zoom out = 10
        zoom(-1)


generate_grid()
gen_graph(points, zoom_amount)
canvas = turtle.getcanvas()
canvas.bind("<MouseWheel>", on_scroll)

root = tkinter.Tk()



turtle.update()
turtle.mainloop()


