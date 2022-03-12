Key Point to understand:
* In Roman, if the value after is a bigger value i.e. CM (100, 1000) or XC (10, 100), then the value becomes a negative value i.e. CM = -100 + 1000 or XC = -10 + 100
​
Sudo-Code:
1. Add integer to an array based on Roman symbol
2. Perform a for loop (that excludes the last value in the array)
3. If the value at position i is less than the next value in the array, we substract it
4. else we add to our final result integer
5. After the loop, add the final integer back into the final result integer
6. return the integer
​
​