# initalise set
# sort nums
# for num in nums
    # target = 0
    # two pointers left and right
    # while left < right
        # check if left + right + num = 0 and r != i and l != i and r != l
            #if yes, add all three digit as an SORTED array to a set
        # if sum is smaller than target, move right pointer right
        # if sum is larger than target, move left pointer left
    # return set as array

    # [-1,0,1,2,-1,-4]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
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
                    res.append([nums[l], nums[r], nums[i]])
                    # arr.sort()
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res