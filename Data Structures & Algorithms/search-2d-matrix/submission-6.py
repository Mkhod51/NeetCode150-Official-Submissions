class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0 
        right = rows * columns - 1 

        while left <= right:
            mid = int(left + (right - left) / 2)

            x = mid // columns
            y = mid % columns


            if matrix[x][y] == target:
                return True 

            if target > matrix[x][y]:
                left = mid + 1
            else:
                right = mid - 1

        return False
        

            

