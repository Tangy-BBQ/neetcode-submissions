class CountSquares:
    # ok so for our checking we can do a few things
    # if we have a point we must find 3 other points in any of 4 directions
    # if we find a point that is valid we know what the other two must be
    # if they exist we continue, otherwise we are invalid and continue
    # we could try to iterate using all points and check if x or y matches and go from there
    # we would have an O(n^2) operation to check all points
    # we can improve on this if we use a x->y map and a y->x map and sets

    # duplicates make this a bit confusing, we must count double
    # this means we can use memozation for duplicates

    def __init__(self):
        self.xy = {}
        self.yx = {}
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        # self.points.append(point)
        self.points[(point[0], point[1])] = self.points.get((point[0], point[1]), 0) + 1

        cur = self.xy.get(point[0], set())
        cur.add(point[1])
        self.xy[point[0]] = cur

        cur = self.yx.get(point[1], set())
        cur.add(point[0])
        self.yx[point[1]] = cur
        

    def count(self, point: List[int]) -> int:
        # now we can simply check what will work
        # we can operate based on the following

        # we find all valid starts for x and y and add them to a set of points
        # we then must check of these which have a full square given the first line length

        # our problem is that we need to check each existing point with dups

        # we know that if we have any squares we will have the opposite corner
        # however we would need to know the distance of the corners?

        # now we just check if the two corners are valid
        # our problem is that we no longer have the correct count

        x1 = point[0]
        y1 = point[1]

        count = 0
        # print('test')
        for x2, y2 in self.points:
            if abs(x1 - x2) != abs(y1 - y2) or x1 == x2:
                continue
            # print(x2, y2)
            # we have two opposite corners
            # we simply check if the two options work
            if x1 in self.yx[y2] and y1 in self.xy[x2]:
                cur = math.comb(self.points[(x2, y2)], 1) * math.comb(self.points[(x1, y2)], 1) * math.comb(self.points[(x2, y1)], 1)
                count += cur
                # print('found')
        return count