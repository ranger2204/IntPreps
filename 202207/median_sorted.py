def find_median(a, b):
    m = len(a)
    n = len(b)
    prev = None
    m1 = None
    c, d = 0, 0
    i = 0
    while i < ((m+n)//2 + 1):
        if (c < len(a) and a[c] < b[d]) or d >= len(b):    
            prev = m1
            m1 = a[c]
            c += 1
        elif d < len(b):
                prev = m1
                m1 = b[d]
                d += 1
        else:
            break
        i += 1
    
    if (len(a) + len(b))%2 == 0:
        return (prev + m1)/ 2
    else:
        return m1


# 1 2 3
# 4 5 6     c = 1 d = 0 m=1 mp = None 
            # c = 2 d = 0 m=2 mp = None

tests = [
    {
        'a': [1,2,3],
        'b': [4,5,6]
    },
    {
        'a': [1,2],
        'b': [4,5,6]
    },
    {
        'a': [1,2,3],
        'b': [4,5]
    }
]

for t in tests:
    print(t, find_median(**t))
