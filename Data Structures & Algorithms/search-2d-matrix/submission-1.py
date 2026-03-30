class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        def getNum(idx):
            row = idx // N
            col = idx % N
            return matrix[row][col]

        left, right = 0, M * N - 1

        while left < right:
            mid = left + (right - left) // 2

            if getNum(mid) >= target:
                right = mid
            else:
                left = mid + 1

        return getNum(left) == target
    