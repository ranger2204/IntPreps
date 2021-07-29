def check_palindrome(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    
    odds = 0
    for c in counts:
        if counts[c] % 2 != 0:
            odds += 1
    
    return odds % 2 != 0


tests = [
    'carrace',
    'malayalam',
    'name'
]

for t in tests:
    print(t, check_palindrome(t))

