def check_possible(timings):
    min_time = min([t[0] for t in timings])
    max_time = max([t[1] for t in timings])

    timespan = [0 for i in range(min_time, max_time+1)]
    for t in timings:
        x,y = t
        for i in range(x, y):
            timespan[i] = timespan[i] + 1
            if timespan[i] > 1:
                return False
    return True



tests = [
    [
        [0, 5], [6, 10], [11, 20] 
    ]
]

for t in tests:
    print(check_possible(t))
