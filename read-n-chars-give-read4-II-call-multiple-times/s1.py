#Error 1: forgot the case when n == 0 return ''
#Error 2: Need to understand the problem better, read api is about reading n chars into buf, read4 reads 4 chars into buf
#Error 3: 
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        self.queue = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        idx = 0
        while True:
            tmp = ['']*4
            read4(tmp)
            self.queue.extend(tmp)
            curr = min(len(self.queue), n - idx)
            for i in xrange(curr):
                buf[idx] = self.queue.pop(0)
                idx += 1
            if curr == 0:
                break
            
        return idx
        

