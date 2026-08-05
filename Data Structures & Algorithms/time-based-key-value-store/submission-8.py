class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append((value, timestamp))
        else:
            self.mp[key] = [(value, timestamp)]
        print(self.mp)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.mp:
            return res 
        
        arr = self.mp[key]
        l = 0
        r = len(arr) - 1 

        while l <= r:
            mid = (l + r) // 2
            curTS = arr[mid][1]

            if curTS <= timestamp:
                res = arr[mid][0]
                l = mid + 1 
            
            else:
                r = mid - 1
        
        return res
            


        
