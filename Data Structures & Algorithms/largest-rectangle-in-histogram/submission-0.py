class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # first idea is this
        # for each starting point we want to run a max rectangle function
        # we reset our total max variable with the current highest and return at the end
        # the way we reduce runtime is by keeping track of all visited states

        # the issue however is that we are processing a list instead of a 2d array
        # this requires us to do some slightly different operations
        # instead of actual traversal, we will do some math

        # we know that our max height is the minimum across our width
        # we can do some kind of sliding window to unlock our height (if possible)

        # similar to the rain bucket question, we should start from the edges?

        
        stack = [(-1, 0)]
        cur_max = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # we need to remove the previous
                # we can also extend our current
                j, k = stack.pop()
                cur_max = max(cur_max, (i - j) * k)

                start = j
            # this minimizes our start
            stack.append((start, h))
        
        for i, h in stack:
            # now we must process all that are left
            cur_max = max(cur_max, (len(heights) - i) * h)
            
        return cur_max
            





        
