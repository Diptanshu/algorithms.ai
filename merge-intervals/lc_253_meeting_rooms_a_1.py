# Approach 1 
class Solution(object):
    # Insert tuple into a heap ?
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        import heapq
        timestamps = sorted(intervals, key = lambda x:x[0])

        heap_list = []
        heapq.heapify(heap_list)
        # condition for overlap e < s 
        # (s1,e1) , (s2,e2), (s3,e3) ....
        # construct a min heap 
        # print (timestamps)
        for index, timeslot in enumerate(timestamps):
            if heap_list and heap_list[0] <= timeslot[0]:
                heapq.heappop(heap_list)
            heapq.heappush(heap_list, timeslot[1])
        return len(heap_list)


# Approach 2 
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start_arr, end_arr = [],[]
        for start,end in intervals:
            start_arr.append(start)
            end_arr.append(end)

        start_arr.sort()
        end_arr.sort()
        s, e = 0,0
        available, numRooms = 0,0
        while s < len(start_arr):
            if start_arr[s] < end_arr[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                s += 1 
            else:
                available += 1
                e += 1
        return numRooms



# Approach 3  Pending
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
            

        


if __name__ == '__main__':
    obj = Solution()
    obj.minMeetingRooms([[0,30],[5,10],[15,20]])

        
