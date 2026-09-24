class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp/backtracking 
        
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]+1
            if i == len(nums)-1:
                return 0
            if nums[i] == 0:
                return 1001
            
            res = []
            m = min(i+nums[i]+1, len(nums))
            for cur in range(i+1, m):
                res.append(dfs(cur))
            dp[i] = min(res)
            return dp[i]+1
            
        return dfs(0)