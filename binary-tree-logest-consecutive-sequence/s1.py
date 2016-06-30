# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root is None:
                return 0, 0

            left1, left2 = dfs(root.left)
            right1, right2 = dfs(root.right)
            
            if root.left is not None and root.val + 1 == root.left.val:
                with_root_left = left1 + 1
            else:
                with_root_left = 1
                
            if root.right is not None and root.val + 1 == root.right.val:
                with_root_right = right1 + 1
            else:
                with_root_right = 1

            return max(with_root_left, with_root_right), max(left1, left2, right1, right2)
        
        r1, r2 = dfs(root)
        return max(r1, r2)
