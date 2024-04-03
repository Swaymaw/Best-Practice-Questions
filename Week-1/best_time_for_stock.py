def best_time_stock(prices):
    if len(prices) < 2:
        return 0
    
    l = 0
    r = 1
    max_profit = 0

    while l < len(prices) and r < len(prices):
        print(prices[l], prices[r])
        max_profit = max(prices[r] - prices[l], max_profit)  
        if prices[r] < prices[l]:
            l = r 
        r += 1
    
    return max_profit

print(best_time_stock([2, 1, 4]))