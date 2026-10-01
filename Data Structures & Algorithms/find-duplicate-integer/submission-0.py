class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counted = Counter(nums)
        result = [key for key in counted.keys() if counted[key] >= 2]
        return result[0]