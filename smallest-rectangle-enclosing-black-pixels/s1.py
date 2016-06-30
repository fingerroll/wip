# max/min initialized to be the starting x, y instead of infinity
# careful with poped out subfix and the initial subfix
# read the problem the image is a list of strings
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        max_row, max_col = x, y
        min_row, min_col = x, y
        
        if not image:
            return 0
        row_len = len(image)
        
        if not image[0]:
            return 0
        col_len = len(image[0])
        
        q = [(x,y)]
        visited = {}
        while q:
            x, y  = q.pop(0)
            for i, j in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
                if 0<=i<row_len and 0<=j< col_len and (i,j) not in visited and image[i][j] == '1':
                    max_row = max(i, max_row)
                    max_col = max(j, max_col)
                    min_row = min(i, min_row)
                    min_col = min(j, min_col)
                    visited[(i,j)] = True
                    q.append((i,j))
        return (max_row - min_row + 1) * (max_col - min_col + 1)
        
