class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we have O(1) space meaning we cannot make a map or a count
        # we also cannot modify nums to be a count
        # we are not sorted and cant sort
        # so is this a two pointer question then?
        # we have a fast and slow pointer and then try to find the match?

        # we know that we have 1-n represented in our list
        # we will always have exactly one extra

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        first = slow
        slow = 0
        while slow != first:
            slow = nums[slow]
            first = nums[first]
        return slow