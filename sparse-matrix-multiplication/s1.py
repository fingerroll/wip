# Brute force mulplication failed
# Read the problem carefully! This is a sparse matrix so, most elements are zeros

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        a_row = len(A)
        a_col = len(A[0])
        b_row = len(B)
        b_col = len(B[0])
        
        res = [[0]*b_col for _ in xrange(a_row)]
        
        a_dict = {}
        b_dict = {}
        for i in xrange(a_row):
            for j in xrange(a_col):
                if A[i][j] != 0:
                    a_dict[(i,j)] = A[i][j]

        for i in xrange(b_row):
            for j in xrange(b_col):
                if B[i][j] != 0:
                    b_dict[(i,j)] = B[i][j]

        for x in a_dict:
            for y in b_dict:
                if x[1] == y[0]:
                    res[x[0]][y[1]] += a_dict[x] * b_dict[y]
        
        #for i in xrange(a_row):
        #    for j in xrange(b_col):
                
        #        res[i][j] = sum([A[i][k] * B[k][j] for k in xrange(a_col)])
        return res
