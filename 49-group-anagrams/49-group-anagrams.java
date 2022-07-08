import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

//create a hashmap<String, List<String>>
//for-loop: where key is sorted value, and value is added to the String list
//as we loop, if the key matches one of the keys, we add it to the String list
//convert hashtable values into an array. Example: ArrayList<String> arr = new ArrayList<Word>(hw.values());

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        for(int i = 0; i < strs.length;  i++){
            //convert strs[i] to char and sort it ;
            char[] c = strs[i].toCharArray();
            Arrays.sort(c);
            String s = new String(c);
            //if s exists as key in the map, we add it to the 
            if(!map.containsKey(s)){
                List<String> arr = new ArrayList<String>();
                arr.add(strs[i]);
                map.put(s, arr);
            }else {
                List<String> arr = map.get(s);
                arr.add(strs[i]);
                map.put(s, arr);
            }
        }
        
        //convert hashtable values into an array
        List<List<String>> result = new ArrayList<List<String>>(map.values());
        
        return result;
    }
}

//Time Complexity = O(n log n) becauase we are sorting it in a loop
//Space Complexity = O(n), because we are storing values in an array on each loop
