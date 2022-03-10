class Solution {
    public int[] buildArray(int[] nums) {
        
        int[] num2 = new int[nums.length];
        
        for(int i = 0; i< nums.length; i++){            
            num2[i] = nums[nums[i]];
            
        }
        return num2;
    }
}