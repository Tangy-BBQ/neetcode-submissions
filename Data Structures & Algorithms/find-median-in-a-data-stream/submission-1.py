class MedianFinder:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = self.Node('dummy')
        self.tail = self.Node('dummy')

        self.head.next = self.tail
        self.tail.prev = self.head
        self.median = None
        self.l = 0
        

    def addNum(self, num: int) -> None:
        # print(num)
        # just keep a sorted list
        # this would likely need to be a double linked list to insert
        # this would also mean we cant simply reference the median
        # both would then be O(n)
        # if we keep track of the current median
        # we would know when to increase or decrease our index based on our inserted val
        # this would be O(n)

        # so what do we need?
        # find where to insert in our list O(n)
        # increase or decrease our median (this needs to be even/odd sensitive)
        # we keep the left of the two as the median

        new = self.Node(num)

        cur = self.head
        if self.l == 0:
            self.head.next = new
            self.tail.prev = new
            new.prev = self.head
            new.next = self.tail
            self.l += 1
            self.median = new
            return None
        # we have SOME nodes already
        i = 0
        while cur.next.data != 'dummy' and cur.next.data < num:
            
            cur = cur.next
            i += 1
        
        # now we have our location and since we use dummy we are safe from out of bounds
        # we always insert AFTER cur
        # prev = cur.prev
        # prev.next = new
        tmp = cur.next
        tmp.prev = new
        new.next = tmp
        cur.next = new

        self.l += 1

        # we now need to identify how to handle our median shifting
        # print(self.median.data, self.l, num)
        # print('if', i, self.l // 2)
        if i >= self.l // 2:
            # if we went past our previous median we need to increase it
            # HOWEVER if we are currently even we do nothing
            if self.l % 2 != 0:
                # print('inc')
                self.median = self.median.next
        else:
            if self.l % 2 == 0:
                # print('inc')
                self.median = self.median.prev





        

    def findMedian(self) -> float:
        # if we need to find median we have O(n)
        # if we keep track of len we have O(1)
        print('median', self.median.data, self.l)
        if self.l == 0:
            return 0
        if self.l % 2 == 0:
            return (self.median.data + self.median.next.data) / 2
        return self.median.data
        
        