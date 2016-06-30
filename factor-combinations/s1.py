class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(low, n):
            res = []
            i = low
            while i*i <= n:
                if n % i== 0:
                    for l in dfs(i, n/i):
                        res.append([i] + l)
                i += 1
            if n >= low:
                res.append([n])
            return res

        res = dfs(2, n)
        if [n] in res:
            res.remove([n])
        return res
            
                
