class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimze idle time
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        
        while maxHeap or q: # when still have tasks to process
            time += 1
            
            # process maxheap
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 #because maxheap's negative integer
                if cnt:
                    q.append([cnt, time + n])
            
            # process deque and add back to the maxheap if there are tasks available
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time
            
        