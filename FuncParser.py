import math


def lengthen(array):
    new_array = [None] * (len(array) * 2)
    for i in range(len(array)):
        new_array[i] = array[i]
    return new_array

def add_to_back(array, item):
    if len(array) == 0:
        array = [None]
    if array == [None]:
        array[0] = item
        return array
    elif array[-1] != None:
        array = lengthen(array)
    for i in range(len(array)):
        if array[-i-1] != None:
            array[-i] = item
            return array
    return array

def add_to(array, index, item):
    if array[-1]:
        array = lengthen(array)
    for i in range(len(array)-index):
        if i > 0:
            array[-i] = array[-i-1]
    array[index] = item
    return array

def remove_at(array, index):
    for i in range(len(array)-index-1):
        array[i+index] = array[i+index+1]
    array[-1] = None
    return array

def duplicate(array):
    new_array = [None]*len(array)
    for i in range(len(array)):
        new_array[i] = array[i]
    return new_array

def is_number(item):
    if isinstance(item, float):
        return True
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if item[-1] in numbers:
        return True
    return False

def is_operator(item):
    operators = ["log", "ln", "sin", "cos", "tan", "asin", "acos", "atan"]
    if item in operators:
        return True
    return False

def combine_numbers(fx):
    i = 0
    while i < len(fx)-1 and fx[i+1] != None:
        if is_number(fx[i]) and is_number(fx[i+1]):
            fx[i] += fx[i+1]
            remove_at(fx, i+1)
        else:
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
            fx[i-1] += fx[i]
            remove_at(fx, i)
            fx[i-1] += fx[i]
            remove_at(fx, i)
        i += 1
    return fx

def convert_negatives(fx):
    i = 0
    while i < len(fx)-1:
        if fx[i] == "-":
            match i:
                case 0:
                    fx[i] = "-1"
                    fx = add_to(fx, i+1, "*")
                case _:
                    if not is_number(fx[i-1]) and fx[i-1] != "x":
                        fx[i] = "-1"
                        fx = add_to(fx, i+1, "*")
        i += 1
    return fx

def convert_to_floats(fx):
    for i in range(len(fx)):
        if not fx[i]:
            return fx
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
                    remove_at(fx, i+1)
            case "e":
                fx[i] = math.e
        i += 1
    return fx

def convert_operators(fx):
    i = 0
    while i < len(fx):
        match fx[i]:
            case "l":
                match fx[i+1]:
                    case "o":
                        if fx[i+2] == "g":
                            fx[i] = "log"
                            remove_at(fx, i+1)
                            remove_at(fx, i+1)
                    case "n":
                        fx[i] = "ln"
                        remove_at(fx, i+1)
            case "s":
                if fx[i+1] == "i" and fx[i+2] == "n":
                    fx[i] = "sin"
                    remove_at(fx, i+1)
                    remove_at(fx, i+1)
            case "c":
                if fx[i+1] == "o" and fx[i+2] == "s":
                    fx[i] = "cos"
                    remove_at(fx, i+1)
                    remove_at(fx, i+1)
            case "t":
                if fx[i+1] == "a" and fx[i+2] == "n":
                    fx[i] = "tan"
                    remove_at(fx, i+1)
                    remove_at(fx, i+1)
            case "a":
                match fx[i+1]:
                    case "s":
                        if fx[i+2] == "i" and fx[i+3] == "n":
                            fx[i] = "asin"
                            remove_at(fx, i+1)
                            remove_at(fx, i+1)
                            remove_at(fx, i+1)
                    case "c":
                        if fx[i+2] == "o" and fx[i+3] == "s":
                            fx[i] = "acos"
                            remove_at(fx, i+1)
                            remove_at(fx, i+1)
                            remove_at(fx, i+1)
                    case "t":
                        if fx[i+2] == "a" and fx[i+3] == "n":
                            fx[i] = "atan"
                            remove_at(fx, i+1)
                            remove_at(fx, i+1)
                            remove_at(fx, i+1)
        i += 1
    return fx

def convert_mult_shorthand(fx):
    i = 0
    while i < len(fx)-1 and fx[i] and fx[i+1]:
        if ((is_number(fx[i]) or fx[i] == "x") and (is_number(fx[i+1]) or fx[i+1] == "x" or fx[i+1] == "("))\
        or ((is_number(fx[i]) or fx[i] == "x" or fx[i] == ")") and (is_number(fx[i+1]) or fx[i+1] == "x" or is_operator(fx[i+1])))\
        or (fx[i] == ")" and fx[i+1] == "("):
            fx = add_to(fx, i+1, "*")
        i += 1
    return fx

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


def check_operators(fx):
    for i in fx:
        if is_operator(i):
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
    has_operators = check_operators(fx)
    has_powers = check_powers(fx)
    has_multiplication_division = check_multiplication_division(fx)

    while i < len(fx):
        if fx[i] == "(":
            fx = remove_at(fx, i)
            fx2 = []
            bracket_count = 0
            while bracket_count >= 0:
                if fx[i] == "(":
                    bracket_count += 1
                if fx[i] == ")":
                    bracket_count -= 1
                if bracket_count >= 0:
                    fx2 = add_to_back(fx2, fx[i])
                    fx = remove_at(fx, i)
            fx[i] = calculate(fx2)
            has_brackets = check_brackets(fx)
            has_operators = check_operators(fx)
            has_powers = check_powers(fx)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "|":
            remove_at(fx, i)
            fx2 = []
            while fx[i] != "|":
                fx2 = add_to_back(fx2, fx[i])
                fx = remove_at(fx, i)
            fx[i] = abs(calculate(fx2))
            has_brackets = check_brackets(fx)
            has_operators = check_operators(fx)
            has_powers = check_powers(fx)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "log" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.log10(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "ln" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.log(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "sin" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.sin(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "cos" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.cos(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "tan" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.tan(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "asin" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.asin(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "acos" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.acos(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "atan" and not is_operator(fx[i+1]) and not has_brackets:
            fx[i] = math.atan(fx[i+1])
            remove_at(fx, i+1)
            has_operators = check_operators(fx)
            i = 0
        elif fx[i] == "^" and not has_brackets and not has_operators:
            fx[i-1] = fx[i-1] ** fx[i+1]
            if isinstance(fx[i-1], complex):
                return None
            remove_at(fx, i)
            remove_at(fx, i)
            has_powers = check_powers(fx)
            i = 0
        elif fx[i] == "*" and not has_brackets and not has_operators and not has_powers:
            fx[i-1] = fx[i-1] * fx[i+1]
            remove_at(fx, i)
            remove_at(fx, i)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "/" and not has_brackets and not has_operators and not has_powers:
            fx[i-1] = fx[i-1] / fx[i+1]
            remove_at(fx, i)
            remove_at(fx, i)
            has_multiplication_division = check_multiplication_division(fx)
            i = 0
        elif fx[i] == "+" and not has_brackets and not has_operators and not has_powers and not has_multiplication_division:
            fx[i-1] = fx[i-1] + fx[i+1]
            remove_at(fx, i)
            remove_at(fx, i)
            i = 0
        elif fx[i] == "-" and not has_brackets and not has_operators and not has_powers and not has_multiplication_division:
            fx[i-1] = fx[i-1] - fx[i+1]
            remove_at(fx, i)
            remove_at(fx, i)
            i = 0
        else:
            i += 1
    return fx[0]

fx_input = list(input("function: "))
try:
    fx_input = combine_numbers(fx_input)
    fx_input = convert_commas(fx_input)
    fx_input = combine_decimals(fx_input)
    fx_input = convert_negatives(fx_input)
    fx_input = convert_to_floats(fx_input)
    fx_input = convert_constants(fx_input)
    fx_input = convert_operators(fx_input)
    fx_input = convert_mult_shorthand(fx_input)
except:
    fx_input = [None]
x_range = [-500 ,500]
x_step = 0.01
points = [None]
for i in range(int((x_range[1]-x_range[0])/x_step)+1):
    x = (i+x_range[0]/x_step)*x_step
    try:
        y = calculate(insert_x(duplicate(fx_input), x))
    except:
        y = None
    if i >= len(points):
        points = lengthen(points)
    points[i] = [x, y]
