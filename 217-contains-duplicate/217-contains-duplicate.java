class Solution {
    public boolean containsDuplicate(int[] nums) {
        boolean result = false;
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(set.contains(nums[i])){
                result = true;
            } else {
                set.add(nums[i]);
            }
        }
        return result;
    }
}

//Time Complexity: O(n)
//Space Complexity: O(n)
