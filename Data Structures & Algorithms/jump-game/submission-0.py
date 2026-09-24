class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we can do bfs or dfs to find the end
        # if we find it we return true immediately
        # if we never find it we return false

        dp = {}
        def dfs(i):
            if i == len(nums)-1:
                return True
            if i in dp:
                return dp[i]
            res = False
            for cur in range(i+1, i+nums[i]+1):
                if cur < len(nums):
                    res = res | dfs(cur)
            dp[i] = res
            return res
        return dfs(0)