class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def pre_order_traversal(root):
    if not root: return
    print(root.value, end=' ')
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)
