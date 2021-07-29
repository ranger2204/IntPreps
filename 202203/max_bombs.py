class Solution:
    def maximumDetonation(self, bombs: list) -> int:

        def dist(a, b):
            x1, y1, _ = a
            x2, y2, _ = b
            return ((x2-x1)**2 + (y2-y1)**2)**0.5

        graph = {}
        for i,b in enumerate(bombs):
            for j in range(i+1, len(bombs)):
                c = bombs[j]
                if dist(b, c) <= b[-1]:
                    graph[i] = graph.get(i, []) + [j]
    
                if dist(c, b) <= c[-1]:
                    graph[j] = graph.get(j, []) + [i]

        def dfs(graph, cur, marked):
            if cur in marked:
                return
            else:
                marked.append(cur)
                for n in graph.get(cur, []):
                    dfs(graph, n, marked)

        max_so_far = 0
        for i, b in enumerate(bombs):
            marked = []
            dfs(graph, i, marked)
            if len(marked) > max_so_far:
                max_so_far = len(marked)
            if max_so_far == len(bombs):
                break
        return max_so_far

tests = [
    [[2,1,3],[6,1,4]],
    [[1,1,5],[10,10,5]],
    [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]],
    [[868,658,84],[82,386,48],[464,157,11],[422,654,85],[864,418,84],[366,314,72],[955,270,60],[460,98,60],[824,147,38],[580,660,27],[423,102,73],[317,471,74]],
    [[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
]


for t in tests:
    print(Solution().maximumDetonation(t))