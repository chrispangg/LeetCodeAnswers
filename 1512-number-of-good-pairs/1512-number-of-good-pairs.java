class Solution {
    public int numIdenticalPairs(int[] nums) {
        
        int total = 0;
        
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int key: nums){
            if(map.get(key) == null){
                map.put(key, 0);
            } else {
                map.put(key, map.get(key) + 1);
            }
        }
        
        for(int value: map.values()){
            total += (value+1)*(value+1-1)/2;
        }
        
        return total;
        
    }
}