def find_min_boats(people, k):
    people.sort()
    s, e = 0, len(people) - 1
    boats = 0
    while s <= e:
        w = people[s] + people[e]
        if w <= k:
            s += 1
            e -= 1
        else:
            e -= 1
        boats += 1
    return boats


tests = [
    {
        'people': [200, 100, 300],
        'k': 400
    },
    {
        'people': [200, 100, 300],
        'k': 300
    }
]

for t in tests:
    print(t, find_min_boats(**t))