#Edge case matrix = []
# Using nexted loop exceed time/list comprehension
# each element stores summation so far
# col_len not existing
# if matrix self.col_len\
# xrange using (arg1, arg2)
# 0<=col1<=col2< self.col_len instead of 0<=col1<col2<self.col_len

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col-1]

        self.matrix = matrix
        self.row_len = len(matrix)
        self.col_len = -1
        if matrix:
            self.col_len = len(matrix[0])
        
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if col == 0:
            origin = self.matrix[row][col]
        else:
            origin = self.matrix[row][col] - self.matrix[row][col-1]

        diff = val - origin

        for j in xrange(col, self.col_len):
            self.matrix[row][j] += diff
            
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        summ = 0
        row1, row2 = max(0, row1), min(row2, self.row_len)
        col1, col2 = max(0, col1), min(col2, self.col_len)
        
        if 0<= col1 <= col2 <self.col_len:
            for i in range(row1, row2 +1):
                if col1 == 0:
                    summ += self.matrix[i][col2]
                else:
                    summ += self.matrix[i][col2] - self.matrix[i][col1 - 1]
        return summ
        
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)

