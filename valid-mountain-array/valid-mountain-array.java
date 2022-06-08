class Solution {
    public boolean validMountainArray(int[] arr) {
        Boolean status = false;
        if (arr.length < 3) {
            return false;
        }
        int p1 = 0;
        int p2 = arr.length - 1;
        int timer = arr.length;
        while (timer != 0) {
            if (p2 == 0 || p1 == arr.length-1) {
                System.out.println(p2);
                return false;
            }
            if (arr[p1] == arr[p1 + 1] || arr[p2] == arr[p2 - 1]) {
                return false;
            }
            if (arr[p1] < arr[p1 + 1]) {
                p1++;
            }
            if (arr[p2] < arr[p2 - 1]) {
                p2--;
            }

            timer--;
        }
        if (p1 == p2) {
            status = true;
        }
        return status;
    }
}