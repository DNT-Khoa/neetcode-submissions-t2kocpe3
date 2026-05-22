class Solution {
    public void sortColors(int[] nums) {
        int[] colors = new int[3];

        // count the number of each color
        for (int num : nums) {
            colors[num] += 1;
        }

        // override/sort the num in place
        int k = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < colors[i]; j++) {
                nums[k] = i;
                k++;
            }
        }
    }
}