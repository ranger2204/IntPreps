
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list) -> str:
        def compare(x, y):
            return -1 if int(str(x)+str(y)) > int(str(y)+str(x)) else 1
        nums = sorted(nums, key=cmp_to_key(compare))
        out_str = ''
        for n in nums:
            out_str += str(n)
        return out_str


tests = [
    [10, 2],
    [3,9,34, 30]
]

for t in tests:
    print(Solution().largestNumber(t))