def evaluate(expr):
    s = []
    for c in expr:
        if isinstance(c, int):
            s.append(c)
        else:
            a = s.pop(-1)
            b = s.pop(-1)
            if c == '+':
                z = a + b
            elif c == '-':
                z = a - b
            elif c == '/':
                z = a / b
            elif c == '*':
                z = a * b
            s.append(z)
    return s.pop(-1)

tests = [
    [5, 3, '+'],
    [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
]

for t in tests:
    print(t, evaluate(t))