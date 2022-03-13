class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for(char jewel: jewels.toCharArray()){
            map.put(jewel, 0);
        }
        
        char[] stonesArray = stones.toCharArray();
        
           
        for(char stone: stonesArray){
            if(map.containsKey(stone)){
                map.put(stone, map.get(stone) + 1);
            }
        }
        
        int sum = 0;
        for(int value: map.values()){
            sum = sum + value;
        }
        
        return sum;
    }
}