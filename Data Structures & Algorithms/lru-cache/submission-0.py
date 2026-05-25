class Node:
    def __init__(self, key : int, value : int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.map:
            existing_node = self.map[key]
            self.remove(existing_node)
            self.insert_after_head(existing_node)
            return existing_node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            existing_node = self.map[key]
            existing_node.value = value
            self.remove(existing_node)
            self.insert_after_head(existing_node)
        else:
            if len(self.map) == self.capacity:
                last_node = self.tail.prev
                del self.map[last_node.key]
                self.remove(last_node)
            new_node = Node(key, value)
            self.map[key] = new_node
            self.insert_after_head(new_node)
    
    def remove(self, node: Node):
        next_node = node.next
        prev_node = node.prev
        
        prev_node.next = next_node
        next_node.prev = prev_node


    def insert_after_head(self, node):
        first_node = self.head.next

        first_node.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        

        
