# return sort results
# x^2 should be x*x or x**2
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        return sorted(map(lambda x: a* (x*x) + b*x + c, nums))
