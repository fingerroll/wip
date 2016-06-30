
from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        
        self.d = defaultdict(list)
        for i,w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a, b= self.d[word1], self.d[word2]
        m, n, i, j = len(a), len(b), 0, 0
        res = float('inf')
        
        while i < m and j < n:
            idx1, idx2 = a[i], b[j]
            
            if idx1 > idx2:
                res = min(res, idx1 - idx2)
                j += 1
            else:
                res = min(res, idx2 - idx1)
                i += 1

        return res
        
        
            
                    
        
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
