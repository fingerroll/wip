# O(n^2) solution time exceeded

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Using map to store the accu
        ans, acc = 0, 0

        mp = { 0: -1 }
        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in mp:
                mp[acc] = i
            v = acc - k
            if v in mp:
                ans = max(ans, i - mp[v])

        return ans
            
        
