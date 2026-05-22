class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length, cols = matrix[0].length;

        int left = 0, right = rows * cols - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int valueAtMid = matrix[mid / cols][mid % cols];
            if (valueAtMid < target) {
                left = mid + 1;
            } else if (valueAtMid > target) {
                right = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
