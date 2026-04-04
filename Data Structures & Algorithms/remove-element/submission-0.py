class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, left = 0, 0
        
        for num in nums:
            if num != val:
                nums[left] = num
                left += 1
                k += 1
        return k