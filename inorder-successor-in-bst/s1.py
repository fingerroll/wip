# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        def dfs(root, p, found_p):
            
            node = None
            if root.left:
                node, found_p = dfs(root.left, p, found_p)

            if node:
                return node, True
                
            if found_p:
                return root, True
                
            if root is p:
                found_p = True
            else:
                found_p = False
                
            if root.right:
                node, found_p = dfs(root.right, p, found_p)

            return node, found_p
        node, _ = dfs(root, p, False)
        return node

