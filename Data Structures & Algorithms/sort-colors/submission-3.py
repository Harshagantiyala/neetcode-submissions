class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        current_index = 0
        while current_index <= right:
            if nums[current_index] == 0:
                nums[left], nums[current_index] = nums[current_index], nums[left]
                left += 1
                current_index += 1
            elif nums[current_index] == 2:
                nums[right], nums[current_index] = nums[current_index], nums[right]
                right -= 1
            else:
                current_index += 1