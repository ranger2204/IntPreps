class Solution:
    def find_optimal(self, miles, hits, t, M):

        def recur(cur_mile, miles, hits, t, M, T=0):
            if cur_mile >= M:
                return T
            else:
                if cur_mile in miles:
                    index = miles.index(cur_mile)
                    return max(
                        recur(cur_mile+t+1, miles, hits, t, M, T+hits[index]),
                        recur(cur_mile+1, miles, hits, t, M, T)
                    )
                else:
                    return recur(cur_mile+1, miles, hits, t, M, T)
        
        return recur(1, miles, hits, t, M)

tests = [
    {
        'miles': [6, 7, 12, 13, 14],
        'hits': [5, 6, 5,  3,  1],
        't': 5,
        'M': 20
    },
    {
        'M': 15,
        'miles': [6, 9, 12, 14],
        'hits': [5, 6, 3, 7],
        't': 2
    }
]

for t in tests:
    print(Solution().find_optimal(**t))