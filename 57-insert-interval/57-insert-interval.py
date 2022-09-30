"""
[1,3] [6,9] [2,5]
[1,3] and [2,5] are merged
    We know they are NOT overlapping when:
        option 1: when l2 end node is before l1 start node
        option 2: when l2 start node is after l1 end node
        
    once identify there's an overlap:
        merge by putting taking the min(l1[start], l2[start]) and max(l1[end], l2[end])

"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                print(newInterval ," is overlapping with", interval)
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        res.append(newInterval)
        return res