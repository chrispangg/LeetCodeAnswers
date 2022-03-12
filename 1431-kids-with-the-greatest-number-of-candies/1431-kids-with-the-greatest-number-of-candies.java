class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        int max = 0;
        List<Boolean> list = new ArrayList<Boolean>();
        
        for(int num: candies){
            if(num>max) max = num;
        }
        
        for(int num: candies){
            if(num + extraCandies >= max){
                list.add(true);
            } else list.add(false);
        }
        
        return list;
    }
}