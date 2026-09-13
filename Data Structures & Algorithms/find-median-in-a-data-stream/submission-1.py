class MedianFinder:

    def __init__(self):
        self.size = 0
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        biggestMax = -heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, biggestMax)

        if len(self.minHeap) > len(self.maxHeap):
            smallestMin = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -smallestMin)
        
            

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        