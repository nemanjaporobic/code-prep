class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.left = self.right = None

    def enqueue(self, val):
        new_node = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = new_node
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = new_node

    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None

        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val

    def print(self):
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end="")
            cur = cur.next
        print()  # new line
