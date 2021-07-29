class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = []
        result = []
        l, r = 0, 0
        while r < len(nums):
            if r - l > k - 1:
                if len(dq) > 0 and dq[0] == l:
                    dq.pop(0)
            
            if len(dq) == 0:
                dq.append(r)
            elif nums[dq[0]] > nums[r]:
                dq.append(r)
            else:
                while len(dq) > 0 and nums[dq[-1]] < nums[r]:
                    dq.pop(-1)
                dq.append(r)
            if r - l  == k - 1:
                result.append(nums[dq[0]])
            r += 1
        return result
