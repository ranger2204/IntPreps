from heapq import heappop, heapify, heappush

def sort_k(arr, k):
    heap = arr[:k+1]

    heapify(heap)
    out_index = 0
    for i in range(k+1, len(arr)):
        e = heappop(heap)
        heappush(heap, arr[i])
        arr[out_index] = e
        out_index += 1
    while len(heap) > 0:
        arr[out_index] = heappop(heap)
        out_index += 1
    
tests = [
    [1,3,2,6,5]
]

for t in tests:
    print(sort_k(t, 1), t)