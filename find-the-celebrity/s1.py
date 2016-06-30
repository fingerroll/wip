# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
import copy

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        # for each i, if the current celebrity knows the i, then celebrity should be i.
        for i in xrange(n):
            if knows(x, i):
                x = i

        know_x = all([knows(i,x) for i in xrange(n)])
        x_know = any([knows(x, i) for i in xrange(n) if i!=x ])
        
        if know_x and not x_know:
            return x
        else:
            return -1
                
                
            
                
