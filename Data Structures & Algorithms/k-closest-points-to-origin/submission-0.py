import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(x1, y1, x2, y2):
            return (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

        priority_queue = []

    

        # brute force is to just check all points and keep a priority queue of the min
        # we can do this in O(n) if we dont need to sort and keep our queue maintained
        # we could also use some kind of min heap etc
        # basically we have O(n) to find the distances and then O(sort/store)
        # the max of these is our time

        for point in points:
            cur_dist = dist(point[0], point[1], 0, 0)

            heapq.heappush(priority_queue, (cur_dist, point))

        final = []
        for _ in range(k):
            final.append(heapq.heappop(priority_queue)[1])

        return final

        