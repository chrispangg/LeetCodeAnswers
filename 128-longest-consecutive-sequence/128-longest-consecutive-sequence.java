import java.util.*;
class Solution {
    public int longestConsecutive(int[] nums) {
        //Add them to a set
        //For-loop: identify the start of the sequence
        //If set contains key(n-1), we skip
        //If doesn't contains key(n-1), we perform a while loop to check if key(n+1) exist
        //As we loop, we increment a temp counter
        //If temp counter > main counter, replace main counter = temp counter
        Set<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int res = 1;
        if(nums.length == 0){
            return 0;
        }
        for(int i = 0; i < nums.length; i++){
            if(set.contains(nums[i] -1)){
                continue;
            } else {
                int key = nums[i] + 1;
                int temp = 1;
                while(set.contains(key)){
                    temp++;
                    key++;
                }
                if(temp > res) res = temp;
            }
        }
        return res;
    }
}