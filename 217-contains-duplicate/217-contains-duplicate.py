# for loop the array
# if we cannot add to hashset, then return false
# else we keep adding to the set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for n in nums:
            if n in res:
                return True
            else:
                res.add(n)
        return False