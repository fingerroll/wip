# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#BST, the maximum of left tree < root < the minimum of the right tree
#Use -inf/inf as default for max/min value so that the bst requirement is always met
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root):
            if root is None:
                return 0, 0, -float('inf'), float('inf')
            N1, n1, ma1, mi1 = dfs(root.left)
            N2, n2, ma2, mi2 = dfs(root.right)
            if  ma1 < root.val < mi2:
                n = n1 + n2 + 1
            else:
                n = float('-inf')
            
            return max(N1, N2, n), n, max(ma1, ma2, root.val), min(mi1, mi2, root.val)

        N, n, ma, mi = dfs(root)
        
        return N
