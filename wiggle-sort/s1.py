class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        snums = sorted(nums)
        
        for x in range(1, size, 2) + range(0, size, 2):
            v = snums.pop()
            nums[x] = v
        
