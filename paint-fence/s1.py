class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k

        i = 2
        same, diff = k, k*(k-1)
        while i < n:
            i += 1
            same, diff = diff, same*(k-1) + diff*(k-1)
        return same + diff
            
