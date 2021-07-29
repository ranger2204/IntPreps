# Problem #544 [Hard]
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

class Solution:

    def find_subset(self, S, k):
        def recur(k, c, s, S):
            if c == k:
                return s
            
            if c > k:
                return None
            
            for i, v in enumerate(S):
                valid = recur(k, c+v, s+[v], S[0:i]+S[i+1:])
                if valid is not None:
                    return valid
            
            return None
        
        return recur(k, 0, [], S)



class DSolution:

    def find_subset(self, S, k):

        t = [[False for i in range(k+1)] for j in range(len(S))]
        for i in range(len(S)):
            t[i][0] = True
        
        
        for i in range(len(S)):
            for j in range(0, k+1):
                if S[i] > j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = t[i-1][j] or t[i-1][j-S[i]]
        
        return t[len(S)-1][k]

test = [
    {
        'S': [12, 1, 61, 5, 9, 2],
        'k': 4
    }
]

for t in test:
    print(DSolution().find_subset(**t))