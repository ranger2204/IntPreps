class Solution:
    def toh(self, n):
        def recur(n, s, d, a):
            if n == 1:
                print("Moving from {} to {}".format(s, d))
            else:
                recur(n-1, s, a, d)
                print("Moving from {} to {}".format(s, d))
                recur(n-1, a, d, s)
        

        recur(n, 1, 3, 2)

tests = [
    3
]

for t in tests:
    Solution().toh(t)