# aabaa
# aabbaa

class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_pal(pivot):
            odd_length = check_pal(pivot, pivot)
            even_length = check_pal(pivot, pivot+1)

            return math.ceil(odd_length/2) + int(even_length / 2)

        
        def check_pal(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1 
            
            return r-l-1
        
        total = 0 

        for pivot in range(len(s)):
            total += count_pal(pivot)
        
        return total 