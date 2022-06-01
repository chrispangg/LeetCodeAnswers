class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        Map<Integer, Integer> rm = new HashMap<Integer, Integer>();
        int max = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                max = max + 1;
                if(i == nums.length-1){
                    rm.put(i,max);
                }
            } else if (nums[i] == 0 || i == nums.length-1){
                rm.put(i,max);
                max = 0;
            }
        }
        Map.Entry<Integer, Integer> maxEntry = null;
        for (Map.Entry<Integer, Integer> entry : rm.entrySet()) {
            if (maxEntry == null || entry.getValue()
                .compareTo(maxEntry.getValue()) > 0) {
                maxEntry = entry;
            }
        }
        return maxEntry.getValue();
    }
}