class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=0
        profit=0
        n=len(prices)
        buy=prices[0]
        profit=0
        for i in range(1,n):
            if (prices[i]-buy)>profit:
                profit=prices[i]-buy

            if prices[i]<buy:
                buy=prices[i]
        return profit

        