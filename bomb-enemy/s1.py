# Be careful when exiting while loop, there is another element
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row_len, col_len = len(grid), len(grid[0])
        bomb = [[0]*col_len for _ in xrange(row_len)]
        
        for i in xrange(row_len):
            j = 0
            v = 0
            start = 0
            end = col_len -1
            while j < col_len:
                if grid[i][j] == 'W':
                    end = max(j-1, 0)
                    for x in xrange(start, end+1):
                        if grid[i][x] == '0':
                            bomb[i][x] = v
                    start = end = j + 1
                    v = 0
                elif grid[i][j] == 'E':
                    v += 1
                j += 1
            for x in xrange(start, col_len):
                if grid[i][x] == '0':
                    bomb[i][x] = v
        
        for j in xrange(col_len):
            i = 0
            v = 0
            start = 0
            end = row_len -1
            while i < row_len:
                if grid[i][j] == 'E':
                    v += 1
                elif grid[i][j] == 'W':
                    end = max(i-1, 0)
                    for x in xrange(start, end + 1):
                        if grid[x][j] == '0':
                            bomb[x][j] += v
                    start = end = i + 1
                    v = 0
                i += 1
            for x in xrange(start, row_len):
                if grid[x][j] == '0':
                    bomb[x][j] += v
        
        return max([max(row) for row in bomb])
