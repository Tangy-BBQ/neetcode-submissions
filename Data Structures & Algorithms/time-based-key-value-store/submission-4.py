class TimeMap:

    def __init__(self):
        # create a map from a value to a list of timestamps stored in increasing order
        # the list needs to be the size of the latest time stamp (seems space inefficient) 
        # or it could be a tuple with the first value as the timestamp (is less time efficient)
        # if we have a map of maps then we can have O(1) time and O(timestamps) space
        # do we need to worry about multiple sets with 1 timestamp?

        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamps = self.vals[key]

        if len(timestamps) == 0:
            timestamps.append((timestamp, value))
            return
        print(timestamps)
        i = 0
        cur = timestamps[i]
        while i < len(timestamps) - 1 and cur[0] < timestamp:
            i += 1
            cur = timestamps[i]
        # we can now insert the value at this timestamp in order
        timestamps.insert(i + 1, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # print(key, timestamp)

        timestamps = self.vals[key]

        if len(timestamps) == 0 or timestamps[0][0] > timestamp:
            return ""
        # print(timestamps)
        # i = -1
        # cur = (0, 0)
        # while i < len(timestamps) and cur[0] < timestamp:
        #     print(i, i < len(timestamps) - 1, cur[0] < timestamp)
            
        #     cur = timestamps[i]
        #     i += 1
        # print(cur, i)
        # return timestamps[i][1]


        i = 0

        while i + 1 < len(timestamps) and timestamps[i + 1][0] <= timestamp:
            i += 1

        return timestamps[i][1]
        
