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
class Solution:
    def maxDepth(self, root):
    	if not root: return 0
    	if not root.children: return 1
    	
    	max_depth = 1
    	queue = [(max_depth+1,node) for node in root.children]

    	for (depth,child) in queue:
    		if hasattr(child,'children'):
    			queue += [(depth+1,node) for node in child.children]
    		if max_depth<depth:
    			max_depth = depth

    	return max_depth
