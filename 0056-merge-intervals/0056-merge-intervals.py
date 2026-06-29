class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda interval: interval[0])
        merged=[]
        for i in intervals:
            if not merged or merged[-1][1]< i[0]:
                merged.append(i)
            else:
                merged[-1]= [merged[-1][0], max (merged[-1][1], i[-1])]

        return merged