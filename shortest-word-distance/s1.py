class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # calculating a running minimum
        # the min distance is calculated using the last seen other word index
        
        distance = float('inf')
        i1 = i2 = -1
        res = float('inf')
        for i, w in enumerate(words):
            if w == word1:
                if i2 != -1:
                    res = min(res, abs(i-i2))
                i1 = i
            if w == word2:
                if i1 != -1:
                    res = min(res, abs(i-i1))
                i2 = i
        return res
                    
                    
        
        
