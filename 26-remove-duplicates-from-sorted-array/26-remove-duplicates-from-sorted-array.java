class Solution {
    public int removeDuplicates(int[] nums) {
        // for-loop
        // if nums[i] == nums[i-1]
        // move all elements by one in position
        // else we move pointer up 
        int k = nums.length;
        int i = 1;
        while (i < k) {
            if (nums[i] == nums[i - 1]) {
                k--;
                for (int j = i; j <= k; j++) {
                    nums[j - 1] = nums[j];
                }
            } else {
                i++;
            }
        }
        return k;
    }
}