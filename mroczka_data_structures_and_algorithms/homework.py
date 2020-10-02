from tree_helpers import TreeNode,pre_order_traversal
"""
Assume for all questions your answers can be either:
1) O(1)
2) O(log N)
3) O(N)
4) O(N*logN)
5) O(N^2)
6) O(N^3)
7) O(2^N)
8) O(3^N)
9) O(N!)
"""

def question_1(arr):
    for i in range(len(arr) / 2):
        other = len(arr) - i - 1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp


QUESTION_1_ANSWER = 0  # change to value you believe to be correct


def question_2(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum


QUESTION_2_ANSWER = 0  # change to value you believe to be correct


def question_3(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return question_3(n - 1) + question_3(n - 2)


QUESTION_3_ANSWER = 0  # change to value you believe to be correct


def repeat(n):
    for i in range(n):
        print(f'{i}: {question_4(i)}')


def question_4(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return question_4(n - 1) + question_4(n - 2)


# we'd analyze by starting at repeat() with some value, for instance, something like...
# repeat(15)
QUESTION_4_ANSWER = 0  # change to value you believe to be correct


def question_5(word1, word2, i, j):
    if i == len(word1):
        return len(word2) - j
    if j == len(word2):
        return len(word1) - i

    if word1[i] == word2[j]:  # letters match in both words!
        return 0 + question_5(word1, word2, i + 1, j + 1)

    insert_letter = 1 + question_5(word1, word2, i + 1, j)
    delete_letter = 1 + question_5(word1, word2, i, j + 1)
    substitute_letter = 1 + question_5(word1, word2, i + 1, j + 1)

    return min(insert_letter, delete_letter, substitute_letter)


QUESTION_5_ANSWER = 0  # change to value you believe to be correct

'''
Which of the following are equivalent to O(N)?
  A) O(N + P), where P < N/2
  B) O(2N)
  C) O(N + log N)
  D) O(N + M)
'''
QUESTION_6_ANSWER = ['A', 'B', 'C', 'D']  # multiple values are possible, remove the ones you disagree with

'''
BALANCED BINARY TREE
Review FULL question at this link:
https://i.imgur.com/d1sroyH.png

Test inputs copied for your convenience. Work _inside_ the function. Do not change it. You shouldn't have to edit the
tests to achieve a valid answer. Just fill in the function and feel free to make helper functions.
'''

class Solution(object):
    def __init__(self, tree):
        self.root = tree

    def get_balanced_binary_tree(self):
        return self.is_balanced(self.root)

    def is_balanced(self, root):
        # TODO: Write your code here
        pass

'''
    3            # height 1
   / \
  9  20          # height 2
    /  \
   15   7        # height 3
IS BALANCED --> Return True
'''
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
'''
        1
       / \
      2   2
     / \
    3   3
   / \
  4   4
  IS NOT BALANCED --> Return False
'''
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)

print('TREE TESTS')
print('TREE 1')
solver = Solution(root1)
print(f'Tree one is_balanced answer: {solver.get_balanced_binary_tree()}\n')

print('TREE 2')
solver = Solution(root2)
print(f'Tree two is_balanced answer: {solver.get_balanced_binary_tree()}')
'''
Review FULL question at this link:
https://i.imgur.com/HIhBPTk.png

Test inputs copied for your convenience. Work _inside_ the function. Do not change it. You shouldn't have to edit the
tests to achieve a valid answer. Just fill in the orangeRotting function and feel free to make helper functions.
'''


def orangesRotting(matrix):
    # TODO: Write your code here
    pass


print('\n\n======= GRAPHS ========')
print('Public tests for Rotting Oranges question')
matrix = [[2, 1, 1],
          [1, 1, 0],
          [0, 1, 1]]
print(orangesRotting(matrix) == 4)
matrix = [[0, 2]]
print(orangesRotting(matrix) == 0)


'''
MINE SWEEPER
Review FULL question at this link:
https://i.imgur.com/D8I2PiZ.png

Test inputs copied for your convenience. Work _inside_ the function. Do not change it. You shouldn't have to edit the
tests to achieve a valid answer. Just fill in the orangeRotting function and feel free to make helper functions.
'''


def minesweeper(matrix):
    # TODO: Write your code here
    pass


print('\n\nPublic tests for Minesweeper question')
board = [['E','E','E','E','E'],
         ['E','E','M','E','E'],
         ['E','E','E','E','E'],
         ['E','E','E','E','E']]

expected_ouput = [['B','1','E','1','B'],
                  ['B','1','M','1','B'],
                  ['B','1','1','1','B'],
                  ['B','B','B','B','B']]

print(minesweeper(board) == expected_ouput)
board = [['B','1','E','1','B'],
         ['B','1','M','1','B'],
         ['B','1','1','1','B'],
         ['B','B','B','B','B']]

expected_ouput = [['B','1','E','1','B'],
                  ['B','1','X','1','B'],
                  ['B','1','1','1','B'],
                  ['B','B','B','B','B']]
print(minesweeper(board) == expected_ouput)
