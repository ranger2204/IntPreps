class Solution:
    def get_factorial(self, v):
        if v <= 1:
            return 1
        return v*self.get_factorial(v-1)

    def getPermutation(self, n: int, k: int) -> str:

        def recur(s, k):

            if k <= 0:
                return s
            
            f = self.get_factorial(len(s)-1)
            d = k // f
            r = k % f

            v = recur(s[:d]+s[d+1:], r)
            
            return s[d] + v

        s = ''.join(map(str, [i for i in range(1, n+1)]))
        return recur(s, k-1)

class Solution2:
    def get_factorial(self, v):
        if v <= 1:
            return 1
        return v*self.get_factorial(v-1)

    def getPermutation(self, n: int, k: int) -> str:

        result = []

        def recur(s, c, n):
            nonlocal result
            if len(c) == n:
                result.append(c)
                if len(result) == k:
                    return True
                return False
            else:
                r = False
                for i in range(len(s)):
                    r = recur(s[:i]+s[i+1:], c+s[i], n)
                    if r:
                        return r
                return r

        s = ''.join(map(str, [i for i in range(1, n+1)]))
        recur(s, "", n)
        return result[-1]

tests = [
    {
        'k': 2,
        'n': 2
    },
    {
        'k': 2,
        'n': 3
    },
    {
        'k': 3,
        'n': 3
    },
    {
        'k': 9,
        'n': 4
    },

]

for t in tests:
    print(Solution().getPermutation(**t))


