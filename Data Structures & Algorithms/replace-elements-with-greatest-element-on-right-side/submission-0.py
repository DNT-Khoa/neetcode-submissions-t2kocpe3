class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max_num = -1

        for i in range(len(arr) - 1, -1, -1):
            curr_num = arr[i]
            arr[i] = curr_max_num
            curr_max_num = max(curr_max_num, curr_num)

        return arr