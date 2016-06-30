# Forget '00' can be a number

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        sbg = ['69', '88','11', '96', '00']
        if n == 0:
            return []
        if n == 1:
            return ['0', '8', '1']
        if n == 2:
            return sbg[:4]
        
        def dfs(n):
            if n == 1:
                return ['0', '8', '1']
            if n == 2:
                return sbg
                
            ret = []
            res = dfs(n - 2)
            for s in res:
                for w in sbg:
                    ret.append(w[0] + s + w[1])
            return ret
        
        res = dfs(n)
        # remove sbgs with '0' in front
        res = [s for s in res if not s.startswith('0')]
        
        return res
        
