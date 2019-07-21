'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

For exaple, given 3-ary tree:

        1
        |
    3 - 2 - 4
   / \
   5  6

We should return its max depth, which is 3
'''



"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        stack = []
        if root: stack.append((1,root))
        depth = 0
        while stack:
            (d,node) = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append((d+1,child))
        return depth

