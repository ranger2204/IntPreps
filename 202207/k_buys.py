def find_max_profit(prices, k):
    s = prices[0]
    profits = []
    i = 0
    while i < len(prices):
        if prices[i] < s:
            p = prices[i-1] - s
            print(s, prices[i-1], p)
            profits.append(p)
            s = prices[i]
        i += 1
    
    if prices[i-1] > s:
        p = prices[i-1] - s
        profits.append(p)
    
    profits.sort()
    profits = profits[::-1]
    return sum(profits[:k])


tests = [
    {
        'prices': [5,2,4,0,1],
        'k': 2
    }
]

for t in tests:
    print(find_max_profit(**t))
