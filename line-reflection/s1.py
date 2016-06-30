class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True

        min_x = min([x[0] for x in points])
        max_x = max([x[0] for x in points])
        
        mid = (min_x + max_x) / 2.0
        
        def reflect(x, mid):
            return mid*2 - x
        
        points = set([(p[0], p[1]) for p in points])
        for p in points:
            if p[0] != mid:
                if (reflect(p[0], mid), p[1]) not in points:
                    return False
        return True
