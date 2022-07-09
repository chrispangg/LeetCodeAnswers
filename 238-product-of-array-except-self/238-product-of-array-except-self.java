
class Solution {
    public int[] productExceptSelf(int[] nums) {
        //nums =    [1,   2, 3, 4]
        //prefix =  [1,   1, 2, 6]
        //postfix = [24, 12, 4, 1]
        //result =  [24, 12, 8, 6]
        
        int[] res = new int[nums.length];
        res[0] = 1;
        
        //prefix
        for(int i = 1; i < res.length; i++){
            res[i] = nums[i-1] * res[i-1];
        }
        
        //prefix*postfix = result
        int nextPostfix = 1;
        for(int i = res.length-1; i >= 0; i--){
            res[i] = res[i]*nextPostfix;
            nextPostfix = nums[i]*nextPostfix;
        }
        
        
        return res;
    }
}
        