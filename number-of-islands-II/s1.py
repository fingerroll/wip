# 4 directions typo
# when counting the first position, no results in ret yet
# an added land can connect two islands
# careful when using index, might overwrite sufix i,j
# careful doing list operaion with + and append
# using set to deduplicate 
# using set to check contain o(1)
# set.union won't change set in-place
# check matrix boundary

class Solution(object):


    def numIslands2(self, m, n, positions):
        parent, depth = {}, {}
        
        def find(x):
            # Find the root of the set
            if parent[x] == x:
                return x
            return find(parent[x])

        def union(x, y):
            # union two sets, each including x and y
            x, y = find(x), find(y)
            if x == y:
                return 0
            if depth[x] > depth[y]:
                x, y = y, x
            parent[x] = y
            # the depth is only increased if the depth of x and y are equal
            depth[y] += depth[x] == depth[y]
            return 1

        counts, count = [], 0

        for x, y in positions:
            parent[(x,y)] = (x,y)
            depth[(x,y)] = 0
            for i, j in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
                if (i, j) in parent:
                    v = union((x,y), (i,j))
                    count -= v
            count += 1
            counts.append(count)
        return counts
                    
        
        
