class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want to find a relative min and max
        # easy solution is to just try every combo
        # we can do better 
        # if we traverse backwards we can just keep track of our current best
        # we would know our current highest and just update it

        m = 0
        diff = 0
        for i in range(len(prices)-1,-1,-1):
            # print(m, diff, prices[i])
            if m-prices[i] > diff:
                diff = m-prices[i]
            if prices[i] > m:
                m = prices[i]
                # print(m)
        return diff