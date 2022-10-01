class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i, interval in enumerate(intervals):
            if not res: 
                res.append(interval)
                continue

            last = res.pop(-1)
            if last[1] >= interval[0]:
                combined = [min(last[0], interval[0]), max(last[1], interval[1])]
                res.append(combined)
            else:
                res.append(last)
                res.append(interval)
        
        return res