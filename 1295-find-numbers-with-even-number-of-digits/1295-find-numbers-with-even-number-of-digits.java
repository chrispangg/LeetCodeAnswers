class Solution {
    public int findNumbers(int[] nums) {
        int countEven = 0;
        int array[] = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int count = 1;
            while (nums[i] / 10 > 0) {
                nums[i] = nums[i] / 10;
                count++;
                array[i] = count;
            }
            if(array[i]%2==0 && array[i] !=0){
                countEven++;
            }
        }
        return countEven;
    }
}