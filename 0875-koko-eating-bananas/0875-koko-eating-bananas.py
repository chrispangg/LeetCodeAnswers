class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def helper(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile/k)
            return res
        
        while l <= r:
            m = (l + r) // 2
            times = helper(m)
            if times > h: 
                # if rate is too slow i.e. finishing all piles in 10 times as opposed to target 8 times
                # then increase the min rate by 1
                l = m + 1
            else:
                # if rate is too fast i.e. finishing all piles in 4 times as opposed to target 8 times
                # then we know our m is too big so reduce max rate by 1 of mid
                r = m - 1
            
        return l
    