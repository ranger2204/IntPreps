def print_diagonal(mat):
    m = len(mat)
    n = len(mat[0])

    for i in range(m+n-1):
        if i <= m-1:
            x = i
            y = 0
        else:
            x = m - 1
            y = i - m + 1
        
        tmp = []
        while x >= 0 and y <= n-1:
            tmp.append(mat[x][y])
            x -= 1
            y += 1
        if i == 0 or i%2 == 0:
            print(tmp)
        else:
            print(tmp[::-1])


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_diagonal(mat)