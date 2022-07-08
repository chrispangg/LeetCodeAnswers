import java.util.TreeMap;
import java.util.ArrayList;

class Solution {
     public int[] topKFrequent(int[] nums, int k) {

        // frequency map
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // bucket sort on freq
        ArrayList<Integer>[] bucket = new ArrayList[nums.length + 1];
        for (int key : map.keySet()) {
            int frequency = map.get(key);
            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(key);
        }

        int[] res = new int[k];
        int count = 0;
        for (int i = bucket.length - 1; i >= 0; i--) {
            if (bucket[i] != null) {
                ArrayList<Integer> freq = bucket[i];
                for (Integer integer : freq) {
                    int val = integer;
                    res[count] = val;
                    count++;
                    if (count == k) {
                        return res;
                    }
                }
            }
        }
        return res;
    }
}

//Solutioning:
    //Use a hashmap to count the frequency
    //Use a variant of bucket sort:
        //List - size = nums.length
        //index: store frequency
        //value: store a list of keys that matches the frequency
    //return array of the top k elements (using a for-loop)