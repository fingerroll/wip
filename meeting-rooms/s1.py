# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        
        def overlap(itv1, itv2):
            return itv1.start < itv2.end and itv2.start < itv1.end
        
        for i in range(len(intervals)-1):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
                else:
                    break
        return True
