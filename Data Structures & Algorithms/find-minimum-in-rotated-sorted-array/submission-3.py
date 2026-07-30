class Solution:
    def findMin(self, nums: List[int]) -> int:
        print(-1 // 5)
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int(left + (right - left) / 2)
            mid_1 = mid - 1
            midP1 = mid + 1
            if mid_1 == -1:
                mid_1 = len(nums) - 1


            if nums[mid_1] > nums[mid]:
                return nums[mid]
            
            if nums[right] < nums[mid]:
                left = mid + 1 
            else:
                right = mid - 1 
        
        return nums[left]
            
            
