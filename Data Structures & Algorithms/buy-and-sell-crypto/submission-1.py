class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = prices[0]
        for price in prices:
            profit = max(profit, price - cheapest)
            cheapest = min(cheapest, price)
        return profit


        # l = 0
        # r = 1
        # profit = 0
        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         profit = max(profit, prices[r]-prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return profit
