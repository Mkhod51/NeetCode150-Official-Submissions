class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1 
        maxi = 0

        while left < right:
            vol = (right - left) * min(heights[left], heights[right])
            maxi = max(maxi, vol)

            if heights[left] > heights[right]:
                right -= 1 
            else:
                left += 1 
        
        return maxi

