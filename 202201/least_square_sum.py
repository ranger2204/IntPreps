class Solution:
    def find_least(self, n, least_so_far):
        if n == 0:
            return least_so_far
        else:
            for i in range(n//2, 1, -1):
                if i**2 <= n:
                    r = self.find_least(n-i**2, min(least_so_far, i))
                    if r > 0:
                        return r
            return -1


tests = [
    13, 27
]

for t in tests:
    print(Solution().find_least(t, float('inf')))