class Solution {
    public int minimumSum(int num) {
        
        int[] values = new int[4];
            
        int mod = 1000;
        int temp = num;
        
        for(int i = 0; i< values.length; i++){
            values[i] = (temp-temp%mod)/mod;
            temp = temp%mod;
            mod = mod/10;    
        }
        
        Arrays.sort(values); // Ascending order
        
        int value1 = values[0] * 10 + values[2];
        int value2 = values[1] * 10 + values[3];
        
        return value1 + value2;
    }
}