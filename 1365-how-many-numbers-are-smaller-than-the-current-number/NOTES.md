This is a copied answer but it's brilliant because this example shows the power of using the index of a hashmap.
​
### Example given:
Let's use this input for illustration: [8,1,2,2,3]
​
Create a copy of the input array. copy = [8,1,2,2,3]
Sort the copy array. copy = [1,2,2,3,8]
Fill the map: number => count (where count is an index in sorted array, so first number with index 0 has 0 numbers less than it, index 1 has 1 number less, etc). We update only first time we enocunter the number so that way we skip duplicates.
* map[1]=>0
* map[2]=>1
* map[3]=>3
* map[8]=>4
We re-use our copy array to get our result, we iterate over original array, and get counts from the map.
[4,0,1,1,3]