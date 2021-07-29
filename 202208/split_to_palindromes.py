def split_to_palindromes(s):
    mat = [[0 for _ in s] for _ in s]

    for i in range(len(s)):
        mat[i][i] = 1

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            mat[i][i+1] = 1

    for j in range(1, len(s)):
        r = j
        for i in range(len(s)-1):
            mat[i][r] = 1 if s[i] == s[r] and mat[i+1][r-1] == 1 else mat[i][r]
            r += 1
            if r >= len(s):
                break
    
    for i, r in enumerate(mat):
        print(s[i], r)

    i = j = 0
    while i < len(s):
        j = len(s)-1
        while j > i:
            if mat[i][j] == 1:
                break
            j -= 1
        print(s[i:j+1])
        if j >= 0:
            i += (j-i)

        i += 1



tests = [
    'racecarannakayak'
]

for t in tests:
    split_to_palindromes(t)