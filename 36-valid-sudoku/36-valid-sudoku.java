import java.util.HashSet;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        //For in element in every array we add the following String to a set (if the element is not ".")
            //'5' in row 0
            //'5' in column 0
            //'5' in cube (0,0)
        //if one of them cannot be added to a set, return false, because it means 5 occured again in the same row/column/cube
        //To calculate cube, we can use the loop
            //horizontal = 3
        
        Set seen = new HashSet();
        for(int i = 0; i < 9; i++){ //verti
            for(int j = 0; j < 9; j++){ //hori
                if(board[i][j] != '.'){
                    if(!seen.add(board[i][j] + " in row " + i) ||
                        !seen.add(board[i][j] + " in column " + j) ||
                            !seen.add(board[i][j] + " in cube " + i/3 + "," + j/3)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}