
def split_merge(arr):
    ans = 0
    def recur(arr, l, r):
        nonlocal ans
        if l == r:
            return [arr[l]]
        if l > r:
            return []
        else:
            m = (l+r)//2
            a = recur(arr, l, m)
            b = recur(arr, m+1, r)
            
            i = 0
            j = 0
            r = []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    r.append(a[i])
                    i += 1
                elif b[j] < a[i]:
                    k = i
                    while k < len(a):
                        if a[k] > 2*b[j]:
                            ans += 1
                        k += 1
                    r.append(b[j])
                    j += 1
            
            if i == len(a):
                r += b[j:]
            else:
                r += a[i:]
            return r

    _ = recur(arr, 0, len(arr)-1)
    return ans

tests = [
    [1,3,2,3,1],
    [2,4,3,5,1]
]
for t in tests:
    print(split_merge(t))

