class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Using sliding window approach
        if not s:
            return 0
        size = len(s)
        i, j = 0, 0
        chars = {}
        longest = 0

        while i <= j and j < size:
            if len(chars) == 2 and s[j] not in chars:
                while i<=j and len(chars) == 2:
                    chars[s[i]] -= 1
                    if chars[s[i]] == 0:
                        del chars[s[i]]
                    i += 1
            else:
                if s[j] in chars:
                    chars[s[j]] += 1
                else:
                    chars[s[j]] = 1
                j += 1
                longest = max(longest, j - i)

        return longest
