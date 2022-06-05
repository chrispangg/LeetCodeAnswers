class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int localmax = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                localmax += 1;
                if (localmax > max) {
                    max = localmax;
                }
            } else if (nums[i] == 0 || i == nums.length - 1) {
                if (localmax > max) {
                    max = localmax;
                }
                localmax = 0;
            }
        }
        return max;
    }
}