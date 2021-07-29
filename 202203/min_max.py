class Solution:
    def find_min_max(self, arr):
        if len(arr) == 0:
            return float('inf'), float('-inf')
        if len(arr) == 1:
            return arr[-1], arr[-1]
        else:
            l = len(arr)
            a = arr[:l//2]
            b = arr[l//2:]
            amn, amx = self.find_min_max(a)
            bmn, bmx = self.find_min_max(b)

            mn = min(amn, bmn)
            mx = max(amx, bmx)
            # print("||")
            return mn, mx


tests = [
    [1,2,3,4,5],
    [30, 1, 6, 19, 455, 678, -1]
]

for t in tests:
    print(Solution().find_min_max(t))
