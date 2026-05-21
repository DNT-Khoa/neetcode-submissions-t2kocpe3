class Solution {
    public int[] sortArray(int[] nums) {
        return quickSort(nums, 0, nums.length - 1);
    }

    static int[] quickSort(int[] nums, int start, int end) {
        if (end - start + 1 <= 1) return nums;

        int pivot = nums[end];
        int left = start;

        for (int i = start; i < end; i++) {
            if (nums[i] < pivot) {
                int temp = nums[left];
                nums[left] = nums[i];
                nums[i] = temp;
                left++;
            }
        }

        nums[end] = nums[left];
        nums[left] = pivot;

        quickSort(nums, start, left - 1);
        quickSort(nums, left + 1, end);
        return nums;
    }
}