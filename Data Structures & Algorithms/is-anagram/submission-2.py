class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        counts1: dict[str, int] = {}
        counts2: dict[str, int] = {}
        for char in s:
            if char not in counts1:
                counts1[char] = 1
            else:
                counts1[char] += 1
        for char in t:
            if char not in counts2:
                counts2[char] = 1
            else: 
                counts2[char] += 1
            
        return counts1 == counts2

