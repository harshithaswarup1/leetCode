class Solution(object):
    def transpose(self, matrix):
        #print (len(matrix))
        #trans_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        rows = len(matrix)
        cols = len(matrix[0])
        trans_matrix = [[0] * rows for _ in range(cols)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                trans_matrix[j][i] = matrix[i][j]
        return trans_matrix

solution = Solution()
result = solution.transpose([[1, 2, 3], [4, 5, 6]])        
        