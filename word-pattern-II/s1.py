# different letters should map to different string
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Using dfs with a dict to store existing patterns
        def dfs(p, s, c2s):
            
            if len(p) == len(s) == 0:
                return True
            if (len(p) == 0 and len(s) >0) or (len(p) > 0 and len(s)==0):
                return False
            
            if p[0] in c2s:
                substr = c2s[p[0]]
                if s.startswith(substr):
                    return dfs(p[1:], s[len(substr):], c2s)
                return False

            i = 1
            while i <= len(s):
                substr = s[:i]
                if substr in c2s.values():
                    i += 1
                    continue
                c2s[p[0]] = substr
                res = dfs(p[1:], s[i:], c2s)
                if res:
                    return True
                else:
                    del c2s[p[0]]
                i += 1
            return False
        return dfs(pattern, str, {})
            
            
            
