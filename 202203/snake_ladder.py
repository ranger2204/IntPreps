class Solution:
    def find_min_turns(self, board):
        snakes = {}
        ladders = {}
        
        arr = []
        for i, v in enumerate(board[::-1]):
            if i % 2 == 1:
                arr += board[::-1][i][::-1]
            else:
                arr += board[::-1][i]

        for i, v in enumerate(arr):
            if v != -1:
                if v < i+1:
                    snakes[i] = v - 1
                else:
                    ladders[i] = v - 1
        inv_ladder = {v:k for k, v in ladders.items()}
        l = len(arr)
        memo = [float('inf') for i in range(l)]
        for i in range(0, l):
            if i <= 0:
                memo[i] = 0
                continue
            min_so_far = float('inf')
            for j in range(1, 7):
                k = i - j
                if k >= 0:
                    d = 1 + memo[k]
                    min_so_far = d if d < min_so_far else min_so_far
                    # if k > 30:
                    #     print(i, k, d, 1+memo[k], min_so_far)
            
            if i in ladders:
                memo[ladders[i]] = min(min_so_far, memo[ladders[i]])
                # print(f'{ladders[i]} : {memo[ladders[i]]}')
            elif i in snakes:
                memo[snakes[i]] = min(min_so_far, memo[snakes[i]])
            else:
                memo[i] = min(min_so_far, memo[i])

        # print(ladders)
        print(list(zip(memo, [i+1 for i in range(l)])))
        return memo[l-1] if memo[l-1] != float('inf') else -1


        

# test = {
#     'snakes': {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78},
#     'ladders': {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
# }

boards = [
    # [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]],
    # [[-1,-1,-1],[-1,9,8],[-1,8,9]],
    # [[-1,7,-1],[-1,6,9],[-1,-1,2]],
    # [[1,1,-1],[1,1,1],[-1,1,1]],
    # [[-1,-1,2,21,-1],[16,-1,24,-1,4],[2,3,-1,-1,-1],[-1,11,23,18,-1],[-1,-1,-1,23,-1]],
    # [[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]],
    # [[-1,-1,27,13,-1,25,-1],[-1,-1,-1,-1,-1,-1,-1],[44,-1,8,-1,-1,2,-1],[-1,30,-1,-1,-1,-1,-1],[3,-1,20,-1,46,6,-1],[-1,-1,-1,-1,-1,-1,29],[-1,29,21,33,-1,-1,-1]],
    [
        [-1,-1,-1,-1,48,5,-1],
        [12,29,13,9,-1,2,32],
        [-1,-1,21,7,-1,12,49],
        [42,37,21,40,-1,22,12],
        [42,-1,2,-1,-1,-1,6],
        [39,-1,35,-1,-1,39,-1],
        [-1,36,-1,-1,-1,-1,5]
    ]
]

for b in boards:
    print(Solution().find_min_turns(b))