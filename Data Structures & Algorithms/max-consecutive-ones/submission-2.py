class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = 0
        tmp_counter = 0

        for num in nums:
            if num == 1:
                tmp_counter += 1
                max_num = max(max_num, tmp_counter)
            else:
                tmp_counter = 0
        return max_num