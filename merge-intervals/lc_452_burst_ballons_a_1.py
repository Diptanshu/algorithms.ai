# Approach 1 
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: (x[0],x[1]))
        range_arr = []
        range_arr.append(points[0])
        # (s1, e1) (s2, e2) -> e1 >= s2
        for idx, s_e in enumerate(points[1:]):
            if range_arr[-1][1] >= s_e[0]:
                s,e = range_arr.pop()
                e = min(e, s_e[1])
                range_arr.append((s_e[0],e))
            else:
                range_arr.append((s_e[0], s_e[1]))
        return len(range_arr)
                
                                  
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: (x[0],x[1]))
        #range_arr = []
        #range_arr.append(points[0])
        s_e_prev = points[0]
        # (s1, e1) (s2, e2) -> e1 >= s2
        count = 1
        for r_i in range(1, len(points)):
            if s_e_prev[1] >= points[r_i][0]:
                s_e_prev = (points[r_i][0],min(s_e_prev[1],points[r_i][1]))
            else:
                count += 1
                s_e_prev = points[r_i]
        return count
                                             