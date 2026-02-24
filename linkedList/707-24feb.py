class Node:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length: return -1
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val


    def addAtHead(self, val: int) -> None:
        newHead = Node(val, self.head)
        self.head = newHead
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.length+=1
            return
        l = self.length-1
        cur = self.head
        while l:
            cur = cur.next
            l-=1
        cur.next = Node(val)
        self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length : return
        if index == 0: 
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        cur = self.head
        index -= 1
        while index:
            cur = cur.next
            index -= 1
        cur.next = Node(val, cur.next)
        self.length+=1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length : return
        # LL me 1 hi node h
        if self.length == 1:
            self.head = None
            self.length -= 1
            return
        # removal at head
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        # removal at tail
        if index == self.length - 1:
            l = self.length - 2
            cur = self.head
            while l :
                cur = cur.next
                l -= 1
            cur.next = None
            self.length -= 1
            return
        # normal index removal
        l = index - 1
        cur = self.head
        while l : 
            cur = cur.next
            l-=1
        cur.next = cur.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# 19
# 234
