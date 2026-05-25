class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = 0

        for end  in range(1,len(prices)):
            if prices[start] < prices[end]:
                current_profit = prices[end] - prices[start]
                max_profit = max(max_profit, current_profit)
            else:
                start = end
        return max_profit

# 2,1,2,1,0,1,2

# s 1
# e 3

# 1 < 2

# cp 1
# mp 1

