class Solution {
    public int maximumWealth(int[][] accounts) {
         int result = 0;
        
        for(int[] account: accounts){
            int accountVal = 0;
            
            for(int value: account){
                accountVal = accountVal + value;
            }
            
            if(accountVal > result){
                result = accountVal;
            }
        }
       return result;
            
    }
}