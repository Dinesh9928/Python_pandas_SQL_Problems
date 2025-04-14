class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col -1
        while(i <row and j >=0):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1 
            else:
                i += 1

        return False
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     if target <= matrix[i][n-1]:
        #         low, high = 0, n-1
        #         while(low <= high):
        #             mid = (low + high)//2
        #             if (matrix[i][mid] == target):
        #                 return True
        #             elif(matrix[i][mid] > target):
        #                 high = mid -1
        #             else:
        #                 low = mid + 1
        # return False

        