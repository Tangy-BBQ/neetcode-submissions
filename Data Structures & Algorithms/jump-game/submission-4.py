class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        l = r = 0

        while r < len(nums)-1:
            f = 0
            for i in range(l, r+1):
                f = max(f, i + nums[i])
            if f == 0:
                return False
            l = r + 1
            r = f
        return True