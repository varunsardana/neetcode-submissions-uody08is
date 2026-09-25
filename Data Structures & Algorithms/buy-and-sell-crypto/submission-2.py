class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        overall_profit = 0
        l = 0
        r = 1

        while r < len(prices):

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                overall_profit = max(overall_profit, profit)
            else:
                l = r

            r +=1
        return overall_profit

