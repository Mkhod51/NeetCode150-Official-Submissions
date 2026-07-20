class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 

        counts1 = {}
        counts2 = {}
        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i],0)
        
        for i in range(len(s1)):
            counts2[s2[i]] = 1 + counts2.get(s2[i],0)

            if counts1 == counts2:
                return True
        
        l = 0
        r = len(s1) - 1
        print(counts1)
        while r < len(s2) - 1: 
            counts2[s2[l]] = counts2.get(s2[l], 0) - 1
            if counts2[s2[l]] < 1:
                counts2.pop(s2[l])
            l += 1

            r += 1 
            counts2[s2[r]] = 1 + counts2.get(s2[r],0)

            if counts1 == counts2:
                return True
           
        
        return False
        
        
            