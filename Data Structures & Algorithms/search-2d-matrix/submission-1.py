class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # vertical binary search
        top = 0
        bottom = len(matrix)-1
        row = 0
        while top <= bottom:
            mid = (top + bottom) //2
            if matrix[mid][0] < target:
                top = mid + 1
                row = mid
            elif matrix[mid][0] > target:
                bottom = mid - 1
                row = mid - 1
            else:
                return True
        
        # horizontal binary search
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False