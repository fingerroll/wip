# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        
        lroot = self.upsideDownBinaryTree(root.left)
        rmost = lroot
        while rmost.right:
            rmost = rmost.right
        
        root, rmost.left, rmost.right = lroot, root.right, TreeNode(root.val)
        return root
                
        
