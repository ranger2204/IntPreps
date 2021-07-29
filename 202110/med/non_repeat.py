# Rearrange characters in a string such that no two adjacent are same

import heapq

class Solution:
    def rearrange(self, s):
        f = {}
        for c in s:
            f[c] = f.get(c, 0) + 1

        data = [[c, -1*f[c]] for c in f]

        heapq.heapify(data)
        
        result = ""

        while True:
            
            attached = False
            pop_list = []
            while len(data) > 0:
                popped = heapq.heappop(data)

                if len(result) == 0 or popped[0] != result[-1]:
                    popped[1] += 1
                    if popped[1] < 0:
                        pop_list.append(popped)
                    result += popped[0]
                    attached =  True
                    for each in pop_list:
                        heapq.heappush(data, each)
                    break
                else:
                    pop_list.append(popped)
            
            if attached is False:
                return None
            else:
                if len(data) == 0:
                    return result

        
        


tests = [
    "aaabbc",
    "aaaac"
]

for t in tests:
    print(Solution().rearrange(t))