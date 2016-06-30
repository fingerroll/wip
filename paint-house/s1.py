class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        
        n = len(costs)
        
        tmp = costs[0]
        
        def combine(tmp, house):
            m, i = min(tmp), tmp.index(min(tmp))
            tmp = [m]*i + [min(tmp[:i] + tmp[i+1:])] + [m]*(2-i)
            return map(sum, zip(house, tmp))
        
        for house in costs[1:]:
            tmp = combine(tmp, house)
        
        return min(tmp)
        
