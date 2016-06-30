# consider the rotate case
# total 26 chars
import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        offsets = collections.defaultdict(list)
        for s in strings:
            if len(s) == 1:
                offsets['single'].append(s)
            else:
                offset = []
                for i in range(1, len(s)):
                    
                    offset.append((ord(s[i]) - ord(s[i-1])) % 26)
                offset = tuple(offset)
                offsets[offset].append(s)
        return offsets.values()
                
                
                
