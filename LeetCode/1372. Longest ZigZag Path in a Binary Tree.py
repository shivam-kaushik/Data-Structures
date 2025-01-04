# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left, length):
            if not node:
                return
            self.max_length = max(self.max_length, length)

            if is_left:
                dfs(node.left, False, length + 1)
                dfs(node.right, True, 1) 
            else:
                dfs(node.right, True, length + 1)
                dfs(node.left, False, 1)

        self.max_length = 0
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.max_length
