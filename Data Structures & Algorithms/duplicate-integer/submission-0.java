class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> visited = new HashSet<>();

        for (int num : nums) {
            visited.add(num);
        }

        return visited.size() != nums.length;
    }
}