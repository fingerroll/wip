class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        odds = sum([1 for c in d if d[c]%2==1])

        if odds > 1:
            return []
        
        def dfs(d):
            if len(d) == 1:
                c = d.keys()[0]
                return [c*d[c]]
            res = []
            chars = d.keys()
            for c in chars:
                if d[c] >= 2:
                    d[c] -= 2
                    if d[c] == 0:
                        del d[c]
                    pas = dfs(d)
                    for pa in pas:
                        res.append(c + pa + c)
                    if c not in d:
                        d[c] = 2
                    else:
                        d[c] += 2
            return res
            
        return dfs(d)
                
        
