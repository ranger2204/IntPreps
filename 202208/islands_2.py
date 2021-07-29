

def get_count(pos, m, n):

    result = []
    parent = [-1 for i in range(m*n)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    count  = 0

    def get_parent(r):
        nonlocal parent
        if r == parent[r]:
            return r
        p = get_parent(parent[r])
        parent[r] = p
        return p

    for p in pos:
        x, y = p[0], p[1]
        r = m*x + y
        if parent[r] != -1:
            continue
        parent[r] = r
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            rn = m*nx + ny
            if nx < 0 or ny < 0 or nx >= m or ny >= n or rn < 0:   #not in limits
                continue
            
            if parent[rn] == -1: #neighbor not an island
                continue

            par_r = get_parent(r)
            par_rn = get_parent(rn)

            print(p, (nx, ny), par_r, par_rn)
            if par_r != par_rn:
                parent[par_rn] = par_r
                count -= 1

        result.append(count)
    return result


pos = [
    [0,0], [0,2], [2,0], [2,2], [1,1], [1,0], [1,2]
]

print(get_count(pos, 3, 3))

        
            