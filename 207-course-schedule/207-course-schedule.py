class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # map each course to prereq list
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c] = preMap.get(c, [])
            preMap[c].append(p)
        
        #visit Set = all courses along the curr DFS path
        visit = set()
        
        def dfs(c):
            # base case 1: when there's a loop
            if c in visit:
                return False
            # base case 2: when the course has no prereq. Return True as it can be completed
            if preMap[c] == []:
                return True
            visit.add(c)
            for p in preMap[c]:
                if not dfs(p): # return false when there's a prereq that caused a loop
                    return False
            visit.remove(c) # clean up
            preMap[c] = [] # this helps us reduce rework when we reach the same course again
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        