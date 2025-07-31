class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # buy =0
        # sell = 1
        # max_profit = 0

        # while sell < len(prices):
        #     if prices[sell] > prices[buy]:
        #         profit = prices[sell] - prices[buy]
        #         max_profit = max(max_profit,profit)
           
        #     else:
        #         buy = sell
            
        #     sell += 1
        
        # return max_profit

        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        
        return profit

        