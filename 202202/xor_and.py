class Solution:
    def find_valid(self, num):
        for i in range(0, num):
            k = num - i
            if (k^i == num) and (k&i==0):
                return 1
        return 0


test = [
    0, 5
]
for t in test:
    print(Solution().find_valid((t)))