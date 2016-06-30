class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        chars = {}
        
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        odds = sum([ 1 for c in chars if chars[c] % 2 == 1])
        return odds <= 1
