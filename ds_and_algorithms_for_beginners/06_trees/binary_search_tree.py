from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True


def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root


def min_value_node(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


def remove(root, val):
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = min_value_node(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    return


# DFS - Depth First Search
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


# BFS - Breadth First Search (by layers)
def bfs(root):
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

