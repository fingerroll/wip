#careful to handle remainings at the end of while loop
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            return sum([1 for i in xrange(len(s)) if s[i]!=t[i]]) == 1
        
        if len(s) > len(t):
            s, t = t, s
        
        if len(t) - len(s) == 1:
            i = 0
            j = 0
            while i < len(s):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                    continue
                return s[i:] == t[j+1:]
            return True
        return False           
