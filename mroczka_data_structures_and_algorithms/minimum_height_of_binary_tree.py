from tree_helpers import TreeNode,pre_order_traversal

class Solution(object):
    def __init__(self, tree):
        self.root = tree

    def get_max_height(self):
        return self.maxHeight(self.root)

    def maxHeight(self, root):
        if not root: return 0
        l = self.maxHeight(root.left)
        r = self.maxHeight(root.right)
        return max(l, r) + 1



if __name__ == "__main__":

    '''
        3            # height 1
       / \
      9  20          # height 2
        /  \
       15   7        # height 3
    '''
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    '''
            3            # height 1
           / \
          9  20          # height 2
            /  \
           15   7        # height 3
          / \
         13  19          # height 4
        /
       10                # height 5
    '''
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    root2.right.left.left = TreeNode(13)
    root2.right.left.right = TreeNode(19)
    root2.right.left.left.left = TreeNode(10)

    print('TREE TESTS')
    print('TREE 1')
    print('Pre-order traversal for tree is:')
    pre_order_traversal(root1)
    solver = Solution(root1)
    print(f'\nThe height of the given tree is: {solver.get_max_height()}\n')

    print('TREE 2')
    print('Pre-order traversal for tree is:')
    pre_order_traversal(root2)
    solver = Solution(root2)
    print(f'\nThe height of the given tree is: {solver.get_max_height()}')


