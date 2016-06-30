class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        sbg = {'6':'9', 
               '9':'6',
               '8':'8',
               '1':'1',
               '0':'0'
               }
        s = ''
        for i in num:
            if i not in sbg:
                return False
            s = sbg[i] + s
        return s == num
        
