class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logtime = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.logtime or timestamp - self.logtime[message] >= 10:
            self.logtime[message] = timestamp
            return True

        return False
