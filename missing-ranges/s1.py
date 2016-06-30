class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def format(lo, hi):
            if lo == hi:
                return '%s' % lo
            return '%s->%s' % (lo, hi) 
        
        if not nums:
            return [format(lower, upper)]
        
        ret = []
        i = 0

        nums = sorted(list(set(nums)))

        while i < len(nums):
            
            if nums[i] == lower:
                lower += 1
            else:
                ret.append(format(lower, nums[i] - 1))
                lower = nums[i] + 1
            i += 1
        if lower > upper:
            return ret
        else:
            ret.append(format(lower, upper))
            return ret
            
