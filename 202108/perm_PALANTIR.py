class Solution:
    def permuteUnique(self, nums: list) -> int:

        def recur(s):
            if len(s) <= 1:
                return [s]
            else:
                result = []
                for i, c in enumerate(s):
                    r = recur(s[:i]+s[i+1:])
                    for k in r:
                        result.append([c]+k)
                return result
        
        return recur(nums)

tests = [
    [1,2,3]
]

for t in tests:
    print(Solution().permuteUnique(t))