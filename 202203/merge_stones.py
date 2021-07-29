class Solution:
    def mergeStones(self, stones: list, k: int) -> int:
        def recur(stones, k, cost):
            if len(stones) == 1:
                return cost
            if len(stones) < k:
                return float('inf')
            else:
                least_so_far = float('inf')
                for i in range(len(stones) - k):
                    current_cost = sum(stones[i: i+k])
                    new_stones = stones[i:] + [current_cost] + stones[i+k:]
                    cost = recur(new_stones, k, cost + current_cost)
                    least_so_far = least_so_far if least_so_far < cost else cost
                return least_so_far
        cost = recur(stones, k, 0)
        if cost == float('inf'):
            cost = -1
        return cost

tests = [
    {
        'stones' : [3,2,4,1], 
        'k': 2
    },
    {
        'stones': [3,2,4,1], 
        'k': 3
    }
]

for t in tests:
    print(Solution().mergeStones(**t))