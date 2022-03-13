class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        
        int[] result = new int[nums.length];
        
        HashSet<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            set.add(nums[i]);
            
            for(int j = 0; j < nums.length; j++){       
                if(nums[j] < nums[i] && j != i){
                    result[i] +=1;
                }
            }
            
        }
        return result;
    }
}