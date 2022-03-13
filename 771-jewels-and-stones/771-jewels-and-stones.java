class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        
        HashSet<Character>set = new HashSet<Character>();
        for(char jewel: jewels.toCharArray()){
            set.add(jewel);
        }
        
        int sum = 0;
        for(char stone: stones.toCharArray()){
            if(set.contains(stone)){
                sum +=1;
            }
        }
        
        return sum;
    }
}