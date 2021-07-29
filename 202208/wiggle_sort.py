def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def wiggle_sort(arr):
    arr.sort()
    s = 0
    m = (s + len(arr))// 2
    r = []
    
    for i in range(len(arr)):
        if i %2 == 0:
            r.append(arr[s])
            s += 1
            
        else:
            while m < len(arr) and arr[m] <= arr[s-1]:
                m += 1
            r.append(arr[m])
            m += 1
    return r
        

tests = [
    [3,5,2,1,6,4],
    [5,5,4,4,4]
]

for t in tests:
    print(wiggle_sort(t))