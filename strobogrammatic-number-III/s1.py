import bisect

numbers = [0, 1, 6, 8, 9]

def get_count(digit_len):

    if digit_len == 1:
        return 3
    
    if digit_len % 2 == 1:
        return 3*(4*5**(digit_len/2 - 1))
    
    return 4*(5**(digit_len/2 - 1))


def below(n, include=True):
    count = 0
    
    for i in xrange(1, len(n)):
        count += get_count(i)
    
    l = sbg(len(n))

    # filter out numbers that are bigger and starts with 0
    if include:
        l = [num for num in l if (len(num)==1 or num[0]!='0') and num <= n]
    else:
        l = [num for num in l if (len(num)==1 or num[0]!='0') and num < n]


    return len(l) + count


def sbg(n):
    if n == 1:
        return ['0', '1', '8']
    
    if n == 2:
        return ['00', '11','88','69','96']
    
    res = sbg(n-2)
    ret = []
    for num in res:
        ret.append('0' + num + '0')
        ret.append('1' + num + '1')
        ret.append('6' + num + '9')
        ret.append('9' + num + '6')
        ret.append('8' + num + '8')
    return ret
        

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """

        a = below(high)
        #print high, a
        b = below(low, include=False)
        #print low, b
        return a-b if a-b > 0 else 0

        
            
            
