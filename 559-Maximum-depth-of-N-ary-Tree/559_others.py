
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1

class Solution:
    def maxDepth(self, root):
        def dfs(root):
            if not root:
                return 0
            depth = 0
            for child in root.children:
                depth = max(dsf(child),depth)
            return depth + 1
        return dfs(root)        
        