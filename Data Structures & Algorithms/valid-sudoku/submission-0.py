class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hashmap storing number: [[rows its in],[columns its in],[boxes its in]], invalid if one number is added to a hashmap its already in
        # 1 - rows
        # 2 - columns
        # 3 - boxes
        hm = {str(i+1): [set(),set(),set()] for i in range(9)}
        
        curRow = 0
        counter = -1
        for r,row in enumerate(board):
            curRow = r


            for c,n in enumerate(row):
                if n == ".":
                    continue

                curColumn = c
                curSquare = (curRow // 3) * 3 + (curColumn // 3)

                if curRow in hm[n][0] or curColumn in hm[n][1] or curSquare in hm[n][2]:
                    return False
                else:
                    hm[n][0].add(curRow)
                    hm[n][1].add(curColumn)
                    hm[n][2].add(curSquare)
        
        return True
                



                