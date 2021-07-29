from heapq import heappop, heappush

def get_no_of_rooms(timings):
    h  = []
    count = 0
    timings.sort()
    for t in timings:
        if len(h) == 0:
            heappush(h, t[1])
            count += 1
        else:
            if(h[0] > t[0]):
                count += 1
                _ = heappop(h)
            heappush(h, t[1])
    return count



tests = [
    [[ 0, 5 ],
    [ 1, 2 ],
    [ 1, 10 ]]
]

for t in tests:
    print(get_no_of_rooms(t))