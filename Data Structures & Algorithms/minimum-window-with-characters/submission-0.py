from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        def check_match(countsS, countsT):
            match = True
            for key,value in countsT.items(): 
                if (key not in countsS) or countsS[key] < value:
                    match = False
            return match

        best = ""
        bestLen = float("infinity")
        dynamic = deque()

        countsT = {}
        countsS = {}

        for c in t:
            countsT[c] = 1 + countsT.get(c,0)

        print(countsT)
        l,r = 0,0
        while r < len(s):
                    dynamic.append(s[r])
                    countsS[s[r]] = 1 + countsS.get(s[r], 0)

                    while check_match(countsS, countsT):
                        if r - l + 1 < bestLen:
                            best = "".join(dynamic)
                            bestLen = r - l + 1
                        dynamic.popleft()
                        countsS[s[l]] -= 1
                        l += 1

                    r += 1

        return best


            

             
            

        
        
        
        
