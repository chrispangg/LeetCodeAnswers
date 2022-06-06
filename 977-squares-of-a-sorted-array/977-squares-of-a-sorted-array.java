class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] array = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            array[i] = nums[i] * nums[i];
        }
        Arrays.sort(array);
        return array;
    }   
}