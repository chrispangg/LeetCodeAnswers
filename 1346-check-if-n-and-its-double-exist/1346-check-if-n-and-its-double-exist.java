class Solution {
    public boolean checkIfExist(int[] arr) {
        // 10,2,5,3
        HashMap<Integer, Integer> map = new HashMap<>();
        Boolean status = false;
        for (int i = 0; i < arr.length; i++) {
            // check if the arr[i]*2 returns something
            // if not, put arr[i] as key and arr[i] as value
            Integer b = map.get(arr[i] * 2);
            if (b != null) {
                return true;
            } else if (arr[i] % 2 == 0) {
                Integer c = map.get(arr[i] / 2);
                if (c != null) {
                    return true;
                }
            }
            map.put(arr[i], arr[i] * 2);
        }
        return status;
    }
}