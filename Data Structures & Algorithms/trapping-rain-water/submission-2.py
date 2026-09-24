class Solution:
    def trap(self, height: List[int]) -> int:
        # we can drop leading and trailing 0's
        # we need to identify the height of each valid index
        # this would be the minimum of the valid edges - current height
        # we can use two pointers that converge towards the middle

        # we can move right and left independently
        # we will keep track of the previous max for each 
        # and as we change our bound will calculate the current index area

        left = 0 
        right = len(height) - 1
        lmax = height[0]
        rmax = height[len(height)-1]

        # could probably do this inplace but
        # water = [0]*len(height)

        while left <= right:
            # change our bounds
            if height[left] <= height[right]:
                # before changing we calculate because we know max already
                height[left] = min(lmax, rmax) - height[left]
                left += 1
                if left < len(height) and height[left] > lmax:
                    lmax = height[left]
            else:
                height[right] = min(lmax, rmax) - height[right]
                right -= 1
                if right >= 0 and height[right] > rmax:
                    rmax = height[right]
        # print(height)
        return sum(height)