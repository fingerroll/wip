# 1. global populate not defined
# 2. wrong answer for test case [[1]] # consider edge case
# 3. wrong answer [[0,2,1],[1,0,2],[0,1,0]] # need to understand the problem better
# 4. typo houst should be house
# 5. should initialize house_cnt[(i, j)] to be 1 first time instead of 0
# 6. add pruning when populating a house that is not reachable
# 7. breath first search should always pop 0!!!!

class Solution(object):
    
    def shortestDistance(self, grid):
        # populate grid with distance to the house at i, j
        def populate(grid, i,j, house_cnt, houses):
            q = []
            dist = {(i,j): 0}
            q.append([i,j])
            
            row_len = len(grid)
            col_len = len(grid[0])
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            reach = 0
            while q:
                [x, y] = q.pop(0)
                val = dist[(x,y)]
                for direction in dirs:
                    new_i, new_j = x+ direction[0], y+ direction[1]
                    
                    if 0<=new_i<row_len and 0<=new_j<col_len and grid[new_i][new_j] not in [-1, -2]\
                        and (new_i, new_j) not in dist:
                            reach = 1
                            dist[(new_i, new_j)] = val + 1
                            q.append([new_i, new_j])
                            grid[new_i][new_j] += val + 1
                            if (new_i, new_j) in house_cnt:
                                house_cnt[(new_i, new_j)] += 1 
                            else:
                                house_cnt[(new_i, new_j)] = 1
            if reach == 0:
                return False
            return True
        
        # For each house, populate all the locations with distances
        row_len = len(grid)
        col_len = len(grid[0])
        
        grid = map(lambda x: map(lambda y: -1 * y, x), grid)

        houses = sum([1 for i in range(row_len) for j in range(col_len) if grid[i][j]==-1])
        house_cnt = {}
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == -1:
                    if not populate(grid, i, j, house_cnt, houses):
                        return -1
        
        min_distance = float('inf')
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] > 0 and house_cnt[(i, j)] == houses:
                    min_distance = min(min_distance, grid[i][j])
        if min_distance == float('inf'):
            return -1
        return min_distance

"""
class Solution(object):
    def shortestDistance(self, grid):
        if not grid or not grid[0]: return -1
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]
    
        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings  
    
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y): return -1
        
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])
"""
                
                
                
