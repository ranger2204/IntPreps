def check_valid_tree(graph):

    node_colors = {}
    def recur(graph, node):
        nonlocal node_colors
        if node is None:
            return True
        else:
            if node_colors.get(node, 'W') != 'W':
                return False
            else:
                node_colors[node] = 'G'
                for n in graph[node]:
                    r = recur(graph, n)
                    if r is False:
                        return r
                node_colors[node] = 'B'
                return True

    r = recur(graph, 0)
    return r and len(node_colors) == len(graph)