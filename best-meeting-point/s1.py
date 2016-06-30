#initialize dict as {}
# careful checking grid[x][y] == 0 instead of grid[i][j]==0
# can meet as someone's house
# do not reuse suffix
# The initial algorithm that calculates distance for each spot for each house is too time consuming
# get X coordinates of each house and calculates the sum of x-distance to the median
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        row_len = len(grid)
        col_len = len(grid[0])
        
        dgrid = {}
        
        for i in xrange(row_len):
            for j in xrange(col_len):
                if grid[i][j] == 1:
                    q = [(i,j)]
                    
                    dist = {(i,j):  0}
                    while q:
                        a, b = q.pop(0)
                        for x, y in [(a+1, b), (a-1, b),(a, b+1),(a, b-1)]:
                            if (x,y) not in dist and 0<=x< row_len and 0<=y<col_len:
                                if (x,y) in dgrid:
                                    dgrid[(x, y)] += dist[(a, b)] + 1
                                else:
                                    dgrid[(x, y)] = dist[(a,b)] + 1
                                q.append((x, y))
                                dist[(x,y)] = dist[(a,b)] + 1
        
        return min(dgrid.values())
        """
        total = 0
        for grid in grid, zip(*grid):
            X = []
            for x, row in enumerate(grid):
                X += [x]*sum(row)
            #avg = sum(X)/len(X)
            total += sum([abs(x - X[len(X)/2]) for x in X])
        return total
        
                
                                    
                            
