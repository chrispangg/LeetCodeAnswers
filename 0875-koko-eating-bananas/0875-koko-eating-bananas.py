class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        def helper(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile/k)
            return res
        
        while l <= r:
            m = (l + r) // 2
            times = helper(m)

            if times > h: # meaning times is on the big
                l = m + 1
            else: #times is on the small side
                r = m - 1
                res = min(m, res)
            
        return res
    