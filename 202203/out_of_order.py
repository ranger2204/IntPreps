class Solution:
    def find_no_inversions(self, arr):
        no_of_inversions = 0
        def mergeS(arr):
            nonlocal no_of_inversions
            if len(arr) <= 1:
                return arr
            else:
                a = mergeS(arr[:len(arr)//2])
                b = mergeS(arr[len(arr)//2:])

                c = []
                i, j = 0, 0
                while i < len(a) and j < len(b):
                    if a[i] < b[j]:
                        c.append(a[i])
                        i += 1
                    else:
                        c.append(b[j])
                        no_of_inversions += len(a[i:])
                        # print(a[i:], b[j:], no_of_inversions)
                        j += 1
  
                c += b[j:]
                c += a[i:]

                return c
        c = mergeS(arr)
        return no_of_inversions

tests = [
    [2, 4, 1, 3, 5],
    [5, 4, 3, 2, 1]
]

for t in tests:
    print(Solution().find_no_inversions(t))


# 0 + 2 + 1

# 2
#     24
# 4       124
#     1
# 1
#         35
# 3   35

# 5