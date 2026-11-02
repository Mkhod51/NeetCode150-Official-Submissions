class Solution:
    # [d,a,a,b,a,a,c]
    def longestPalindrome(self, s: str) -> str:
        best = 0
        final_l = 0
        final_r = 0 

        def get_palindrome_pivot(pivot):
            #If odd
            l_odd = pivot 
            r_odd = pivot 
            while l_odd >= 0 and r_odd < len(s) and s[l_odd] == s[r_odd]:
                l_odd -= 1 
                r_odd += 1 
            odd_piv = r_odd - l_odd - 1
        
            #If even
            l_even = pivot 
            r_even = pivot + 1 
            while l_even >= 0 and r_even < len(s) and s[l_even] == s[r_even]:
                l_even -= 1 
                r_even += 1 
            even_piv = r_even - l_even - 1


            if even_piv > odd_piv:
                return even_piv, l_even, r_even 
            
            return odd_piv, l_odd, r_odd

    


        for pivot in range(len(s)):
            attempt_length, l, r = get_palindrome_pivot(pivot)
            if attempt_length > best:
                best = attempt_length
                final_l = l 
                final_r = r 
        
        return s[final_l+1:final_r]
        

