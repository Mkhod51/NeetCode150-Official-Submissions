class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x,y,cur,seen):
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return False

            if (x,y) in seen:
                return False 
            
            if cur != word[0:len(cur)]:
                return False 

            if cur + board[y][x] == word:
                return True
            
            

            for x1,y1 in [(1,0), (-1,0), (0,1), (0,-1)]:
                seen.add((x,y))
                if dfs(x+x1, y+y1, cur+board[y][x], seen.copy()):
                    return True 
                seen.remove((x,y))
            
            return False 
            
        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(x,y,"", set()):
                    return True
            
        return False

