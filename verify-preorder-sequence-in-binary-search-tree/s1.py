# Using dfs method too timg consuming!!!
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        """
        def dfs(l, max_v, min_v):
            # verify preorder
            if len(l) == 0:
                return True
            
            for i in l:
                if i > max_v or i < min_v:
                    return False
            
            root_val = l[0]
            
            i = 1
            while i < len(l) - 1:
                if l[i] < root_val and l[i+1] > root_val:
                    if all([root_val < x < max_v for x in l[i+1:]]):
                        return dfs(l[1:i+1], root_val, min_v) and dfs(l[i+1:], max_v, root_val)
                    return False
                i += 1

            if all([min_v < x < root_val for x in l[1:]]):
                return dfs(l[1:], root_val, min_v)
            elif all([root_val < x < max_v for x in l[1:]]):
                return dfs(l[1:], max_v, root_val)
            else:
                return False
        """
        #if not preorder:
        #    return True
        stack = []
        low = -float('inf')
        for x in preorder:
            if x < low:
                return False
            while stack and x > stack[-1]:
                low = stack.pop()
            stack.append(x)
        return True

        
