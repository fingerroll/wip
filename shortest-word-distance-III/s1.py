class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = i2 = j= -1
        res = float('inf')
        
        if word1 == word2:
            for i, w in enumerate(words):
                if w== word1:
                    if j != -1 :
                        res = min(abs(i-j), res)
                    j = i
            if res==float('inf'):
                return 0
            return res
                
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
                if i2!= -1:
                    res = min(abs(i1 - i2), res)
            elif w == word2:
                i2 = i
                if i1!= -1:
                    res = min(abs(i1-i2), res)
        return res
                
