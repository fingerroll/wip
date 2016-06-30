class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return ['']
        res = self.generateAbbreviations(word[1:])
    
        ret = []
        
        for a in res:
            if a and a[0].isdigit():
                l = list(a)
                # the digit can span multiple chars
                for i, v in enumerate(l):
                    if not v.isdigit():
                        break
                if v.isdigit():
                    newint = str(int(a) + 1)
                    rest = ''
                else:
                    newint = str(int(a[:i]) + 1)
                    rest = ''.join(l[i:])

                ret.append(newint + rest)
                ret.append(word[0] + a)
            else:
                ret.append(word[0] + a)
                ret.append('1' + a)
        return ret
