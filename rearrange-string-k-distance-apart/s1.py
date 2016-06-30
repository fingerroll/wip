# store the frequecy of the chars 
# sort them from big to small in freq
# greedy: use the char with biggest freq, if it does not work, use the second biggest, if all tried and not working, fail...
# steps >= k - 1
# list.sort(key=lambda x: fun(x))

class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        freq = {}
        for i in str:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        steps = {}
        
        res = []
        while freq:
            l = freq.keys()
            l.sort(key=lambda x:freq[x], reverse=True)
            for char in l:
                if char not in steps or steps[char] >= k:
                    res.append(char)
                    for key in steps:
                        steps[key] += 1
            
                    steps[char] = 1
                    if freq[char] == 1:
                        del freq[char]
                    else:
                        freq[char] -= 1
                    break
            else:
                return ''
        return ''.join(res)
