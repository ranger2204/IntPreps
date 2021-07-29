class Solution():
    def find_unordered(self, arr):
        l = len(arr)
        lower_index = -1
        for i in range(0, l-1):
            if arr[i] > arr[i+1]:
                lower_index = i
                break
        
        higher_index = -1
        for i in range(l-1, 0, -1):
            if arr[i] < arr[i-1]:
                higher_index = i
                break
        if higher_index == -1 or lower_index == -1:
            return []
            
        min_in_unordered = min(arr[lower_index: higher_index+1])
        max_in_unordered = max(arr[lower_index: higher_index+1])
        

        for i in range(lower_index-1, 0, -1):
            if arr[i] > min_in_unordered:
                lower_index = i
                break
        
        for i in range(higher_index+1, l):
            if arr[i] < max_in_unordered:
                higher_index = i
                break
        
        return arr[lower_index: higher_index+1]


tests = [
    [1,2,4,5,3,2,6,7],
    [1,2,3]
]

for t in tests:
    print(Solution().find_unordered(t))