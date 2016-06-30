# Ask for the number combos instead of combos themselves
# So list can be sorted!

#two end move closer method
#if the sums is less than target
#plus k - j (as nums[k] becomes smaller)
#j += 1
#else k -= 1

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size < 3:
            return 0
        nums.sort()
        count = 0
        i = 0
        while i < size:
            j, k = i+1, size -1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums < target:
                    count += k -j
                    j += 1
                else:
                    k -= 1
            i += 1
                
        return count
