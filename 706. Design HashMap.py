class ListNode:
    def __init__(self,  key= -1, value=0, next=None):
        self.value = value
        self.next = next
        self.key = key

class MyHashMap:
    def __init__(self):
        constraint = 10 ** 4
        self.map = [ ListNode() for i in range(constraint)]
        
    def hash(self,key):
        return key%len(self.map)


    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        curr = self.map[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next 
        curr.next =ListNode(key,value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.map[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1
    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)