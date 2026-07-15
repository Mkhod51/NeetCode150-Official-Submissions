class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for e in nums:
            if e not in hm:
                hm[e] = 1 
            else:
                hm[e] += 1 
        buckets = [[] for _ in range(len(nums) + 1)]

        for num,count in hm.items():
            buckets[count].append(num)
        
        bucketsCounter = len(buckets)
        
        retList = [0 for _ in range(k)]
        for i in range(k):
            while len(buckets[bucketsCounter - 1]) < 1:
                bucketsCounter -= 1
            retList[i] = buckets[bucketsCounter - 1].pop()

            

        return retList