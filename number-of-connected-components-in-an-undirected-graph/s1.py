
# not all values in (0 , n-1 ) are included in edges

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Use disjoint set method
        # define find, union method
        # each set is defined by one root
        # to find total number of sets just search the parent dict for number of nodes that points to itself
        parent, rank = {}, {}
        
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
    
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0 
            if rank[x] < rank[y]:
                x, y = y, x
            rank[y] += 1
            parent[y] = x
            return 1

        count = 0
        for x, y in edges:
            if x in parent and y not in parent:
                parent[y] = x
                rank[y] = 1
            elif x not in parent and y in parent:
                parent[x] = y
                rank[x] = 1
            elif x in parent and y in parent:
                v = union(x, y)
                count -= v
            else:
                parent[x] = y
                parent[y] = y
                rank[x] = 1
                rank[y] = 2
                count += 1
        return count + n - len(parent)
            
