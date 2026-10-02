class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       nums = s.split()
       return len(nums[-1])