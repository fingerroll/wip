# No cycles == tree
# using disjoint set
# !! no edges makes up a valid tree
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        #if not edges:
        #    return True

        parent, rank = {}, {}

        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

        def union(x, y):
            x, y = find(x), find(y)

            if x == y:
                return 0

            if rank[x] > rank[y]:
                x, y = y, x

            parent[x] = y
            rank[y] += rank[x] == rank[y]
            return 1

        count = 0
        for e in edges:
            
            if e[0] not in parent and e[1] not in parent:
                parent[e[0]] = e[1]
                parent[e[1]] = e[1]
                rank[e[0]] = 0
                rank[e[1]] = 1
                count += 1
                continue

            elif e[0] not in parent and e[1] in parent:
                parent[e[0]] = e[1]
                rank[e[0]] = 0
            
            elif e[0] in parent and e[1] not in parent:
                parent[e[1]] = e[0]
                rank[e[1]] = 0
            else:
                if find(e[0]) == find(e[1]):
                    return False

                count -= union(e[0], e[1])

        #if count > 1 or  len(parent) < n:
        #    return False

        if n - len(parent) + count > 1:
            return False
        
        return True
