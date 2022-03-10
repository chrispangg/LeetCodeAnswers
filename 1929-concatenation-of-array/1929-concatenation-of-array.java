class Solution {
    public int[] getConcatenation(int[] nums) {
        
        int[] newArray = new int[nums.length*2];
        
        int pos = 0;
        
        for(int i=0; i<2; i++){
            
            for(int num: nums){
                newArray[pos] = num;
                pos++;
            }
        }
        
        return newArray;

    }
}