# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is not None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.left = None
            root.right = self.prev
            self.prev = root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        stack = [root]
        
        while stack:
            current = stack.pop()
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
            if stack:
                current.right = stack[-1]
            
            current.left = None





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        right_subtree = root.right
        
        root.right = root.left
        root.left = None
        
        current = root
        while current.right:
            current = current.right
        
        current.right = right_subtree

        