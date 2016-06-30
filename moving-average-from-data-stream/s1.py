class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.buffer = []        
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.buffer) < self.size:
            self.buffer.append(val)
        else:
            self.buffer.pop(0)
            self.buffer.append(val)
        return sum(self.buffer)/float(len(self.buffer))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
