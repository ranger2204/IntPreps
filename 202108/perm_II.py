class Solution:
    def permuteUnique(self, nums: list) -> list:
        def recur(nums):
            if len(nums) == 1:
                return [nums]
            else:
                output = []
                for i in range(len(nums)):
                    if i != 0:
                        if nums[i] == nums[i-1]:
                            continue
                    ret =  recur(nums[:i] + nums[i+1:])
                    for r in ret:
                        output.append([nums[i]] + r)
                return output
        nums.sort()
        return recur(nums)

tests = [
    [],
    [1],
    [1,1,1],
    [1,1,2],
    [1,2,3],
    [1,2,1],
] 
for t in tests:
    print(Solution().permuteUnique(t))

        