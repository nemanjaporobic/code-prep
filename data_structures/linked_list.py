from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> bool:
        new_node = ListNode(val)
        i = 0
        curr = self.head
        while i < index and curr.next:
            i += 1
            curr = curr.next
        if i == index:
            new_node.next = curr.next
            curr.next = new_node
            if not new_node.next:
                self.tail = new_node
            return True
        return False

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


if __name__ == "__main__":
    # Test case:
    # ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
    ll = LinkedList()
    print(f"Init linked list: {ll.getValues()}")
    ll.insertHead(1)
    print(f"Insert head with val 1: {ll.getValues()}")
    ll.insertTail(2)
    print(f"Insert tail with val 2: {ll.getValues()}")
    ll.insertHead(0)
    print(f"Insert head with val 0: {ll.getValues()}")
    ll.remove(1)
    print(f"Remove el at index 1: {ll.getValues()}")

    print("--------------------------------------------")
    # Test case:
    # ["insertHead", 1, "insertHead", 2, "get", 5]
    ll = LinkedList()
    print(f"Init linked list: {ll.getValues()}")
    ll.insertHead(1)
    print(f"Insert head with val 1: {ll.getValues()}")
    ll.insertHead(2)
    print(f"Insert head with val 2: {ll.getValues()}")
    print(f"Get el at 5 index: {ll.get(5)}")
    ll.addAtIndex(1, 10)
    print(f"Insert 10 at index 1: {ll.getValues()}")
