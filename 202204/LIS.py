class Solution:
    def find_lis(self, arr):
        max_before = [0 for i in range(len(arr))]
        for i, v in enumerate(arr):
            for j in range(i):
                if arr[j] < v:
                    max_before[i] = max(max_before[i], 1 + max_before[j])
        max_mb = max(max_before)
        index = max_before.index(max_mb)
        result = []
        while index >= 0:
            result.append(arr[index])
            if max_before[index] == 0:
                break
            for j in range(1, index+1):
                cur_index = index - j
                if arr[cur_index] < arr[index] and max_before[cur_index] + 1 == max_before[index]:
                    index = cur_index
                    break
        return result[::-1]
            

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

tests = [
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
]

for t in tests:
    print(Solution().find_lis(t))