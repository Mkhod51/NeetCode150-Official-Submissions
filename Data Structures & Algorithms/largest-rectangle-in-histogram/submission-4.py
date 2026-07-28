class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] #(h, i)
        maxA = 0

        for i,h in enumerate(heights + [0]):
            if not st:
                st.append((h,i))
                continue 
            
            start = i 

            while st and h < st[-1][0]:
                area = (i - st[-1][1]) * st[-1][0] 
                start = st[-1][1]
                maxA = max(area,maxA)
                st.pop()
            
            st.append((h,start))

        
        return maxA
            
        


            



            