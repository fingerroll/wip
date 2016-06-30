class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        array = [0] * length
        for u in updates:
            array[u[0]] += u[2]
            if u[1] < length - 1:
                array[u[1] + 1] -= u[2]
        
        summ = 0
        for i, x in enumerate(array):
            summ += x
            array[i] = summ

        return array
