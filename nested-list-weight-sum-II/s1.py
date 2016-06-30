# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        def get_level(nestedList):
            level = 1
            for e in nestedList:
                if not e.isInteger():
                    level = max(level, get_level(e.getList()) + 1)
            return level
        
        def dfs(nestedList, level):
            summ = 0
            for e in nestedList:
                if e.isInteger():
                    summ += e.getInteger() * level
                else:
                    l = e.getList()
                    summ += dfs(l, level - 1)
            return summ
        
        
        return dfs(nestedList, get_level(nestedList))
