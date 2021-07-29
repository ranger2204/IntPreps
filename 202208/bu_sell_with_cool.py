class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def recur(prices, l, r):
            nonlocal memo
            if r - l <= 1:
                return 0
            if r - l == 2:
                x,y = prices[l:r]
                memo[l] = memo.get(l, {})
                memo[l][r] = max(0, y-x)
                return memo[l][r]
            if r - l == 3:
                memo[l] = memo.get(l, {})
                memo[l][r] = max(0, prices[l+1]-prices[l], prices[r-1]-prices[l])
                return memo[l][r]
            else:
                if l in memo:
                    if r in memo[l]:
                        return memo[l][r]
                max_profit = 0
                m = (l+r)//2
                d1 = recur(prices, l, m) + recur(prices, m+1, r)
                d2 = recur(prices, l, m+1) + recur(prices, m+2, r)

                max_profit = max(d1, d2)

                memo[l] = memo.get(l, {})
                memo[l][r] = max_profit
                return max_profit
        return recur(prices, 0, len(prices))
