# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            count = prefix_sums.get(current_sum - targetSum, 0)

            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            prefix_sums[current_sum] -= 1

            return count

        prefix_sums = {0: 1}
        return dfs(root, 0)



# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         def countPathsFromNode(node, target):
#             if not node:
#                 return 0
#             count = 1 if node.val == target else 0
#             count += countPathsFromNode(node.left, target - node.val)
#             count += countPathsFromNode(node.right, target - node.val)
#             return count

#         if not root:
#             return 0
#         return (
#             countPathsFromNode(root, targetSum)
#             + self.pathSum(root.left, targetSum)
#             + self.pathSum(root.right, targetSum)
#         )
