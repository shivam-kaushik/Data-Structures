# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        
        # BFS traversal
        queue = [root]
        result = []
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        i = 1
        
        while queue:
            current = queue.pop(0)
            if nodes[i] != "null":
                current.left = TreeNode(int(nodes[i]))
                queue.append(current.left)
            i += 1
            if nodes[i] != "null":
                current.right = TreeNode(int(nodes[i]))
                queue.append(current.right)
            i += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))