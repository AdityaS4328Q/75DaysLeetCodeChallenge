import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= -stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            largest=heapq.heappop(stones)
            sec_largest = heapq.heappop(stones)

            if largest!= sec_largest:
                heapq.heappush(stones, largest-sec_largest)

        if len(stones)==1:
            return -stones[0]
        else:
            return 0
