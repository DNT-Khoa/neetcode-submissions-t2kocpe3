class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        def condition(idx):
            return nums[idx] >= target

        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return -1 if nums[left] != target else left