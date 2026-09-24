class LRUCache:

    class Node:
        def __init__(self, key, val):
            # Initialize a new node with data, previous, and next pointers
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = [None]*capacity
        self.cache_map = {}
        self.cur_len = 0
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        node = self.cache_map.get(key, None)
        if node is None:
            return -1
        self.mru(key)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map[key].val = value
            self.mru(key)
            return
        if self.head is None:
            new_node = self.Node(key, value)
            self.cache_map[key] = new_node
            self.head = new_node
            self.tail = new_node
            self.cur_len+=1
            return

        new_node = self.cache_map.get(key, self.Node(key, value))
        
        self.cache_map[key] = new_node
        self.cur_len += 1
        if self.cur_len > self.capacity:
            tmp = self.head
            self.head = tmp.next
            if self.head:
                self.head.prev = None
            tmp.next = None
            del self.cache_map[tmp.key]
            self.cur_len -= 1

        tmp = self.tail
        tmp.next = new_node
        new_node.prev = tmp
        self.tail = new_node  # Set tail to the new node

        self.mru(key)
        return

    def mru(self, key):
        cur_node = self.cache_map[key]
        prev_node = cur_node.prev
        next_node = cur_node.next
        # 3 cases: middle, head, tail
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
            self.tail.next = cur_node
            cur_node.prev = self.tail
            cur_node.next = None
            
        # tail
        elif prev_node:
            prev_node.next = cur_node
        # head
        elif next_node:
            next_node.prev = None
            self.head = next_node
            self.tail.next = cur_node
            cur_node.prev = self.tail
            cur_node.next = None

        self.tail = cur_node

        
