import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.hp = nums
        self.k = k 

        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp) 
        
        return self.hp[0]

            

        
