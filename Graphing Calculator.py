import turtle

def can_be_number(item):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if item[0] in numbers:
        return True
    return False

def combine_numbers(fx):
    i = 0
    while i < len(fx)-1:
        if can_be_number(fx[i]) and can_be_number(fx[i+1]):
            fx[i] += fx.pop(i+1)
            i = 0
        i += 1
    return fx

def convert_commas(fx):
    for i in range(len(fx)):
        if fx[i] == ",":
            fx[i] = "."
    return fx

def combine_decimals(fx):
    i = 0
    while i < len(fx)-1:
        if fx[i] == ".":
            fx[i-1] += fx.pop(i)
            fx[i-1] += fx.pop(i)
            i = 0
        i += 1
    return fx

def convert_mult_shorthand(fx):
    i = 0
    while i < len(fx)-1:
        if ((can_be_number(fx[i]) or fx[i] == "x") and (fx[i+1] == "x" or fx[i+1] == "(")) or ((can_be_number(fx[i+1]) or fx[i+1] == "x") and (fx[i] == "x" or fx[i] == ")")):
            fx.insert(i+1, "*")
            i = 0
        i += 1

def convert_to_numbers(fx):
    for i in range(len(fx)):
        if can_be_number(fx[i]):
            fx[i] = float(fx[i])
    return fx

def insert_x(fx, x):
    for i in range(len(fx)):
        if fx[i] == "x":
            fx[i] = x
    return fx

def check_brackets(fx):
    for i in range(len(fx)):
        if fx[i] == "(":
            return True
    return False

def check_powers(fx):
    for i in range(len(fx)):
        if fx[i] == "^":
            return True
    return False

def check_multiplication_division(fx):
    for i in range(len(fx)):
        if fx[i] == "*" or fx[i] == "/":
            return True
    return False

def calculate(fx):
    i = 0
    has_brackets = check_brackets(fx)
    has_powers = check_powers(fx)
    has_multiplication_division = check_multiplication_division(fx)
    while i < len(fx):
        if fx[i] == "(":
            fx.pop(i)
            fx2 = []
            while fx[i] != ")":
                fx2.append(fx.pop(i))
            fx[i] = calculate(fx2)
            has_brackets = check_brackets(fx)
            i = 0
        elif fx[i] == "^" and not has_brackets:
            fx[i-1] = fx[i-1] ** fx[i+1]
            if isinstance(fx[i-1], complex):
                return None
            fx.pop(i)
            fx.pop(i)
            has_powers = check_powers(fx)
            i = 0
        elif fx[i] == "*" and not has_powers and not has_brackets:
            fx[i-1] = fx[i-1] * fx[i+1]
            fx.pop(i)
            fx.pop(i)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "/" and not has_powers and not has_brackets:
            fx[i-1] = fx[i-1] / fx[i+1]
            fx.pop(i)
            fx.pop(i)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "+" and not has_powers and not has_brackets and not has_multiplication_division:
            fx[i-1] = fx[i-1] + fx[i+1]
            fx.pop(i)
            fx.pop(i)
            i = 0
        elif fx[i] == "-" and not has_powers and not has_brackets and not has_multiplication_division:
            fx[i-1] = fx[i-1] - fx[i+1]
            fx.pop(i)
            fx.pop(i)
            i = 0
        i += 1
    if len(fx) == 1:
        return fx[0]
    else:
        return None

fx_input = list(input("function: "))
combine_numbers(fx_input)
convert_commas(fx_input)
combine_decimals(fx_input)
convert_mult_shorthand(fx_input)
convert_to_numbers(fx_input)
points = []
for i in range(201):
    x = (i-100)*0.1
    try:
        y = calculate(insert_x(fx_input.copy(), x))
    except:
        y = None
    points.append([x, y])
for point in points:
    print(point)