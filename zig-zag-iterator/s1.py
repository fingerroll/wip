# First Mistake being that initializing, next() need to return first element
# Second mistake is 0 can be regarded as False
# so be specific about bool checking
# Do not use next_row, col
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lists = [v1, v2]
        self.num_lists = 2
        self.cur_row = None
        self.cur_col = None


    def next(self):
        """
        :rtype: int
        """
        if self.cur_row is None:
            for row in range(self.num_lists):
                if self.lists[row]:
                    self.cur_row = row
                    self.cur_col = 0
                    break
            return self.lists[self.cur_row][0]

        for row in range(self.cur_row + 1, self.num_lists):
            if self.cur_col >= len(self.lists[row]):
                continue
            
            self.cur_row = row
            return self.lists[self.cur_row][self.cur_col]

        for row in range(0, self.cur_row + 1):
            if self.cur_col + 1 < len(self.lists[row]):
                self.cur_col += 1
                self.cur_row = row
                return self.lists[self.cur_row][self.cur_col]

    def hasNext(self):
        """
        :rtype: bool
        """
        # determine if there is next number
        # if yes set cur_row, cur_col to the correct
        if not any(self.lists):
            return False

        if self.cur_row is None:
            return True
    
        c1 = any([self.cur_col < len(self.lists[row]) -1 for row in range(self.cur_row + 1)])
        c2 = any([self.cur_col <= len(self.lists[row]) - 1 for row in range(self.cur_row + 1, self.num_lists)])
        return c1 or c2
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
