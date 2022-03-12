class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        int max = 0;
        List<Boolean> list = new ArrayList<Boolean>();
        
        for(int num: candies){
            if(num>max) max = num;
        }
        
        for(int num: candies){
            list.add(num + extraCandies >= max);
        }
        
        return list;
    }
}