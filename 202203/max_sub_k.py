class Solution:
    def find_max_in_k(self, arr, k):
        dq = []
        ws, we = 0, 0
        result = []
        while we < len(arr):
            if len(dq) >= k:
                dq.pop(0)

            while len(dq) > 0 and dq[-1] < arr[we]:
                dq.pop(-1)
            dq.append(arr[we])

            if we - ws + 1 >= k:
                result.append(dq[0])
                ws += 1

            we += 1
        return result


tests = [
    [
        [1,2,3,4], 3
    ],
    [
        [1, 2, 3, 1, 4, 5, 2, 3, 6], 3
    ],
    [
        [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4
    ]
]

for t in tests:
    arr, k = t
    print(Solution().find_max_in_k(arr, k))