class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def bfs(root):
            if not root.left and not root.right:
                return None, [root.val]
                
            q = []
            q.append(root)
            leaves = []

            while q:
                node = q.pop()
                if node.left:
                    if not node.left.left and not node.left.right:
                        leaves.append(node.left.val)
                        node.left = None
                    else:
                        q.append(node.left)
                
                if node.right:
                    if not node.right.left and not node.right.right:
                        leaves.append(node.right.val)
                        node.right = None
                    else:
                        q.append(node.right)
                #for n in q:
                #    print n.val
                #print leaves
            return root, leaves

        if not root:
            return []

        res = []
        while root:
            root, leaves = bfs(root)
            res.append(leaves)
        return res
