import java.util.HashSet;

class Solution {
    public boolean isAnagram(String s, String t) {
        // Option 1: add stringS as char into a HashMap. Loop through stringT to check
        // if it contains the char.
        // If it does, reduce value by one, if value = 0, remove key. If it doesn't,
        // return false.
        
        //add String s to a HashMap
        boolean result = true;
        HashMap<Character, Integer> charList = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);
            if (charList.containsKey(letter)) {
                charList.put(letter, charList.get(letter) + 1);
            } else {
                charList.put(letter, 1);
            }
        }
        //check String t against the HashMap
        for (int i = 0; i < t.length(); i++) {
            char letter = t.charAt(i);
            if(charList.containsKey(letter)){
                if(charList.get(letter) == 1){
                    charList.remove(letter);
                } else {
                    charList.put(letter, charList.get(letter) - 1);
                }
            } else {
                return false;
            }
        }
        //check against charList size to ensure there's nothing left inside i.e. "ab" and "b"
        if(charList.size() > 0){
            result = false;
        }
        
        return result;
    }
               
}

//Time Complexity = O(n)
//Space Complexity = O(n)
