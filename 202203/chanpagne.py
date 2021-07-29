class Solution:
    def champagneTower(self, poured: int, r: int, c: int) -> float:

        row = [poured]
        s = 1
        while s <= r:

            new_row = [0 for i in range(s+1)]
            for j in range(s):
                if row[j] > 1:
                    overflow = row[j] - 1
                    row[j] =  1
                    new_row[j] += overflow/2.0
                    new_row[j+1] += overflow/2.0
 
            if sum(new_row) == 0:
                break
            row = new_row
            s += 1
        if c >= len(row):
            return 0
        return min(1, row[c])




tests = [
    [3, 0, 0],
    [3, 1, 1],
    [4, 2, 1],
    [25, 6, 1]
    # [100000009, 33, 17]
]

for t in tests:
    p, x, y = t
    print(Solution().champagneTower(p, x, y))