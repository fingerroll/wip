# join arguments should be a list
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = list(s)
        size = len(l)
        ret = []
        for i in range(size-1):
            if l[i] == '+' and l[i+1] == '+':
                ret.append(''.join(l[0:i] + ['-', '-'] + l[i+2:]))
        return ret
