class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for rows in range(9):
            #har row k 
            seen =set()
            for element in range(9):
                if board[rows][element]== '.': continue
                
                if board[rows][element] not in seen:
                    seen.add(board[rows][element])
                else :
                    return False
        
        for cols in range(9):
            #har row k 
            seen =set()
            for element in range(9):
                if board[element][cols]== '.': continue
                
                if board[element][cols] not in seen:
                    seen.add(board[element][cols])
                else :
                    return False
        
        for row_start in range (0,9,3):
            for col_start in range(0,9,3):
                seen =set()
                for i in range(3):
                    for j in range(3):
                        if board[row_start+i][col_start+j]== '.': continue
                        if board[row_start+i][col_start+j] not in seen:
                            seen.add(board[row_start+i][col_start+j])
                        else :
                            return False

        return True
                 
                

        