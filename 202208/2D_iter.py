def iter2D(td):
    for each in td:
        for c in each:
            yield c


td = [
    [1],
    [2,3],
    [4,5,6]
]

iter = iter2D(td)
for c in iter:
    print(c)