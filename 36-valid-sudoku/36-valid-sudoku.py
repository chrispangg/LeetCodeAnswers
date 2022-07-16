"""
Use a set to save the positions. If we can't add it into our set, then it's repeated, return false.
For each char that is not ".", we add three entries to our set. Examples:
"5 in row 0" -> num in row j
"5 in column 0" -> num in column i
"5 in cube 0,0", 1st 0 = i//3, and 2nd 0 is j//3

Time = O(n), Space = O(n) 

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        resSet = set()
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != ".":
                    row = c + " in row " + str(i)
                    column = c + " in column " + str(j)
                    cube = c + " in cube " + str(i//3) + "," + str(j//3)
                                
                    if row in resSet or column in resSet or cube in resSet:
                        return False
                    else:
                        resSet.update([row, column, cube])
                    
        return True