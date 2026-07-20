class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = 0
        
        hs = set()
        left = 0

        streak = 0

        for (i) in range(len(s)):
            while s[i] in hs:
                hs.remove(s[left])
                left += 1 
                
                
                        
            hs.add(s[i])
            win = max(i-left + 1, win)
        
        return win 