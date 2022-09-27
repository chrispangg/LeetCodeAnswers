class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        
        dic = {}
        for k in hand:
            dic[k] = dic.get(k, 0) + 1
        
        minH = list(dic.keys())
        heapify(minH)
        
        while minH:
            first = minH[0]
            
            for i in range(first, first + groupSize):
                if i not in dic: 
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    # check if the value we want to pop if the min value,
                    # if not, then we 
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True