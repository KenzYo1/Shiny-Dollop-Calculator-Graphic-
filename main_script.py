import tkinter
import turtle
import GraphGen
import FuncParser
import json_parser

canvas = turtle.getcanvas()
root = canvas.master
OPTIONS = ["aaa", "AAAA"]

# Main stuff
title = tkinter.Label(root, text="Shiny Dollop Graphic Calculator", font="Arial, 16")
title.pack(before=canvas)

main_frame = tkinter.Frame(root, width=300)
main_frame.pack(after=canvas, side="left", fill="both", padx=10)

# Riemann
r_sum_btn = tkinter.Button(main_frame, text="Riemann Sum", font="Arial, 12",
                           width=15)
r_sum_btn.grid(row=1, column=0, sticky="W")

# History
history_btn = tkinter.Button(main_frame, text="History", font="Arial, 12")

fx_input = tkinter.Entry(main_frame, font="Arial, 12")
fx_input.grid(row=0, column=2)


def gen_riemann(n, l_lim, u_lim, area_label):
    n = int(n)
    l_lim = float(l_lim)
    u_lim = float(u_lim)
    GraphGen.turt3.clear()
    area = GraphGen.riemann_sum(n, l_lim, u_lim)
    if u_lim < l_lim:
        area *= -1
    area_label.config(text=f"Area = {area:.4f}")
    GraphGen.turt3.screen.update()

# Riemann Entries
popped_up = False
r_s_popup = None

def riemann_popup():
    global popped_up, r_s_popup
    if popped_up:
        r_s_popup.destroy()
        popped_up = False
        return
    else:
        r_s_popup = tkinter.Toplevel(main_frame)
    r_s_popup.overrideredirect(True)
    r_s_popup.attributes('-topmost', True)

    input_frame = tkinter.Frame(r_s_popup, bd=3, relief="sunken")
    input_frame.pack()

    r_s_popup_x = main_frame.winfo_x() + r_sum_btn.winfo_x()
    r_s_popup_y = main_frame.winfo_y() + r_sum_btn.winfo_y()
    r_s_popup.geometry(f"{190}x{200}+{r_s_popup_x+125}+{r_s_popup_y-50}")
    # n
    n_txt = tkinter.Label(input_frame, text="n (amout of subdivisions)",
                          font="Arial, 12")
    n_entry = tkinter.Entry(input_frame, font="Arial, 12")
    n_txt.grid(row=1, column=0)
    n_entry.grid(row=2, column=0)

    # lower limit
    low_lim_txt = tkinter.Label(input_frame, text="lower limit",
                                font="Arial, 12")
    low_lim_entry = tkinter.Entry(input_frame, font="Arial, 12")
    low_lim_txt.grid(row=3, column=0)
    low_lim_entry.grid(row=4, column=0)

    # upper limit
    upper_lim_txt = tkinter.Label(input_frame, text="upper limit",
                                  font="Arial, 12")
    upper_lim_entry = tkinter.Entry(input_frame, font="Arial, 12")
    upper_lim_txt.grid(row=5, column=0)
    upper_lim_entry.grid(row=6, column=0)
    popped_up = True

    r_gen_btn = tkinter.Button(input_frame, font="Arial, 12", text=
                               "Generate!", command=lambda: gen_riemann(n_entry.get(),
                                low_lim_entry.get(), upper_lim_entry.get(), area_label))
    r_gen_btn.grid(row=7, padx=50)
    area_label = tkinter.Label(input_frame, font="Arial, 12", text="Area = 0")
    area_label.grid(row=8, column=0, padx=50)

def run():
    GraphGen.turt2.clear()
    GraphGen.turt3.clear()
    fx = FuncParser.parse(list(fx_input.get()))
    GraphGen.points = fx
    GraphGen.gen_graph(fx, GraphGen.zoom_amount)
    GraphGen.turt2.screen.update()
    if len(fx) > 1000:  # length of the whole (x, y) cords should be more than 1k
        json_parser.abc(fx_input.get())


r_sum_btn.config(command=riemann_popup)
run_btn = tkinter.Button(main_frame, text="Generate Graph", font="Arial, 12",
                         width=15, command=run)

run_btn.grid(row=0, column=0, columnspan=2, sticky="W")


GraphGen.starting_graph()
var = tkinter.StringVar(root)
root.mainloop()