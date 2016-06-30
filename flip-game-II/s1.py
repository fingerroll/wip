# Time limit exceeded
# Wrong answer '++'
# string find >=0 means a pattern found not just > 0
# copied solution and forget return True
class Solution(object):


    def __init__(self):
        self.result = {}

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        res = self.after_flip(s)
        if not res:
            return False
        
        for flip in res:
            res = self.after_flip(flip)
            if not res:
                return True
            for flip_again in self.after_flip(flip):
                if not self.canWin(flip_again):
                    break
            else:
                return True
        return False
        """
        if s in self.result:
            return self.result[s]
        
        for i in range(len(s) -1):
            if s[i:i+2] == '++':
                if not self.canWin(s[:i] + '--' + s[i+2:]):
                    self.result[s[:i] + '--' + s[i+2:]] = False
                    self.result[s] = True
                    return True
        return False
                    
        
