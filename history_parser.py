parsed_list = ["Empty"] * 10
j = 0
def write_into(fx):
    with open("graph_history.txt", "a") as f:
        f.write(f"{fx}\n")


def split_manually(line):
    splitted = ""
    for i in line:
        if i != "\n":
            splitted += i
    return splitted


def read_from():
    i = 0
    with open("graph_history.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if i < len(parsed_list):
                parsed_list[i] = split_manually(line)
                i += 1
    return parsed_list

def check_and_write(fx):
    write_into(fx)
    with open("graph_history.txt", "w"):
        update_elements(parsed_list)
        parsed_list[0] = fx
    for lines in parsed_list:
        if lines != "":
            write_into(lines)


def update_elements(fx):    # move each element to the right
    for i in range(9, 0, -1):  # parsed list len - 1
        fx[i] = fx[i-1]
