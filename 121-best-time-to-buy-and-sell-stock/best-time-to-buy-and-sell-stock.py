class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        cur_min =max(prices)
        for i in range(len(prices)):
            cur_min = min(cur_min,prices[i])
            profit = max(profit,prices[i]-cur_min)
        return profit