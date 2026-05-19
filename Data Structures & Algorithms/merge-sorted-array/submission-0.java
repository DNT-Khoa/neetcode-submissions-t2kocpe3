class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums1Temp = new int[m];
        for (int i = 0; i < m; i++) {
            nums1Temp[i] = nums1[i];
        }

        int p1 = 0, p2 = 0, k = 0;
        while (p1 < m && p2 < n) {
            if (nums1Temp[p1] <= nums2[p2]) {
                nums1[k] = nums1Temp[p1];
                p1++;
            } else {
                nums1[k] = nums2[p2];
                p2++;
            }
            k++;
        }

        while (p1 < m) {
            nums1[k] = nums1Temp[p1];
            p1++;
            k++;
        }

        while (p2 < n) {
            nums1[k] = nums2[p2];
            p2++;
            k++;
        }
    }
}