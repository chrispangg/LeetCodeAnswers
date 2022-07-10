# Two Pointers
    # if sum of two value is less than target, move left pointer up
    # if sum of two value is more than target, move right pointer down
    # if sum = to target return the position of array (remember to plus 1)
# Two Pointers meet in at num[i] return empty array

# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []
        l = 0
        r = len(numbers) - 1
        
        while r > l:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] == target:
                res.append(l + 1)
                res.append(r + 1)
                return res
            
        return res