def find_max_path(triangle, i=0, j=0):
    if i < len(triangle):
        if j < len(triangle[i]):
            return triangle[i][j] + max(
                find_max_path(triangle, i+1, j),
                find_max_path(triangle, i+1, j+1)
            )
    return 0

tests = [
    {
        'triangle': [[1], [2, 3], [1, 5, 1]]
    }
]

for t in tests:
    print(find_max_path(**t))