def get_longest_palindromic(s):
    n = len(s)
    tab = [[False for _ in s] for _ in s]
    max_len = 1
    for i in range(n):
        tab[i][i] = True
    
    i = 0
    while i < n - 1:
        if s[i] == s[i+1]:
            tab[i][i+1] = True
            max_len = 2
        i += 1
    
    for j in range(n):
        for i in range(n):
            if j < i + 1:
                continue
            if s[i] == s[j]  and tab[i+1][j-1]:
                tab[i][j] = True
                max_len = max(max_len, j - i + 1)
    
    return max_len


tests = [
    'geeksforgeeks',
    'banana'
]
for t in tests:
    print(t, get_longest_palindromic(t))