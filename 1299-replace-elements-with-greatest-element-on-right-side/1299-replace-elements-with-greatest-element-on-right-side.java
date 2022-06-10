class Solution {
    public int[] replaceElements(int[] arr) {

        int maxVal = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            if (i == arr.length - 1) {
                maxVal = arr[i];
                arr[i] = -1;
            } else if (arr[i] > maxVal) {
                int temp = arr[i];
                arr[i] = maxVal;
                maxVal = temp;
            } else {
                arr[i] = maxVal;
            }
        }

        return arr;
    }
}