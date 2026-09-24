class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we need to find all things than end with x and begin with x
        # anything within those boundaries can also be consumed
        # initial idea is to start with the first element and consume everything in the list
        # while we do so we expand in both directions if possible
        # for each pass we would have a min and max that we keep track of

        # the main concern would be in making sure we collapse all
        # when we start with something we can be certain that it is complete only at the end
        # this can be solved if we sort by the start
        # this ensures that we consume things properly
        # when we consume we can remove from the list

        intervals = sorted(intervals, key = lambda tup: tup[0])
        sol = []

        # we want to greedily add to sets
        # if we cant match it to something existing then we create a new one
        # the final step would be to collapse the resulting sets

        for (i, j) in intervals:
            if not sol or sol[-1][1] < i:
                sol.append([i, j])
                continue
            if sol[-1][1] >= i:
                sol[-1][1] = max(j, sol[-1][1])
                
        return sol




        