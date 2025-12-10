import turtle

turt1 = turtle.Turtle()
turt2 = turtle.Turtle()
turt3 = turtle.Turtle()
turt_m = turtle.Turtle()
turt_n = turtle.Turtle()
turtle.tracer(0, 0)
points = []
camera = [0,0]
def draw_scale(i, zoom_amount):
    turt_n.penup()
    turt_n.pencolor("black")
    unit = ((i)/zoom_amount)
    str_unit = f"{unit:.2f}"
    if i % 50 == 0:  # every 5 grid
        # if i != 0:
        # y
        turt_n.pencolor("black")  # horizontal lines for each numbered grid
        turt_n.goto(-camera[0]*zoom_amount, i)
        turt_n.write(f"{(float(str_unit)+camera[1]):.2f}", align="right", font=("Courier", 7, "bold"))
        turt_n.pendown()
        turt_n.goto((-5/40-camera[0])*zoom_amount, i)
        turt_n.penup()
        # x
        turt_n.goto(i, (-15/40-camera[1])*zoom_amount)
        turt_n.write(f"{(float(str_unit)+camera[0]):.2f}", align="right", font=("Courier", 7, "bold"))
        turt_n.goto(i, -camera[1]*zoom_amount)
        turt_n.pendown()
        turt_n.goto(i, (-5/40-camera[1])*zoom_amount)
        turt_n.penup()
        # if i == 0:
        #     turt_n.goto((-5/40-camera[0])*zoom_amount, (-15/40-camera[1])*zoom_amount)
        #     turt_n.write(0, align="center", font=("Courier", 7, "bold"))
        #     turt_n.goto(i, -camera[1]*zoom_amount)
        #     turt_n.pendown()
        #     turt_n.goto(i, (-5/40-camera[1])*zoom_amount)
        #     turt_n.penup()
        #     turt_n.goto(-camera[0]*zoom_amount, i)
        #     turt_n.pendown()
        #     turt_n.goto((-5/40-camera[0])*zoom_amount, i)
        #     turt_n.penup()



graph_size_x = 1000
graph_size_y = 1000
grid_size = 1

def generate_grid():
    turt1.penup()
    turt1.pencolor("light grey")
    # generate grid
    for i in range(-graph_size_y, graph_size_y + grid_size, grid_size):
        turt1.penup()
        # verticals
        turt1.setpos((i-camera[0])*zoom_amount, -graph_size_y*zoom_amount)
        turt1.pendown()
        turt1.goto((i-camera[0])*zoom_amount, graph_size_y*zoom_amount)
        turt1.penup()

        # horizontal
        turt1.setpos(-graph_size_x*zoom_amount, (i-camera[1])*zoom_amount)
        turt1.pendown()
        turt1.goto(graph_size_x*zoom_amount, (i-camera[1])*zoom_amount)
        turt1.penup()

    turt1.pencolor("black")
    turt1.setpos(-graph_size_x*zoom_amount, -camera[1]*zoom_amount)
    turt1.pendown()
    turt1.goto(graph_size_x*zoom_amount, -camera[1]*zoom_amount)
    turt1.penup()
    turt1.goto(-camera[0]*zoom_amount, graph_size_y*zoom_amount)
    turt1.pendown()
    turt1.goto(-camera[0]*zoom_amount, -graph_size_y*zoom_amount)
    turt1.penup()


def draw_scale_graph():
    for i in range(-graph_size_y, graph_size_y + grid_size, grid_size):
        draw_scale(i, zoom_amount)


def gen_graph(points, zoom_amount):
    turt2.pencolor("red")
    turt2.penup()
    for point in points:
        if point is None:
            return
        if point[1] is None or (int(point[1]) > 200 or int(point[1] < -200)):    # this should fix tan(x)
            turt2.penup()
        else:
            if -200 < point[0] < 200: # why? well it's off-screen
                turt2.goto((point[0]-camera[0]) * zoom_amount, (point[1]-camera[1]) * zoom_amount)
                turt2.pendown()


zoom_amount = 40  # default zoom

def draw_squares(d_x, x, y):
    turt3.pencolor("blue")
    turt3.penup()
    turt3.goto(x, -camera[1] * zoom_amount)
    turt3.pendown()
    turt3.goto(x-d_x, -camera[1] * zoom_amount)
    turt3.goto(x-d_x, y)
    turt3.goto(x, y)
    turt3.goto(x, -camera[1] * zoom_amount)

riemann_called = False
# placeholder n, low_lim, up_lim:
pl_n = 0
pl_ll = 0
pl_ul = 0

def riemann_sum(n, low_lim, up_lim):
    global riemann_called
    # Calculate the real length
    real_len = 0
    for i in range(len(points)):
        if points[i] is not None:
            real_len += 1
    start_point = int(real_len / 2)
    area = 0
    d_x = (up_lim-low_lim) / n
    d_x_raw = (up_lim-low_lim) / n  # for area calculation, more accurate
    d_x *= zoom_amount
    low_lim *= 100  # scaling from the 0.01 steps
    up_lim *= 100
    for i in range(1, 1 + 2*n):  # the 2*n serves to increase accuracy
        x_cor = int(start_point + low_lim + ((d_x * 100/zoom_amount) * i))
        if (points[x_cor] is not None and points[x_cor][1] is not None
                and points[x_cor][0] <= up_lim/100):
            turt3.penup()
            turt3.goto((points[x_cor][0] - camera[0]) * zoom_amount,
                        (points[x_cor][1] - camera[1]) * zoom_amount)

            draw_squares(d_x, (points[x_cor][0] - camera[0]) * zoom_amount,
                         (points[x_cor][1] - camera[1]) * zoom_amount)
            area += d_x_raw * (points[x_cor][1])
    return area

def redraw():
    global riemann_called, pl_n, pl_ll, pl_ul
    turt1.clear()
    turt2.clear()
    turt3.clear()
    turt_n.clear()
    generate_grid()
    gen_graph(points, zoom_amount)
    draw_scale_graph()
    if riemann_called:
        riemann_sum(pl_n, pl_ll, pl_ul)
    turtle.update()

def zoom(z):
    global zoom_amount
    if z > 0:
        zoom_amount += 1
    else:
        zoom_amount -= 1
    redraw()


def on_scroll(event):
    if event.delta > 0:
        zoom(1)
    elif event.delta < 0 and zoom_amount > 10:  # max zoom out = 10
        zoom(-1)


def on_up():
    camera[1] += 1.25*40/zoom_amount
    redraw()

def on_down():
    camera[1] -= 1.25*40/zoom_amount
    redraw()

def on_left():
    camera[0] -= 1.25*40/zoom_amount
    redraw()

def on_right():
    camera[0] += 1.25*40/zoom_amount
    redraw()

# hide cursor
turt1.ht()
turt2.ht()
turt3.ht()
turt_m.ht()
turt_n.ht()


def starting_graph():
    generate_grid()
    draw_scale_graph()


canvas = turtle.getcanvas()
screen = turtle.TurtleScreen(canvas)
canvas.bind("<MouseWheel>", on_scroll)
screen.onkey(on_up, "Up")
screen.onkey(on_down, "Down")
screen.onkey(on_left, "Left")
screen.onkey(on_right, "Right")
screen.listen()
turtle.update()
