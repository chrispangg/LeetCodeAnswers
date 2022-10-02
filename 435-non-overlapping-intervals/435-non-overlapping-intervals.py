class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        newIntervals = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = newIntervals[-1][1]
            if prevEnd > start: #overlapped
                newIntervals[-1][1] = min(prevEnd, end)
            else:
                newIntervals.append([start, end])
        return len(intervals) - len(newIntervals)