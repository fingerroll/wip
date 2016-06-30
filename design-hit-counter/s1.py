mport bisect
#using bisect_right instead of bisect_left
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.ts.append(timestamp)
        while self.ts and timestamp - self.ts[0] > 300:
            self.ts.pop(0)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        
        idx = bisect.bisect_right(self.ts, timestamp - 300)
        return len(self.ts[idx:])
