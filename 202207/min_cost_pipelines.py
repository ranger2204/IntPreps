def get_min_cost_connection(graph):
    links = []
    parent = {}
    for k in graph:
        for n in graph[k]:
            links.append(
                [graph[k][n], k, n]
            )
            parent[k] = k
            parent[n] = n

    links.sort()
    cost = 0

    def get_parent(s):
        if parent[s] == s:
            return s
        else:
            return get_parent(parent[s])

    for l in links:
        w, s, e = l
        p_s = get_parent(s)
        p_e = get_parent(e)
        if p_e != p_s:
            parent[p_e] = p_s
            cost += w
    return cost

tests = [
    {
        'graph': {
            'plant': {'A': 1, 'B': 5, 'C': 20},
            'A': {'C': 15},
            'B': {'C': 10},
            'C': {}
        }
    }
]

for t in tests:
    print(get_min_cost_connection(**t))