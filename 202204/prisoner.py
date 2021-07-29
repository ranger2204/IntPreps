class Solution:
    def find_last_prisoner(self, n, k):
        order = [i+1 for i in range(n)]
        cur = 0
        last_dead = -1
        while len(order) > 0:
            cur += (k-1)
            cur %= len(order)
            last_dead = order.pop(cur)
        
        return last_dead

    def find_last_prisoner_recur(self, n, k):
        
        def recur(order, k, index):
            if len(order) == 1:
                return order[0]
            else:
                
                index = (index+k) % len(order)
                r = order.pop(index)
                print(r)

                return recur(order, k, index)

        order = [i+1 for i in range(n)]
        return recur(order, k-1, 0)

tests = [
    {
        'n': 5,
        'k': 2
    },
    # {
    #     'n': 5,
    #     'k': 3
    # }
]
for t in tests:
    Solution().find_last_prisoner_recur(**t)