# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#Sort by start, so each room just remember the end
# if the new interval start is less than the end time of a room
# then it is surely will be overlapping with the interval

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        rooms = []
        intervals = sorted(intervals, key=lambda x: x.start)

        rooms = [intervals[0].end]
        for itv in intervals[1:]:
            j = 0
            while j < len(rooms):
                if rooms[j] <= itv.start:
                    rooms[j] = itv.end
                    break
                j += 1
            else:
                rooms.append(itv.end)
        return len(rooms)
                

    
