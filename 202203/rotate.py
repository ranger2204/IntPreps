class Solution():
    def reverse(self, arr, start, end):
        while start < end:
            tmp = arr[start]
            arr[start] = arr[end]
            arr[end]=tmp
            start += 1
            end -= 1
        
    def left_rotate(self, arr, k):
        n = len(arr)
        self.reverse(arr, 0, k-1)
        self.reverse(arr, k, n-1)
        self.reverse(arr, 0, n-1)
        print(arr)
    
    def right_rotate(self, arr, k):
        n = len(arr)
        self.reverse(arr, n-k, n-1)
        self.reverse(arr, 0, n-k-1)
        self.reverse(arr, 0, n-1)
        print(arr)


tests = [
    "1234567"
]

for t in tests:
    Solution().left_rotate(list(t), 3)
    Solution().right_rotate(list(t), 3)