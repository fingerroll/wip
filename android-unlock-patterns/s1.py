import re
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Using backtracking method
        patterns = [['']]
        bad = '[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|91|46|64|37|73|28|82)'
        bad = re.compile(bad).match
        i = 1
        while i <= n:
            new_ps = []
            
            for p in patterns[-1]:
                for c in '123456789':
                    if c not in p:
                        new_p = p + c
                        if not bad(new_p):
                            new_ps.append(new_p)
            patterns.append(new_ps)
            
            # patterns += [ p + c for p in patterns[-1] for c in '123456789' if c not in p and not bad(p+c)]
            
            i += 1
        return sum(map(len, patterns[m:n+1]))
