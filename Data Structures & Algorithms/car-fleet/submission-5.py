class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = [] #(pos, speed)
        positionPairs = [(p,i) for i,p in enumerate(position)]
        positionPairs.sort(key=lambda x: x[0], reverse=True)
        

        for i in range(len(positionPairs)):
            curTime = (target - positionPairs[i][0]) / speed[positionPairs[i][1]]
            if not st or curTime > st[-1]:
                st.append(curTime)


        return len(st)