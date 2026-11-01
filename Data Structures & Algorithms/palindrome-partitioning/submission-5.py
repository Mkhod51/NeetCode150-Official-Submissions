class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPal(word):
            l = 0
            r = len(word) - 1 
            while l < r:
                if word[r] != word[l]:
                    return False 
                l += 1 
                r -= 1 
            
            return True
        
        res = []

        def dfs(ind, path):
            if ind >= len(s):
                res.append(path.copy())
                return 
            
            for i in range(ind, len(s)):
                if not checkPal(s[ind:i+1]):
                    continue 
                
                path.append(s[ind:i+1])
                dfs(i+1, path)
                path.pop()
            
        dfs(0,[])
        return res
