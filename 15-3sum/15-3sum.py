# initalise array res
# sort nums
# for num in nums
    # this is not the first input in the input array and nums[i] is equal nums[i-1], then we want to skip this num, because we don't want duplicates
    # two pointers left and right
    # while left < right
        # if threeSum is smaller than target, move right pointer right
        # if threeSum is larger than target, move left pointer left
        # else we append all numbers to the array res
            #to avoid duplicates, we can use a while loop to move forward until they are not equal
            #or we can convert array res to a set
    # return set as array

# Time Complexity = O(n logn n ), because we sorted. But because we have two loops, it is therefore O(n^2)
# Space Complexity = O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[l] + nums[r] + nums[i]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.add(tuple([nums[l], nums[r], nums[i]]))
                    l += 1
        return list(res)