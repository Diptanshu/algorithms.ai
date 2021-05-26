class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:(x[0],[1]))
        print (intervals)
        # condition for overlap
        # e (prev) >= s (start)
        prev, count = 0,0
        for idx, min_max in enumerate(intervals[1:]):
            print (prev)
            if intervals[prev][1] > min_max[0]:
                if intervals[prev][1] >= min_max[1]:
                    prev = idx+1
                count += 1
            else:
                prev = idx+1
        return count 
                