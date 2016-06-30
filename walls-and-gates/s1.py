# Recursion limit is too low to pass all tests
# Using stack for dfs can be useful
INF = 2147483647
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        row_len = len(rooms)
        col_len = len(rooms[0])
        stack = []
        dirs = [[0, 1],[0, -1],[1, 0],[-1, 0]]

        for i in range(row_len):
            for j in range(col_len):
                if rooms[i][j] == 0:
                    for d in dirs:
                        stack.append(d + [1])
                    while stack:
                        [d0, d1, v] = stack.pop()
                        ni, nj = i + d0, j + d1
                        if 0 <= ni < row_len and 0 <= nj < col_len and rooms[ni][nj] > rooms[i][j] + v:
                            rooms[ni][nj] = rooms[i][j] + v
                            for d in dirs:
                                stack.append([d0 + d[0], d1 + d[1], v + 1])

                        
            
