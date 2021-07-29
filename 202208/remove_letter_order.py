class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        lookup = {}
        for c in s:
            lookup[c] = lookup.get(c, 0) + 1
            
        for c in s:
            if not stk:
                stk.append([c, lookup[c]])
            else:
                if stk[-1][0] > c and stk[-1][1] > 1:
                    tc, f = stk.pop(-1)
                    lookup[tc] -= 1
                    
                stk.append([c, lookup[c]])
        return ''.join(stk)
