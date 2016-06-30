# Forget checking invalid rules
# when making twos, need to break the loop once a letter is different than the other

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # First zip every two word together
        # Then for each pair of words, zip the letters
        # zip first letters of all 2-len words and then second letters
        
        twos = []
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    twos.append(a+b)
                    break
        
        # obtained a list of two letter words
        # zip the two-letter list
        alpha = set(''.join(words))
        order = []
        while twos:
            # Get the lexicographally high chars
            chars = alpha - set(zip(*twos)[1])
            
            if not chars:
                # invalid rules
                # as all the lower order chars making up the whole alphabet
                return ''
            # chars will be cast to list
            order += chars
            # Filter out two-letter words with c in chars
            twos = filter(chars.isdisjoint, twos)
            alpha -= chars
        return ''.join(order + list(alpha))
        
        
        

        
