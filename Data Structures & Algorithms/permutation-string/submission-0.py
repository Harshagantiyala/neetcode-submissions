class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        n1 = len(s1)
        n2 = len(s2)
        target = sorted(s1)
        for i in range(n2 - n1 + 1):
            if sorted(s2[i:n1 + i]) == target:
                return True
        return False