class Solution(object):
    
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        #Use dynamic programming, but calculate the min cost total for each color on the current house
        if not costs or not costs[0]:
            return 0
        n = len(costs)
        k = len(costs[0])
        
        tmp = costs[0]
        #tmp represents the minimum costs for paiting the current house with different colors
        def combine(house, tmp):
            m, colors, i = min(tmp), len(tmp), tmp.index(min(tmp))
            l = [m] * i + [min(tmp[:i] + tmp[i+1:])] + [m] * (colors - i -1)
            return map(sum, zip(house, l))
        
        for i in range(1, n):
            tmp = combine(costs[i], tmp)

        return min(tmp)
            
                
            
        
