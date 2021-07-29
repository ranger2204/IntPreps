# def recur(arr, index):
#     if index >= len(arr):
#         return 1, -1
#     else:
#         v = arr[index]
#         h, l = recur(arr, index+1)
#         if v > 0:
#             return v*h, -1*(v+1)*l
#         return -1*(v+1)*h, v*l

def recur(arr, index, cur_prod=1):
    if index >= len(arr):
        return cur_prod
    else:
        v = arr[index]
        return max(
            recur(arr, index+1, v*cur_prod),
            recur(arr, index+1, -1*(v+1)*cur_prod)
        )

tests = [
    [6, -10, 1],
    [-1, -1]
]

for t in tests:
    print(t, recur(t, 0))