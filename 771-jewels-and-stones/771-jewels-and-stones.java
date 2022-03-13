class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for(char jewel: jewels.toCharArray()){
            map.put(jewel, 0);
        }
        
        int sum = 0;
        for(char stone: stones.toCharArray()){
            if(map.containsKey(stone)){
                sum +=1;
            }
        }
        
        return sum;
    }
}