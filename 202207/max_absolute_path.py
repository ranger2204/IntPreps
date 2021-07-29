def clean(p):
    p = p.replace('\t', '')
    return p

def get_max_abs_path(s):
    tokens = s.split('\n')
    stk = []
    lvl = 0
    max_so_far = 0
    for t in tokens:
        ct = clean(t)
        lvl = t.count('\t')
        while len(stk) > lvl:
            stk.pop(-1)

        cur_len = len(ct)
        if len(stk) > 0:
            cur_len += stk[-1]

        stk.append(cur_len)
        if '.' in ct:
            
            max_so_far = max(max_so_far, cur_len + len(stk) - 1)

    return max_so_far


tests = [
    "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
]

for t in tests:
    print(t, get_max_abs_path(t))