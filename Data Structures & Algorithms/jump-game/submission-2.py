class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we can iterate one time and kee track of our current maximum distance
        # if we ever run out of maximum jumps we return False
        # we either choose the current, skip it, or have run out of jumps
        n = len(nums)-1
        ends = set()
        ends.add(n)
        min_end = n

        for i in range(len(nums)-2, -1, -1):
            print(i)
            if i+nums[i] in ends:
                ends.add(i)
            if i+nums[i] >= min_end:
                ends.add(i)
                min_end = i

        return 0 in ends