class Solution {
    public int[] runningSum(int[] nums) {
        
        int[] newArray = new int[nums.length];
        
        int runningSum = 0;
        
        for(int i=0; i<nums.length; i++){
            newArray[i] = nums[i] + runningSum;
            runningSum = runningSum+ nums[i];
        }
        
        return newArray;
    }
}