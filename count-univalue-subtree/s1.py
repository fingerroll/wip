# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        def dfs(root):

            if root.left is None and root.right is None:
                return 1, True

            left_count, right_count = 0, 0

            including_left, including_right, including_root = True, True, True

            if root.left is not None:
                left_count, including_left = dfs(root.left)
                if root.val != root.left.val or not including_left:
                    including_root = False

            if root.right is not None:
                right_count, including_right = dfs(root.right)
                if root.val != root.right.val or not including_right:
                    including_root = False

            if including_root:
                count = left_count + right_count + 1
            else:
                count = left_count + right_count
                
            return count, including_root
        count, _= dfs(root)
        return count
