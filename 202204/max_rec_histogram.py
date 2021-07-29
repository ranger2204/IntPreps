class Solution:
    def max_rectangle(self, arr):
        stack = []
        max_rec = 0
        for i, v in enumerate(arr):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) > 0 and arr[stack[-1]] > v:
                    top_index = stack.pop(-1)
                    left_index = 0 if len(stack) == 0 else stack[-1]
                    rec = arr[top_index] * (i-left_index-1)
                    max_rec = max(max_rec, rec)

                stack.append(i)	
        
        right_index = len(arr) - 1
        while len(stack) != 0:
            top_index = stack.pop(-1)
            left_index = 0 if len(stack) == 0 else stack[-1]
            rec = arr[top_index] *(right_index - left_index - 1)
            max_rec = max(max_rec, rec)
                
        return max_rec
        



tests = [
    [
        6, 2, 5, 4, 5, 1, 6
    ]
]


for t in tests:
    print(Solution().max_rectangle(t))
    
#6
#6 2
#2	max_rec = 6
#2 5
#2 5 4
#2 4 max_rec = 6
#2 4 5
#2 4 5 1
#recs = 5, 12, 8
#max_rec = 12
#1 6

