class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)

            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[right]:
                
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1 
            
            else: 
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] == target:
            return left 

        return -1
