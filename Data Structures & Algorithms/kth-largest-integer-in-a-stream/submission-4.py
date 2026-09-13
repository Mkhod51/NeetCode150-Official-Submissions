import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = [-n for n in nums]
        heapq.heapify(nums)
        self.hp = nums
        self.k = k 

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, -val)
        copyHeap = self.hp.copy()

        for i in range(self.k-1):
            heapq.heappop(copyHeap)
        return -copyHeap[0]

            

        
