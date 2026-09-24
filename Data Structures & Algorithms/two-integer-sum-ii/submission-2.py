class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # need to add two numbers with different indices
        # we are increasing only
        # we can do this in two passes easily
        # first pass is to make a map of val to index
        # second is to check if at each step we have the missing number available

        # the problem is that we cannot use any additional space
        # brute force is just n^2 for checking each combo
        # if we use a two pointer solution can we do it in one pass?
        # we would need to start at 0 and 1
        # increasing our long pointer will always give us the next highest increment
        # but this is not good enough if we overshoot and need to decrease

        # we could compute target - numbers[i] and use it somehow?

        # what if we start from the ends
        # if we only move toward the middle we will always be within time
        # the question is how we KNOW we can increase/decrease

        # if our small + large is too big we always decrease large
        # if we are too small we increase small

        l = 0
        r = len(numbers) - 1
        while l < r:
            
            cursum = numbers[l] + numbers[r]
            # print(l+1, r+1, cursum)
            if cursum == target:
                return [l+1, r+1]
            elif cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
        return