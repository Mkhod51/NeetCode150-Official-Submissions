class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def getIndex(char):
            if 'a' <= char <= 'z':
                return ord(char) - ord('a')
            else:
                return ord(char) - ord('A') + 26            
        def checkListEq(sList, tList):
            for i in range(52):
                if sList[i] < tList[i]:
                    return False 
                
            return True 

        res = ""

        if len(t) > len(s):
            return res 

        tCount = [0] * 52 
        for c in t:
            tCount[getIndex(c)] += 1 

        best = float("inf")
        l = 0
        sCount = [0] * 52 

        for r in range(len(s)):
            sCount[getIndex(s[r])] += 1 

            while checkListEq(sCount, tCount):
                if r-l+1 < best:
                    best = r-l+1
                    start = l
                
                sCount[getIndex(s[l])] -= 1
                l += 1 
        
        if not best < float("inf"):
            return ""

        return s[start: start+best] 





