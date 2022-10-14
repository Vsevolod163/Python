x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def do_it(char):
    if char == '*':
        return x * y
    elif char == '/':
        return x / y
    elif char == '+':
        return x + y
    elif char == '-':
        return x - y