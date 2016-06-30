# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while True:
            tmp = [''] * 4
            read4(tmp)
            curr = min(len(tmp), n - idx)
            for x in xrange(curr):
                buf[idx] = tmp.pop(0)
                idx += 1
            if curr == 0:
                break

        return idx

