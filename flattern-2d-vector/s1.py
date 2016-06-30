class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.cur_col = None
        self.cur_row = None
        self.row_num = len(vec2d)
        self.empty = not (self.vec2d and any([row for row in self.vec2d]))

    def next_row(self):
        if self.cur_row is None:
            new_row = 0
        else:
            new_row = self.cur_row + 1
        
        for idx, row in enumerate(self.vec2d[new_row:]):
            if row:
                return idx + new_row

        return False


    def next(self):
        """
        :rtype: int
        """

        if self.cur_row is None:
            self.cur_row = self.next_row()
            self.cur_col = 0
        
        elif self.cur_col < len(self.vec2d[self.cur_row]) - 1:
            self.cur_col += 1
            
        else:
            self.cur_row = self.next_row()
            self.cur_col = 0
        return self.vec2d[self.cur_row][self.cur_col]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur_row is None:
            return not self.empty

        next_on_cur_row = (self.cur_col < len(self.vec2d[self.cur_row]) - 1)
        return next_on_cur_row or self.next_row()

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
