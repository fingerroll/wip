# Need to understand the problem better
# if the abbreviation is unique, it means the abbreviated word not in the dictionary or only the word itself is in dictionary
# which generates the same abbreviation

from collections import defaultdict

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = defaultdict(set)
        for w in dictionary:
            a = self.abbr(w)
            self.abbrs[a].add(w)

    def abbr(self, w):
        if len(w) > 2:
            l = list(w)
            w = ''.join([l[0], str(len(l[1:-1])), l[-1]])
        return w

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        aw = self.abbr(word)
        
        return aw not in self.abbrs or self.abbrs[aw] == set([word])
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
