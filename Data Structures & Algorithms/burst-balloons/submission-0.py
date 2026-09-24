class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # burst i -> nums[i - 1] * nums[i] * nums[i + 1]
        # if i-1 or i+1 out of bound then we defaul to 1
        # once we burst a balloon we remove it from the list
        # we need to figure out the max 

        # at each step we have a choice, burst now or later, we want the max of these options
        # how can we reduce our computations?
        # for each possible sublist, we can keep a map to prevent future recomputations

        # if we burst now our computation is the current coins plus the max of the remaining

        # if we burst later?

        # we can instead try to burst each balloon at the start
        # this will allow us to always choose 

        dp = {}
        def rec(n):
            # print(n)
            if len(n) == 0:
                return 0
            if n in dp:
                return dp[n]

            # we need to check each 
            max_coins = 0
            for i in range(len(n)):
                prev = n[i - 1] if i - 1 >= 0 else 1
                next = n[i + 1] if i + 1 < len(n) else 1
                burst = prev * n[i] * next
                cur = rec(tuple(n[:i] + n[i + 1:])) + burst
                if cur > max_coins:
                    max_coins = cur

            dp[n] = max_coins
            return max_coins
        
        return rec(tuple(nums))
            
                

