# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# waste hours on over-complicated recursion solution

import collections

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, x = queue.pop(0)
            if node:
                cols[x].append(node.val)
                queue += (node.left, x-1), (node.right, x+1)
        
        return [cols[x] for x in sorted(cols.keys())]
        


        
