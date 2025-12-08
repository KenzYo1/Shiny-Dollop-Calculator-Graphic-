from FuncParser import points
import turtle

camera = [0,0]
turt1 = turtle.Turtle()
turt_n = turtle.Turtle()
turt1.penup()
turt_n.penup()
turt_n.pencolor("black")
turtle.tracer(0, 0)


def draw_scale(grid_size, i, zoom_amount):
    unit = (i/zoom_amount)  # /10 to make up for grid size = 10
    str_unit = f"{unit:.2f}"
    if i % 50 == 0:  # every 5 grid
        if i != 0:
            # y
            turt_n.pencolor("black")  # horizontal lines for each numbered grid
            turt_n.goto(0, i)
            turt_n.write(str_unit, align="right", font=("Courier", 7, "bold"))
            turt_n.pendown()
            turt_n.goto(-5, i)
            turt_n.penup()
            # x
            turt_n.goto(i, -15)
            turt_n.write(str_unit, align="right", font=("Courier", 7, "bold"))
            turt_n.goto(i, 0)
            turt_n.pendown()
            turt_n.goto(i, -5)
            turt_n.penup()
        if i == 0:
            turt_n.goto(-5, -15)
            turt_n.write(0, align="center", font=("Courier", 7, "bold"))


graph_size_x = 1000
graph_size_y = 1000
grid_size = 10

def generate_grid():
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

def draw_scale_graph():
    for i in range(-graph_size_y, graph_size_y + grid_size, grid_size):
        draw_scale(grid_size, i, zoom_amount)

def gen_graph(points, zoom_amount, camera):
    print(camera)
    turt2.penup()
    for point in points:
        if point is None:
            return
        if point[1] is None or (point[1] > 200 or point[1] < -200):    # this should fix tan(x)
            turt2.penup()
        else:
            if -200 < point[0] < 200: # why? well it's off-screen
                turt2.goto((point[0]-camera[0]) * zoom_amount, (point[1]-camera[0]) * zoom_amount)
                turt2.pendown()


zoom_amount = 40 #40    # default zoom
turt3 = turtle.Turtle()
turt3.pencolor("blue")


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

real_len = 0
for i in range(len(points)):
    if points[i] is not None:
        real_len += 1

start_point = int(real_len / 2)
def riemann_sum(n, low_lim, up_lim):
    d_x = (up_lim-low_lim) / n
    d_x *= zoom_amount
    d_x = int(d_x)
    low_lim *= 100  # scaling from the 0.01 steps
    up_lim *= 100
    for i in range(1, 1 + n):
        x_cor = start_point + low_lim + (int(d_x * 100/zoom_amount) * i)
        if points[x_cor][1] is not None:
            turt3.penup()
            turt3.goto(points[x_cor][0] * zoom_amount, points[x_cor][1] * zoom_amount)
            draw_squares(d_x, points[x_cor][1])


def zoom(z):
    global zoom_amount
    if z > 0:
        zoom_amount += 1
    else:
        zoom_amount -= 1
    turt_n.clear()
    turt2.clear()
    gen_graph(points, zoom_amount, camera)
    draw_scale_graph()
    turt2.screen.update()
    turt_n.screen.update()


def on_scroll(event):
    if event.delta > 0:
        zoom(1)
    elif event.delta < 0 and zoom_amount > 10:  # max zoom out = 10
        zoom(-1)

def on_left(event):
    camera[0] -= 100

def on_right(event):
    camera[0] += 100

def on_up(event):
    camera[1] += 100

def on_down(event):
    camera[1] -= 100

# hide cursor
turt1.ht()
turt2.ht()
turt3.ht()
turt_n.ht()
turtle.delay(0)
draw_scale_graph()
generate_grid()
gen_graph(points, zoom_amount, camera)


canvas = turtle.getcanvas()
canvas.bind("<MouseWheel>", on_scroll)
canvas.bind("<Left>", on_left)
canvas.bind("<Right>", on_right)
canvas.bind("<Up>", on_up)
canvas.bind("<Down>", on_down)
canvas.focus_set()
turtle.update()
turtle.mainloop()


