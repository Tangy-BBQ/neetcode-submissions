"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we are not inclusive for our upper bound
        # we need to keep track of how many things are happening simultaneously
        # if we have a new meeting we can either reuse a previous room OR open a new one
        # we just need to know how many are open at a time

        # brute force would be to check how many things overlap each and take the max
        # we can improve on this with one pass by keeping a set of open
        # we can keep a map of how many things open and close at each time

        # our one issue is that we do not know if the input is sorted
        # we may have random start times

        opening = {}
        closing = {}
        tuples = []
        times = set()

        for interval in intervals:
            start = interval.start
            end = interval.end
            tuples.append((start, end))
            times.add(start)
            times.add(end)

        for start, end in tuples:
            opening[start] = opening.get(start, 0) + 1
            closing[end] = closing.get(end, 0) + 1

        cur_total = 0
        max_total = 0

        for time in sorted(list(times)):
            cur_total += opening.get(time, 0)
            cur_total -= closing.get(time, 0)

            max_total = max(cur_total, max_total)
        return max_total

        