class Solution:
    def get_subset(self, set_, sum_):
        result_set = []
        def recur(st, sm, c=[]):
            nonlocal result_set
            if sm == 0:
                result_set = c
            if len(st) == 0:
                return
            else:
                recur(st[1:], sm-st[0], c+[st[0]])
                recur(st[1:], sm, c)

        recur(set_, sum_)
        return result_set

tests = [
    {
        'set_': list({3, 34, 4, 12, 5, 2}), 
        'sum_' : 9
    },
    {
        'set_': list({3, 34, 4, 12, 5, 2}), 
        'sum_' : 30
    }
]

for t in tests:
    print(Solution().get_subset(**t))