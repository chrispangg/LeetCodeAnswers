class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #convert tasks to maxHeap
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)
        
        q = deque() #pop from front, append from back
        time = 0
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n]) #add 1 because maxHeap are in negative integer
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
        