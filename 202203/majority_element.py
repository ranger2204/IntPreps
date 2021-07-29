def find_majority(arr):
    e = None
    c = 0
    for i, v in enumerate(arr):
        if e is None:
            e = i
            c += 1
        else:
            if v != arr[e]:
                c -= 1
        
        if c==0:
            e = None
    c = 0
    if e is not None:
        for v in arr:
            if v == arr[e]:
                c += 1
    if c > len(arr)//2:
        return arr[e]
    return None


tests = [
    [1, 2, 1, 1, 3, 4, 0],
    [3, 3, 4, 2, 4, 4, 2, 4, 4],
    [3, 3, 4, 2, 4, 4, 2, 4]
]

for t in tests:
    print(find_majority(t))