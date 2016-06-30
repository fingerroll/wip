class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        
        i = start = 0
        j = end = len(s) - 1
        
        while True:
            while i < j and s[i] != ' ':
                i += 1
            
            if i >= j:
                return

            while j > i and s[j] != ' ':
                j -= 1
    
            tmp = s[start:i]
            
            s[start:i] = s[j+1:end+1]
            
            diff = (end - j) - (i - start)
            s[j+1+diff:end+1+diff] = tmp
            
            start, end  = start + end - j + 1, end - (i - start + 1)
            i = start
            j = end
        
            
