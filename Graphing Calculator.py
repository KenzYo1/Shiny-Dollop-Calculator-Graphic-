import math
import turtle

def is_number(item):
    if isinstance(item, float):
        return True
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in item:
        if i in numbers:
            return True
    return False

def combine_numbers(fx):
    i = 0
    while i < len(fx)-1:
        if is_number(fx[i]) and is_number(fx[i+1]):
            fx[i] += fx.pop(i+1)
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
        i += 1
    return fx

def convert_negatives(fx):
    i = 0
    while i < len(fx)-1:
        if fx[i] == "-":
            match i:
                case 0:
                    fx[i] = "-1"
                    fx.insert(i+1, "*")
                case _:
                    if not is_number(fx[i-1]):
                        fx[i] = "-1"
                        fx.insert(i+1, "*")
        i += 1
    return fx

def convert_to_floats(fx):
    for i in range(len(fx)):
        if is_number(fx[i]):
            fx[i] = float(fx[i])
    return fx

def convert_constants(fx):
    i = 0
    while i < len(fx):
        match fx[i]:
            case "p":
                if fx[i+1] == "i":
                    fx[i] = math.pi
                    fx.pop(i+1)
            case "e":
                fx[i] = math.e
        i += 1
    return fx

def convert_operators(fx):
    i = 0
    while i < len(fx):
        if fx[i] == "l":
            if fx[i+1] == "o":
                if fx[i+2] == "g":
                    fx[i] = "log"
                    fx.pop(i+1)
                    fx.pop(i+1)
            elif fx[i+1] == "n":
                fx[i] = "ln"
                fx.pop(i+1)
        i += 1
    return fx

def convert_mult_shorthand(fx):
    i = 0
    while i < len(fx)-1:
        if ((is_number(fx[i]) or fx[i] == "x") and (is_number(fx[i+1]) or fx[i+1] == "x" or fx[i+1] == "(")) or ((is_number(fx[i]) or fx[i] == "x" or fx[i] == ")") and (is_number(fx[i+1]) or fx[i+1] == "x" or fx[i+1] == "log" or fx[i+1] == "ln")) or (fx[i] == ")" and fx[i+1] == "("):
            fx.insert(i+1, "*")
        i += 1

def insert_x(fx, x):
    for i in range(len(fx)):
        if fx[i] == "x":
            fx[i] = x
    return fx

def check_brackets(fx):
    for i in range(len(fx)):
        if fx[i] == "(" or fx[i] == "|":
            return True
    return False

def check_logarithms(fx):
    for i in fx:
        if i == "log" or i == "ln":
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
    has_logarithms = check_logarithms(fx)
    has_powers = check_powers(fx)
    has_multiplication_division = check_multiplication_division(fx)
    while i < len(fx):
        if fx[i] == "(":
            fx.pop(i)
            fx2 = []
            bracket_count = 0
            while bracket_count >= 0:
                if fx[i] == "(":
                    bracket_count += 1
                if fx[i] == ")":
                    bracket_count -= 1
                if bracket_count >= 0:
                    fx2.append(fx.pop(i))
            fx[i] = calculate(fx2)
            has_brackets = check_brackets(fx)
            has_logarithms = check_logarithms(fx)
            has_powers = check_powers(fx)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "|":
            fx.pop(i)
            fx2 = []
            while fx[i] != "|":
                fx2.append(fx.pop(i))
            fx[i] = abs(calculate(fx2))
            has_brackets = check_brackets(fx)
            has_logarithms = check_logarithms(fx)
            has_powers = check_powers(fx)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "log" and fx[i+1] != "log" and fx[i+1] != "ln" and not has_brackets:
            fx[i] = math.log10(fx[i+1])
            fx.pop(i+1)
            has_logarithms = check_logarithms(fx)
            i = 0
        elif fx[i] == "ln" and fx[i+1] != "log" and fx[i+1] != "ln" and not has_brackets:
            fx[i] = math.log(fx[i+1])
            fx.pop(i+1)
            has_logarithms = check_logarithms(fx)
            i = 0
        elif fx[i] == "^" and not has_brackets and not has_logarithms:
            fx[i-1] = fx[i-1] ** fx[i+1]
            if isinstance(fx[i-1], complex):
                return None
            fx.pop(i)
            fx.pop(i)
            has_powers = check_powers(fx)
            i = 0
        elif fx[i] == "*" and not has_brackets and not has_logarithms and not has_powers:
            fx[i-1] = fx[i-1] * fx[i+1]
            fx.pop(i)
            fx.pop(i)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "/" and not has_brackets and not has_logarithms and not has_powers:
            fx[i-1] = fx[i-1] / fx[i+1]
            fx.pop(i)
            fx.pop(i)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "+" and not has_brackets and not has_logarithms and not has_powers and not has_multiplication_division:
            fx[i-1] = fx[i-1] + fx[i+1]
            fx.pop(i)
            fx.pop(i)
            i = 0
        elif fx[i] == "-" and not has_brackets and not has_logarithms and not has_powers and not has_multiplication_division:
            fx[i-1] = fx[i-1] - fx[i+1]
            fx.pop(i)
            fx.pop(i)
            i = 0
        else:
            i += 1
    if len(fx) == 1:
        return fx[0]
    else:
        return None

fx_input = list(input("function: "))
combine_numbers(fx_input)
convert_commas(fx_input)
combine_decimals(fx_input)
convert_negatives(fx_input)
convert_to_floats(fx_input)
convert_constants(fx_input)
convert_operators(fx_input)
convert_mult_shorthand(fx_input)
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