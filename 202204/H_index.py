class Solution:
    def find_h_index(self, arr):
        arr.sort()
        max_so_far = 0
        for i, v in enumerate(arr):
            d = len(arr) - i
            if d >= v:
                max_so_far = max(v, max_so_far)
        return max_so_far


tests = [
    [4, 3, 0, 1, 5]
]

for t in tests:
    print(Solution().find_h_index(t))