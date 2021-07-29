class Solution:
    def find_ops(self, l1, l2):
        
        def recur(l1: list, l2:list, ops:int=0):
            if len(l1) == 0:
                return ops
            else:
                f = l2[0]
                f_index = l1.index(f)
                if f_index != 0:
                    d = f_index
                    l = len(l1)
                    new_l1 = [0 for i in range(l)]
                    for i in range(l):
                        new_index =   ((i - d) + l)%l
                        new_l1[new_index] = l1[i]
                    ops += d

                    return recur(new_l1[1:], l2[1:], ops+1)
                else:
                    return recur(l1[1:], l2[1:], ops+1)

        return recur(l1, l2)

test = [
    [
        [1,3,2],
        [2,3,1]
    ]
]

for t in test:
    a, b = t
    print(Solution().find_ops(a, b))