def find_max_area(v):
    s = []
    max_so_far = 0
    for i, d in enumerate(v):
        if len(s) > 0:
            while len(s) > 0 and v[s[-1]] > d:
                h = s.pop(-1)
                try:
                    f = s[-1]
                except IndexError:
                    f = -1
                
                a = (i-f-1)*v[h]
                max_so_far = max(max_so_far, a)

        s.append(i)
    
    while len(s) != 0:
        h = s.pop(-1)
        try:
            f = s[-1]
        except IndexError:
            f = -1
        a = (len(v) - 1 - f)*v[h]
        max_so_far = max(max_so_far, a)
    print(v, max_so_far)
    return max_so_far
        

def find_max_area_rec(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                mat[i][j] = mat[i-1][j] + mat[i][j]

    # for l in mat:
    #     print(l)
    max_area_so_far = 0
    for v in mat:
        area = find_max_area(v)
        max_area_so_far = max(max_area_so_far, area)
    return max_area_so_far



t = [
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0]
]

print(find_max_area_rec(t))