class Solution {
    public int maximumWealth(int[][] accounts) {
        
        //find total account size;
        int totalAccountLength = 0;
        for(int[] account: accounts){
            totalAccountLength = totalAccountLength + account.length;
        }
                
        //find total value per account;
        int[] maxes = new int[accounts.length];
        
        int pos = 0;
        for(int[] account: accounts){
            int totalval = 0;
            for(int value: account){
                totalval = totalval + value;
            }
            
            maxes[pos] = totalval;
            pos++;
        }
        
        //find the largest;
        int max = maxes[0];
        
        for (int i = 1; i < maxes.length; i++){
            if (maxes[i] > max){
                max = maxes[i];
            }  
        }

    return max;
        
    }
}